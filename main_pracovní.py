from table_manager import *
from lists_and_dictionaries import *


window = ctk.CTk()
window.geometry("1600x800")

current_frame = 0
as_value = 0.9

# sestavení dvou horních rámečků (hlavní informace o objektu a panel pro tlačítka)
f_seznam_PU = ctk.CTkFrame(window)
f_main = ctk.CTkFrame(window)

# definice widgetů pro panel na tlačítka
b_add_f = ctk.CTkButton(f_main, text="nový požární úsek", command=lambda: add_f(window, list_nazvy_pu, list_f_PU, list_l_S, list_l_an, list_l_pn, list_l_ps, list_l_p, list_l_a, list_l_hs, list_l_so, list_l_ho, f_seznam_PU))
b_remove_f = ctk.CTkButton(f_main, text="odebrat požární úsek", command=lambda: remove_f(list_cisla_pu, list_nazvy_pu, list_e_typ))
b_lift = ctk.CTkButton(f_main, text="předchozí PÚ", command=lift_frame)
b_lower = ctk.CTkButton(f_main, text="další PÚ", command=lower_frame)
om_konstrukcni_system = ctk.CTkOptionMenu(f_main, values=["nehořlavý", "smíšený", "hořlavý"])
e_pozarni_vyska = ctk.CTkEntry(f_main)
l_konstrukcni_system = ctk.CTkLabel(f_main, text="konstrukční systém")
l_pozarni_vyska = ctk.CTkLabel(f_main, text="požární výška")

# umístění dvou horních rámečků
f_main.place(relwidth=0.3, relheight=0.5)
f_seznam_PU.place(relx= 0.3, relwidth=0.8, relheight=0.5)

# umístění tlačítek do panelu pro tlačítka
om_konstrukcni_system.grid(row=1, column=2)
l_konstrukcni_system.grid(row=1, column=1)
e_pozarni_vyska.grid(row=2, column=2)
l_pozarni_vyska.grid(row=2, column=1)

b_add_f.grid(row=4, column=1)
b_remove_f.grid(row=5, column=1)

b_lift.grid(row=7, column=1)
b_lower.grid(row=7, column=3)

# f_seznamPU widgets
l_oznaceni = ctk.CTkLabel(f_seznam_PU, text="Označení PÚ")
l_PU = ctk.CTkLabel(f_seznam_PU, text="Název PÚ")
l_typ = ctk.CTkLabel(f_seznam_PU, text="typ objektu")
l_pn = ctk.CTkLabel(f_seznam_PU, text ="pn celkem: ")
l_an = ctk.CTkLabel(f_seznam_PU, text="an celkem: ")
l_p = ctk.CTkLabel(f_seznam_PU, text="p celkem: ")
l_ps = ctk.CTkLabel(f_seznam_PU, text="ps celkem: ")
l_S = ctk.CTkLabel(f_seznam_PU, text="Suma S: ")

# f_seznamPU layout
l_oznaceni.grid(row=0, column=0)
l_PU.grid(row=0, column=1)
l_typ.grid(row=0, column=2)


# spuštění okna
window.mainloop()