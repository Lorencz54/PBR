from Classes import *
from widget_variables_counter import *
import customtkinter as ctk

# funkce na vkládání řádků pro nové místnosti do current framu
def OB1_m_plus():
    dic_m_rows[current_frame[0]].append(1)
    for i in range(7):
        if i <= 1:
            e_text = ctk.CTkEntry(list_f_PU[current_frame[0]])
            e_text.grid(row=len(dic_m_rows[current_frame[0]]), column=i)
            if i == 0:
                e_text.configure(width=40)
                dic_mc_text_entries[current_frame[0]].append(e_text)
            else:
                e_text.configure(width=200)
                dic_nazvy_m_text_entries[current_frame[0]].append(e_text)
        elif i <= 5:
            var_e = tk.StringVar()
            e_pu_parametr = EntryWithLimit(list_f_PU[current_frame[0]], width=80, textvariable=var_e)
            e_pu_parametr.grid(row=len(dic_m_rows[current_frame[0]]), column=i)
            e_pu_parametr.bind("<FocusIn>", lambda event, entry=e_pu_parametr: entry.delete(0, tk.END) if e_pu_parametr.get() == "0.0" else None)
            e_pu_parametr.bind("<FocusOut>", lambda event, entry=e_pu_parametr: entry.insert(0, "0.0") if entry.get() == "" else None)
            if i == 2:
                dic_S_var_entries[current_frame[0]].append(var_e)
                dic_S_entries[current_frame[0]].append(e_pu_parametr)
                var_e.trace_add("write", lambda name, index, mode, sv=var_e: plocha_PU(current_frame, list_l_S))
                var_e.trace_add("write", lambda name, index, mode, sv=var_e: ps(current_frame, list_l_ps, dic_ps_var_entries, dic_S_var_entries))
            elif i <=5:
                dic_ps_var_entries[current_frame[0]].append(var_e)
                dic_psi_entries[current_frame[0]].append(e_pu_parametr)
                var_e.trace_add("write", lambda name, index, mode, sv=var_e: ps(current_frame, list_l_ps, dic_ps_var_entries, dic_S_var_entries))
        else:
                var_l_psi = tk.DoubleVar()
                l_ps = ctk.CTkLabel(list_f_PU[current_frame[0]], text="0.0", width=80, anchor="center", textvariable=var_l_psi)
                l_ps.grid(row=len(dic_m_rows[current_frame[0]]), column=i)
                dic_var_ps_labels[current_frame[0]].append(var_l_psi)
                dic_ps_row_sum_labels[current_frame[0]].append(l_ps)


def OB1_m_minus():
    if len(dic_m_rows[current_frame[0]]) != 1:
        dic_m_rows[current_frame[0]].pop(1)
        dic_mc_text_entries[current_frame[0]][-1].destroy()
        dic_mc_text_entries[current_frame[0]].pop(-1)
        dic_nazvy_m_text_entries[current_frame[0]][-1].destroy()
        dic_nazvy_m_text_entries[current_frame[0]].pop(-1)
        dic_S_entries[current_frame[0]][-1].destroy()
        dic_S_entries[current_frame[0]].pop(-1)
        dic_ps_row_sum_labels[current_frame[0]][-1].destroy()
        dic_ps_row_sum_labels[current_frame[0]].pop(-1)
        for entry in dic_psi_entries[current_frame[0]][-3:]:
            entry.destroy()
            dic_psi_entries[current_frame[0]].pop(-1)


def PU_m_plus(curent_frame):
    dic_m_rows[current_frame[0]].append(1)

    for i in range(11):
        if i <= 1:
            e_text = ctk.CTkEntry(list_f_PU[current_frame[0]])
            e_text.grid(row=len(dic_m_rows[current_frame[0]]), column=i)
            if i == 0:
                e_text.configure(width=40)
                dic_mc_text_entries[current_frame[0]].append(e_text)
            else:
                e_text.configure(width=200)
                dic_nazvy_m_text_entries[current_frame[0]].append(e_text)
        elif i <= 9:
            var_e = tk.StringVar()
            e_pu_parametr = EntryWithLimit(list_f_PU[current_frame[0]], width=80, textvariable=var_e)
            e_pu_parametr.grid(row=len(dic_m_rows[current_frame[0]]), column=i)
            e_pu_parametr.bind("<FocusIn>", lambda event, entry=e_pu_parametr: entry.delete(0, tk.END) if e_pu_parametr.get() == "0.0" else None)
            e_pu_parametr.bind("<FocusOut>", lambda event, entry=e_pu_parametr: entry.insert(0, "0.0") if entry.get() == "" else None)
            if i == 2:
                dic_S_var_entries[current_frame[0]].append(var_e)
                dic_S_entries[current_frame[0]].append(e_pu_parametr)
                var_e.trace_add("write", lambda name, index, mode, sv=var_e: plocha_PU(current_frame, list_l_S))
                var_e.trace_add("write", lambda name, index, mode, sv=var_e: pn(current_frame, list_l_pn, dic_pni_var_entries, dic_S_var_entries))
                var_e.trace_add("write", lambda name, index, mode, sv=var_e: hs(current_frame))
                var_e.trace_add("write", lambda name, index, mode, sv=var_e: an(current_frame, list_l_an, dic_ani_var_entries, dic_S_var_entries))
                var_e.trace_add("write", lambda name, index, mode, sv=var_e: ps(current_frame, list_l_ps, dic_ps_var_entries, dic_S_var_entries))
            elif i == 3:
                dic_hsi_var_entries[current_frame[0]].append(var_e)
                dic_hsi_entries[current_frame[0]].append(e_pu_parametr)
                var_e.trace_add("write", lambda name, index, mode, sv=var_e: hs(current_frame))
            elif i == 4:
                dic_CSNi_entries[current_frame[0]].append(e_pu_parametr)
            elif i == 5:
                dic_pni_var_entries[current_frame[0]].append(var_e)
                dic_pni_entries[current_frame[0]].append(e_pu_parametr)
                var_e.trace_add("write", lambda name, index, mode, sv=var_e: pn(current_frame, list_l_pn, dic_pni_var_entries, dic_S_var_entries))
            elif i == 6:
                dic_ani_var_entries[current_frame[0]].append(var_e)
                dic_ani_entries[current_frame[0]].append(e_pu_parametr)
                var_e.trace_add("write", lambda name, index, mode, sv=var_e: an(current_frame, list_l_an, dic_ani_var_entries, dic_S_var_entries))
            elif i <=9:
                dic_ps_var_entries[current_frame[0]].append(var_e)
                dic_psi_entries[current_frame[0]].append(e_pu_parametr)
                var_e.trace_add("write", lambda name, index, mode, sv=var_e: ps(current_frame, list_l_ps, dic_ps_var_entries, dic_S_var_entries))
        else:
            var_l_psi = tk.DoubleVar()
            l_ps = ctk.CTkLabel(list_f_PU[current_frame[0]], text="0.0", width=80, anchor="center", textvariable=var_l_psi)
            l_ps.grid(row=len(dic_m_rows[current_frame[0]]), column=i)
            dic_var_ps_labels[current_frame[0]].append(var_l_psi)
            dic_ps_row_sum_labels[current_frame[0]].append(l_ps)

def object_m_plus():
    list_m_rows.append(1)
    for i in range(4):
        e_text = ctk.CTkEntry(list_PBR_frames[1], width=30)
        e_text.grid(row=len(list_m_rows)+2, column=i)
        if i == 0:
            e_text.configure(width=40)
        elif i == 1:
            e_text.configure(width=200)
        else:
            e_text.configure(width=80)

# funkce na odebírání řádků pro místnosti do current framu
def m_minus(current_frame):
    if len(dic_m_rows[current_frame[0]]) != 1:
        dic_m_rows[current_frame[0]].pop(1)
        dic_mc_text_entries[current_frame[0]][-1].destroy()
        dic_mc_text_entries[current_frame[0]].pop(-1)
        dic_nazvy_m_text_entries[current_frame[0]][-1].destroy()
        dic_nazvy_m_text_entries[current_frame[0]].pop(-1)
        dic_S_entries[current_frame[0]].pop(-1)
        dic_S_entries[current_frame[0]][-1].destroy()
        dic_CSNi_entries[current_frame[0]].pop(-1)
        dic_CSNi_entries[current_frame[0]][-1].destroy()
        dic_ps_row_sum_labels[current_frame[0]][-1].destroy()
        dic_ps_row_sum_labels[current_frame[0]].pop(-1)
        dic_pni_entries[current_frame[0]][-1].destroy()
        dic_pni_entries[current_frame[0]].pop(-1)
        dic_ani_entries[current_frame[0]][-1].destroy()
        dic_ani_entries[current_frame[0]].pop(-1)
        for entry in dic_psi_entries[current_frame[0]][-3:]:
            entry.destroy()
            dic_psi_entries[current_frame[0]].pop(-1)
        dic_hsi_entries[current_frame[0]][-1].destroy()
        dic_hsi_entries[current_frame[0]].pop(-1)