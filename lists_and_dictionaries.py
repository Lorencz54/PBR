
sirka_okna = [1600]
vyska_okna = [1000]
m_current_value = []
#list of frames and rows
list_f_PU = []
list_f_info_PU = []
list_m_rows = []
list_pu_number = []
list_PBR_frames = []

# lists of global variables
current_frame = [0]
list_e_pozarni_vyska = []
list_var_e_pozarni_vyska = []
list_var_om_konstrukcni_system = []
list_var_om_typ_pu = []

#lists of pu entries
list_om_typ_pu = []
list_om_konstrukcni_system_pu = []
list_var_l_pv = []
list_nazvy_pu_default = []
list_cisla_pu = []
list_nazvy_pu = []

#labels
list_l_S = []
list_l_an = []
list_l_pn = []
list_l_ps = []
list_l_p = []
list_l_a = []
list_l_hs = []
list_l_so = []
list_l_ho = []
list_l_b = []
list_l_n = []
list_l_k = []
list_l_pv = []
list_l_SPB = []
#lists of entries from individual pu
list_pocty_podlazi_pu = []
list_sirky_pu = []
list_delky_pu = []
list_vyskove_polohy_pu = []

#list of output variables PU
list_S = []
list_pn = []
list_hs = []
list_an = []
list_ps = []
list_a = []
list_ho = []
list_so = []
list_k = []
list_b = []
list_p = []
list_pv = []
list_mezni_pocty_podlazi = []
list_mezni_delky = []
list_mezni_sirky = []
list_var_l_SPB = []

# dictionaries
dic_m_rows = []
dic_ps_group_sums = []
dic_o_rows = []
list_e_PU = []
dic_so_ot = []

# row entry widget dictionaries
dic_hsi_entries = []
dic_pni_entries = []
dic_ani_entries = []
dic_psi_entries = []
dic_S_entries = []
dic_CSNi_entries = []
dic_mc_text_entries = []
dic_nazvy_m_text_entries = []
dic_ps_row_sum_labels = []

dic_pocet_ot_entries = []
dic_sirka_ot_entries = []
dic_vyska_ot_entries = []
dic_typy_ot_option_menues = []


# listy pro vars, které spouští navazující funkce entry widgetů
dic_hsi_var_entries = []
dic_pni_var_entries = []
dic_ani_var_entries = []
dic_ps_var_entries = []
dic_S_var_entries = []
dic_var_pocet_ot = []
dic_var_sirka_ot = []
dic_var_vyska_ot = []

# dictionary pro listy s vars, které automaticky updatují součty ps v každém řádku místností PÚ
dic_var_ps_labels = []