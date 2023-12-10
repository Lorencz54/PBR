from widget_variables_ounter import *
from Classes import *
import customtkinter as ctk

# funkce na vkládání nových řádků pro otvory do current framu
def o_plus(current_frame):
    dic_o_rows[int(current_frame[0])].append(1)
    o_typ_otvoru = ctk.CTkOptionMenu(list_f_PU[int(current_frame[0])], values=["okno", "dveře", "vrata", "světlík", "jiný"], width=80)
    o_typ_otvoru.grid(row=len(dic_o_rows[int(current_frame[0])]), column=11)
    dic_typy_ot_option_menues[int(current_frame[0])].append(o_typ_otvoru)

    for i in range(3):
        var_e_rozmer_otvoru = tk.StringVar()
        e_parametr_otvoru = EntryWithLimit(list_f_PU[current_frame[0]], width=80, textvariable=var_e_rozmer_otvoru)
        e_parametr_otvoru.grid(row=len(dic_o_rows[current_frame[0]]), column=12+i)
        if i == 0:
            dic_pocet_ot_entries[int(current_frame[0])].append(e_parametr_otvoru)
            dic_var_pocet_ot[int(current_frame[0])].append(var_e_rozmer_otvoru)
        elif i == 1:
            dic_sirka_ot_entries[int(current_frame[0])].append(e_parametr_otvoru)
            dic_var_sirka_ot[int(current_frame[0])].append(var_e_rozmer_otvoru)
        else:
            dic_vyska_ot_entries[int(current_frame[0])].append(e_parametr_otvoru)
            dic_var_vyska_ot[int(current_frame[0])].append(var_e_rozmer_otvoru)
        e_parametr_otvoru.bind("<FocusIn>", lambda event, entry=e_parametr_otvoru: entry.delete(0, tk.END) if e_parametr_otvoru.get() == "0.0" else None)
        e_parametr_otvoru.bind("<FocusOut>", lambda event, entry=e_parametr_otvoru: entry.insert(0, "0.0") if entry.get() == "" else None)
        var_e_rozmer_otvoru.trace_add("write", lambda name, index, mode, sv=var_e_rozmer_otvoru: hs_so(current_frame))




# funkce na odebírání řádků pro otvory do current framu
def o_minus(current_frame):
    if len(dic_o_rows[current_frame[0]]) != 1:
        dic_o_rows[int(current_frame[0])].pop(1)
        dic_pocet_ot_entries[int(current_frame[0])][-1].destroy()
        dic_pocet_ot_entries[int(current_frame[0])].pop(-1)
        dic_sirka_ot_entries[int(current_frame[0])][-1].destroy()
        dic_sirka_ot_entries[int(current_frame[0])].pop(-1)
        dic_vyska_ot_entries[int(current_frame[0])][-1].destroy()
        dic_vyska_ot_entries[int(current_frame[0])].pop(-1)
        dic_typy_ot_option_menues[int(current_frame[0])][-1].destroy()
        dic_typy_ot_option_menues[int(current_frame[0])].pop(-1)