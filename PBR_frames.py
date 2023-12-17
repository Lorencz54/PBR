from m_plus_and_minus import *
def create_room_list(window):
    f_room_list = ctk.CTkFrame(window)
    f_room_list.place(relx=0.3, relwidth=0.7, relheight=0.5)
    list_PBR_frames.append(f_room_list)

    # nadpis sloupců v rámečku
    l_room_list_nadpis = ctk.CTkLabel(f_room_list, text="Seznam místností objektu", anchor="center")
    l_room_list_nadpis.grid(row=0, column=1, columnspan=10)

    b_new_room = ctk.CTkButton(f_room_list, text="nová místnost", command=m_plus)
    b_new_room.grid(row=0, column=0)

    l_cm = ctk.CTkLabel(f_room_list, text="č. m.", anchor="center", width=40)
    l_cm.grid(row=1, column=0)
    l_nazev_m = ctk.CTkLabel(f_room_list, text="název místnosti", anchor="center", width=200)
    l_nazev_m.grid(row=1, column=1)
    l_S = ctk.CTkLabel(f_room_list, text="plocha místnosti", anchor="center", width=80, wraplength=60)
    l_S.grid(row=1, column=2)
    l_hsi_m = ctk.CTkLabel(f_room_list, text="hsi", anchor="center", width=80)
    l_hsi_m.grid(row=1, column=3)
    l_CSN_pol_02 = ctk.CTkLabel(f_room_list, text="ČNS 73 0802", anchor="center", width=80)
    l_CSN_pol_02.grid(row=1, column=4)
    l_pn_m = ctk.CTkLabel(f_room_list, text="pni", anchor="center", width=80)
    l_pn_m.grid(row=1, column=5)
    l_an_m = ctk.CTkLabel(f_room_list, text="ani", anchor="center", width=80)
    l_an_m.grid(row=1, column=6)
    l_ps_d = ctk.CTkLabel(f_room_list, text="psi dveře", anchor="center", width=80, wraplength=50)
    l_ps_d.grid(row=1, column=7)
    l_ps_o = ctk.CTkLabel(f_room_list, text="psi okna", anchor="center", width=80, wraplength=40)
    l_ps_o.grid(row=1, column=8)
    l_ps_p = ctk.CTkLabel(f_room_list, text="psi podlahy", anchor="center", width=80, wraplength=50)
    l_ps_p.grid(row=1, column=9)
    l_pocet_os_PD = ctk.CTkLabel(f_room_list, text="počet osob dle PD", anchor="center", width=80, wraplength=60)
    l_pocet_os_PD.grid(row=1, column=10)
    l_CSN_pol_18 = ctk.CTkLabel(f_room_list, text="ČNS 73 0818", anchor="center", width=80, wraplength=60)
    l_CSN_pol_18.grid(row=1, column=11)
    l_m2_na_os = ctk.CTkLabel(f_room_list, text="m2/os", anchor="center", width=80, wraplength=60)
    l_m2_na_os.grid(row=1, column=12)
    l_soucinitel_na_os = ctk.CTkLabel(f_room_list, text="násobek osob dle PD", anchor="center", width=80, wraplength=60)
    l_soucinitel_na_os.grid(row=1, column=13)
def create_seznam_PU(window):
    f_seznam_PU = ctk.CTkFrame(window)
    f_seznam_PU.place(relx=0.3, relwidth=0.7, relheight=0.5)
    list_PBR_frames.append(f_seznam_PU)

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

def lift_seznam_PU():
    list_PBR_frames[0].lift()

def lift_room_list():
    list_PBR_frames[1].lift()


