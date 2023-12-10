import pandas as pd
import numpy as np

data_path = r'C:\Users\kevin\PycharmProjects\pythonProject\data.xlsx'

k_system = "hořlavý"
pv_PÚ = 110
pozarni_vyska = 3
soucinitel_a = 1.2

# sheets
sh_SPB = "SPB"
df_SPB = pd.read_excel(data_path, sheet_name=sh_SPB, header=0)

if k_system == "nehořlavý":
    df_pv_values = np.array(df_SPB.iloc[0:7, 0].values)
    pv_higher_than_pvpu_indexes = np.where(df_pv_values >= pv_PÚ)[0]
    min_index = pv_higher_than_pvpu_indexes[np.argmin(df_pv_values[pv_higher_than_pvpu_indexes])]

elif k_system == "smíšený":
    df_pv_values = np.array(df_SPB.iloc[9:16, 0].values)
    pv_higher_than_pvpu_indexes = np.where(df_pv_values >= pv_PÚ)[0]
    min_index = 9+pv_higher_than_pvpu_indexes[np.argmin(df_pv_values[pv_higher_than_pvpu_indexes])]

else:
    df_pv_values = np.array(df_SPB.iloc[18:25, 0].values)
    pv_higher_than_pvpu_indexes = np.where(df_pv_values >= pv_PÚ)[0]
    min_index = 18+pv_higher_than_pvpu_indexes[np.argmin(df_pv_values[pv_higher_than_pvpu_indexes])]

list = df_SPB.iloc[min_index, 1:8].tolist()

for i in range (len(list)):
    if list[i] == "N1":
        pass
    elif list[i] == "Oa":
        if pozarni_vyska == 0 and soucinitel_a <= 1.1:
            print(df_SPB.columns[i+1])
            break
        pass
    elif list[i] == "O":
        if pozarni_vyska == 0:
            print(df_SPB.columns[i+1])
            break
        pass
    elif float(list[i]) < pozarni_vyska or float(list[i]) >= pozarni_vyska :
        if float(list[i]) < pozarni_vyska:
            pass
        else:
            print(df_SPB.columns[i+1])
            break
    elif list[i] == "-":
        print(df_SPB.columns[i+1])
        break

    elif list[i] == "N2":
        if k_system == "nehořlavý" or k_system == "smíšený":
            print(df_SPB.columns[i+1])
            break
        pass
