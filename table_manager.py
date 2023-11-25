import tkinter as tk
from tkinter import ttk
from counter import *

def add_f(window, list_nazvy_pu_default,list_f_PU,list_l_S, list_l_an, list_l_pn,list_l_ps, list_l_p, list_l_a,
          list_l_hs, list_l_so, list_l_ho, frame_count, current_frame, f_main):
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

# přiřazení nových listů do nadlistů mimo funkci
    dic_S_entries.append(m_S_entries)
    dic_ps_entries.append(m_ps_entries)
    dic_ps_labels.append(m_ps_labels)
    dic_pni_entries.append(m_pni_entries)
    dic_ani_entries.append(m_ani_entries)
    dic_m_rows.append(m_rows)
    dic_o_rows.append(o_rows)
    dic_text_entries.append(m_text_entries)
    dic_ps_group_sums.append(m_ps_group_sums)
    dic_hsi_entries.append(m_hsi_entries)
    dic_pocet_ot.append(list_pocet_ot)
    dic_sirka_ot.append(list_sirka_ot)
    dic_vyska_ot.append(list_vyska_ot)
    dic_so_ot.append(list_so_ot)

# tvorba rámečku
    f_PU = ttk.Frame(window, width=500, height=500, relief="ridge")
    f_PU.place(rely=0.5, relwidth=1, relheight=0.5)

# zařazení rámečku požárního úseku do listu a jeho nastavení jako current frame
    list_f_PU.append(f_PU)
    current_frame = list_f_PU.index(f_PU)

# vytvoří číslo rámečku PÚ
    frame_count[0] += 1

#nadpis rámečku požárního úseku a sloupců v rámečku
    l_nadpis_pu = ttk.Label(f_PU, anchor="center", background="red", text="požární úsek č." + str(frame_count[0]))
    l_nadpis_pu.grid(row=0, column=0, columnspan=9)
    l_cm = ttk.Label(f_PU, text="č. m.", anchor="center", width=6)
    l_cm.grid(row=1, column=0)
    l_nazev_m = ttk.Label(f_PU, text="název místnosti", anchor="center", width=31)
    l_nazev_m.grid(row=1, column=1)
    l_S = ttk.Label(f_PU, text="Plocha místnosti", anchor="center", width=16)
    l_S.grid(row=1, column=2)
    l_pn_m = ttk.Label(f_PU, text="pni", anchor="center", width=11)
    l_pn_m.grid(row=1, column=3)
    l_hsi_m = ttk.Label(f_PU, text="hni", anchor="center", width=11)
    l_hsi_m.grid(row=1, column=4)
    l_an_m = ttk.Label(f_PU, text="ani", anchor="center", width=11)
    l_an_m.grid(row=1, column=5)
    l_ps_d = ttk.Label(f_PU, text="psi dveře", anchor="center", width=11)
    l_ps_d.grid(row=1, column=6)
    l_ps_o = ttk.Label(f_PU, text="psi okna", anchor="center", width=11)
    l_ps_o.grid(row=1, column=7)
    l_ps_p = ttk.Label(f_PU, text="psi podlahy", anchor="center", width=11)
    l_ps_p.grid(row=1, column=8)
    l_psi_sum = ttk.Label(f_PU, text="psi celkem", anchor="center", width=11)
    l_psi_sum.grid(row=1, column=9)
    list_nazvy_pu_default.append(l_nadpis_pu)

# výsledky tabulky
    l_S = ttk.Label(f_PU, text="S celkem: ")
    l_S.grid(row=4, column=10)
    list_l_S.append(l_S)
    l_an = ttk.Label(f_PU, text="an celkem: ")
    l_an.grid(row=5, column=10)
    list_l_an.append(l_an)
    l_pn = ttk.Label(f_PU, text="pn celkem: ")
    l_pn.grid(row=6, column=10)
    list_l_pn.append(l_pn)
    l_ps = ttk.Label(f_PU, text="ps celkem: ")
    l_ps.grid(row=7, column=10)
    list_l_ps.append(l_ps)
    l_p = ttk.Label(f_PU, text="p celkem: ")
    l_p.grid(row=8, column=10)
    list_l_p.append(l_p)
    l_factor_a = ttk.Label(f_PU, text="součinitel a: ")
    l_factor_a.grid(row=9, column=10)
    list_l_a.append(l_factor_a)
    l_hs = ttk.Label(f_PU, text="světlá výška PÚ: ")
    l_hs.grid(row=4, column=15)
    list_l_hs.append(l_hs)
    l_So = ttk.Label(f_PU, text="celková plocha otvorů PÚ: ")
    l_So.grid(row=5, column=15)
    list_l_so.append(l_So)
    l_ho = ttk.Label(f_PU, text="celková výška otvorů PÚ: ")
    l_ho.grid(row=6, column=15)
    list_l_ho.append(l_ho)

# nadpisy tabulky otvorů
    l_typ_ot = ttk.Label(f_PU, text="typ otvoru", anchor="center", width=12)
    l_typ_ot.grid(row=1, column=11)
    l_pocet_ot = ttk.Label(f_PU, text="počet otvorů", anchor="center", width=12)
    l_pocet_ot.grid(row=1, column=12)
    l_sirka_ot = ttk.Label(f_PU, text="šířka otvoru", anchor="center", width=12)
    l_sirka_ot.grid(row=1, column=13)
    l_vyska_ot = ttk.Label(f_PU, text="výška otvoru", anchor="center", width=12)
    l_vyska_ot.grid(row=1, column=14)

    if frame_count[0] >= 1:
        b_new_row = ttk.Button(f_PU, text="nová místnost", command=lambda:m_plus(current_frame))
        b_new_row.grid(row=2, column=10)
        b_remove_row = ttk.Button(f_PU, text="odebrat místnost", command=lambda:m_minus(current_frame))
        b_remove_row.grid(row=3, column=10)
        b_new_hole = ttk.Button(f_PU, text="nový otvor", command=lambda:o_plus(current_frame))
        b_new_hole.grid(row=2, column=15)
        b_remove_hole = ttk.Button(f_PU, text="odebrat otvor", command=lambda:o_minus(current_frame))
        b_remove_hole.grid(row=3, column=15)
# widgety pro požární úsek v rámečku pro celý objekt
    e_oznaceni = ttk.Entry(f_main)
    e_oznaceni.grid(row=frame_count, column=0)
    e_oznaceni.bind("<FocusOut>", pu_rename)
    list_cisla_pu.append(e_oznaceni)
    e_PU = ttk.Entry(f_main)
    e_PU.grid(row=frame_count, column=1)
    e_PU.bind("<FocusOut>", pu_rename)
    list_nazvy_pu.append(e_PU)
    e_typ = ttk.Entry(f_main)
    e_typ.grid(row=frame_count, column=2)
    list_e_typ.append(e_typ)



def remove_f(list_cisla_pu, list_nazvy_pu, list_e_typ, current_frame):
    frame_count[0] -= 1
    list_cisla_pu[-1].destroy()
    list_cisla_pu.pop(-1)
    list_nazvy_pu[-1].destroy()
    list_nazvy_pu.pop(-1)
    list_e_typ[-1].destroy()
    list_e_typ.pop(-1)
    list_f_PU[-1].destroy()
    list_f_PU.pop(-1)
    dic_m_rows.pop(current_frame)
    dic_o_rows.pop(current_frame)

# funkce na vkládání řádků pro nové místnosti do current framu
def m_plus(current_frame):
    dic_m_rows[current_frame].append(1)
    for i in range(2):
        e_text = ttk.Entry(list_f_PU[current_frame])
        e_text.grid(row=len(dic_m_rows[current_frame]), column=i)
        dic_text_entries[current_frame].append(e_text)
        if i % 2 == 0:
            e_text.config(width=5)
        else:
            e_text.config(width=30)
    for i in range(1):
        e_S = ttk.Entry(list_f_PU[current_frame], width=15)
        e_S.grid(row=len(dic_m_rows[current_frame]), column=2)
        dic_S_entries[current_frame].append(e_S)
        e_S.insert(0, "0")
        e_S.bind("<FocusOut>", lambda event: wrap_p(current_frame))
        e_S.bind("<FocusIn>", lambda event: e_S.delete(0, tk.END) if e_S.get() == "0" else None)
        e_S.bind("<FocusOut>", lambda event: e_S.insert(0, "0") if e_S.get() == "" else None)
    for i in range(1):
        e_pni = ttk.Entry(list_f_PU[current_frame], width=10)
        e_pni.grid(row=len(dic_m_rows[current_frame]), column=3)
        dic_pni_entries[current_frame].append(e_pni)
        e_pni.insert(0, "0")
        e_pni.bind("<FocusOut>", lambda event: wrap_p(current_frame))
        e_pni.bind("<FocusIn>", lambda event: e_pni.delete(0, tk.END) if e_pni.get() == "0" else None)
        e_pni.bind("<FocusOut>", lambda event: e_pni.insert(0, "0") if e_pni.get() == "" else None)
    for i in range(1):
        e_hsi = ttk.Entry(list_f_PU[current_frame], width=10)
        e_hsi.grid(row=len(dic_m_rows[current_frame]), column=4)
        dic_hsi_entries[current_frame].append(e_hsi)
        e_hsi.insert(0, "0")
        e_hsi.bind("<FocusOut>", lambda event: wrap_p(current_frame))
        e_hsi.bind("<FocusIn>", lambda event: e_hsi.delete(0, tk.END) if e_hsi.get() == "0" else None)
        e_hsi.bind("<FocusOut>", lambda event: e_hsi.insert(0, "0") if e_hsi.get() == "" else None)
    for i in range(1):
        e_ani = ttk.Entry(list_f_PU[current_frame], width=10)
        e_ani.grid(row=len(dic_m_rows[current_frame]), column=5)
        dic_ani_entries[current_frame].append(e_ani)
        e_ani.insert(0, "0")
        e_ani.bind("<FocusOut>", lambda event: wrap_p(current_frame))
        e_ani.bind("<FocusIn>", lambda event: e_ani.delete(0, tk.END) if e_ani.get() == "0" else None)
        e_ani.bind("<FocusOut>", lambda event: e_ani.insert(0, "0") if e_ani.get() == "" else None)
    for i in range(3):
        e_psi = ttk.Entry(list_f_PU[current_frame], width=10)
        e_psi.grid(row=len(dic_m_rows[current_frame]), column=6 + i)
        dic_ps_entries[current_frame].append(e_psi)
        e_psi.insert(0, "0")
        e_psi.bind("<FocusOut>", lambda event: wrap_p(current_frame))
        e_psi.bind("<FocusIn>", lambda event, entry=e_psi: entry.delete(0, tk.END) if e_psi.get() == "0" else None)
        e_psi.bind("<FocusOut>", lambda event, entry=e_psi: entry.insert(0, "0") if entry.get() == "" else None)
    for i in range(1):
        l_ps = ttk.Label(list_f_PU[current_frame], text="0.0", width=10, anchor="center")
        l_ps.grid(row=len(dic_m_rows[current_frame]), column=9)
        dic_ps_labels[current_frame].append(l_ps)

# funkce na odebírání řádků pro místnosti do current framu
def m_minus(current_frame):
    dic_m_rows[current_frame].pop(1)
    for entry in dic_text_entries[current_frame][-2:]:
        entry.destroy()
        dic_text_entries[current_frame].pop(-1)
    dic_S_entries[current_frame][-1].destroy()
    dic_S_entries[current_frame].pop(-1)
    dic_ps_labels[current_frame][-1].destroy()
    dic_ps_labels[current_frame].pop(-1)
    dic_pni_entries[current_frame][-1].destroy()
    dic_pni_entries[current_frame].pop(-1)
    dic_ani_entries[current_frame][-1].destroy()
    dic_ani_entries[current_frame].pop(-1)
    for entry in dic_ps_entries[current_frame][-3:]:
        entry.destroy()
        dic_ps_entries[current_frame].pop(-1)
    dic_hsi_entries[current_frame][-1].destroy()
    dic_hsi_entries[current_frame].pop(-1)


# funkce na vkládání nových řádků pro otvory do current framu
def o_plus(current_frame):
    dic_o_rows[current_frame].append(1)
    for i in range(1):
        e_pocet_ot = ttk.Entry(list_f_PU[current_frame], width=10)
        e_pocet_ot.grid(row=len(dic_o_rows[current_frame]), column=12)
        dic_pocet_ot[current_frame].append(e_pocet_ot)
        e_pocet_ot.insert(0, "0")
        e_pocet_ot.bind("<FocusOut>", lambda event: wrap_otvory(current_frame))
        e_pocet_ot.bind("<FocusIn>", lambda event, entry=e_pocet_ot: entry.delete(0, tk.END) if e_pocet_ot.get() == "0" else None)
        e_pocet_ot.bind("<FocusOut>", lambda event: e_pocet_ot.insert(0, "0") if e_pocet_ot.get() == "" else None)
    for i in range(1):
        e_sirka_ot = ttk.Entry(list_f_PU[current_frame], width=10)
        e_sirka_ot.grid(row=len(dic_o_rows[current_frame]), column=13)
        dic_sirka_ot[current_frame].append(e_sirka_ot)
        e_sirka_ot.insert(0, "0")
        e_sirka_ot.bind("<FocusOut>", lambda event: wrap_otvory(current_frame))
        e_sirka_ot.bind("<FocusIn>", lambda event, entry=e_sirka_ot: entry.delete(0, tk.END) if e_sirka_ot.get() == "0" else None)
        e_sirka_ot.bind("<FocusOut>", lambda event: e_sirka_ot.insert(0, "0") if e_sirka_ot.get() == "" else None)
    for i in range(1):
        e_vyska_ot = ttk.Entry(list_f_PU[current_frame], width=10)
        e_vyska_ot.grid(row=len(dic_o_rows[current_frame]), column=14)
        dic_vyska_ot[current_frame].append(e_vyska_ot)
        e_vyska_ot.insert(0, "0")
        e_vyska_ot.bind("<FocusOut>", lambda event: wrap_otvory(current_frame))
        e_vyska_ot.bind("<FocusIn>", lambda event, entry=e_vyska_ot: entry.delete(0, tk.END) if e_vyska_ot.get() == "0" else None)
        e_vyska_ot.bind("<FocusOut>", lambda event: e_vyska_ot.insert(0, "0") if e_vyska_ot.get() == "" else None)

# funkce na odebírání řádků pro otvory do current framu
def o_minus(current_frame):
    dic_o_rows[current_frame].pop(1)
    dic_pocet_ot[current_frame][-1].destroy()
    dic_pocet_ot[current_frame].pop(-1)
    dic_sirka_ot[current_frame][-1].destroy()
    dic_sirka_ot[current_frame].pop(-1)
    dic_vyska_ot[current_frame][-1].destroy()
    dic_vyska_ot[current_frame].pop(-1)

# funkce na listování mezi rámečky vpřed
def lift_frame(current_frame):
    current_frame -= 1
    if current_frame < 0:
        current_frame = len(list_f_PU) - 1
        list_f_PU[-1].lift()
    else:
        list_f_PU[current_frame].lift()
    return current_frame

# funkce na zpětné listování mezi rámečky
def lower_frame(current_frame):
    if current_frame == len(list_f_PU)-1:
        current_frame = 0
        list_f_PU[current_frame].lift()
    else:
        current_frame += 1
        list_f_PU[current_frame].lift()
    return current_frame
def pu_rename(event):
    for i in range(len(list_cisla_pu)):
        cislo_pu = list_cisla_pu[i].get()
        nazev_pu = list_nazvy_pu[i].get()
        list_nazvy_pu_default[i].config(text=cislo_pu + " - " + nazev_pu)