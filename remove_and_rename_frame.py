from widget_variables_ounter import *

def remove_f(current_frame, list_cisla_pu, list_nazvy_pu):
    if len(list_pu_number) != 0:
        list_om_typ_pu[current_frame[0]].destroy()
        list_om_typ_pu.pop(current_frame[0])
        list_om_konstrukcni_system_pu[current_frame[0]].destroy()
        list_om_konstrukcni_system_pu.pop(current_frame[0])
        list_cisla_pu[current_frame[0]].destroy()
        list_cisla_pu.pop(current_frame[0])
        list_var_om_typ_pu.pop(current_frame[0])
        list_nazvy_pu[current_frame[0]].destroy()
        list_nazvy_pu.pop(current_frame[0])
        list_l_pv[current_frame[0]].destroy()
        list_l_pv.pop(current_frame[0])
        list_pu_number.pop(current_frame[0])
        for i in range(len(list_om_typ_pu)):
            element = list_om_typ_pu[i]
            element.grid(row=list_om_typ_pu.index(element)+1, column=0)
        for i in range(len(list_om_konstrukcni_system_pu)):
            element = list_om_konstrukcni_system_pu[i]
            element.grid(row=list_om_konstrukcni_system_pu.index(element)+1, column=1)
        for i in range(len(list_cisla_pu)):
            element = list_cisla_pu[i]
            element.grid(row=list_cisla_pu.index(element)+1, column=2)
        for i in range(len(list_nazvy_pu)):
            element = list_nazvy_pu[i]
            element.grid(row=list_nazvy_pu.index(element)+1, column=3)
        for i in range(len(list_l_pv)):
            element = list_l_pv[i]
            element.grid(row=list_l_pv.index(element)+1, column=4)
        if len(list_f_PU) != 0:
            list_f_info_PU[current_frame[0]].destroy()
            list_f_info_PU.pop(current_frame[0])
            list_f_PU[current_frame[0]].destroy()
            list_f_PU.pop(current_frame[0])
            list_nazvy_pu_default.pop(current_frame[0])
            dic_m_rows.pop(current_frame[0])
            dic_o_rows.pop(current_frame[0])
            if 0 <= current_frame[0] < len(list_S):
                list_S.pop(current_frame[0])
            if 0<= current_frame[0] < len(list_pn):
                list_pn.pop(current_frame[0])
            if 0<= current_frame[0] < len(list_hs):
                list_hs.pop(current_frame[0])
            if 0<= current_frame[0] < len(list_an):
                list_an.pop(current_frame[0])
            if 0<= current_frame[0] < len(list_ps):
                list_ps.pop(current_frame[0])
            if 0<= current_frame[0] < len(list_a):
                list_a.pop(current_frame[0])
            if 0<= current_frame[0] < len(list_ho):
                list_ho.pop(current_frame[0])
            if 0<= current_frame[0] < len(list_so):
                list_so.pop(current_frame[0])
            if 0<= current_frame[0] < len(list_l_n):
                list_l_n.pop(current_frame[0])
            if 0<= current_frame[0] < len(list_k):
                list_k.pop(current_frame[0])
            if 0<= current_frame[0] < len(list_b):
                list_b.pop(current_frame[0])
            if 0<= current_frame[0] < len(list_p):
                list_p.pop(current_frame[0])
            if 0<= current_frame[0] < len(list_pv):
                list_pv.pop(current_frame[0])
            current_frame[0] -= 1


def pu_rename(event):
    for i in range(len(list_cisla_pu)):
        cislo_pu = list_cisla_pu[i].get()
        nazev_pu = list_nazvy_pu[i].get()

        list_nazvy_pu_default[i].configure(text=cislo_pu + " - " + nazev_pu)