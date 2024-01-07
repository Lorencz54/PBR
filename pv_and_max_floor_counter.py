from lists_and_dictionaries import *
from data import *
from determine_SPB import *
import statistics
import math

def calculate_short_pv_value():
    ps_value = float(list_l_ps[current_frame[0]].get())
    pv_value = float(list_CSN_pv[current_frame[0]].get())
    if ps_value > 5:
        short_pv_value = pv_value*(ps_value-5)*1.15
        list_var_l_pv[current_frame[0]].set(short_pv_value)
    else:
        list_var_l_pv[current_frame[0]].set(pv_value)
    determine_SPB()
def calculate_pv_value(current_frame):
    # p_value
    p_value = round(list_l_pn[current_frame[0]].get() + list_l_ps[current_frame[0]].get(), 2)
    list_l_p[current_frame[0]].set(p_value)
    list_p[current_frame[0]] = p_value
    if list_l_pn[current_frame[0]].get() != 0 and list_l_ps[current_frame[0]].get() != 0:
        # a_value
        if (list_l_pn[current_frame[0]].get()*list_l_an[current_frame[0]].get()+list_l_ps[current_frame[0]].get()*0.9) == 0 or list_l_pn[current_frame[0]].get()+list_l_ps[current_frame[0]].get() == 0:
            list_l_a[current_frame[0]].set(0.0)
            list_a[current_frame[0]] = 0.0
        else:
            a_value = round((list_l_pn[current_frame[0]].get()*list_l_an[current_frame[0]].get()+list_l_ps[current_frame[0]].get()*0.9)/(list_l_pn[current_frame[0]].get()+list_l_ps[current_frame[0]].get()),2)
            list_l_a[current_frame[0]].set(a_value)
            list_a[current_frame[0]] = a_value
        # n_value
        if list_l_so[current_frame[0]].get() == 0 or list_l_S[current_frame[0]].get() == 0 or list_l_ho[current_frame[0]].get() == 0 or list_l_hs[current_frame[0]].get() == 0:
            list_l_n[current_frame[0]].set(0.005)
        else:
            pomer_S_So_value = round(list_l_so[current_frame[0]].get() / list_l_S[current_frame[0]].get(),2)
            list_pomer_S_So[current_frame[0]] = pomer_S_So_value
            pomer_ho_hs_value = round(list_l_ho[current_frame[0]].get() / list_l_hs[current_frame[0]].get(),2)
            list_pomer_ho_hs[current_frame[0]] = pomer_ho_hs_value
            n_value = round(pomer_S_So_value * pomer_ho_hs_value ** 0.5,3)
            list_l_n[current_frame[0]].set(max(0.005, min(n_value, 1.0)))
        # k factor
        df = pd.DataFrame(hodnoty_k, index=sloupec_hodnot_n, columns=radek_hodnot_S)
        n = list_l_n[current_frame[0]].get()
        list_n[current_frame[0]] = n
        S_mean = round(statistics.mean(float(entry.get()) if entry.get() != "" else 0.0 for entry in dic_S_entries[current_frame[0]]),2)
        list_Sm[current_frame[0]] = S_mean
        if S_mean > 500:
            S_mean = 500
        elif S_mean < 5:
            S_mean = 5
        elif n > 0.35:
            n = 0.35
        elif n < 0.005:
            n = 0.005
        df.loc[n, S_mean] = np.nan
        df = df.interpolate(method="spline", order=3).interpolate(method="spline", order=3, axis=1).round(3)
        list_l_k[current_frame[0]].set(df.loc[n, S_mean])
        list_k[current_frame[0]] = df.loc[n,S_mean]
        # b_value
        if list_l_so[current_frame[0]].get() == 0:
            b_value = round(list_l_k[current_frame[0]].get() / (0.005 * (list_l_hs[current_frame[0]].get() ** 0.5)),2)
            list_l_b[current_frame[0]].set(max(0.5, min(b_value, 1.7)))
            list_b[current_frame[0]] = b_value
        else:
            b_value = round((list_l_S[current_frame[0]].get() * list_l_k[current_frame[0]].get()) / (
                        list_l_so[current_frame[0]].get() * (list_l_ho[current_frame[0]].get() ** 0.5)), 2)
            list_l_b[current_frame[0]].set(max(0.5, min(b_value, 1.7)))
            list_b[current_frame[0]] = b_value
        # pv_value
        pv_value = round(list_l_a[current_frame[0]].get() * list_l_b[current_frame[0]].get() * 1 * list_l_p[current_frame[0]].get(), 2)
        list_pv[current_frame[0]] = pv_value
        list_var_l_pv[current_frame[0]].set(pv_value)
        if list_pv[current_frame[0]] > 0:
            if list_var_om_konstrukcni_system[0].get() == "nehořlavý":
                max_floor_value = math.floor(180 / list_var_l_pv[current_frame[0]].get())
                list_mezni_pocty_podlazi[current_frame[0]].set(max_floor_value)
                list_max_pocty_podlazi_PU[current_frame[0]] = max_floor_value
            elif list_var_om_konstrukcni_system[0].get() == "smíšený":
                max_floor_value = math.floor(140 / list_var_l_pv[current_frame[0]].get())
                list_mezni_pocty_podlazi[current_frame[0]].set(max_floor_value)
                list_max_pocty_podlazi_PU[current_frame[0]] = max_floor_value
            else:
                max_floor_value = math.floor(100 / list_var_l_pv[current_frame[0]].get())
                list_mezni_pocty_podlazi[current_frame[0]].set(max_floor_value)
                list_max_pocty_podlazi_PU[current_frame[0]] = max_floor_value
    determine_SPB()

def append_pocet_podlazi_in_list():
    pocet_podlazi_value = list_e_pocty_podlazi_pu[current_frame[0]].get()
    list_pocty_podlazi_PU[current_frame[0]] = pocet_podlazi_value