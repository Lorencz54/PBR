import pandas as pd
import numpy as np
from scipy.interpolate import interp1d

data_path = r'C:\Users\Lenovo\PycharmProjects\PBR\data.xlsx'


# sheets
sh_mezni_rozmery_pu = "limit_dimension_pu"
df_mezni_rozmery_pu = pd.read_excel(data_path, sheet_name=sh_mezni_rozmery_pu, header=6)

# extracted data
# hodnoty k pro požární úsek do 500 m2
radek_hodnot_S = [5, 10, 20, 30, 50, 100, 250, 500]
sloupec_hodnot_n = [0.005, 0.01, 0.015, 0.02, 0.025, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.12, 0.14, 0.16, 0.18, 0.2, 0.25, 0.3, 0.35]
hodnoty_k = [[0.005, 0.007, 0.009, 0.011, 0.013, 0.015, 0.016, 0.02], [0.013, 0.015, 0.018, 0.02, 0.024, 0.027, 0.033, 0.038], [0.018, 0.022, 0.027, 0.031, 0.035, 0.04, 0.049, 0.055], [0.024, 0.029, 0.036, 0.04, 0.044, 0.051, 0.062, 0.071], [0.029, 0.036, 0.044, 0.049, 0.055, 0.062, 0.076, 0.085], [0.035, 0.044, 0.051, 0.056, 0.064, 0.073, 0.089, 0.098], [0.045, 0.056, 0.065, 0.073, 0.08, 0.093, 0.113, 0.125], [0.055, 0.067, 0.08, 0.087, 0.096, 0.113, 0.133, 0.147], [0.065, 0.078, 0.093, 0.102, 0.113, 0.129, 0.153, 0.165], [0.075, 0.089, 0.105, 0.115, 0.127, 0.145, 0.167, 0.182], [0.084, 0.1, 0.118, 0.127, 0.14, 0.158, 0.18, 0.193], [0.091, 0.111, 0.129, 0.14, 0.153, 0.171, 0.191, 0.204], [0.1, 0.12, 0.14, 0.151, 0.164, 0.18, 0.2, 0.211], [0.116, 0.138, 0.158, 0.169, 0.182, 0.197, 0.215, 0.224], [0.131, 0.155, 0.175, 0.184, 0.195, 0.209, 0.225, 0.236], [0.144, 0.167, 0.185, 0.195, 0.205, 0.218, 0.235, 0.245], [0.156, 0.178, 0.196, 0.205, 0.215, 0.227, 0.245, 0.255], [0.167, 0.187, 0.205, 0.213, 0.222, 0.235, 0.253, 0.264], [0.187, 0.207, 0.222, 0.229, 0.24, 0.253, 0.267, 0.273], [0.204, 0.22, 0.235, 0.244, 0.253, 0.265, 0.273, 0.273], [0.215, 0.233, 0.247, 0.255, 0.264, 0.273, 0.273, 0.273]]

# hodnoty (součinitel a, délka a šířka) pro mezní rozměry PÚ s nehořlavým konstrukčním systémem
data_nehorlavy_a_values_mr_pu = df_mezni_rozmery_pu.iloc[:, 0].values
data_nehorlavy_1_np_mezni_delky_pu = df_mezni_rozmery_pu.iloc[:, 2].values
data_nehorlavy_1_np_mezni_sirky_pu = df_mezni_rozmery_pu.iloc[:, 3].values
data_nehorlavy_22_mezni_delky_pu = df_mezni_rozmery_pu.iloc[:, 4].values
data_nehorlavy_22_mezni_sirky_pu = df_mezni_rozmery_pu.iloc[:, 5].values
data_nehorlavy_45_mezni_delky_pu = df_mezni_rozmery_pu.iloc[:, 6].values
data_nehorlavy_45_mezni_sirky_pu = df_mezni_rozmery_pu.iloc[:, 7].values
data_nehorlavy_vetsi_45_mezni_delky_pu = df_mezni_rozmery_pu.iloc[:, 8].values
data_nehorlavy_vetsi_45_mezni_sirky_pu = df_mezni_rozmery_pu.iloc[:, 9].values

data_smiseny_1_np_mezni_delky_pu = df_mezni_rozmery_pu.iloc[:, 13].values
data_smiseny_1_np_mezni_sirky_pu = df_mezni_rozmery_pu.iloc[:, 15].values
data_smiseny_vice_np_mezni_delky_pu = df_mezni_rozmery_pu.iloc[:, 17].values
data_smiseny_vice_np_mezni_sirky_pu = df_mezni_rozmery_pu.iloc[:, 19].values

data_horlavy_1_np_mezni_delky_pu = df_mezni_rozmery_pu.iloc[:, 24].values
data_horlavy_1_np_mezni_sirky_pu = df_mezni_rozmery_pu.iloc[:, 26].values
data_horlavy_vice_np_mezni_delky_pu = df_mezni_rozmery_pu.iloc[:, 28].values
data_horlavy_vice_np_mezni_sirky_pu = df_mezni_rozmery_pu.iloc[:, 30].values


# funkce
interpolation_function = interp1d(data_nehorlavy_a_values_mr_pu, data_nehorlavy_1_np_mezni_delky_pu, kind='linear', fill_value='extrapolate')
new_a_point = np.array([0.65])
interpolated = interpolation_function(new_a_point)