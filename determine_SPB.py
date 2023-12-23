from data import *
from lists_and_dictionaries import *

def determine_SPB():
    if len(list_f_PU) != 0:
        if list_om_typ_pu[current_frame[0]].get() == "nevýrobní":
            if list_om_konstrukcni_system_pu[current_frame[0]].get() == "nehořlavý":
                df_pv_values = np.array(df_SPB.iloc[0:7, 0].values)
                pv_higher_than_pvpu_indexes = np.where(df_pv_values >= list_var_l_pv[current_frame[0]].get())[0]
                min_index = pv_higher_than_pvpu_indexes[np.argmin(df_pv_values[pv_higher_than_pvpu_indexes])]

            elif list_om_konstrukcni_system_pu[current_frame[0]].get() == "smíšený":
                df_pv_values = np.array(df_SPB.iloc[9:16, 0].values)
                pv_higher_than_pvpu_indexes = np.where(df_pv_values >= list_var_l_pv[current_frame[0]].get())[0]
                min_index = pv_higher_than_pvpu_indexes[np.argmin(df_pv_values[pv_higher_than_pvpu_indexes])]

            else:
                df_pv_values = np.array(df_SPB.iloc[18:25, 0].values)
                pv_higher_than_pvpu_indexes = np.where(df_pv_values >= list_var_l_pv[current_frame[0]].get())[0]
                min_index = pv_higher_than_pvpu_indexes[np.argmin(df_pv_values[pv_higher_than_pvpu_indexes])]

            list = df_SPB.iloc[min_index, 1:].tolist()

            for i in range (len(list)):
                if list[i] == "N1":
                    pass
                elif list[i] == "Oa":
                    if list_e_pozarni_vyska[0].get() == 0 and float(list_a[current_frame[0]]) <= 1.1:
                        list_var_l_SPB[current_frame[0]].set(df_SPB.columns[i + 1])
                        break
                    pass
                elif list[i] == "O":
                    if list_e_pozarni_vyska[0].get() == 0:
                        list_var_l_SPB[current_frame[0]].set(df_SPB.columns[i + 1])
                        break
                    pass
                elif float(list[i]) < list_e_pozarni_vyska[0].get() or float(list[i]) >= list_e_pozarni_vyska[0].get() :
                    if float(list[i]) < list_e_pozarni_vyska[0].get():
                        pass
                    else:
                        list_var_l_SPB[current_frame[0]].set(df_SPB.columns[i + 1])
                        break
                elif list[i] == "-":
                    list_var_l_SPB[current_frame[0]].set(df_SPB.columns[i + 1])
                    break

                elif list[i] == "N2":
                    if list_var_om_konstrukcni_system[0].get() == "nehořlavý" or list_var_om_konstrukcni_system[0].get() == "smíšený":
                        list_var_l_SPB[current_frame[0]].set(df_SPB.columns[i + 1])
                        break
                    pass
        else:
            if list_var_e_pocet_NP_objektu[0] == 1:
                list_var_l_SPB[current_frame[0]].set("I.")
            elif list_var_om_konstrukcni_system[0].get() == "nehořlavý" or list_var_om_konstrukcni_system[
                0].get() == "smíšený":
                if list_var_e_pocet_NP_objektu[0] <= 3:
                    list_var_l_SPB[current_frame[0]].set("II.")
            elif list_var_om_konstrukcni_system[0].get() == "hořlavý" and list_var_e_pocet_NP_objektu[0] == 2:
                list_var_l_SPB[current_frame[0]].set("II.")
            elif list_var_om_konstrukcni_system[0].get() == "hořlavý" and list_var_e_pocet_NP_objektu[0] == 3:
                list_var_l_SPB[current_frame[0]].set("III.")
            else:
                if list_om_konstrukcni_system_pu[current_frame[0]].get() == "nehořlavý":
                    df_pv_values = np.array(df_SPB.iloc[0:7, 0].values)
                    pv_higher_than_pvpu_indexes = np.where(df_pv_values >= list_var_l_pv[current_frame[0]].get())[0]
                    min_index = pv_higher_than_pvpu_indexes[np.argmin(df_pv_values[pv_higher_than_pvpu_indexes])]

                elif list_om_konstrukcni_system_pu[current_frame[0]].get() == "smíšený":
                    df_pv_values = np.array(df_SPB.iloc[9:16, 0].values)
                    pv_higher_than_pvpu_indexes = np.where(df_pv_values >= list_var_l_pv[current_frame[0]].get())[0]
                    min_index = pv_higher_than_pvpu_indexes[np.argmin(df_pv_values[pv_higher_than_pvpu_indexes])]

                else:
                    df_pv_values = np.array(df_SPB.iloc[18:25, 0].values)
                    pv_higher_than_pvpu_indexes = np.where(df_pv_values >= list_var_l_pv[current_frame[0]].get())[0]
                    min_index = pv_higher_than_pvpu_indexes[np.argmin(df_pv_values[pv_higher_than_pvpu_indexes])]

                list = df_SPB.iloc[min_index, 1:].tolist()

                for i in range(len(list)):
                    if list[i] == "N1":
                        pass
                    elif list[i] == "Oa":
                        if list_e_pozarni_vyska[0].get() == 0 and float(list_a[current_frame[0]]) <= 1.1:
                            list_var_l_SPB[current_frame[0]].set(df_SPB.columns[i + 1])
                            break
                        pass
                    elif list[i] == "O":
                        if list_e_pozarni_vyska[0].get() == 0:
                            list_var_l_SPB[current_frame[0]].set(df_SPB.columns[i + 1])
                            break
                        pass
                    elif float(list[i]) < list_e_pozarni_vyska[0].get() or float(list[i]) >= list_e_pozarni_vyska[
                        0].get():
                        if float(list[i]) < list_e_pozarni_vyska[0].get():
                            pass
                        else:
                            list_var_l_SPB[current_frame[0]].set(df_SPB.columns[i + 1])
                            break
                    elif list[i] == "-":
                        list_var_l_SPB[current_frame[0]].set(df_SPB.columns[i + 1])
                        break

                    elif list[i] == "N2":
                        if list_var_om_konstrukcni_system[0].get() == "nehořlavý" or list_var_om_konstrukcni_system[
                            0].get() == "smíšený":
                            list_var_l_SPB[current_frame[0]].set(df_SPB.columns[i + 1])
                            break
                        pass