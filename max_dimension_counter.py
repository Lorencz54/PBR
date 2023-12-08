from lists_and_dictionaries import *
from data import *
from scipy.interpolate import interp1d


# mezní rozměry požárního úseku
def calculate_max_dimensions(current_frame):
    if len(list_l_a) != 0:
        a = list_l_a[int(current_frame[0])].get()
        if a < 0.3:
            a = 0.3
        elif a > 1.3:
            a = 1.3

        if list_var_om_konstrukcni_system[0].get() == "nehořlavý":
            if list_var_e_pozarni_vyska[0].get() == 0:
                mezni_sirka_pu = interp1d(data_nehorlavy_a_values_mr_pu, data_nehorlavy_1_np_mezni_sirky_pu, kind='linear',fill_value='extrapolate')
                mezni_sirka_interpolated = np.round(mezni_sirka_pu(np.array(a)), 2)
                list_mezni_sirky[int(current_frame[0])].set(mezni_sirka_interpolated)
                mezni_delka_pu = interp1d(data_nehorlavy_a_values_mr_pu, data_nehorlavy_1_np_mezni_delky_pu, kind='linear',fill_value='extrapolate')
                mezni_delka_interpolated = np.round(mezni_delka_pu(np.array(a)), 2)
                list_mezni_delky[int(current_frame[0])].set(mezni_delka_interpolated)
            elif list_var_e_pozarni_vyska[0].get() <= 22.5:
                mezni_sirka_pu = interp1d(data_nehorlavy_a_values_mr_pu, data_nehorlavy_22_mezni_sirky_pu, kind='linear',fill_value='extrapolate')
                mezni_sirka_interpolated = np.round(mezni_sirka_pu(np.array(a)), 2)
                list_mezni_sirky[int(current_frame[0])].set(mezni_sirka_interpolated)
                mezni_delka_pu = interp1d(data_nehorlavy_a_values_mr_pu, data_nehorlavy_22_mezni_delky_pu, kind='linear',fill_value='extrapolate')
                mezni_delka_interpolated = np.round(mezni_delka_pu(np.array(a)), 2)
                list_mezni_delky[int(current_frame[0])].set(mezni_delka_interpolated)
            elif list_var_e_pozarni_vyska[0].get() <= 45:
                mezni_sirka_pu = interp1d(data_nehorlavy_a_values_mr_pu, data_nehorlavy_45_mezni_sirky_pu, kind='linear',fill_value='extrapolate')
                mezni_sirka_interpolated = np.round(mezni_sirka_pu(np.array(a)), 2)
                list_mezni_sirky[int(current_frame[0])].set(mezni_sirka_interpolated)
                mezni_delka_pu = interp1d(data_nehorlavy_a_values_mr_pu, data_nehorlavy_45_mezni_delky_pu, kind='linear',fill_value='extrapolate')
                mezni_delka_interpolated = np.round(mezni_delka_pu(np.array(a)), 2)
                list_mezni_delky[int(current_frame[0])].set(mezni_delka_interpolated)
            else:
                mezni_sirka_pu = interp1d(data_nehorlavy_a_values_mr_pu, data_nehorlavy_vetsi_45_mezni_sirky_pu, kind='linear', fill_value='extrapolate')
                mezni_sirka_interpolated = np.round(mezni_sirka_pu(np.array(a)), 2)
                list_mezni_sirky[int(current_frame[0])].set(mezni_sirka_interpolated)
                mezni_delka_pu = interp1d(data_nehorlavy_a_values_mr_pu, data_nehorlavy_vetsi_45_mezni_delky_pu, kind='linear', fill_value='extrapolate')
                mezni_delka_interpolated = np.round(mezni_delka_pu(np.array(a)), 2)
                list_mezni_delky[int(current_frame[0])].set(mezni_delka_interpolated)
        elif list_var_om_konstrukcni_system[0].get() == "smíšený":
            if list_var_e_pozarni_vyska[0].get() == 0:
                mezni_sirka_pu = interp1d(data_nehorlavy_a_values_mr_pu, data_smiseny_1_np_mezni_sirky_pu, kind='linear',fill_value='extrapolate')
                mezni_sirka_interpolated = np.round(mezni_sirka_pu(np.array(a)), 2)
                list_mezni_sirky[int(current_frame[0])].set(mezni_sirka_interpolated)
                mezni_delka_pu = interp1d(data_nehorlavy_a_values_mr_pu, data_smiseny_1_np_mezni_delky_pu, kind='linear',fill_value='extrapolate')
                mezni_delka_interpolated = np.round(mezni_delka_pu(np.array(a)), 2)
                list_mezni_delky[int(current_frame[0])].set(mezni_delka_interpolated)
            else:
                mezni_sirka_pu = interp1d(data_nehorlavy_a_values_mr_pu, data_smiseny_vice_np_mezni_sirky_pu, kind='linear',fill_value='extrapolate')
                mezni_sirka_interpolated = np.round(mezni_sirka_pu(np.array(a)), 2)
                list_mezni_sirky[int(current_frame[0])].set(mezni_sirka_interpolated)
                mezni_delka_pu = interp1d(data_nehorlavy_a_values_mr_pu, data_smiseny_vice_np_mezni_delky_pu, kind='linear',fill_value='extrapolate')
                mezni_delka_interpolated = np.round(mezni_delka_pu(np.array(a)), 2)
                list_mezni_delky[int(current_frame[0])].set(mezni_delka_interpolated)
        else:
            if list_var_e_pozarni_vyska[0].get() == 0:
                mezni_sirka_pu = interp1d(data_nehorlavy_a_values_mr_pu, data_horlavy_1_np_mezni_sirky_pu, kind='linear',fill_value='extrapolate')
                mezni_sirka_interpolated = np.round(mezni_sirka_pu(np.array(a)), 2)
                list_mezni_sirky[int(current_frame[0])].set(mezni_sirka_interpolated)
                mezni_delka_pu = interp1d(data_nehorlavy_a_values_mr_pu, data_horlavy_1_np_mezni_delky_pu, kind='linear',fill_value='extrapolate')
                mezni_delka_interpolated = np.round(mezni_delka_pu(np.array(a)), 2)
                list_mezni_delky[int(current_frame[0])].set(mezni_delka_interpolated)
            else:
                mezni_sirka_pu = interp1d(data_nehorlavy_a_values_mr_pu, data_horlavy_vice_np_mezni_sirky_pu, kind='linear',fill_value='extrapolate')
                mezni_sirka_interpolated = np.round(mezni_sirka_pu(np.array(a)), 2)
                list_mezni_sirky[int(current_frame[0])].set(mezni_sirka_interpolated)
                mezni_delka_pu = interp1d(data_nehorlavy_a_values_mr_pu, data_horlavy_vice_np_mezni_delky_pu, kind='linear',fill_value='extrapolate')
                mezni_delka_interpolated = np.round(mezni_delka_pu(np.array(a)), 2)
                list_mezni_delky[int(current_frame[0])].set(mezni_delka_interpolated)