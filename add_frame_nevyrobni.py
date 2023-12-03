from table_manager import *
import tkinter as tk
import customtkinter as ctk

def add_f(window, list_f_PU,list_l_S, list_l_an, list_l_pn,list_l_ps, list_l_p, list_l_a,
          list_l_hs, list_l_so, list_l_ho, f_seznam_PU, list_mezni_pocty_podlazi):
    global current_frame, om_konstrukcni_system
# listy pro nový požární úsek
    m_rows = [1]
    o_rows = [1]
    m_S_entries = []
    m_ps_entries = []
    m_text_entries = []
    m_ps_labels = []
    m_pni_entries = []
    m_ani_entries = []
    m_ps_group_sums = []
    m_hsi_entries = []
    list_pocet_ot = []
    list_sirka_ot = []
    list_vyska_ot = []
    list_so_ot = []
    m_S_var_entries = []
    m_ps_var_entries = []
    m_pni_var_entries = []
    m_ani_var_entries = []
    m_hsi_var_entries = []
    o_pocet_var_entries = []
    o_sirka_var_entries = []
    o_vyska_var_entries = []

# přiřazení nových listů do nadlistů mimo funkci
    dic_S_var_entries.append(m_S_var_entries)
    dic_ps_var_entries.append(m_ps_var_entries)
    dic_ps_labels.append(m_ps_labels)
    dic_pni_var_entries.append(m_pni_var_entries)
    dic_ani_var_entries.append(m_ani_var_entries)
    dic_hsi_var_entries.append(m_hsi_var_entries)

    dic_S_entries.append(m_S_entries)
    dic_ps_entries.append(m_ps_entries)
    dic_pni_entries.append(m_pni_entries)
    dic_ani_entries.append(m_ani_entries)
    dic_hsi_entries.append(m_hsi_entries)

    dic_m_rows.append(m_rows)
    dic_o_rows.append(o_rows)
    dic_text_entries.append(m_text_entries)
    dic_ps_group_sums.append(m_ps_group_sums)

    dic_var_pocet_ot.append(o_pocet_var_entries)
    dic_var_sirka_ot.append(o_sirka_var_entries)
    dic_var_vyska_ot.append(o_vyska_var_entries)
    dic_so_ot.append(list_so_ot)

    dic_pocet_ot.append(list_pocet_ot)
    dic_sirka_ot.append(list_sirka_ot)
    dic_vyska_ot.append(list_vyska_ot)
    dic_so_ot.append(list_so_ot)

# tvorba rámečku
    f_PU = ctk.CTkFrame(window, width=500, height=500)
    f_PU.place(rely= 0.5, relheight=0.5, relwidth= 1)

# zařazení rámečku požárního úseku do listu a jeho nastavení jako current frame
    list_f_PU.append(f_PU)
    current_frame = list_f_PU.index(f_PU)

#nadpis požárního úseku a obecné informace o něm
    f_parametry_pu = ctk.CTkFrame(f_PU)
    f_parametry_pu.grid(row=0, column=0, columnspan=3)
    l_nazev_pu_default = ctk.CTkLabel(f_parametry_pu, text="Požární úsek č. ", anchor="center", width=6)
    l_nazev_pu_default.grid(row=0, column=0, columnspan=15)
    list_nazvy_default.append(l_nazev_pu_default)
    l_vyska_pu = ctk.CTkLabel(f_parametry_pu, text="výšková poloha PÚ")
    l_vyska_pu.grid(row=1, column=0)
    l_pocet_podlazi_pu = ctk.CTkLabel(f_parametry_pu, text="počet podlaží PÚ")
    l_pocet_podlazi_pu.grid(row=2, column=0)
    l_sirka_pu = ctk.CTkLabel(f_parametry_pu, text="max. skutečná šířka")
    l_sirka_pu.grid(row=3, column=0)
    l_delka_pu = ctk.CTkLabel(f_parametry_pu, text="max. skutečná délka")
    l_delka_pu.grid(row=4, column=0)
    list_nazvy_default[current_frame].configure(text="požární úsek č. " + str(current_frame+1))
    var_l_mezni_pocet_podlazi = tk.DoubleVar()
    l_mezni_pocet_podlazi = ctk.CTkLabel(f_parametry_pu, text="mezní počet podlaží", textvariable = var_l_mezni_pocet_podlazi)
    l_mezni_pocet_podlazi.grid(row=2, column=2)
    list_mezni_pocty_podlazi.append(var_l_mezni_pocet_podlazi)

    var_l_mezni_sirka = tk.StringVar()
    l_mezni_sirka = ctk.CTkLabel(f_parametry_pu, text="mezní šířka PÚ", textvariable = var_l_mezni_sirka)
    l_mezni_sirka.grid(row=4, column=2)
    list_mezni_sirky.append(var_l_mezni_sirka)

    var_l_mezni_delka = tk.StringVar()
    l_mezni_delka = ctk.CTkLabel(f_parametry_pu, text="mezní délka PÚ", textvariable = var_l_mezni_delka)
    l_mezni_delka.grid(row=3, column=2)
    list_mezni_delky.append(var_l_mezni_delka)

    e_vyskova_poloha_pu = ctk.CTkEntry(f_parametry_pu, width=80)
    list_vyskove_polohy_pu.append(e_vyskova_poloha_pu)
    e_vyskova_poloha_pu.grid(row=1, column=1)
    e_vyskova_poloha_pu.insert(0, "0")
    e_vyskova_poloha_pu.bind("<FocusIn>", lambda event: e_vyskova_poloha_pu.delete(0, tk.END) if e_vyskova_poloha_pu.get() == "0" else None)
    e_vyskova_poloha_pu.bind("<FocusOut>", lambda event: e_vyskova_poloha_pu.insert(0, "0") if e_vyskova_poloha_pu.get() == "" else None)
    e_pocet_podlazi_pu = ctk.CTkEntry(f_parametry_pu, width=80)
    list_pocty_podlazi_pu.append(e_pocet_podlazi_pu)
    e_pocet_podlazi_pu.grid(row=2, column=1)
    e_pocet_podlazi_pu.insert(0, "0")
    e_pocet_podlazi_pu.bind("<FocusIn>", lambda event: e_pocet_podlazi_pu.delete(0, tk.END) if e_pocet_podlazi_pu.get() == "0" else None)
    e_pocet_podlazi_pu.bind("<FocusOut>", lambda event: e_pocet_podlazi_pu.insert(0, "0") if e_pocet_podlazi_pu.get() == "" else None)

    var_e_sirka_pu = tk.StringVar()
    e_sirka_pu = ctk.CTkEntry(f_parametry_pu, width=80, textvariable= var_e_sirka_pu)
    list_sirky_pu.append(e_sirka_pu)
    e_sirka_pu.grid(row=3, column=1)
    e_sirka_pu.insert(0, "0")
    e_sirka_pu.bind("<FocusIn>", lambda event: e_sirka_pu.delete(0, tk.END) if e_sirka_pu.get() == "0" else None)
    e_sirka_pu.bind("<FocusOut>", lambda event: e_sirka_pu.insert(0, "0") if e_sirka_pu.get() == "" else None)
    var_e_sirka_pu.trace_add("write", lambda name, index, mode, sv=var_e_sirka_pu: calculate_pv_value(current_frame))

    var_e_delka_pu = tk.StringVar()
    e_delka_pu = ctk.CTkEntry(f_parametry_pu, width=80, textvariable= var_e_delka_pu)
    list_delky_pu.append(var_e_delka_pu)
    e_delka_pu.grid(row=4, column=1)
    e_delka_pu.insert(0, "0")
    e_delka_pu.bind("<FocusIn>", lambda event: e_delka_pu.delete(0, tk.END) if e_delka_pu.get() == "0" else None)
    e_delka_pu.bind("<FocusOut>", lambda event: e_delka_pu.insert(0, "0") if e_delka_pu.get() == "" else None)
    var_e_delka_pu.trace_add("write", lambda name, index, mode, sv=var_e_delka_pu: calculate_pv_value(current_frame))

#nadpis sloupců v rámečku
    l_cm = ctk.CTkLabel(f_PU, text="č. m.", anchor="center", width=40)
    l_cm.grid(row=1, column=0)
    l_nazev_m = ctk.CTkLabel(f_PU, text="název místnosti", anchor="center", width=200)
    l_nazev_m.grid(row=1, column=1)
    l_S = ctk.CTkLabel(f_PU, text="plocha místnosti", anchor="center", width=80, wraplength=60)
    l_S.grid(row=1, column=2)
    l_pn_m = ctk.CTkLabel(f_PU, text="pni", anchor="center", width=80)
    l_pn_m.grid(row=1, column=3)
    l_hsi_m = ctk.CTkLabel(f_PU, text="hsi", anchor="center", width=80)
    l_hsi_m.grid(row=1, column=4)
    l_an_m = ctk.CTkLabel(f_PU, text="ani", anchor="center", width=80)
    l_an_m.grid(row=1, column=5)
    l_ps_d = ctk.CTkLabel(f_PU, text="psi dveře", anchor="center", width=80, wraplength=50)
    l_ps_d.grid(row=1, column=6)
    l_ps_o = ctk.CTkLabel(f_PU, text="psi okna", anchor="center", width=80, wraplength=40)
    l_ps_o.grid(row=1, column=7)
    l_ps_p = ctk.CTkLabel(f_PU, text="psi podlahy", anchor="center", width=80, wraplength=50)
    l_ps_p.grid(row=1, column=8)
    l_psi_sum = ctk.CTkLabel(f_PU, text="psi celkem", anchor="center", width=80, wraplength=60)
    l_psi_sum.grid(row=1, column=9)

# výsledky tabulky
    var_l_S = tk.DoubleVar()
    l_S = ctk.CTkLabel(f_PU, text="S celkem: ", textvariable=var_l_S)
    l_S_text = ctk.CTkLabel(f_PU, text= "S")
    l_S_text.grid(row=4, column = 11)
    l_S.grid(row=4, column=10)
    list_l_S.append(var_l_S)
    var_l_pn = tk.DoubleVar()
    l_pn = ctk.CTkLabel(f_PU, text="pn celkem: ", textvariable=var_l_pn)
    l_pn_text = ctk.CTkLabel(f_PU, text= "pn")
    l_pn_text.grid(row=5, column = 11)
    l_pn.grid(row=5, column=10)
    list_l_pn.append(var_l_pn)
    var_l_an = tk.DoubleVar()
    l_an = ctk.CTkLabel(f_PU, text="an celkem: ", textvariable=var_l_an)
    l_an_text = ctk.CTkLabel(f_PU, text= "an")
    l_an_text.grid(row=6, column = 11)
    l_an.grid(row=6, column=10)
    list_l_an.append(var_l_an)
    var_l_ps = tk.DoubleVar()
    l_ps = ctk.CTkLabel(f_PU, text="ps celkem: ", textvariable=var_l_ps)
    l_ps_text = ctk.CTkLabel(f_PU, text= "ps")
    l_ps_text.grid(row=7, column = 11)
    l_ps.grid(row=7, column=10)
    list_l_ps.append(var_l_ps)
    var_l_p = tk.DoubleVar()
    l_p = ctk.CTkLabel(f_PU, text="p celkem: ", textvariable=var_l_p)
    l_p_text = ctk.CTkLabel(f_PU, text= "p")
    l_p_text.grid(row=8, column = 11)
    l_p.grid(row=8, column=10)
    list_l_p.append(var_l_p)
    var_l_a = tk.DoubleVar()
    l_factor_a = ctk.CTkLabel(f_PU, text="součinitel a: ", textvariable=var_l_a)
    l_a_text = ctk.CTkLabel(f_PU, text= "a")
    l_a_text.grid(row=9, column = 11)
    l_factor_a.grid(row=9, column=10)
    list_l_a.append(var_l_a)
    var_l_n = tk.DoubleVar()
    l_n = ctk.CTkLabel(f_PU, text="pomocná hodnota n: ", textvariable=var_l_n)
    l_n_text = ctk.CTkLabel(f_PU, text= "n")
    l_n_text.grid(row=10, column = 11)
    l_n.grid(row=10, column=10)
    list_l_n.append(var_l_n)
    var_l_k = tk.DoubleVar()
    l_k = ctk.CTkLabel(f_PU, text="součinitel k: ", textvariable=var_l_k)
    l_k_text = ctk.CTkLabel(f_PU, text= "k")
    l_k_text.grid(row=11, column = 11)
    l_k.grid(row=11, column=10)
    list_l_k.append(var_l_k)

    var_l_b = tk.IntVar()
    l_b = ctk.CTkLabel(f_PU, text="b celkem: ", textvariable=var_l_b)
    l_b_text = ctk.CTkLabel(f_PU, text= "b")
    l_b_text.grid(row=12, column = 11)
    l_b.grid(row=12, column=10)
    list_l_b.append(var_l_b)

    var_l_hs = tk.IntVar()
    l_hs = ctk.CTkLabel(f_PU, text="světlá výška PÚ: ", textvariable=var_l_hs)
    l_hs_text = ctk.CTkLabel(f_PU, text= "hs")
    l_hs_text.grid(row=4, column = 16)
    l_hs.grid(row=4, column=15)
    list_l_hs.append(var_l_hs)
    var_l_so = tk.IntVar()
    l_So = ctk.CTkLabel(f_PU, text="celková plocha otvorů PÚ: ", textvariable=var_l_so)
    l_So_text = ctk.CTkLabel(f_PU, text= "So")
    l_So_text.grid(row=5, column = 16)
    l_So.grid(row=5, column=15)
    list_l_so.append(var_l_so)
    var_l_ho = tk.IntVar()
    l_ho = ctk.CTkLabel(f_PU, text="celková výška otvorů PÚ: ", textvariable=var_l_ho)
    l_ho_text = ctk.CTkLabel(f_PU, text= "ho")
    l_ho_text.grid(row=6, column = 16)
    l_ho.grid(row=6, column=15)
    list_l_ho.append(var_l_ho)


# nadpisy tabulky otvorů
    l_typ_ot = ctk.CTkLabel(f_PU, text="typ otvoru", anchor="center",  width=80, wraplength=50)
    l_typ_ot.grid(row=1, column=11)
    l_pocet_ot = ctk.CTkLabel(f_PU, text="počet otvorů", anchor="center",  width=80, wraplength=50)
    l_pocet_ot.grid(row=1, column=12)
    l_sirka_ot = ctk.CTkLabel(f_PU, text="šířka otvoru", anchor="center",  width=80, wraplength=50)
    l_sirka_ot.grid(row=1, column=13)
    l_vyska_ot = ctk.CTkLabel(f_PU, text="výška otvoru", anchor="center",  width=80, wraplength=50)
    l_vyska_ot.grid(row=1, column=14)

    if len(list_f_PU) >= 1:
        b_new_row = ctk.CTkButton(f_PU, text="nová místnost", command=lambda:m_plus(current_frame))
        b_new_row.grid(row=2, column=10)
        b_remove_row = ctk.CTkButton(f_PU, text="odebrat místnost", command=lambda:m_minus(current_frame))
        b_remove_row.grid(row=3, column=10)
        b_new_hole = ctk.CTkButton(f_PU, text="nový otvor", command=lambda:o_plus(current_frame))
        b_new_hole.grid(row=2, column=15)
        b_remove_hole = ctk.CTkButton(f_PU, text="odebrat otvor", command=lambda:o_minus(current_frame))
        b_remove_hole.grid(row=3, column=15)

# widgety pro požární úsek v rámečku pro celý objekt
    e_oznaceni = ctk.CTkEntry(f_seznam_PU)
    e_oznaceni.grid(row=len(list_f_PU), column=0)
    e_oznaceni.bind("<FocusOut>", pu_rename)
    list_cisla_pu.append(e_oznaceni)
    e_PU = ctk.CTkEntry(f_seznam_PU)
    e_PU.grid(row=len(list_f_PU), column=1)
    e_PU.bind("<FocusOut>", pu_rename)
    list_nazvy_pu.append(e_PU)
    e_typ = ctk.CTkEntry(f_seznam_PU)
    e_typ.grid(row=len(list_f_PU), column=2)
    list_e_typ.append(e_typ)
    var_l_pv = tk.IntVar()
    l_pv = ctk.CTkLabel(f_seznam_PU, text ="pv = ", textvariable=var_l_pv)
    l_pv.grid(row=len(list_f_PU), column=3)
    list_l_pv.append(var_l_pv)
    return current_frame