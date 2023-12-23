from pu_plus_and_minus import *
from lists_and_dictionaries import *
import tkinter as tk
import customtkinter as ctk

def add_pu_f_OB1(index):
    # listy pro nový požární úsek
    m_rows = [1]
    o_rows = [1]
    m_S_entries = []
    m_CSNi_entries = []
    m_ps_entries = []
    m_mc_text_entries = []
    m_nazvy_m_text_entries = []
    m_ps_labels = []
    m_pni_entries = []
    m_ani_entries = []
    m_ps_group_sums = []
    m_hsi_entries = []
    list_pocet_ot = []
    list_sirka_ot = []
    list_vyska_ot = []

    m_S_var_entries = []
    m_ps_var_entries = []
    m_ps_var_labels = []
    m_pni_var_entries = []
    m_ani_var_entries = []
    m_hsi_var_entries = []
    o_pocet_var_entries = []
    o_sirka_var_entries = []
    o_vyska_var_entries = []
    o_typ_option_menues = []

    # přiřazení nových listů do nadlistů umístěných mimo funkci
    dic_S_var_entries.append(m_S_var_entries)
    dic_ps_var_entries.append(m_ps_var_entries)
    dic_var_ps_labels.append(m_ps_var_labels)
    dic_pni_var_entries.append(m_pni_var_entries)
    dic_ani_var_entries.append(m_ani_var_entries)
    dic_hsi_var_entries.append(m_hsi_var_entries)

    dic_S_entries.append(m_S_entries)
    dic_CSNi_entries.append(m_CSNi_entries)
    dic_psi_entries.append(m_ps_entries)
    dic_pni_entries.append(m_pni_entries)
    dic_ani_entries.append(m_ani_entries)
    dic_hsi_entries.append(m_hsi_entries)
    dic_ps_row_sum_labels.append(m_ps_labels)
    dic_m_rows.append(m_rows)
    dic_o_rows.append(o_rows)
    dic_mc_text_entries.append(m_mc_text_entries)
    dic_nazvy_m_text_entries.append(m_nazvy_m_text_entries)
    dic_ps_group_sums.append(m_ps_group_sums)

    dic_var_pocet_ot.append(o_pocet_var_entries)
    dic_var_sirka_ot.append(o_sirka_var_entries)
    dic_var_vyska_ot.append(o_vyska_var_entries)

    dic_typy_ot_option_menues.append(o_typ_option_menues)
    dic_pocet_ot_entries.append(list_pocet_ot)
    dic_sirka_ot_entries.append(list_sirka_ot)
    dic_vyska_ot_entries.append(list_vyska_ot)

    list_a.append(0)
    list_k.append(0)
    list_b.append(0)
    list_p.append(0)
    list_pocty_podlazi_pu.append(0)
    list_sirky_pu.append(0)
    list_delky_pu.append(0)
    list_vyskove_polohy_pu.append(0)
    list_mezni_pocty_podlazi.append(0)
    list_mezni_delky.append(0)
    list_mezni_sirky.append(0)

    # vytvoření míst v listech pro jednotlivé parametry PÚ
    list_pv.append(0)

# nadpis požárního úseku
    l_nazev_pu_default = ctk.CTkLabel(list_f_info_PU[index], text="Požární úsek č. ", anchor="center")
    l_nazev_pu_default.grid(row=0, column=0, columnspan=12)
    list_nazvy_pu_default[current_frame[0]] = l_nazev_pu_default
    list_nazvy_pu_default[current_frame[0]].configure(text="požární úsek č. " + str(current_frame[0] + 1))

# výpočtové hodnoty pro celý PÚ
    l_factor_a = ctk.CTkLabel(list_f_info_PU[index], text="součinitel a")
    l_factor_a.grid(row=1, column=0)
    l_c_factor = ctk.CTkLabel(list_f_info_PU[index], text="součinitel c")
    l_c_factor.grid(row=2, column=0)
    l_CSN_pv = ctk.CTkLabel(list_f_info_PU[index], text="pv")
    l_CSN_pv.grid(row=3, column=0)

    e_factor_a = ctk.CTkEntry(list_f_info_PU[index], width=80)
    list_a.append(e_factor_a)
    e_factor_a.grid(row=1, column=1)
    e_factor_a.insert(0, "0")
    e_factor_a.bind("<FocusIn>", lambda event: e_factor_a.delete(0, tk.END) if e_factor_a.get() == "0" else None)
    e_factor_a.bind("<FocusOut>", lambda event: e_factor_a.insert(0, "0") if e_factor_a.get() == "" else None)

    e_factor_c = ctk.CTkEntry(list_f_info_PU[index], width=80)
    list_c.append(e_factor_c)
    e_factor_c.grid(row=2, column=1)
    e_factor_c.insert(0, "0")
    e_factor_c.bind("<FocusIn>", lambda event: e_factor_c.delete(0, tk.END) if e_factor_c.get() == "0" else None)
    e_factor_c.bind("<FocusOut>", lambda event: e_factor_c.insert(0, "0") if e_factor_c.get() == "" else None)

    var_CSN_pv = tk.StringVar()
    e_CSN_pv = ctk.CTkEntry(list_f_info_PU[index], width=80, textvariable=var_CSN_pv)
    list_CSN_pv.append(e_CSN_pv)
    e_CSN_pv.grid(row=3, column=1)
    e_CSN_pv.insert(0, "0")
    e_CSN_pv.bind("<FocusIn>", lambda event: e_CSN_pv.delete(0, tk.END) if e_CSN_pv.get() == "0" else None)
    e_CSN_pv.bind("<FocusOut>", lambda event: e_CSN_pv.insert(0, "0") if e_CSN_pv.get() == "" else None)
    var_CSN_pv.trace_add("write", lambda name, index, mode, sv=var_CSN_pv: calculate_short_pv_value)

    # nadpis sloupců místností
    l_cm = ctk.CTkLabel(list_f_PU[index], text="č. m.", anchor="center", width=40)
    l_cm.grid(row=1, column=0)
    l_nazev_m = ctk.CTkLabel(list_f_PU[index], text="název místnosti", anchor="center", width=200)
    l_nazev_m.grid(row=1, column=1)
    l_S = ctk.CTkLabel(list_f_PU[index], text="plocha místnosti", anchor="center", width=80, wraplength=60)
    l_S.grid(row=1, column=2)
    l_ps_d = ctk.CTkLabel(list_f_PU[index], text="psi dveře", anchor="center", width=80, wraplength=50)
    l_ps_d.grid(row=1, column=3)
    l_ps_o = ctk.CTkLabel(list_f_PU[index], text="psi okna", anchor="center", width=80, wraplength=40)
    l_ps_o.grid(row=1, column=4)
    l_ps_p = ctk.CTkLabel(list_f_PU[index], text="psi podlahy", anchor="center", width=80, wraplength=50)
    l_ps_p.grid(row=1, column=5)
    l_psi_sum = ctk.CTkLabel(list_f_PU[index], text="psi celkem", anchor="center", width=80, wraplength=60)
    l_psi_sum.grid(row=1, column=6)

# výsledné hodnoty (S a ps)
    for i in range(4):
        l_mezera = ctk.CTkLabel(list_f_info_PU[index], text="", width=250)
        l_mezera.grid(row=1+i, column=4)

    l_text_S = ctk.CTkLabel(list_f_info_PU[index], text="S celkem: ")
    l_text_S.grid(row=1, column=5)
    l_text_ps = ctk.CTkLabel(list_f_info_PU[index], text="ps celkem: ")
    l_text_ps.grid(row=2, column=5)

    var_l_S = tk.DoubleVar()
    l_S = ctk.CTkLabel(list_f_info_PU[index], text="0.0", textvariable=var_l_S)
    l_S.grid(row=1, column=6)
    list_l_S.append(var_l_S)
    var_l_ps = tk.DoubleVar()
    l_ps = ctk.CTkLabel(list_f_info_PU[index], text="0.0", textvariable=var_l_ps)
    l_ps.grid(row=2, column=6)
    list_l_ps.append(var_l_ps)

    if len(list_f_PU) >= 1:
        b_new_row = ctk.CTkButton(list_f_PU[index], text="+", command=lambda:OB1_m_plus(), width=25, height=25)
        b_new_row.grid(row=2, column=7)
        b_remove_row = ctk.CTkButton(list_f_PU[index], text="-", command=lambda:OB1_m_minus(), width=25, height=25)
        b_remove_row.grid(row=3, column=7)