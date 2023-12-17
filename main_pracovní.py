from pu_rows_manager import *
from PBR_frames import *

as_value = 0.9
# funkce na listování mezi rámečky vpřed
def lift_frame():
    if len(list_f_PU) != 0:
        current_frame[0] -= 1
        if current_frame[0] < 0:
            current_frame[0] = len(list_f_PU) - 1
            list_f_PU[-1].lift()
            list_f_info_PU[-1].lift()
        else:
            list_f_PU[current_frame[0]].lift()
            list_f_info_PU[current_frame[0]].lift()

# funkce na zpětné listování mezi rámečky
def lower_frame():
    if len(list_f_PU) != 0:
        if current_frame[0] == len(list_f_PU)-1:
            current_frame[0] = 0
            list_f_PU[current_frame[0]].lift()
            list_f_info_PU[current_frame[0]].lift()
        else:
            current_frame[0] += 1
            list_f_PU[current_frame[0]].lift()
            list_f_info_PU[current_frame[0]].lift()

window = ctk.CTk()
window.geometry(f"{sirka_okna[0]}x{vyska_okna[0]}")

# sestavení dvou horních rámečků (hlavní informace o objektu a panel pro tlačítka)
f_room_list = ctk.CTkFrame(window)
f_seznam_PU = ctk.CTkFrame(window)
f_info_objekt = ctk.CTkFrame(window)


# vložení PBR framů do listu (seznam požárních úseků a seznam místností)
list_PBR_frames.append(f_seznam_PU)
list_PBR_frames.append(f_room_list)



# definice widgetů pro panel na tlačítka
b_add_f = ctk.CTkButton(f_info_objekt, text="nový požární úsek", command=lambda: add_new_pu(f_seznam_PU, window))
b_remove_f = ctk.CTkButton(f_info_objekt, text="odebrat požární úsek", command=lambda: remove_f(current_frame, list_cisla_pu, list_nazvy_pu))
b_lift = ctk.CTkButton(f_info_objekt, text="předchozí PÚ", command=lift_frame)
b_lower = ctk.CTkButton(f_info_objekt, text="další PÚ", command=lower_frame)

var_om_konstrukcni_system = tk.StringVar()
om_konstrukcni_system = ctk.CTkOptionMenu(f_info_objekt, values=["nehořlavý", "smíšený", "hořlavý"], variable=var_om_konstrukcni_system)
list_var_om_konstrukcni_system.append(var_om_konstrukcni_system)
var_om_konstrukcni_system.trace_add("write", lambda name, index, mode, sv=list_var_om_konstrukcni_system: calculate_max_dimensions(current_frame))
var_om_konstrukcni_system.trace_add("write", lambda name, index, mode, sv=list_var_e_pozarni_vyska: determine_SPB(current_frame))

var_e_pozarni_vyska = tk.StringVar()
e_pozarni_vyska = EntryWithLimit(f_info_objekt, textvariable=var_e_pozarni_vyska)
list_e_pozarni_vyska.append(e_pozarni_vyska)
list_var_e_pozarni_vyska.append(var_e_pozarni_vyska)
var_e_pozarni_vyska.trace_add("write", lambda name, index, mode, sv=list_var_e_pozarni_vyska: calculate_max_dimensions(current_frame))
var_e_pozarni_vyska.trace_add("write", lambda name, index, mode, sv=list_var_e_pozarni_vyska: determine_SPB(current_frame))

l_konstrukcni_system = ctk.CTkLabel(f_info_objekt, text="konstrukční systém")

l_pozarni_vyska = ctk.CTkLabel(f_info_objekt, text="požární výška")

b_list_pu = ctk.CTkButton(f_info_objekt, text="požární úseky", command=lift_seznam_PU)
b_room_list = ctk.CTkButton(f_info_objekt, text="seznam místností", command=create_or_lift_room_list)

# umístění dvou horních rámečků
f_info_objekt.place(relwidth=0.3, relheight=0.5)
f_room_list.place(relx=0.3, relwidth=0.7, relheight=0.5)
f_seznam_PU.place(relx= 0.3, relwidth=0.7, relheight=0.5)

label = ctk.CTkLabel(f_room_list, text="ddd")
label.pack()

# umístění tlačítek do panelu pro tlačítka
om_konstrukcni_system.grid(row=1, column=2)
l_konstrukcni_system.grid(row=1, column=1)
e_pozarni_vyska.grid(row=2, column=2)
l_pozarni_vyska.grid(row=2, column=1)

b_add_f.grid(row=4, column=1)
b_remove_f.grid(row=5, column=1)

b_lift.grid(row=7, column=1)
b_lower.grid(row=7, column=2)

b_list_pu.grid(row=3, column=3)
b_room_list.grid(row=4, column=3)

# f_seznamPU widgets
l_typ_pu = ctk.CTkLabel(f_seznam_PU, text="typ objektu", width=140)
l_konstrukcni_system_pu = ctk.CTkLabel(f_seznam_PU, text="konstrukční systém", width=140)
l_oznaceni_pu = ctk.CTkLabel(f_seznam_PU, text="Označení PÚ", width=140)
l_nazev_pu = ctk.CTkLabel(f_seznam_PU, text="Název PÚ", width=140)
l_pv = ctk.CTkLabel(f_seznam_PU, text="pv", width=140)
l_SPB = ctk.CTkLabel(f_seznam_PU, text="SPB", width=140)

# f_seznamPU layout
l_typ_pu.grid(row=0, column=0)
l_konstrukcni_system_pu.grid(row=0, column=1)
l_oznaceni_pu.grid(row=0, column=2)
l_nazev_pu.grid(row=0, column=3)
l_pv.grid(row=0, column=4)
l_SPB.grid(row=0, column=5)


# spuštění okna
window.mainloop()