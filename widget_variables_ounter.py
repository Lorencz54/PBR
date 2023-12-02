from functions_following_widget_variables import *

def plocha_PU(current_frame,list_l_S):
    list_l_S[current_frame].set(np.sum((float(entry.get()) if entry.get().isdigit() else 0 for entry in dic_S_var_entries[current_frame])))

    # funkce na výpočet pn v current framu
def pn(current_frame, list_l_pn, dic_pni_entries, dic_S_entries):
    pn_values = [float(entry.get()) if entry.get().isdigit() else 0 for entry in dic_pni_entries[current_frame]]
    S_values = [float(entry.get()) if entry.get().isdigit() else 0 for entry in dic_S_entries[current_frame]]
    S_suma = np.sum((float(entry.get()) if entry.get().isdigit() else 0 for entry in dic_S_entries[current_frame]))
    if np.dot(pn_values, S_values) == 0 or S_suma == 0:
        list_l_pn[current_frame].set(0)
    else:
        list_l_pn[current_frame].set(round(np.dot(pn_values, S_values)/S_suma,2))
    calculate_pv_value(current_frame)

# funkce na výpočet an v current framu
def an(current_frame, list_l_an, dic_ani_entries, dic_S_entries):
    an_values = [float(entry.get()) if entry.get().isdigit() else 0 for entry in dic_ani_entries[current_frame]]
    S_values = [float(entry.get()) if entry.get().isdigit() else 0 for entry in dic_S_entries[current_frame]]
    S_suma = np.sum((float(entry.get()) if entry.get().isdigit() else 0 for entry in dic_S_entries[current_frame]))
    if np.dot(an_values, S_values) == 0 or S_suma == 0:
        list_l_an[current_frame].set(0)
    else:
        list_l_an[current_frame].set(round(np.dot(an_values, S_values)/S_suma,2))
    calculate_pv_value(current_frame)
#funkce na výpočet ps v current framu
def ps(current_frame, list_l_ps, dic_ps_entries, dic_S_entries):
    S_values = [float(entry.get()) if entry.get().isdigit() else 0 for entry in dic_S_entries[current_frame]]
    S_suma = np.sum((float(entry.get()) if entry.get().isdigit() else 0 for entry in dic_S_entries[current_frame]))
    psi_values = [float(entry.get()) if entry.get().isdigit() else 0 for entry in dic_ps_entries[current_frame]]
    list_ps_arr = np.array(psi_values)
    list_ps_reshape = list_ps_arr.reshape(-1,3)
    ps_sum = np.sum(list_ps_reshape, axis=1)
    ps_sum_list = ps_sum.tolist()
    if np.dot(ps_sum_list, S_values) == 0 or S_suma == 0:
        list_l_ps[current_frame].set(0)
    else:
        list_l_ps[current_frame].set(round(np.dot(ps_sum_list, S_values)/S_suma,2))
    for i in range(len(ps_sum_list)):
        ps_row_sum = ps_sum_list[i]
        label_ps_sum = dic_ps_labels[current_frame][i]
        label_ps_sum.set(ps_row_sum)
    calculate_pv_value(current_frame)

# funkce na výpočet výšky prostoru v požárním úseku
def hs_so(current_frame):
    pocet_values = [float(entry.get()) if entry.get().isdigit() else 0 for entry in dic_var_pocet_ot[current_frame]]
    sirka_values = [float(entry.get()) if entry.get().isdigit() else 0 for entry in dic_var_sirka_ot[current_frame]]
    vyska_values = [float(entry.get()) if entry.get().isdigit() else 0 for entry in dic_var_vyska_ot[current_frame]]
    so_values = np.multiply(np.multiply(pocet_values, sirka_values), vyska_values)
    so_value = np.sum(so_values)
    list_l_so[current_frame].set(round(so_value, 2))
    if np.dot(np.multiply(np.multiply(pocet_values, sirka_values), vyska_values), vyska_values) == 0 or so_value == 0:
        list_l_ho[current_frame].set(0.0)
    else:
        list_l_ho[current_frame].set(round(np.dot(so_values, vyska_values)/so_value,2))
    calculate_pv_value(current_frame)

def hs(current_frame):
    S_values = [float(entry.get()) if entry.get().isdigit() else 0 for entry in dic_S_entries[current_frame]]
    hsi_values = [float(entry.get()) if entry.get().isdigit() else 0 for entry in dic_hsi_entries[current_frame]]
    S_suma = np.sum((float(entry.get()) if entry.get().isdigit() else 0 for entry in dic_S_entries[current_frame]))
    if np.dot(hsi_values, S_values) == 0 or S_suma == 0:
        list_l_hs[current_frame].set(0)
    else:
        list_l_hs[current_frame].set(round(np.dot(hsi_values, S_values)/S_suma,2))
    calculate_pv_value(current_frame)

