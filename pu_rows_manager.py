from add_frame_nevyrobni import *
from remove_and_rename_frame import *
from add_frame_vyrobni import *
from tkinter import messagebox


def add_new_pu(window):
    list_pu_number.append(1)
    list_nazvy_pu_default.append(1)

    # widgety pro požární úsek v rámečku pro celý objekt
    var_om_typ_pu = ctk.StringVar()
    om_typ_pu = ctk.CTkOptionMenu(list_PBR_frames[0], values=["", "nevýrobní", "výrobní", "OB1", "OB2", "garáž", "sklad"], variable=var_om_typ_pu)
    om_typ_pu.grid(row=len(list_pu_number), column=0)
    list_om_typ_pu.append(om_typ_pu)
    list_var_om_typ_pu.append(var_om_typ_pu)
    var_om_typ_pu.trace_add("write", lambda name, mode, index, sv=list_var_om_typ_pu: determine_pu_type(sv.index(var_om_typ_pu), window))

    om_konstrukcni_system_pu = ctk.CTkOptionMenu(list_PBR_frames[0], values=["nehořlavý", "smíšený", "hořlavý"])
    om_konstrukcni_system_pu.grid(row=len(list_pu_number), column=1)
    list_om_konstrukcni_system_pu.append(om_konstrukcni_system_pu)

    e_oznaceni_pu = ctk.CTkEntry(list_PBR_frames[0])
    e_oznaceni_pu.grid(row=len(list_pu_number), column=2)
    e_oznaceni_pu.bind("<FocusOut>", pu_rename)
    list_cisla_pu.append(e_oznaceni_pu)

    e_nazev_pu = ctk.CTkEntry(list_PBR_frames[0])
    e_nazev_pu.grid(row=len(list_pu_number), column=3)
    e_nazev_pu.bind("<FocusOut>", pu_rename)
    list_nazvy_pu.append(e_nazev_pu)

    var_l_pv = tk.IntVar()
    l_pv = ctk.CTkLabel(list_PBR_frames[0], textvariable=var_l_pv)
    l_pv.grid(row=len(list_pu_number), column=4)
    list_l_pv.append(l_pv)
    list_var_l_pv.append(var_l_pv)

    var_l_SPB = tk.StringVar()
    l_SPB = ctk.CTkLabel(list_PBR_frames[0], textvariable=var_l_SPB)
    l_SPB.grid(row=len(list_pu_number), column=5)
    list_l_SPB.append(l_SPB)
    list_var_l_SPB.append(var_l_SPB)

    # tvorba rámečků
    f_PU = ctk.CTkFrame(window)
    f_PU.place(rely=0.7, relheight=0.3, relwidth=1)
    f_info_PU = ctk.CTkFrame(window)
    f_info_PU.place(rely=0.5, relheight=0.2, relwidth=1)
    list_f_info_PU.append(f_info_PU)
    list_f_PU.append(f_PU)
    # zařazení rámečku požárního úseku do listu a jeho nastavení jako current frame
    current_frame[0] = list_f_PU.index(f_PU)

def determine_pu_type(index, window):
    add_pu_f_nevyrobni(index, current_frame, list_l_S, list_l_an, list_l_pn, list_l_ps, list_l_p, list_l_a, list_l_hs, list_l_so, list_l_ho, list_mezni_pocty_podlazi, list_f_info_PU, list_f_PU)
