from lists_and_dictionaries import *
from data import *
import statistics

def wrap_p(current_frame):
    plocha_PU(current_frame)
    pn(current_frame)
    an(current_frame)
    ps(current_frame)
    p(current_frame)
    f_a(current_frame)
    pv(current_frame)

def wrap_otvory(current_frame):
    plocha_PU(current_frame)
    hs(current_frame)
    so(current_frame)
    ho(current_frame)
    n(current_frame)
    soucinitel_k(current_frame)
    soucinitel_b(current_frame)
    pv(current_frame)

def plocha_PU(current_frame):
    S_values = [float(entry.get()) for entry in dic_S_entries[current_frame]]
    S_suma = np.sum(S_values)
    list_l_S[current_frame].configure(text="S celkem: " + str(S_suma))
    if current_frame < len(list_S):
        list_S[current_frame] = S_suma
    else:
        list_S.append(S_suma)

#funkce na výpočet ps v current framu
def ps(current_frame):
    S_values = [float(entry.get()) for entry in dic_S_entries[current_frame]]
    S_suma = list_S[current_frame]
    psi_values = [float(entry.get()) for entry in dic_ps_entries[current_frame]]
    list_ps_arr = np.array(psi_values)
    list_ps_reshape = list_ps_arr.reshape(-1,3)
    ps_sum = np.sum(list_ps_reshape, axis=1)
    ps_sum_list = ps_sum.tolist()
    if np.dot(ps_sum_list, S_values) == 0 or S_suma == 0:
        ps_value = 0
        list_l_ps[current_frame].configure(text="ps celkem: " + str(ps_value))
    else:
        ps_value = round(np.dot(ps_sum_list, S_values)/S_suma,2)
        list_l_ps[current_frame].configure(text="ps celkem: " + str(ps_value))
    for i in range(len(ps_sum_list)):
        ps_row_sum = ps_sum_list[i]
        label_ps_sum = dic_ps_labels[current_frame][i]
        label_ps_sum.configure(text=str(ps_row_sum))
    if current_frame < len(list_ps):
        list_ps[current_frame] = ps_value
    else:
        list_ps.append(ps_value)

    # funkce na výpočet pn v current framu
def pn(current_frame):
    S_values = [float(entry.get()) for entry in dic_S_entries[current_frame]]
    pn_values = [float(entry.get()) for entry in dic_pni_entries[current_frame]]
    S_suma = list_S[current_frame]
    if np.dot(pn_values, S_values) == 0 or S_suma == 0:
        pn_value = 0
    else:
        pn_value = round(np.dot(pn_values, S_values)/S_suma,2)
    if current_frame < len(list_pn):
        list_pn[current_frame] = pn_value
    else:
        list_pn.append(pn_value)
    list_l_pn[current_frame].configure(text="pn celkem: " + str(pn_value))

# funkce na výpočet an v current framu
def an(current_frame):
    S_values = [float(entry.get()) for entry in dic_S_entries[current_frame]]
    an_values = [float(entry.get()) for entry in dic_ani_entries[current_frame]]
    S_suma = list_S[current_frame]
    if np.dot(an_values, S_values) == 0 or S_suma == 0:
        an_value = 0
    else:
        an_value = round(np.dot(an_values, S_values)/S_suma,2)
    if current_frame < len(list_an):
        list_an[current_frame] = an_value
    else:
        list_an.append(an_value)
    list_l_an[current_frame].configure(text="an celkem: " + str(an_value))

def f_a(current_frame):
    if (list_pn[current_frame]*list_an[current_frame]+list_ps[current_frame]*0.9) == 0 or (list_pn[current_frame]+list_ps[current_frame]) == 0:
        factor_a = 0
    else:
        factor_a = round((list_pn[current_frame]*list_an[current_frame]+list_ps[current_frame]*0.9)/(list_pn[current_frame]+list_ps[current_frame]),2)
    if current_frame < len(list_a):
        list_a[current_frame] = factor_a
    else:
        list_a.append(factor_a)
    list_l_a[current_frame].config(text="a celkem: " + str(factor_a))

def p(current_frame):
    p_value = round(list_pn[current_frame] + list_ps[current_frame], 2)
    if current_frame < len(list_p):
        list_p[current_frame] = p_value
    else:
        list_p.append(p_value)
    list_l_p[current_frame].configure(text="p celkem: " + str(p_value))

def hs(current_frame):
    S_values = [float(entry.get()) for entry in dic_S_entries[current_frame]]
    hsi_values = [float(entry.get()) for entry in dic_hsi_entries[current_frame]]
    S_suma = list_S[current_frame]
    if np.dot(hsi_values, S_values) == 0 or S_suma == 0:
        hs_value = 0
    else:
        hs_value = round(np.dot(hsi_values, S_values) / S_suma, 2)
    list_l_hs[current_frame].configure(text="Světlá výška PÚ: " + str(hs_value))
    if current_frame < len(list_hs):
        list_hs[current_frame] = hs_value
    else:
        list_hs.append(hs_value)

def n(current_frame):
    if list_so[current_frame] == 0 or list_S[current_frame] == 0 or list_ho[current_frame] == 0 or list_hs[current_frame] == 0:
        n_value = 0.005
    else:
        n_value = (list_so[current_frame]/list_S[current_frame])*(list_ho[current_frame]/list_hs[current_frame])**0.5
    if n_value < 0.005:
        n_value = 0.005
    elif n_value > 1:
        n_value = 1
    else:
        n_value
    if current_frame < len(list_n):
        list_n[current_frame] = n_value
    else:
        list_n.append(n_value)


def soucinitel_k(current_frame):
    df = pd.DataFrame(hodnoty_k, index=sloupec_hodnot_n, columns=radek_hodnot_S)
    n = list_n[current_frame]
    S = statistics.mean(float(entry.get()) for entry in dic_S_entries[current_frame])
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
    if current_frame < len(list_k):
        list_k[current_frame] = df.loc[n, S]
    else:
        list_k.append(df.loc[n, S])

def soucinitel_b(current_frame):
    if list_so[current_frame] == 0:
        b_value = list_k[current_frame]/(0.005*(list_hs[current_frame]**0.5))
    else:
        b_value = (list_S[current_frame]*list_k[current_frame])/(list_so[current_frame]*(list_ho[current_frame]**0.5))
    if b_value < 0.5:
        b_value = 0.5
    elif b_value > 1.7:
        b_value = 1.7
    if current_frame < len(list_b):
        list_b[current_frame] = b_value
    else:
        list_b.append(b_value)
    list_l_b[current_frame].configure(text="b celkem: " + str(b_value))

def so(current_frame):
    pocet_values = [float(entry.get()) for entry in dic_pocet_ot[current_frame]]
    sirka_values = [float(entry.get()) for entry in dic_sirka_ot[current_frame]]
    vyska_values = [float(entry.get()) for entry in dic_vyska_ot[current_frame]]
    so_value = np.sum(np.multiply(np.multiply(pocet_values, sirka_values), vyska_values))
    list_l_so[current_frame].configure(text="Celková plocha otvorů PÚ: " + str(so_value))
    if current_frame < len(list_so):
        list_so[current_frame] = so_value
    else:
        list_so.append(so_value)

def ho(current_frame):
    pocet_values = [float(entry.get()) for entry in dic_pocet_ot[current_frame]]
    sirka_values = [float(entry.get()) for entry in dic_sirka_ot[current_frame]]
    vyska_values = [float(entry.get()) for entry in dic_vyska_ot[current_frame]]
    so_values = np.multiply(np.multiply(pocet_values, sirka_values), vyska_values)
    hoi_values = [float(entry.get()) for entry in dic_vyska_ot[current_frame]]
    so_suma = np.sum(so_values)
    if np.dot(hoi_values, so_values) == 0 or so_suma == 0:
        ho_value = 0
    else:
        ho_value = round(np.dot(hoi_values, so_values) / so_suma, 2)
    list_l_ho[current_frame].configure(text="Celková výška otvorů PÚ: " + str(ho_value))
    if current_frame < len(list_ho):
        list_ho[current_frame] = ho_value
    else:
        list_ho.append(ho_value)

def pv(current_frame):
    if current_frame < len(list_p) and current_frame < len(list_a) and current_frame < len(list_b):
        pv_value = round(list_p[current_frame]*list_a[current_frame]*list_b[current_frame]*1,2)
        if current_frame < len(list_pv):
            list_pv[current_frame] = pv_value
        else:
            list_pv.append(pv_value)
        list_l_vysledky_pv[current_frame].configure(text="pv = " + str(pv_value))