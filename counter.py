from lists_and_dictionaries import *
import numpy as np

def wrap_p(current_frame):
    hs(current_frame)
    ps(current_frame)
    pn(current_frame)
    an(current_frame)
    p(current_frame)
    f_a(current_frame)

def wrap_otvory(current_frame):
    so(current_frame)
    ho(current_frame)

def hs(current_frame):
    S_values = [float(entry.get()) for entry in dic_S_entries[current_frame]]
    hsi_values = [float(entry.get()) for entry in dic_hsi_entries[current_frame]]
    S_suma = np.sum(S_values)
    hs_value = round(np.dot(hsi_values, S_values) / S_suma, 2)
    list_l_hs[current_frame].config(text="Světlá výška PÚ: " + str(hs_value))

    #funkce na výpočet ps v current framu
def ps(current_frame):
    S_values = [float(entry.get()) for entry in dic_S_entries[current_frame]]
    S_suma = np.sum(S_values)
    psi_values = [float(entry.get()) for entry in dic_ps_entries[current_frame]]
    list_ps_arr = np.array(psi_values)
    list_ps_reshape = list_ps_arr.reshape(-1,3)
    ps_sum = np.sum(list_ps_reshape, axis=1)
    ps_sum_list = ps_sum.tolist()
    ps_value = round(np.dot(ps_sum_list, S_values)/S_suma,2)
    list_l_ps[current_frame].config(text="ps celkem: " + str(ps_value))
    for i in range(len(ps_sum_list)):
        ps_row_sum = ps_sum_list[i]
        label_ps_sum = dic_ps_labels[current_frame][i]
        label_ps_sum.config(text=str(ps_row_sum))
    if current_frame < len(list_ps):
        list_ps[current_frame] = ps_value
    else:
        list_ps.append(ps_value)

    # funkce na výpočet pn v current framu
def pn(current_frame):
    S_values = [float(entry.get()) for entry in dic_S_entries[current_frame]]
    pn_values = [float(entry.get()) for entry in dic_pni_entries[current_frame]]
    S_suma = np.sum(S_values)
    pn_value = round(np.dot(pn_values, S_values)/S_suma,2)
    if current_frame < len(list_pn):
        list_pn[current_frame] = pn_value
    else:
        list_pn.append(pn_value)
    list_l_pn[current_frame].config(text="pn celkem: " + str(pn_value))

# funkce na výpočet an v current framu
def an(current_frame):
    S_values = [float(entry.get()) for entry in dic_S_entries[current_frame]]
    an_values = [float(entry.get()) for entry in dic_ani_entries[current_frame]]
    S_suma = np.sum(S_values)
    an_value = round(np.dot(an_values, S_values)/S_suma,2)
    if current_frame < len(list_an):
        list_an[current_frame] = an_value
    else:
        list_an.append(an_value)
    list_l_an[current_frame].config(text="an celkem: " + str(an_value))

def f_a(current_frame):
    factor_a = round((list_pn[current_frame]*list_an[current_frame]+list_ps[current_frame]*0.9)/(list_pn[current_frame]+list_ps[current_frame]),2)
    if current_frame < len(list_a):
        list_a[current_frame] = factor_a
    else:
        list_a.append(factor_a)
    list_l_a[current_frame].config(text="a celkem: " + str(factor_a))

def p(current_frame):
    p = round(list_pn[current_frame]+list_ps[current_frame],2)
    list_l_p[current_frame].config(text="p celkem: " + str(p))

def so(current_frame):
    pocet_values = [float(entry.get()) for entry in dic_pocet_ot[current_frame]]
    sirka_values = [float(entry.get()) for entry in dic_sirka_ot[current_frame]]
    vyska_values = [float(entry.get()) for entry in dic_vyska_ot[current_frame]]
    so_value = np.sum(np.multiply(np.multiply(pocet_values, sirka_values), vyska_values))
    list_l_so[current_frame].config(text="Celková plocha otvorů PÚ: " + str(so_value))

def ho(current_frame):
    pocet_values = [float(entry.get()) for entry in dic_pocet_ot[current_frame]]
    sirka_values = [float(entry.get()) for entry in dic_sirka_ot[current_frame]]
    vyska_values = [float(entry.get()) for entry in dic_vyska_ot[current_frame]]
    so_values = np.multiply(np.multiply(pocet_values, sirka_values), vyska_values)
    hoi_values = [float(entry.get()) for entry in dic_vyska_ot[current_frame]]
    so_suma = np.sum(so_values)
    ho_value = round(np.dot(hoi_values, so_values) / so_suma, 2)
    list_l_ho[current_frame].config(text="Celková výška otvorů PÚ: " + str(ho_value))