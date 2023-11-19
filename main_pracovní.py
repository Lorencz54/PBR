import tkinter as tk
from tkinter import ttk
import numpy as np

# konstanty
current_frame = None
as_value = 0.9

#lists
list_f_PU = []
list_l_S = []
list_l_an = []
list_l_pn = []
list_l_ps = []
list_l_p = []
list_l_a = []
list_nazvy_pu_default = []
list_cisla_pu = []
list_nazvy_pu = []
list_an = []
list_pn = []
list_ps = []
list_a = []
list_m_rows = []
# dictionaries
dic_rows = []
dic_S_entries = []
dic_ps_entries = []
dic_text_entries = []
dic_ps_labels = []
dic_pni_entries = []
dic_ani_entries = []
dic_ps_group_sums = []
list_e_PU = []
list_e_typ = []

frame_count = 0
window = tk.Tk()
window.geometry("850x500")
def add_f():
    global frame_count, current_frame
# listy pro nový požární úsek
    m_rows = [1]
    m_S_entries = []
    m_ps_entries = []
    m_text_entries = []
    m_ps_labels = []
    m_pni_entries = []
    m_ani_entries = []
    m_ps_group_sums = []

# přiřazení nových listů do nadlistů mimo funkci
    dic_S_entries.append(m_S_entries)
    dic_ps_entries.append(m_ps_entries)
    dic_ps_labels.append(m_ps_labels)
    dic_pni_entries.append(m_pni_entries)
    dic_ani_entries.append(m_ani_entries)
    dic_rows.append(m_rows)
    dic_text_entries.append(m_text_entries)
    dic_ps_group_sums.append(m_ps_group_sums)
# počítadlo rámečků
    frame_count += 1
# tvorba rámečku
    f_PU = ttk.Frame(window, width=500, height=500, relief="ridge")
    f_PU.place(rely=0.5, relwidth=1, relheight=0.5)
#nadpis rámečku požárního úseku a sloupců v rámečku
    l_nadpis_pu = ttk.Label(f_PU, anchor="center", background="red", text="požární úsek č." + str(frame_count))
    l_nadpis_pu.grid(row=0, column=0, columnspan=9)
    list_nazvy_pu_default.append(l_nadpis_pu)
    l_cm = ttk.Label(f_PU, text="č. m.", anchor="center", width=6)
    l_cm.grid(row=1, column=0)
    l_nazev_m = ttk.Label(f_PU, text="název místnosti", anchor="center", width=31)
    l_nazev_m.grid(row=1, column=1)
    l_S = ttk.Label(f_PU, text="Plocha místnosti", anchor="center", width=16)
    l_S.grid(row=1, column=2)
    l_pn_m = ttk.Label(f_PU, text="pni", anchor="center", width=11)
    l_pn_m.grid(row=1, column=3)
    l_an_m = ttk.Label(f_PU, text="ani", anchor="center", width=11)
    l_an_m.grid(row=1, column=4)
    l_ps_d = ttk.Label(f_PU, text="psi dveře", anchor="center", width=11)
    l_ps_d.grid(row=1, column=5)
    l_ps_o = ttk.Label(f_PU, text="psi okna", anchor="center", width=11)
    l_ps_o.grid(row=1, column=6)
    l_ps_p = ttk.Label(f_PU, text="psi podlahy", anchor="center", width=11)
    l_ps_p.grid(row=1, column=7)
    l_psi_sum = ttk.Label(f_PU, text="psi celkem", anchor="center", width=11)
    l_psi_sum.grid(row=1, column=8)
# výsledky tabulky
    l_S = ttk.Label(f_PU, text="S celkem: ")
    l_S.grid(row=4, column=9)
    list_l_S.append(l_S)
    l_an = ttk.Label(f_PU, text="an celkem: ")
    l_an.grid(row=5, column=9)
    list_l_an.append(l_an)
    l_pn = ttk.Label(f_PU, text="pn celkem: ")
    l_pn.grid(row=6, column=9)
    list_l_pn.append(l_pn)
    l_ps = ttk.Label(f_PU, text="ps celkem: ")
    l_ps.grid(row=7, column=9)
    list_l_ps.append(l_ps)
    l_p = ttk.Label(f_PU, text="p celkem: ")
    l_p.grid(row=8, column=9)
    list_l_p.append(l_p)
    l_factor_a = ttk.Label(f_PU, text="součinitel a: ")
    l_factor_a.grid(row=9, column=9)
    list_l_a.append(l_factor_a)
# zařazení rámečku požárního úseku do listu a jeho nastavení jako current frame
    list_f_PU.append(f_PU)
    current_frame = f_PU
# pokud se počítadlo rovná 1, vytvoří se tlačítko na vkládání řádků do rámečku požárního úseku
    if frame_count >= 1:
        b_new_row = ttk.Button(f_PU, text="add new row", command=m_plus)
        b_new_row.grid(row=2, column=9)
        b_remove_row = ttk.Button(f_PU, text="remove row", command=m_minus)
        b_remove_row.grid(row=3, column=9)
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
# funkce vrací rámeček, který vytvořila
    return current_frame

# funkce odebírá rámečky
def remove_f():
    global current_frame, frame_count
    frame_count -= 1
    first_covered_frame = list_f_PU[-2]
    first_covered_frame.lift()
    frame_to_destroy = list_f_PU.pop(-1)
    frame_to_destroy.destroy()
    current_frame = first_covered_frame
    list_cisla_pu[-1].destroy()
    list_cisla_pu.pop(-1)
    list_e_PU[-1].destroy()
    list_e_PU.pop(-1)
    list_e_typ[-1].destroy()
    list_e_typ.pop(-1)
    return current_frame

# funkce na listování mezi rámečky vpřed
def lift_frame():
    global current_frame
    bottom_frame = dic_rows[0]
    dic_rows.pop(0)
    dic_rows.append(bottom_frame)
    bottom_frame = list_f_PU[0]
    bottom_frame.lift()
    list_f_PU.pop(0)
    list_f_PU.append(bottom_frame)
    current_frame = bottom_frame
    return current_frame

# funkce na zpětné listování mezi rámečky
def lower_frame(): # funkce kazí vkládání řádků do jednotlivých rámečků (pravděpodobně je nutné kromě pozic v listu list_f_PU měnit i pozice listů v jenodlivých dictionaries
    global current_frame
    first_covered_frame = list_f_PU[-2]
    first_covered_frame.lift()
    list_f_PU.pop(-1)
    list_f_PU.insert(0, current_frame)
    current_frame = first_covered_frame
    return current_frame

# funkce na vkládání řádků pro nové místnosti do current framu
def m_plus():
    global current_frame
    current_frame_index = list_f_PU.index(current_frame)
    dic_rows[current_frame_index].append(1)
    for i in range(2):
        e_text = ttk.Entry(current_frame)
        e_text.grid(row=len(dic_rows[current_frame_index]), column=i)
        dic_text_entries[current_frame_index].append(e_text)
        if i % 2 == 0:
            e_text.config(width=5)
        else:
            e_text.config(width=30)
    for i in range(1):
        e_S = ttk.Entry(current_frame, width=15)
        e_S.grid(row=len(dic_rows[current_frame_index]), column=2)
        dic_S_entries[current_frame_index].append(e_S)
        e_S.insert(0, "0")
        e_S.bind("<FocusOut>", wrap_an_pn_ps_p_a)
        e_S.bind("<FocusIn>", lambda event: e_S.delete(0, tk.END) if e_S.get() == "0" else None)
    for i in range(1):
        e_pni = ttk.Entry(current_frame, width=10)
        e_pni.grid(row=len(dic_rows[current_frame_index]), column=3)
        dic_pni_entries[current_frame_index].append(e_pni)
        e_pni.insert(0, "0")
        e_pni.bind("<FocusOut>", wrap_pn_a)
        e_pni.bind("<FocusIn>", lambda event: e_pni.delete(0, tk.END) if e_pni.get() == "0" else None)
    for i in range(1):
        e_ani = ttk.Entry(current_frame, width=10)
        e_ani.grid(row=len(dic_rows[current_frame_index]), column=4)
        dic_ani_entries[current_frame_index].append(e_ani)
        e_ani.insert(0, "0")
        e_ani.bind("<FocusOut>", wrap_an_a)
        e_ani.bind("<FocusIn>", lambda event: e_ani.delete(0, tk.END) if e_ani.get() == "0" else None)
    for i in range(3):
        e_psi = ttk.Entry(current_frame, width=10)
        e_psi.grid(row=len(dic_rows[current_frame_index]), column=5 + i)
        dic_ps_entries[current_frame_index].append(e_psi)
        e_psi.insert(0, "0")
        e_psi.bind("<FocusOut>", wrap_ps_a)
        e_psi.bind("<FocusIn>", lambda event, entry=e_psi: entry.delete(0, tk.END) if e_psi.get() == "0" else None)
    for i in range(1):
        l_ps = ttk.Label(current_frame, text="0.0", width=10, anchor="center") #zkusit upravit výšku těchto labelů - pomocí nich by se mohly srovnat všechny entries
        l_ps.grid(row=len(dic_rows[current_frame_index]), column=8)
        dic_ps_labels[current_frame_index].append(l_ps)

def m_minus():
    global current_frame
    current_frame_index = list_f_PU.index(current_frame)
    dic_rows[current_frame_index].pop(1)
    for entry in dic_text_entries[current_frame_index][-2:]:
        entry.destroy()
        dic_text_entries[current_frame_index].pop(-1)
    dic_S_entries[current_frame_index][-1].destroy()
    dic_S_entries[current_frame_index].pop(-1)
    dic_ps_labels[current_frame_index][-1].destroy()
    dic_ps_labels[current_frame_index].pop(-1)
    dic_pni_entries[current_frame_index][-1].destroy()
    dic_pni_entries[current_frame_index].pop(-1)
    dic_ani_entries[current_frame_index][-1].destroy()
    dic_ani_entries[current_frame_index].pop(-1)
    for entry in dic_ps_entries[current_frame_index][-3:]:
        entry.destroy()
        dic_ps_entries[current_frame_index].pop(-1)
    wrap_an_pn_ps_p_a(None)

# funkce na výpočet ps v current framu
def ps(event):
    global current_frame
    current_frame_index = list_f_PU.index(current_frame)
    S_values = [float(entry.get()) for entry in dic_S_entries[current_frame_index]]
    S_suma = np.sum(S_values)
    psi_values = [float(entry.get()) for entry in dic_ps_entries[current_frame_index]]
    list_ps_arr = np.array(psi_values)
    list_ps_reshape = list_ps_arr.reshape(-1,3)
    ps_sum = np.sum(list_ps_reshape, axis=1)
    ps_sum_list = ps_sum.tolist()
    ps_value = round(np.dot(ps_sum_list, S_values)/S_suma,2)
    list_l_ps[current_frame_index].config(text="ps celkem: " + str(ps_value))
    for i in range(len(ps_sum_list)):
        ps_row_sum = ps_sum_list[i]
        label_ps_sum = dic_ps_labels[current_frame_index][i]
        label_ps_sum.config(text=str(ps_row_sum))
    if current_frame_index < len(list_ps):
        list_ps[current_frame_index] = ps_value
    else:
        list_ps.append(ps_value)


# funkce na výpočet pn v current framu
def pn(event):
    global current_frame
    current_frame_index = list_f_PU.index(current_frame)
    S_values = [float(entry.get()) for entry in dic_S_entries[current_frame_index]]
    pn_values = [float(entry.get()) for entry in dic_pni_entries[current_frame_index]]
    S_suma = np.sum(S_values)
    pn_value = round(np.dot(pn_values, S_values)/S_suma,2)
    if current_frame_index < len(list_pn):
        list_pn[current_frame_index] = pn_value
    else:
        list_pn.append(pn_value)
    list_l_pn[current_frame_index].config(text="pn celkem: " + str(pn_value))


# funkce na výpočet an v current framu
def an(event):
    global current_frame
    current_frame_index = list_f_PU.index(current_frame)
    S_values = [float(entry.get()) for entry in dic_S_entries[current_frame_index]]
    an_values = [float(entry.get()) for entry in dic_ani_entries[current_frame_index]]
    S_suma = np.sum(S_values)
    an_value = round(np.dot(an_values, S_values)/S_suma,2)
    if current_frame_index < len(list_an):
        list_an[current_frame_index] = an_value
    else:
        list_an.append(an_value)
    list_l_an[current_frame_index].config(text="an celkem: " + str(an_value))

def p(event):
    global current_frame, as_value
    current_frame_index = list_f_PU.index(current_frame)
    p = round(list_pn[current_frame_index]+list_ps[current_frame_index],2)
    list_l_p[current_frame_index].config(text="p celkem: " + str(p))

# soubor funkcí pro navázání na widget
def wrap_an_pn_ps_p_a(event):
    an(event)
    pn(event)
    ps(event)
    p(event)
    f_a(event)

# soubor funkcí pro navázání na widget
def wrap_an_a(event):
    an(event)
    p(event)
    f_a(event)

# soubor funkcí pro navázání na widget
def wrap_pn_a(event):
    pn(event)
    p(event)
    f_a(event)

# soubor funkcí pro navázání na widget
def wrap_ps_a(event):
    ps(event)
    p(event)
    f_a(event)

def pu_rename(event):
    for i in range(len(list_cisla_pu)):
        cislo_pu = list_cisla_pu[i].get()
        nazev_pu = list_nazvy_pu[i].get()
        list_nazvy_pu_default[i].config(text=cislo_pu + " - " + nazev_pu)

def f_a(event):
    global current_frame, as_value
    current_frame_index = list_f_PU.index(current_frame)
    factor_a = round((list_pn[current_frame_index]*list_an[current_frame_index]+list_ps[current_frame_index]*as_value)/(list_pn[current_frame_index]+list_ps[current_frame_index]),2)
    if current_frame_index < len(list_a):
        list_a[current_frame_index] = factor_a
    else:
        list_a.append(factor_a)
    list_l_a[current_frame_index].config(text="a celkem: " + str(factor_a))

# sestavení dvou horních rámečků (hlavní informace o objektu a panel pro tlačítka)
f_main = ttk.Frame(window, width=100, height=200, relief="ridge")
f_button_panel = ttk.Frame(window, width=100, height=200, relief="ridge")

# definice tlačítek pro panel na tlačítka
b_add_f = ttk.Button(f_button_panel, text="nový požární úsek", command= add_f)
b_remove_f = ttk.Button(f_button_panel, text="remove frame", command=remove_f)
b_lift = ttk.Button(f_button_panel, text="lift frame", command= lift_frame)
b_lower = ttk.Button(f_button_panel, text="lower frame", command=lower_frame)

# umístění dvou horních rámečků
f_main.place(relwidth=0.7, relheight=0.5)
f_button_panel.place(relx=0.7, relwidth=0.3, relheight=0.5)

# umístění tlačítek do panelu pro tlačítka
b_add_f.pack()
b_remove_f.pack()
b_lift.pack()
b_lower.pack()

# f_seznamPU widgets
l_oznaceni = ttk.Label(f_main, text="Označení PÚ")
l_PU = ttk.Label(f_main, text="Název PÚ")
l_typ = ttk.Label(f_main, text="typ objektu")
l_pn = ttk.Label(f_main, text = "pn celkem: ")
l_an = ttk.Label(f_main, text="an celkem: ")
l_p = ttk.Label(f_main, text="p celkem: ")
l_ps = ttk.Label(f_main, text="ps celkem: ")
l_S = ttk.Label(f_main, text="Suma S: ")

# f_seznamPU layout
l_oznaceni.grid(row=0, column=0)
l_PU.grid(row=0, column=1)
l_typ.grid(row=0, column=2)

print("hello")
# spuštění okna
window.mainloop()