from lists_and_dictionaries import *
from data import *
import statistics
import math
from scipy.interpolate import interp1d

def calculate_pv_value(current_frame):
    # p_value
    list_l_p[current_frame].set(round(list_l_pn[current_frame].get() + list_l_ps[current_frame].get(), 2))
    if list_l_pn[current_frame].get() != 0 and list_l_ps[current_frame].get():
        # a_value
        if (list_l_pn[current_frame].get()*list_l_an[current_frame].get()+list_l_ps[current_frame].get()*0.9) == 0 or (list_l_pn[current_frame].get()+list_l_ps[current_frame].get()) == 0:
            list_l_a[current_frame].set(0.0)
        else:
            list_l_a[current_frame].set(round((list_l_pn[current_frame].get()*list_l_an[current_frame].get()+list_l_ps[current_frame].get()*0.9)/(list_l_pn[current_frame].get()+list_l_ps[current_frame].get()),2))
        # n_value
        if list_l_so[current_frame].get() == 0 or list_l_S[current_frame].get() == 0 or list_l_ho[current_frame].get() == 0 or list_l_hs[current_frame].get() == 0:
            list_l_n[current_frame].set(0.005)
        else:
            n_value = round((list_l_so[current_frame].get() / list_l_S[current_frame].get()) * (list_l_ho[current_frame].get() / list_l_hs[current_frame].get()) ** 0.5,3)
            list_l_n[current_frame].set(max(0.005, min(n_value, 1.0)))
        # k factor
        df = pd.DataFrame(hodnoty_k, index=sloupec_hodnot_n, columns=radek_hodnot_S)
        n = list_l_n[current_frame].get()
        S = statistics.mean(float(entry.get()) if entry.get().isdigit() else 0 for entry in dic_S_var_entries[current_frame])
        if S > 500:
            S = 500
        elif S < 5:
            S = 5
        elif n > 0.35:
            n = 0.35
        elif n < 0.005:
            n = 0.005
        df.loc[n, S] = np.nan
        df = df.interpolate(method="spline", order=3).interpolate(method="spline", order=3, axis=1).round(3)
        list_l_k[current_frame].set(df.loc[n, S])
        # b_value
        if list_l_so[current_frame].get() == 0:
            b_value = round(list_l_k[current_frame].get() / (0.005 * (list_l_hs[current_frame].get() ** 0.5)),2)
            list_l_b[current_frame].set(max(0.5, min(b_value, 1.7)))
        else:
            b_value = round((list_l_S[current_frame].get() * list_l_k[current_frame].get()) / (
                        list_l_so[current_frame].get() * (list_l_ho[current_frame].get() ** 0.5)), 2)
            list_l_b[current_frame].set(max(0.5, min(b_value, 1.7)))
        # pv_value
        list_l_pv[current_frame].set(round(list_l_a[current_frame].get()*list_l_b[current_frame].get()*1*list_l_p[current_frame].get(),2))
        if list_l_pv[current_frame].get() > 0:
            if list_var_om_konstrukcni_system[0].get() == "nehořlavý":
                list_mezni_pocty_podlazi[current_frame].set(math.floor(180/list_l_pv[current_frame].get()))
            elif list_var_om_konstrukcni_system[0].get() == "smíšený":
                list_mezni_pocty_podlazi[current_frame].set(math.floor(140/list_l_pv[current_frame].get()))
            else:
                list_mezni_pocty_podlazi[current_frame].set(math.floor(100/list_l_pv[current_frame].get()))
        mezni_sirka_pu = interp1d(data_nehorlavy_a_values_mr_pu, data_nehorlavy_1_np_mezni_sirky_pu, kind='linear', fill_value='extrapolate')
        mezni_sirka_interpolated = mezni_sirka_pu(np.array(list_l_a[current_frame].get()))
        list_mezni_sirky[current_frame].set(mezni_sirka_interpolated)
        mezni_delka_pu = interp1d(data_nehorlavy_a_values_mr_pu, data_nehorlavy_1_np_mezni_delky_pu, kind='linear', fill_value='extrapolate')
        mezni_delka_interpolated = mezni_delka_pu(np.array(list_l_a[current_frame].get()))
        list_mezni_delky[current_frame].set(mezni_delka_interpolated)

