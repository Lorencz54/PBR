from widget_variables_ounter import *

def remove_f(current_frame, list_cisla_pu, list_nazvy_pu, list_e_typ):
    print(current_frame)
    list_f_PU[current_frame[0]].destroy()
    list_f_PU.pop(int(current_frame[0]))
    list_f_info_PU[current_frame[0]].destroy()
    list_f_info_PU.pop(int(current_frame[0]))
    list_nazvy_default.pop(int(current_frame[0]))
    list_cisla_pu[current_frame[0]].destroy()
    list_cisla_pu.pop(int(current_frame[0]))
    list_nazvy_pu[current_frame[0]].destroy()
    list_nazvy_pu.pop(int(current_frame[0]))
    list_e_typ[current_frame[0]].destroy()
    list_e_typ.pop(int(current_frame[0]))
    dic_m_rows.pop(int(current_frame[0]))
    dic_o_rows.pop(int(current_frame[0]))
    list_l_pv[current_frame[0]].destroy()
    list_l_pv.pop(int(current_frame[0]))
    if 0 <= int(current_frame[0]) < len(list_S):
        list_S.pop(int(current_frame[0]))
    if 0<= int(current_frame[0]) < len(list_pn):
        list_pn.pop(int(current_frame[0]))
    if 0<= int(current_frame[0]) < len(list_hs):
        list_hs.pop(int(current_frame[0]))
    if 0<= int(current_frame[0]) < len(list_an):
        list_an.pop(int(current_frame[0]))
    if 0<= int(current_frame[0]) < len(list_ps):
        list_ps.pop(int(current_frame[0]))
    if 0<= int(current_frame[0]) < len(list_a):
        list_a.pop(int(current_frame[0]))
    if 0<= int(current_frame[0]) < len(list_ho):
        list_ho.pop(int(current_frame[0]))
    if 0<= int(current_frame[0]) < len(list_so):
        list_so.pop(int(current_frame[0]))
    if 0<= int(current_frame[0]) < len(list_l_n):
        list_l_n.pop(int(current_frame[0]))
    if 0<= int(current_frame[0]) < len(list_k):
        list_k.pop(int(current_frame[0]))
    if 0<= int(current_frame[0]) < len(list_b):
        list_b.pop(int(current_frame[0]))
    if 0<= int(current_frame[0]) < len(list_p):
        list_p.pop(int(current_frame[0]))
    if 0<= int(current_frame[0]) < len(list_pv):
        list_pv.pop(int(current_frame[0]))
    current_frame[0] -= 1



def pu_rename(event):
    for i in range(len(list_cisla_pu)):
        cislo_pu = list_cisla_pu[i].get()
        nazev_pu = list_nazvy_pu[i].get()

        list_nazvy_default[i].configure(text=cislo_pu + " - " + nazev_pu)