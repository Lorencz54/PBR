import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from widget_variables_ounter import *

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

    l_mezni_delka = ctk.CTkLabel(f_parametry_pu, text="mezní délka PÚ")
    l_mezni_sirka = ctk.CTkLabel(f_parametry_pu, text="mezní šířka PÚ")

    l_mezni_delka.grid(row=3, column=2)
    l_mezni_sirka.grid(row=4, column=2)
    list_mezni_sirky.append(l_mezni_sirka)
    list_mezni_delky.append(l_mezni_delka)
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
    e_sirka_pu = ctk.CTkEntry(f_parametry_pu, width=80)
    list_sirky_pu.append(e_sirka_pu)
    e_sirka_pu.grid(row=3, column=1)
    e_sirka_pu.insert(0, "0")
    e_sirka_pu.bind("<FocusIn>", lambda event: e_sirka_pu.delete(0, tk.END) if e_sirka_pu.get() == "0" else None)
    e_sirka_pu.bind("<FocusOut>", lambda event: e_sirka_pu.insert(0, "0") if e_sirka_pu.get() == "" else None)
    e_delka_pu = ctk.CTkEntry(f_parametry_pu, width=80)
    list_delky_pu.append(e_delka_pu)
    e_delka_pu.grid(row=4, column=1)
    e_delka_pu.insert(0, "0")
    e_delka_pu.bind("<FocusIn>", lambda event: e_delka_pu.delete(0, tk.END) if e_delka_pu.get() == "0" else None)
    e_delka_pu.bind("<FocusOut>", lambda event: e_delka_pu.insert(0, "0") if e_delka_pu.get() == "" else None)

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
        b_new_hole = ctk.CTkButton(f_PU, text="nový otvor", command=lambda:o_plus(current_frame, om_konstrukcni_system, list_mezni_pocty_podlazi))
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

def remove_f(list_cisla_pu, list_nazvy_pu, list_e_typ):
    global current_frame
    list_f_PU[current_frame].destroy()
    list_f_PU.pop(current_frame)
    list_nazvy_default.pop(current_frame)
    list_cisla_pu[current_frame].destroy()
    list_cisla_pu.pop(current_frame)
    list_nazvy_pu[current_frame].destroy()
    list_nazvy_pu.pop(current_frame)
    list_e_typ[current_frame].destroy()
    list_e_typ.pop(current_frame)
    dic_m_rows.pop(current_frame)
    dic_o_rows.pop(current_frame)
    list_l_pv[current_frame].destroy()
    list_l_pv.pop(current_frame)
    if 0 <= current_frame < len(list_S):
        list_S.pop(current_frame)
    if 0 <= current_frame < len(list_pn):
        list_pn.pop(current_frame)
    if 0 <= current_frame < len(list_hs):
        list_hs.pop(current_frame)
    if 0 <= current_frame < len(list_an):
        list_an.pop(current_frame)
    if 0 <= current_frame < len(list_ps):
        list_ps.pop(current_frame)
    if 0 <= current_frame < len(list_a):
        list_a.pop(current_frame)
    if 0 <= current_frame < len(list_ho):
        list_ho.pop(current_frame)
    if 0 <= current_frame < len(list_so):
        list_so.pop(current_frame)
    if 0 <= current_frame < len(list_l_n):
        list_l_n.pop(current_frame)
    if 0 <= current_frame < len(list_k):
        list_k.pop(current_frame)
    if 0 <= current_frame < len(list_b):
        list_b.pop(current_frame)
    if 0 <= current_frame < len(list_p):
        list_p.pop(current_frame)
    if 0 <= current_frame < len(list_pv):
        list_pv.pop(current_frame)
    current_frame -= 1
    return current_frame

# funkce na listování mezi rámečky vpřed
def lift_frame():
    global current_frame
    current_frame -= 1
    if current_frame < 0:
        current_frame = len(list_f_PU) - 1
        list_f_PU[-1].lift()
    else:
        list_f_PU[current_frame].lift()
    return current_frame

# funkce na zpětné listování mezi rámečky
def lower_frame():
    global current_frame
    if current_frame == len(list_f_PU)-1:
        current_frame = 0
        list_f_PU[current_frame].lift()
    else:
        current_frame += 1
        list_f_PU[current_frame].lift()
    return current_frame

# funkce na vkládání řádků pro nové místnosti do current framu
def m_plus(current_frame):
    dic_m_rows[current_frame].append(1)
    for i in range(2):
        e_text = ctk.CTkEntry(list_f_PU[current_frame])
        e_text.grid(row=len(dic_m_rows[current_frame]), column=i)
        dic_text_entries[current_frame].append(e_text)
        if i % 2 == 0:
            e_text.configure(width=40)
        else:
            e_text.configure(width=200)
    for i in range(1):
        var_e_S = tk.StringVar()
        e_S = ctk.CTkEntry(list_f_PU[current_frame], width=80, textvariable=var_e_S)
        e_S.grid(row=len(dic_m_rows[current_frame]), column=2)
        dic_S_var_entries[current_frame].append(var_e_S)
        dic_S_entries[current_frame].append(e_S)
        e_S.insert(0, "0")
        e_S.bind("<FocusIn>", lambda event: e_S.delete(0, tk.END) if e_S.get() == "0" else None)
        e_S.bind("<FocusOut>", lambda event: e_S.insert(0, "0") if e_S.get() == "" else None)
        var_e_S.trace_add("write", lambda name, index, mode, sv=var_e_S: plocha_PU(current_frame, list_l_S))
    for i in range(1):
        var_e_pn = tk.StringVar()
        e_pni = ctk.CTkEntry(list_f_PU[current_frame], width=80, textvariable=var_e_pn)
        e_pni.grid(row=len(dic_m_rows[current_frame]), column=3)
        dic_pni_var_entries[current_frame].append(var_e_pn)
        dic_pni_entries[current_frame].append(e_pni)
        e_pni.insert(0, "0")
        e_pni.bind("<FocusIn>", lambda event: e_pni.delete(0, tk.END) if e_pni.get() == "0" else None)
        e_pni.bind("<FocusOut>", lambda event: e_pni.insert(0, "0") if e_pni.get() == "" else None)
        var_e_pn.trace_add("write", lambda name, index, mode, sv=var_e_pn: pn(current_frame, list_l_pn, dic_pni_var_entries, dic_S_var_entries))
        var_e_S.trace_add("write", lambda name, index, mode, sv=var_e_S: pn(current_frame, list_l_pn, dic_pni_var_entries, dic_S_var_entries))
    for i in range(1):
        var_e_hs = tk.StringVar()
        e_hsi = ctk.CTkEntry(list_f_PU[current_frame], width=80, textvariable=var_e_hs)
        e_hsi.grid(row=len(dic_m_rows[current_frame]), column=4)
        dic_hsi_var_entries[current_frame].append(var_e_hs)
        dic_hsi_entries[current_frame].append(e_hsi)
        e_hsi.insert(0, "0")
        e_hsi.bind("<FocusIn>", lambda event: e_hsi.delete(0, tk.END) if e_hsi.get() == "0" else None)
        e_hsi.bind("<FocusOut>", lambda event: e_hsi.insert(0, "0") if e_hsi.get() == "" else None)
        var_e_hs.trace_add("write", lambda name, index, mode, sv=var_e_hs: hs(current_frame))
        var_e_S.trace_add("write", lambda name, index, mode, sv=var_e_hs: hs(current_frame))
    for i in range(1):
        var_e_ani = tk.StringVar()
        e_ani = ctk.CTkEntry(list_f_PU[current_frame], width=80, textvariable=var_e_ani)
        e_ani.grid(row=len(dic_m_rows[current_frame]), column=5)
        dic_ani_var_entries[current_frame].append(var_e_ani)
        dic_ani_entries[current_frame].append(e_ani)
        e_ani.insert(0, "0")
        e_ani.bind("<FocusIn>", lambda event: e_ani.delete(0, tk.END) if e_ani.get() == "0" else None)
        e_ani.bind("<FocusOut>", lambda event: e_ani.insert(0, "0") if e_ani.get() == "" else None)
        var_e_ani.trace_add("write", lambda name, index, mode, sv=var_e_ani: an(current_frame, list_l_an, dic_ani_var_entries, dic_S_var_entries))
        var_e_S.trace_add("write", lambda name, index, mode, sv=var_e_S: an(current_frame, list_l_an, dic_ani_var_entries, dic_S_var_entries))
    for i in range(3):
        var_e_psi = tk.StringVar()
        e_psi = ctk.CTkEntry(list_f_PU[current_frame], width=80, textvariable=var_e_psi)
        e_psi.grid(row=len(dic_m_rows[current_frame]), column=6 + i)
        dic_ps_var_entries[current_frame].append(var_e_psi)
        dic_ps_entries[current_frame].append(e_psi)
        e_psi.insert(0, "0")
        e_psi.bind("<FocusIn>", lambda event, entry=e_psi: entry.delete(0, tk.END) if e_psi.get() == "0" else None)
        e_psi.bind("<FocusOut>", lambda event, entry=e_psi: entry.insert(0, "0") if entry.get() == "" else None)
        var_e_psi.trace_add("write", lambda name, index, mode, sv=var_e_psi: ps(current_frame, list_l_ps, dic_ps_var_entries, dic_S_var_entries))
        var_e_S.trace_add("write", lambda name, index, mode, sv=var_e_psi: ps(current_frame, list_l_ps, dic_ps_var_entries, dic_S_var_entries))
    for i in range(1):
        var_l_ps = tk.IntVar()
        l_ps = ctk.CTkLabel(list_f_PU[current_frame], text="0.0", width=80, anchor="center", textvariable=var_l_ps)
        l_ps.grid(row=len(dic_m_rows[current_frame]), column=9)
        dic_ps_labels[current_frame].append(var_l_ps)


# funkce na odebírání řádků pro místnosti do current framu
def m_minus(current_frame):
    dic_m_rows[current_frame].pop(1)
    for entry in dic_text_entries[current_frame][-2:]:
        entry.destroy()
        dic_text_entries[current_frame].pop(-1)
    dic_S_entries[current_frame][-1].destroy()
    dic_S_var_entries[current_frame].pop(-1)
    dic_ps_labels[current_frame][-1].destroy()
    dic_ps_labels[current_frame].pop(-1)
    dic_pni_entries[current_frame][-1].destroy()
    dic_pni_var_entries[current_frame].pop(-1)
    dic_ani_entries[current_frame][-1].destroy()
    dic_ani_var_entries[current_frame].pop(-1)
    for entry in dic_ps_entries[current_frame][-3:]:
        entry.destroy()
        dic_ps_var_entries[current_frame].pop(-1)
    dic_hsi_entries[current_frame][-1].destroy()
    dic_hsi_var_entries[current_frame].pop(-1)


# funkce na vkládání nových řádků pro otvory do current framu
def o_plus(current_frame, om_konstrukcni_system, list_mezni_pocty_podlazi):
    dic_o_rows[current_frame].append(1)
    o_typ_otvoru = ctk.CTkOptionMenu(list_f_PU[current_frame], values=["okno", "dveře", "vrata", "světlík", "jiný"], width=80)
    o_typ_otvoru.grid(row=len(dic_o_rows[current_frame]), column=11)

    for i in range (3):
        var_e_rozmer_otvoru = tk.StringVar()
        e_parametr_otvoru = ctk.CTkEntry(list_f_PU[current_frame], width=80, textvariable=var_e_rozmer_otvoru)
        e_parametr_otvoru.insert(0, "0")
        e_parametr_otvoru.bind("<FocusIn>",lambda event, entry=e_parametr_otvoru: entry.delete(0, tk.END) if e_parametr_otvoru.get() == "0" else None)
        e_parametr_otvoru.bind("<FocusOut>", lambda event: e_parametr_otvoru.insert(0, "0") if e_parametr_otvoru.get() == "" else None)
        var_e_rozmer_otvoru.trace_add("write", lambda name, index, mode, sv=var_e_rozmer_otvoru: hs_so(current_frame))
        if i == 0:
            e_parametr_otvoru.grid(row=len(dic_o_rows[current_frame]), column=12)
            dic_pocet_ot[current_frame].append(e_parametr_otvoru)
            dic_var_pocet_ot[current_frame].append(var_e_rozmer_otvoru)
        elif i == 1:
            e_parametr_otvoru.grid(row=len(dic_o_rows[current_frame]), column=13)
            dic_sirka_ot[current_frame].append(e_parametr_otvoru)
            dic_var_sirka_ot[current_frame].append(var_e_rozmer_otvoru)
        else:
            e_parametr_otvoru.grid(row=len(dic_o_rows[current_frame]), column=14)
            dic_vyska_ot[current_frame].append(e_parametr_otvoru)
            dic_var_vyska_ot[current_frame].append(var_e_rozmer_otvoru)



# funkce na odebírání řádků pro otvory do current framu
def o_minus(current_frame):
    dic_o_rows[current_frame].pop(1)
    dic_pocet_ot[current_frame][-1].destroy()
    dic_pocet_ot[current_frame].pop(-1)
    dic_sirka_ot[current_frame][-1].destroy()
    dic_sirka_ot[current_frame].pop(-1)
    dic_vyska_ot[current_frame][-1].destroy()
    dic_vyska_ot[current_frame].pop(-1)

def pu_rename(event):
    for i in range(len(list_cisla_pu)):
        cislo_pu = list_cisla_pu[i].get()
        nazev_pu = list_nazvy_pu[i].get()

        list_nazvy_default[i].configure(text=cislo_pu + " - " + nazev_pu)