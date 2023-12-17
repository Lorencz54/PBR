from widget_variables_counter import *

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
        list_pocty_podlazi_pu.pop(current_frame[0])
        list_sirky_pu.pop(current_frame[0])
        list_delky_pu.pop(current_frame[0])
        list_vyskove_polohy_pu.pop(current_frame[0])
        list_mezni_pocty_podlazi.pop(current_frame[0])
        list_mezni_delky.pop(current_frame[0])
        list_mezni_sirky.pop(current_frame[0])
        list_l_SPB[current_frame[0]].destroy()
        list_l_SPB.pop(current_frame[0])
        list_var_l_SPB.pop(current_frame[0])
        list_var_l_pv.pop(current_frame[0])

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
        for i in range(len(list_l_SPB)):
            element = list_l_SPB[i]
            element.grid(row=list_l_SPB.index(element)+1, column=5)
        if len(list_f_PU) != 0:
            list_f_info_PU[current_frame[0]].destroy()
            list_f_info_PU.pop(current_frame[0])
            list_f_PU[current_frame[0]].destroy()
            list_f_PU.pop(current_frame[0])
            list_nazvy_pu_default.pop(current_frame[0])
            dic_m_rows.pop(current_frame[0])
            dic_o_rows.pop(current_frame[0])
            dic_S_entries.pop(current_frame[0])
            dic_S_var_entries.pop(current_frame[0])
            dic_pni_entries.pop(current_frame[0])
            dic_pni_var_entries.pop(current_frame[0])
            dic_hsi_entries.pop(current_frame[0])
            dic_hsi_var_entries.pop(current_frame[0])
            dic_ani_entries.pop(current_frame[0])
            dic_ani_var_entries.pop(current_frame[0])
            dic_psi_entries.pop(current_frame[0])
            dic_ps_var_entries.pop(current_frame[0])
            dic_ps_group_sums.pop(current_frame[0])
            dic_var_ps_labels.pop(current_frame[0])
            dic_ps_row_sum_labels.pop(current_frame[0])
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
            if 0 <= current_frame[0] < len(list_k):
                list_k.pop(current_frame[0])
            if 0 <= current_frame[0] < len(list_b):
                list_b.pop(current_frame[0])
            if 0 <= current_frame[0] < len(list_p):
                list_p.pop(current_frame[0])
            if 0 <= current_frame[0] < len(list_pv):
                list_pv.pop(current_frame[0])
            if 0 <= current_frame[0] < len(list_l_n):
                list_l_n.pop(current_frame[0])
            if 0 <= current_frame[0] < len(list_l_S):
                list_l_S.pop(current_frame[0])
            if 0 <= current_frame[0] < len(list_l_pn):
                list_l_pn.pop(current_frame[0])
            if 0 <= current_frame[0] < len(list_l_an):
                list_l_an.pop(current_frame[0])
            if 0 <= current_frame[0] < len(list_l_hs):
                list_l_hs.pop(current_frame[0])
            if 0 <= current_frame[0] < len(list_l_ho):
                list_l_ho.pop(current_frame[0])
            if 0 <= current_frame[0] < len(list_l_so):
                list_l_so.pop(current_frame[0])
            if 0 <= current_frame[0] < len(list_l_ps):
                list_l_ps.pop(current_frame[0])
            if 0 <= current_frame[0] < len(list_l_b):
                list_l_b.pop(current_frame[0])
            if 0 <= current_frame[0] < len(list_l_k):
                list_l_k.pop(current_frame[0])
            if 0 <= current_frame[0] < len(list_l_p):
                list_l_p.pop(current_frame[0])
            if 0 <= current_frame[0] < len(list_l_a):
                list_l_a.pop(current_frame[0])
            current_frame[0] -= 1


def pu_rename(event):
    for i in range(len(list_cisla_pu)):
        cislo_pu = list_cisla_pu[i].get()
        nazev_pu = list_nazvy_pu[i].get()

        list_nazvy_pu_default[i].configure(text=cislo_pu + " - " + nazev_pu)