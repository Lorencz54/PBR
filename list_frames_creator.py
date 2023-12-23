from m_plus_and_minus import *
def create_room_list():
    # vytvoření framu
    f_room_list = ctk.CTkFrame(window[0])
    f_room_list.place(relx=0.3, relwidth=0.7, relheight=0.5)
    list_PBR_frames.append(f_room_list)

    # nadpis sloupců v rámečku
    l_room_list_nadpis = ctk.CTkLabel(f_room_list, text="Seznam místností objektu", anchor="center")
    l_room_list_nadpis.grid(row=0, column=0, columnspan=4)

    l_cm = ctk.CTkLabel(f_room_list, text="č. m.", anchor="center", width=40)
    l_cm.grid(row=1, column=0)
    l_nazev_m = ctk.CTkLabel(f_room_list, text="název místnosti", anchor="center", width=200)
    l_nazev_m.grid(row=1, column=1)
    l_S = ctk.CTkLabel(f_room_list, text="plocha místnosti", anchor="center", width=80, wraplength=60)
    l_S.grid(row=1, column=2)
    l_hsi_m = ctk.CTkLabel(f_room_list, text="hsi", anchor="center", width=80)
    l_hsi_m.grid(row=1, column=3)

    # tlačítko pro přidání a odebrání místnosti
    b_new_room = ctk.CTkButton(f_room_list, text="+", width=25, height=25, command=object_m_plus)
    b_new_room.grid(row=1, column=4)
    b_remove_room = ctk.CTkButton(f_room_list, text="-", width=25, height=25)
    b_remove_room.grid(row=2, column=4)
def create_seznam_PU():
    # vytvoření framu
    f_seznam_PU = ctk.CTkFrame(window[0])
    f_seznam_PU.place(relx=0.3, relwidth=0.7, relheight=0.5)
    list_PBR_frames.append(f_seznam_PU)
# nadpis seznamu požárních úseků
    l_PU_list_nadpis = ctk.CTkLabel(f_seznam_PU, text="Seznam požárních úseků", anchor="center")
    l_PU_list_nadpis.grid(row=0, column=0, columnspan=5)

# nadpis sloupců v rámečku
    l_typ_pu = ctk.CTkLabel(f_seznam_PU, text="typ objektu", width=140)
    l_typ_pu.grid(row=1, column=0)
    l_konstrukcni_system_pu = ctk.CTkLabel(f_seznam_PU, text="konstrukční systém", width=140)
    l_konstrukcni_system_pu.grid(row=1, column=1)
    l_oznaceni_pu = ctk.CTkLabel(f_seznam_PU, text="Označení PÚ", width=140)
    l_oznaceni_pu.grid(row=1, column=2)
    l_nazev_pu = ctk.CTkLabel(f_seznam_PU, text="Název PÚ", width=140)
    l_nazev_pu.grid(row=1, column=3)
    l_pv = ctk.CTkLabel(f_seznam_PU, text="pv", width=140)
    l_pv.grid(row=1, column=4)
    l_SPB = ctk.CTkLabel(f_seznam_PU, text="SPB", width=140)
    l_SPB.grid(row=1, column=5)

def lift_seznam_PU():
    list_PBR_frames[0].lift()

def lift_room_list():
    list_PBR_frames[1].lift()


