from widget_variables_counter import *

def pu_rename(event):
    for i in range(len(list_cisla_pu)):
        cislo_pu = list_cisla_pu[i].get()
        nazev_pu = list_nazvy_pu[i].get()

        list_nazvy_pu_default[i].configure(text=cislo_pu + " - " + nazev_pu)