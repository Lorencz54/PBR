from lists_and_dictionaries import *
from data import *
import statistics
import math

def calculate_pv_value(current_frame):
    # p_value
    list_l_p[int(current_frame[0])].set(round(list_l_pn[int(current_frame[0])].get() + list_l_ps[int(current_frame[0])].get(), 2))
    if list_l_pn[int(current_frame[0])].get() != 0 and list_l_ps[int(current_frame[0])].get():
        # a_value
        if (list_l_pn[int(current_frame[0])].get()*list_l_an[int(current_frame[0])].get()+list_l_ps[int(current_frame[0])].get()*0.9) == 0 or (list_l_pn[int(current_frame[0])].get()+list_l_ps[int(current_frame[0])].get()) == 0:
            list_l_a[int(current_frame[0])].set(0.0)
        else:
            list_l_a[int(current_frame[0])].set(round((list_l_pn[int(current_frame[0])].get()*list_l_an[int(current_frame[0])].get()+list_l_ps[int(current_frame[0])].get()*0.9)/(list_l_pn[int(current_frame[0])].get()+list_l_ps[int(current_frame[0])].get()),2))
        # n_value
        if list_l_so[int(current_frame[0])].get() == 0 or list_l_S[int(current_frame[0])].get() == 0 or list_l_ho[int(current_frame[0])].get() == 0 or list_l_hs[int(current_frame[0])].get() == 0:
            list_l_n[int(current_frame[0])].set(0.005)
        else:
            n_value = round((list_l_so[int(current_frame[0])].get() / list_l_S[int(current_frame[0])].get()) * (list_l_ho[int(current_frame[0])].get() / list_l_hs[int(current_frame[0])].get()) ** 0.5,3)
            list_l_n[int(current_frame[0])].set(max(0.005, min(n_value, 1.0)))
        # k factor
        df = pd.DataFrame(hodnoty_k, index=sloupec_hodnot_n, columns=radek_hodnot_S)
        n = list_l_n[int(current_frame[0])].get()
        S = statistics.mean(float(entry.get()) for entry in dic_S_var_entries[int(current_frame[0])])
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
        list_l_k[int(current_frame[0])].set(df.loc[n, S])
        # b_value
        if list_l_so[int(current_frame[0])].get() == 0:
            b_value = round(list_l_k[int(current_frame[0])].get() / (0.005 * (list_l_hs[int(current_frame[0])].get() ** 0.5)),2)
            list_l_b[int(current_frame[0])].set(max(0.5, min(b_value, 1.7)))
        else:
            b_value = round((list_l_S[int(current_frame[0])].get() * list_l_k[int(current_frame[0])].get()) / (
                        list_l_so[int(current_frame[0])].get() * (list_l_ho[int(current_frame[0])].get() ** 0.5)), 2)
            list_l_b[int(current_frame[0])].set(max(0.5, min(b_value, 1.7)))
        # pv_value
        list_var_l_pv[int(current_frame[0])].set(round(list_l_a[int(current_frame[0])].get() * list_l_b[int(current_frame[0])].get() * 1 * list_l_p[int(current_frame[0])].get(), 2))
        if list_var_l_pv[int(current_frame[0])].get() > 0:
            if list_var_om_konstrukcni_system[0].get() == "nehořlavý":
                list_mezni_pocty_podlazi[int(current_frame[0])].set(math.floor(180 / list_var_l_pv[int(current_frame[0])].get()))
            elif list_var_om_konstrukcni_system[0].get() == "smíšený":
                list_mezni_pocty_podlazi[int(current_frame[0])].set(math.floor(140 / list_var_l_pv[int(current_frame[0])].get()))
            else:
                list_mezni_pocty_podlazi[int(current_frame[0])].set(math.floor(100 / list_var_l_pv[int(current_frame[0])].get()))

