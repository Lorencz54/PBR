from pv_and_max_floor_counter import *
from max_dimension_counter import *
def plocha_PU(current_frame,list_l_S):
    list_l_S[int(current_frame[0])].set(np.sum((float(entry.get()) if entry.get() != "" else 0.0 for entry in dic_S_entries[int(current_frame[0])])))

    # funkce na výpočet pn v current framu
def pn(current_frame, list_l_pn, dic_pni_entries, dic_S_entries):
    pn_values = [float(entry.get()) if entry.get() != "" else 0.0 for entry in dic_pni_entries[int(current_frame[0])]]
    S_values = [float(entry.get()) if entry.get() != "" else 0.0 for entry in dic_S_entries[int(current_frame[0])]]
    S_suma = np.sum((float(entry.get()) if entry.get() != "" else 0.0 for entry in dic_S_entries[int(current_frame[0])]))
    if np.dot(pn_values, S_values) == 0 or S_suma == 0:
        list_l_pn[int(current_frame[0])].set(0)
    else:
        list_l_pn[int(current_frame[0])].set(round(np.dot(pn_values, S_values)/S_suma,2))
    calculate_pv_value(current_frame)
    calculate_max_dimensions(current_frame)

# funkce na výpočet an v current framu
def an(current_frame, list_l_an, dic_ani_entries, dic_S_entries):
    an_values = [float(entry.get()) if entry.get() != "" else 0.0 for entry in dic_ani_entries[int(current_frame[0])]]
    S_values = [float(entry.get()) if entry.get() != "" else 0.0 for entry in dic_S_entries[int(current_frame[0])]]
    S_suma = np.sum((float(entry.get()) if entry.get() != "" else 0.0 for entry in dic_S_entries[int(current_frame[0])]))
    if np.dot(an_values, S_values) == 0 or S_suma == 0:
        list_l_an[int(current_frame[0])].set(0.0)
    else:
        list_l_an[int(current_frame[0])].set(round(np.dot(an_values, S_values)/S_suma,2))
    calculate_pv_value(current_frame)
    calculate_max_dimensions(current_frame)

#funkce na výpočet ps v current framu
def ps(current_frame, list_l_ps, dic_ps_entries, dic_S_entries):
    S_values = [float(entry.get()) if entry.get() != "" else 0.0 for entry in dic_S_entries[int(current_frame[0])]]
    S_suma = np.sum((float(entry.get()) if entry.get() != "" else 0.0 for entry in dic_S_entries[int(current_frame[0])]))
    psi_values = [float(entry.get()) if entry.get() != "" else 0.0 for entry in dic_ps_entries[int(current_frame[0])]]
    list_ps_arr = np.array(psi_values)
    list_ps_reshape = list_ps_arr.reshape(-1,3)
    ps_sum = np.sum(list_ps_reshape, axis=1)
    ps_sum_list = ps_sum.tolist()
    if np.dot(ps_sum_list, S_values) == 0 or S_suma == 0:
        list_l_ps[int(current_frame[0])].set(0)
    else:
        list_l_ps[int(current_frame[0])].set(round(np.dot(ps_sum_list, S_values)/S_suma,2))
    for i in range(len(ps_sum_list)):
        ps_row_sum = ps_sum_list[i]
        dic_var_ps_labels[int(current_frame[0])][i].set(ps_row_sum)
    calculate_pv_value(current_frame)
    calculate_max_dimensions(current_frame)

    #labels
    print(list_l_S)
    print(list_l_an)
    print(list_l_pn)
    print(list_l_ps)
    print(list_l_p)
    print(list_l_a)
    print(list_l_hs)
    print(list_l_so)
    print(list_l_ho)
    print(list_l_b)
    print(list_l_n)
    print(list_l_k)
    print(list_l_pv)

    #lists of entries from individual pu
    print(list_pocty_podlazi_pu)#
    print(list_sirky_pu)#
    print(list_delky_pu)#
    print(list_vyskove_polohy_pu)#

    #list of output variables PU
    print(list_S)
    print(list_pn)
    print(list_hs)
    print(list_an)
    print(list_ps)
    print(list_a)
    print(list_ho)
    print(list_so)
    print(list_k)
    print(list_b)
    print(list_p)
    print(list_pv)
    print(list_mezni_pocty_podlazi)#
    print(list_mezni_delky)#
    print(list_mezni_sirky)#
    print(list_var_l_SPB)#
    print(list_var_l_pv)
# funkce na výpočet výšky prostoru v požárním úseku
def hs_so(current_frame):
    pocet_values = [float(entry.get()) if entry.get() != "" else 0.0 for entry in dic_pocet_ot_entries[int(current_frame[0])]]
    sirka_values = [float(entry.get()) if entry.get() != "" else 0.0 for entry in dic_sirka_ot_entries[int(current_frame[0])]]
    vyska_values = [float(entry.get()) if entry.get() != "" else 0.0 for entry in dic_vyska_ot_entries[int(current_frame[0])]]
    so_values = np.multiply(np.multiply(pocet_values, sirka_values), vyska_values)
    so_value = np.sum(so_values)
    list_l_so[int(current_frame[0])].set(round(so_value, 2))
    if np.dot(np.multiply(np.multiply(pocet_values, sirka_values), vyska_values), vyska_values) == 0 or so_value == 0:
        list_l_ho[int(current_frame[0])].set(0.0)
    else:
        list_l_ho[int(current_frame[0])].set(round(np.dot(so_values, vyska_values)/so_value,2))
    calculate_pv_value(current_frame)

def hs(current_frame):
    S_values = [float(entry.get()) if entry.get() != "" else 0.0 for entry in dic_S_entries[int(current_frame[0])]]
    hsi_values = [float(entry.get()) if entry.get() != "" else 0.0 for entry in dic_hsi_entries[int(current_frame[0])]]
    S_suma = np.sum((float(entry.get()) if entry.get() != "" else 0.0 for entry in dic_S_entries[int(current_frame[0])]))
    if np.dot(hsi_values, S_values) == 0 or S_suma == 0:
        list_l_hs[int(current_frame[0])].set(0.0)
    else:
        list_l_hs[int(current_frame[0])].set(round(np.dot(hsi_values, S_values)/S_suma,2))
    calculate_pv_value(current_frame)

