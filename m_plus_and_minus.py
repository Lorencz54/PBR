import tkinter as tk
from Classes import *
from widget_variables_ounter import *

class EntryWithLimit(CTkEntry):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)


        float_checker = master.register(self.is_valid_input)
        self.configure(validate="key", validatecommand=(float_checker, "%P"))


    def is_valid_input(self, text):
        # Allow backspace
        if text == "" or text == '\b':
            return True

        try:
            float(text)
            return True
        except ValueError:
            return False


# funkce na vkládání řádků pro nové místnosti do current framu
def m_plus(current_frame):
    dic_m_rows[current_frame[0]].append(1)
    for i in range(10):
        if i <= 1:
            for i in range(2):
                e_text = ctk.CTkEntry(list_f_PU[current_frame[0]])
                e_text.grid(row=len(dic_m_rows[current_frame[0]]), column=i)
                dic_text_entries[current_frame[0]].append(e_text)
            if i % 2 == 0:
                e_text.configure(width=40)
            else:
                e_text.configure(width=200)
        elif i <=8:
            var_e = tk.DoubleVar()
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
                dic_pni_var_entries[current_frame[0]].append(var_e)
                dic_pni_entries[current_frame[0]].append(e_pu_parametr)
                var_e.trace_add("write", lambda name, index, mode, sv=var_e: pn(current_frame, list_l_pn, dic_pni_var_entries, dic_S_var_entries))
            elif i == 4:
                dic_hsi_var_entries[current_frame[0]].append(var_e)
                dic_hsi_entries[current_frame[0]].append(e_pu_parametr)
                var_e.trace_add("write", lambda name, index, mode, sv=var_e: hs(current_frame))
            elif i == 5:
                dic_ani_var_entries[current_frame[0]].append(var_e)
                dic_ani_entries[current_frame[0]].append(e_pu_parametr)
                var_e.trace_add("write", lambda name, index, mode, sv=var_e: an(current_frame, list_l_an, dic_ani_var_entries, dic_S_var_entries))
            elif i <=8:
                dic_ps_var_entries[current_frame[0]].append(var_e)
                dic_ps_entries[current_frame[0]].append(e_pu_parametr)
                var_e.trace_add("write", lambda name, index, mode, sv=var_e: ps(current_frame, list_l_ps, dic_ps_var_entries, dic_S_var_entries))
        else:
            var_l_psi = tk.DoubleVar()
            l_ps = ctk.CTkLabel(list_f_PU[current_frame[0]], text="0.0", width=80, anchor="center", textvariable=var_l_psi)
            l_ps.grid(row=len(dic_m_rows[current_frame[0]]), column=9)
            dic_var_ps_labels[current_frame[0]].append(var_l_psi)
            dic_ps_labels[current_frame[0]].append(l_ps)

# funkce na odebírání řádků pro místnosti do current framu
def m_minus(current_frame):
    dic_m_rows[current_frame[0]].pop(1)
    for entry in dic_text_entries[current_frame[0]][-2:]:
        entry.destroy()
        dic_text_entries[current_frame[0]].pop(-1)
    dic_S_entries[current_frame[0]][-1].destroy()
    dic_S_entries[current_frame[0]].pop(-1)
    dic_ps_labels[current_frame[0]][-1].destroy()
    dic_ps_labels[current_frame[0]].pop(-1)
    dic_pni_entries[current_frame[0]][-1].destroy()
    dic_pni_entries[current_frame[0]].pop(-1)
    dic_ani_entries[current_frame[0]][-1].destroy()
    dic_ani_entries[current_frame[0]].pop(-1)
    for entry in dic_ps_entries[current_frame[0]][-3:]:
        entry.destroy()
        dic_ps_entries[current_frame[0]].pop(-1)
    dic_hsi_entries[current_frame[0]][-1].destroy()
    dic_hsi_entries[current_frame[0]].pop(-1)