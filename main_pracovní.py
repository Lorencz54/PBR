from pu_plus_and_minus import *
from list_frames_creator import *
from PDF_generator import *

# funkce na listování mezi rámečky
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

main_window = ctk.CTk()
window.append(main_window)
main_window.geometry(f"{sirka_okna[0]}x{vyska_okna[0]}")

# Hlavní frames (info celého objektu, seznam PU seznam místností)
f_info_objekt = ctk.CTkFrame(main_window)
f_info_objekt.place(relwidth=0.3, relheight=0.5)
create_seznam_PU()
create_room_list()

# widgety framu info celého objektu
b_add_f = ctk.CTkButton(f_info_objekt, text="nový požární úsek", command= add_new_pu)
b_add_f.grid(row=4, column=1)
b_remove_f = ctk.CTkButton(f_info_objekt, text="odebrat požární úsek", command= remove_f)
b_remove_f.grid(row=5, column=1)
b_lift = ctk.CTkButton(f_info_objekt, text="předchozí PÚ", command=lift_frame)
b_lift.grid(row=7, column=1)
b_lower = ctk.CTkButton(f_info_objekt, text="další PÚ", command=lower_frame)
b_lower.grid(row=7, column=2)

l_pozarni_vyska = ctk.CTkLabel(f_info_objekt, text="požární výška")
l_pozarni_vyska.grid(row=2, column=1)
var_e_pozarni_vyska = tk.StringVar()
e_pozarni_vyska = EntryWithLimit(f_info_objekt, textvariable=var_e_pozarni_vyska)
list_e_pozarni_vyska.append(e_pozarni_vyska)
e_pozarni_vyska.grid(row=2, column=2)
list_var_e_pozarni_vyska.append(var_e_pozarni_vyska)
var_e_pozarni_vyska.trace_add("write", lambda name, index, mode, sv=list_var_e_pozarni_vyska: calculate_max_dimensions())
var_e_pozarni_vyska.trace_add("write", lambda name, index, mode, sv=list_var_e_pozarni_vyska: determine_SPB())

l_pocet_NP_objektu = ctk.CTkLabel(f_info_objekt, text="počet NP objektu")
l_pocet_NP_objektu.grid(row=3, column=1)
var_e_pocet_NP_objektu = tk.StringVar()
e_pocet_NP_objektu = EntryWithLimit(f_info_objekt, textvariable=var_e_pocet_NP_objektu)
list_e_pocet_NP_objektu.append(e_pocet_NP_objektu)
e_pocet_NP_objektu.grid(row=3, column=2)
list_var_e_pocet_NP_objektu.append(var_e_pocet_NP_objektu)
var_e_pocet_NP_objektu.trace_add("write", lambda name, index, mode, sv=list_var_e_pocet_NP_objektu: determine_SPB())

b_pu_list = ctk.CTkButton(f_info_objekt, text="požární úseky", command=lift_seznam_PU)
b_pu_list.grid(row=3, column=3)
b_room_list = ctk.CTkButton(f_info_objekt, text="seznam místností", command=lift_room_list)
b_room_list.grid(row=4, column=3)

b_generate_pdf = ctk.CTkButton(f_info_objekt, text="Generate PDF", command=generate_pdf)
b_generate_pdf.grid(row=8, column=1)
# spuštění okna
main_window.mainloop()