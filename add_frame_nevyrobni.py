from pu_plus_and_minus import *
from m_plus_and_minus import *
from o_plus_and_minus import *

def add_pu_f_nevyrobni(index):
    global om_konstrukcni_system
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

# vytvoření míst v listech pro jednotlivé parametry PÚ
    list_pv.append(0)

# nadpis požárního úseku a obecné informace o něm
    l_nazev_pu_default = ctk.CTkLabel(list_f_info_PU[index], text="Požární úsek č. ", anchor="center")
    l_nazev_pu_default.grid(row=0, column=0, columnspan=12)
    list_nazvy_pu_default[current_frame[0]] = l_nazev_pu_default
    list_nazvy_pu_default[current_frame[0]].configure(text="požární úsek č. " + str(list_nazvy_pu_default.index(l_nazev_pu_default) + 1))
    print(list_nazvy_pu_default.index(l_nazev_pu_default))

    l_vyska_pu = ctk.CTkLabel(list_f_info_PU[index], text="výšková poloha PÚ")
    l_vyska_pu.grid(row=1, column=0)
    l_pocet_podlazi_pu = ctk.CTkLabel(list_f_info_PU[index], text="počet podlaží PÚ")
    l_pocet_podlazi_pu.grid(row=2, column=0)
    l_sirka_pu = ctk.CTkLabel(list_f_info_PU[index], text="max. skutečná šířka")
    l_sirka_pu.grid(row=3, column=0)
    l_delka_pu = ctk.CTkLabel(list_f_info_PU[index], text="max. skutečná délka")
    l_delka_pu.grid(row=4, column=0)

    e_vyskova_poloha_pu = ctk.CTkEntry(list_f_info_PU[index], width=80)
    list_vyskove_polohy_pu.append(e_vyskova_poloha_pu)
    e_vyskova_poloha_pu.grid(row=1, column=1)
    e_vyskova_poloha_pu.insert(0, "0")
    e_vyskova_poloha_pu.bind("<FocusIn>", lambda event: e_vyskova_poloha_pu.delete(0,tk.END) if e_vyskova_poloha_pu.get() == "0" else None)
    e_vyskova_poloha_pu.bind("<FocusOut>", lambda event: e_vyskova_poloha_pu.insert(0,"0") if e_vyskova_poloha_pu.get() == "" else None)

    e_pocet_podlazi_pu = ctk.CTkEntry(list_f_info_PU[index], width=80)
    list_pocty_podlazi_pu.append(e_pocet_podlazi_pu)
    e_pocet_podlazi_pu.grid(row=2, column=1)
    e_pocet_podlazi_pu.insert(0, "0")
    e_pocet_podlazi_pu.bind("<FocusIn>", lambda event: e_pocet_podlazi_pu.delete(0,tk.END) if e_pocet_podlazi_pu.get() == "0" else None)
    e_pocet_podlazi_pu.bind("<FocusOut>",lambda event: e_pocet_podlazi_pu.insert(0, "0") if e_pocet_podlazi_pu.get() == "" else None)

    var_e_sirka_pu = tk.StringVar()
    e_sirka_pu = ctk.CTkEntry(list_f_info_PU[index], width=80, textvariable=var_e_sirka_pu)
    list_sirky_pu.append(e_sirka_pu)
    e_sirka_pu.grid(row=3, column=1)
    e_sirka_pu.insert(0, "0")
    e_sirka_pu.bind("<FocusIn>", lambda event: e_sirka_pu.delete(0, tk.END) if e_sirka_pu.get() == "0" else None)
    e_sirka_pu.bind("<FocusOut>", lambda event: e_sirka_pu.insert(0, "0") if e_sirka_pu.get() == "" else None)
    var_e_sirka_pu.trace_add("write", lambda name, index, mode, sv=var_e_sirka_pu: calculate_pv_value(current_frame))

    var_e_delka_pu = tk.StringVar()
    e_delka_pu = ctk.CTkEntry(list_f_info_PU[index], width=80, textvariable=var_e_delka_pu)
    list_delky_pu.append(var_e_delka_pu)
    e_delka_pu.grid(row=4, column=1)
    e_delka_pu.insert(0, "0")
    e_delka_pu.bind("<FocusIn>", lambda event: e_delka_pu.delete(0, tk.END) if e_delka_pu.get() == "0" else None)
    e_delka_pu.bind("<FocusOut>", lambda event: e_delka_pu.insert(0, "0") if e_delka_pu.get() == "" else None)
    var_e_delka_pu.trace_add("write", lambda name, index, mode, sv=var_e_delka_pu: calculate_pv_value(current_frame))

    for i in range(4):
        l_mezera = ctk.CTkLabel(list_f_info_PU[index], text="", width=50)
        l_mezera.grid(row=1+i, column=2)

    l_nadpis_mazni_parametry_pu = ctk.CTkLabel(list_f_info_PU[index], text="Mezní parametry")
    l_nadpis_mazni_parametry_pu.grid(row=1, column=3)
    var_l_mezni_pocet_podlazi = tk.DoubleVar()
    l_mezni_pocet_podlazi = ctk.CTkLabel(list_f_info_PU[index], textvariable = var_l_mezni_pocet_podlazi)
    l_mezni_pocet_podlazi.grid(row=2, column=3)
    list_mezni_pocty_podlazi.append(var_l_mezni_pocet_podlazi)

    var_l_mezni_sirka = tk.DoubleVar()
    l_mezni_sirka = ctk.CTkLabel(list_f_info_PU[index], textvariable = var_l_mezni_sirka)
    l_mezni_sirka.grid(row=4, column=3)
    list_mezni_sirky.append(var_l_mezni_sirka)

    var_l_mezni_delka = tk.DoubleVar()
    l_mezni_delka = ctk.CTkLabel(list_f_info_PU[index], textvariable = var_l_mezni_delka)
    l_mezni_delka.grid(row=3, column=3)
    list_mezni_delky.append(var_l_mezni_delka)

    for i in range(4):
        l_mezera = ctk.CTkLabel(list_f_info_PU[index], text="", width=250)
        l_mezera.grid(row=1+i, column=4)

    l_text_S = ctk.CTkLabel(list_f_info_PU[index], text="S celkem: ")
    l_text_S.grid(row=1, column=5)
    l_text_pn = ctk.CTkLabel(list_f_info_PU[index], text="pn celkem: ")
    l_text_pn.grid(row=2, column=5)
    l_text_an = ctk.CTkLabel(list_f_info_PU[index], text="an celkem: ")
    l_text_an.grid(row=3, column=5)
    l_text_ps = ctk.CTkLabel(list_f_info_PU[index], text="ps celkem: ")
    l_text_ps.grid(row=4, column=5)

    var_l_S = tk.DoubleVar()
    l_S = ctk.CTkLabel(list_f_info_PU[index], text="0.0", textvariable=var_l_S)
    l_S.grid(row=1, column=6)
    list_l_S.append(var_l_S)
    var_l_pn = tk.DoubleVar()
    l_pn = ctk.CTkLabel(list_f_info_PU[index], text="0.0", textvariable=var_l_pn)
    l_pn.grid(row=2, column=6)
    list_l_pn.append(var_l_pn)
    var_l_an = tk.DoubleVar()
    l_an = ctk.CTkLabel(list_f_info_PU[index], text="0.0", textvariable=var_l_an)
    l_an.grid(row=3, column=6)
    list_l_an.append(var_l_an)
    var_l_ps = tk.DoubleVar()
    l_ps = ctk.CTkLabel(list_f_info_PU[index], text="0.0", textvariable=var_l_ps)
    l_ps.grid(row=4, column=6)
    list_l_ps.append(var_l_ps)

    for i in range(4):
        l_mezera = ctk.CTkLabel(list_f_info_PU[index], text="", width=100)
        l_mezera.grid(row=1+i, column=7)

    l_text_p = ctk.CTkLabel(list_f_info_PU[index], text="p celkem: ")
    l_text_p.grid(row=1, column=8)
    l_text_a = ctk.CTkLabel(list_f_info_PU[index], text="a celkem: ")
    l_text_a.grid(row=2, column=8)
    l_text_n = ctk.CTkLabel(list_f_info_PU[index], text="n celkem: ")
    l_text_n.grid(row=3, column=8)
    l_text_k = ctk.CTkLabel(list_f_info_PU[index], text="k celkem: ")
    l_text_k.grid(row=4, column=8)

    var_l_p = tk.DoubleVar()
    l_p = ctk.CTkLabel(list_f_info_PU[index], text="0.0", textvariable=var_l_p)
    l_p.grid(row=1, column=9)
    list_l_p.append(var_l_p)
    var_l_a = tk.DoubleVar()
    l_a = ctk.CTkLabel(list_f_info_PU[index], text="0.0", textvariable=var_l_a)
    l_a.grid(row=2, column=9)
    list_l_a.append(var_l_a)
    var_l_n = tk.DoubleVar()
    l_n = ctk.CTkLabel(list_f_info_PU[index], text="0.0", textvariable=var_l_n)
    l_n.grid(row=3, column=9)
    list_l_n.append(var_l_n)
    var_l_k = tk.DoubleVar()
    l_k = ctk.CTkLabel(list_f_info_PU[index], text="0.0", textvariable=var_l_k)
    l_k.grid(row=4, column=9)
    list_l_k.append(var_l_k)

    for i in range(4):
        l_mezera = ctk.CTkLabel(list_f_info_PU[index], text="", width=100)
        l_mezera.grid(row=1+i, column=10)

    l_text_b = ctk.CTkLabel(list_f_info_PU[index], text="b celkem: ")
    l_text_b.grid(row=1, column=11)
    l_text_hs = ctk.CTkLabel(list_f_info_PU[index], text="hs celkem: ")
    l_text_hs.grid(row=2, column=11)
    l_text_So = ctk.CTkLabel(list_f_info_PU[index], text="So celkem: ")
    l_text_So.grid(row=3, column=11)
    l_text_ho = ctk.CTkLabel(list_f_info_PU[index], text="ho celkem: ")
    l_text_ho.grid(row=4, column=11)

    var_l_b = tk.DoubleVar()
    l_b = ctk.CTkLabel(list_f_info_PU[index], text="0.0", textvariable=var_l_b)
    l_b.grid(row=1, column=12)
    list_l_b.append(var_l_b)
    var_l_hs = tk.DoubleVar()
    l_hs = ctk.CTkLabel(list_f_info_PU[index], text="0.0", textvariable=var_l_hs)
    l_hs.grid(row=2, column=12)
    list_l_hs.append(var_l_hs)
    var_l_so = tk.DoubleVar()
    l_so = ctk.CTkLabel(list_f_info_PU[index], text="0.0", textvariable=var_l_so)
    l_so.grid(row=3, column=12)
    list_l_so.append(var_l_so)
    var_l_ho = tk.DoubleVar()
    l_ho = ctk.CTkLabel(list_f_info_PU[index], text="0.0", textvariable=var_l_ho)
    l_ho.grid(row=4, column=12)
    list_l_ho.append(var_l_ho)

#nadpis sloupců v rámečku
    l_cm = ctk.CTkLabel(list_f_PU[index], text="č. m.", anchor="center", width=40)
    l_cm.grid(row=1, column=0)
    l_nazev_m = ctk.CTkLabel(list_f_PU[index], text="název místnosti", anchor="center", width=200)
    l_nazev_m.grid(row=1, column=1)
    l_S = ctk.CTkLabel(list_f_PU[index], text="plocha místnosti", anchor="center", width=80, wraplength=60)
    l_S.grid(row=1, column=2)
    l_hsi_m = ctk.CTkLabel(list_f_PU[index], text="hsi", anchor="center", width=80)
    l_hsi_m.grid(row=1, column=3)
    l_polozka_CSN_m = ctk.CTkLabel(list_f_PU[index], text="CSN", anchor="center", width=80)
    l_polozka_CSN_m.grid(row=1, column=4)
    l_pn_m = ctk.CTkLabel(list_f_PU[index], text="pni", anchor="center", width=80)
    l_pn_m.grid(row=1, column=5)
    l_an_m = ctk.CTkLabel(list_f_PU[index], text="ani", anchor="center", width=80)
    l_an_m.grid(row=1, column=6)
    l_ps_d = ctk.CTkLabel(list_f_PU[index], text="psi dveře", anchor="center", width=80, wraplength=50)
    l_ps_d.grid(row=1, column=7)
    l_ps_o = ctk.CTkLabel(list_f_PU[index], text="psi okna", anchor="center", width=80, wraplength=40)
    l_ps_o.grid(row=1, column=8)
    l_ps_p = ctk.CTkLabel(list_f_PU[index], text="psi podlahy", anchor="center", width=80, wraplength=50)
    l_ps_p.grid(row=1, column=9)
    l_psi_sum = ctk.CTkLabel(list_f_PU[index], text="psi celkem", anchor="center", width=80, wraplength=60)
    l_psi_sum.grid(row=1, column=10)


# nadpisy tabulky otvorů
    l_typ_ot = ctk.CTkLabel(list_f_PU[index], text="typ otvoru", anchor="center",  width=80, wraplength=50)
    l_typ_ot.grid(row=1, column=12)
    l_pocet_ot = ctk.CTkLabel(list_f_PU[index], text="počet otvorů", anchor="center",  width=80, wraplength=50)
    l_pocet_ot.grid(row=1, column=13)
    l_sirka_ot = ctk.CTkLabel(list_f_PU[index], text="šířka otvoru", anchor="center",  width=80, wraplength=50)
    l_sirka_ot.grid(row=1, column=14)
    l_vyska_ot = ctk.CTkLabel(list_f_PU[index], text="výška otvoru", anchor="center",  width=80, wraplength=50)
    l_vyska_ot.grid(row=1, column=15)

    if len(list_f_PU) >= 1:
        b_new_row = ctk.CTkButton(list_f_PU[index], text="+", command=lambda:PU_m_plus(current_frame), width=25, height=25)
        b_new_row.grid(row=2, column=11)
        b_remove_row = ctk.CTkButton(list_f_PU[index], text="-", command=lambda:m_minus(current_frame), width=25, height=25)
        b_remove_row.grid(row=3, column=11)
        b_new_hole = ctk.CTkButton(list_f_PU[index], text="+", command=lambda:o_plus(current_frame), width=25, height=25)
        b_new_hole.grid(row=2, column=16)
        b_remove_hole = ctk.CTkButton(list_f_PU[index], text="-", command=lambda:o_minus(current_frame), width=25, height=25)
        b_remove_hole.grid(row=3, column=16)




