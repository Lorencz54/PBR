from table_manager import *
from lists_and_dictionaries import *


window = ttk.Window(themename="darkly")
window.geometry("1500x500")

current_frame = 0
as_value = 0.9

def lift_frame_get():
    global current_frame
    current_frame = lift_frame(current_frame)


def lower_frame_get():
    global current_frame
    current_frame = lower_frame(current_frame)

# tvorba tabů
n_PU = ttk.Notebook(window)
n_PU.place(rely=0.5, relwidth = 1)

# sestavení dvou horních rámečků (hlavní informace o objektu a panel pro tlačítka)
f_main = ttk.Frame(window, width=100, height=200, relief="ridge")
f_button_panel = ttk.Frame(window, width=100, height=200, relief="ridge")

# definice tlačítek pro panel na tlačítka
b_add_f = ttk.Button(f_button_panel, text="nový požární úsek", command=lambda: add_f(window, list_nazvy_pu_default, list_f_PU, list_l_S, list_l_an, list_l_pn, list_l_ps, list_l_p, list_l_a, list_l_hs, list_l_so, list_l_ho, frame_count, current_frame, f_main, n_PU))
b_remove_f = ttk.Button(f_button_panel, text="odebrat požární úsek", command=lambda: remove_f(list_cisla_pu, list_nazvy_pu, list_e_typ, current_frame))
b_lift = ttk.Button(f_button_panel, text="předchozí PÚ", command=lift_frame_get)
b_lower = ttk.Button(f_button_panel, text="další PÚ", command=lower_frame_get)

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

# spuštění okna
window.mainloop()