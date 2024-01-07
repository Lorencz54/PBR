from add_frame_nevyrobni import *
from remove_and_rename_frame import *
from add_frame_vyrobni import *
from add_frame_OB1 import *


def add_new_pu():
    list_pu_number.append(1)
    list_nazvy_pu_default.append(1)

    # widgety pro požární úsek v rámečku pro celý objekt
    var_om_typ_pu = ctk.StringVar()
    om_typ_pu = ctk.CTkOptionMenu(list_PBR_frames[0], values=["", "nevýrobní", "OB1"], variable=var_om_typ_pu)
    om_typ_pu.grid(row=len(list_pu_number)+1, column=0)
    list_om_typ_pu.append(om_typ_pu)
    list_var_om_typ_pu.append(var_om_typ_pu)
    var_om_typ_pu.trace_add("write", lambda name, mode, index, sv=list_var_om_typ_pu: determine_pu_type(sv.index(var_om_typ_pu)))

    var_om_konstrukcni_system_pu = tk.StringVar()
    om_konstrukcni_system_pu = ctk.CTkOptionMenu(list_PBR_frames[0], values=["", "nehořlavý", "smíšený", "hořlavý"], variable=var_om_konstrukcni_system_pu)
    om_konstrukcni_system_pu.grid(row=len(list_pu_number)+1, column=1)
    list_om_konstrukcni_system_pu.append(om_konstrukcni_system_pu)
    list_var_om_konstrukcni_system.append(var_om_konstrukcni_system_pu)
    var_om_konstrukcni_system_pu.trace_add("write", lambda name, index, mode, sv=list_var_om_konstrukcni_system: calculate_max_dimensions())
    var_om_konstrukcni_system_pu.trace_add("write", lambda name, index, mode, sv=list_var_e_pozarni_vyska: determine_SPB())

    e_oznaceni_pu = ctk.CTkEntry(list_PBR_frames[0])
    e_oznaceni_pu.grid(row=len(list_pu_number)+1, column=2)
    e_oznaceni_pu.bind("<FocusOut>", pu_rename)
    list_cisla_pu.append(e_oznaceni_pu)

    e_nazev_pu = ctk.CTkEntry(list_PBR_frames[0])
    e_nazev_pu.grid(row=len(list_pu_number)+1, column=3)
    e_nazev_pu.bind("<FocusOut>", pu_rename)
    list_nazvy_pu.append(e_nazev_pu)

    var_l_pv = tk.IntVar()
    l_pv = ctk.CTkLabel(list_PBR_frames[0], textvariable=var_l_pv)
    l_pv.grid(row=len(list_pu_number)+1, column=4)
    list_l_pv.append(l_pv)
    list_var_l_pv.append(var_l_pv)

    var_l_SPB = tk.StringVar()
    l_SPB = ctk.CTkLabel(list_PBR_frames[0], textvariable=var_l_SPB)
    l_SPB.grid(row=len(list_pu_number)+1, column=5)
    list_l_SPB.append(l_SPB)
    list_var_l_SPB.append(var_l_SPB)

    # tvorba rámečků
    f_PU = ctk.CTkFrame(window[0])
    f_PU.place(rely=0.7, relheight=0.3, relwidth=1)
    f_info_PU = ctk.CTkFrame(window[0])
    f_info_PU.place(rely=0.5, relheight=0.2, relwidth=1)
    list_f_info_PU.append(f_info_PU)
    list_f_PU.append(f_PU)
    # zařazení rámečku požárního úseku do listu a jeho nastavení jako current frame
    current_frame[0] = list_f_PU.index(f_PU)

def remove_f():
    if len(list_pu_number) != 0:
        if list_om_typ_pu[current_frame[0]].get() == "":
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
            list_l_SPB[current_frame[0]].destroy()
            list_l_SPB.pop(current_frame[0])
            list_var_l_SPB.pop(current_frame[0])
            list_var_l_pv.pop(current_frame[0])
            list_pu_number.pop(current_frame[0])
            if len(list_f_PU) != 0:
                list_f_PU[current_frame[0]].destroy()
                list_f_PU.pop(current_frame[0])
                current_frame[0] -= 1
        else:
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
            list_l_SPB[current_frame[0]].destroy()
            list_l_SPB.pop(current_frame[0])
            list_var_l_SPB.pop(current_frame[0])
            list_var_l_pv.pop(current_frame[0])

            list_pu_number.pop(current_frame[0])
            list_e_pocty_podlazi_pu.pop(current_frame[0])
            list_e_sirky_pu.pop(current_frame[0])
            list_e_delky_pu.pop(current_frame[0])
            list_vyskove_polohy_pu.pop(current_frame[0])
            list_mezni_pocty_podlazi.pop(current_frame[0])
            list_mezni_delky.pop(current_frame[0])
            list_mezni_sirky.pop(current_frame[0])

            for i in range(len(list_om_typ_pu)):
                element = list_om_typ_pu[i]
                element.grid(row=list_om_typ_pu.index(element)+2, column=0)
            for i in range(len(list_om_konstrukcni_system_pu)):
                element = list_om_konstrukcni_system_pu[i]
                element.grid(row=list_om_konstrukcni_system_pu.index(element)+2, column=1)
            for i in range(len(list_cisla_pu)):
                element = list_cisla_pu[i]
                element.grid(row=list_cisla_pu.index(element)+2, column=2)
            for i in range(len(list_nazvy_pu)):
                element = list_nazvy_pu[i]
                element.grid(row=list_nazvy_pu.index(element)+2, column=3)
            for i in range(len(list_l_pv)):
                element = list_l_pv[i]
                element.grid(row=list_l_pv.index(element)+2, column=4)
            for i in range(len(list_l_SPB)):
                element = list_l_SPB[i]
                element.grid(row=list_l_SPB.index(element)+2, column=5)
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
                if 0 <= current_frame[0] < len(list_pn):
                    list_pn.pop(current_frame[0])
                if 0 <= current_frame[0] < len(list_hs):
                    list_hs.pop(current_frame[0])
                if 0 <= current_frame[0] < len(list_an):
                    list_an.pop(current_frame[0])
                if 0 <= current_frame[0] < len(list_ps):
                    list_ps.pop(current_frame[0])
                if 0 <= current_frame[0] < len(list_a):
                    list_a.pop(current_frame[0])
                if 0 <= current_frame[0] < len(list_ho):
                    list_ho.pop(current_frame[0])
                if 0 <= current_frame[0] < len(list_so):
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

def determine_pu_type(index):
    if list_var_om_typ_pu[index].get() == "nevýrobní":
        add_pu_f_nevyrobni(index)
    elif list_var_om_typ_pu[index].get() == "OB1":
        add_pu_f_OB1(index)



