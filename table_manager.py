import tkinter as tk
import customtkinter as ctk
from widget_variables_ounter import *

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
def o_plus(current_frame):
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