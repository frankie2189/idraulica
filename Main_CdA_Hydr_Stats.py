

# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 14:29:03 2023

@author: franc
"""
#====================================
#questo serve per fare il prodotto cartesiano tra due liste
from itertools import product 
#====================================
#importo le funzioni dal file relativo
from Funzioni_CdA_Hydr import *
# import json
import pandas as pd
import numpy  as np
# import os
# import matplotlib.pyplot as plt
import sys

##
# ---- Definizione delle liste per Pericolosità sormonto
#
# Queste sono le liste dei possibili dati di imput dei due parametri che caratterizzano la valutazione della Pericolosità Strutturale

Y_P_sorm   =          [1,2,3,4,5]  # pos.0 [1 Alta, 2 Medio-Alta, 3 Media, 4 MB, 5 Bassa]

#
# ---- Definizione delle liste per la V_sormonto
#

S_V_dep_acc      =  [True, False] # accentuati fenomeni di deposizione # pos. 0
S_V_mat_veg      =  [True, False] # trasporto di materiale vegetale # pos. 1
S_V_bac_min_100  =  [True, False] # dimensione bacino idrografico <100 kmq # pos. 2
S_V_dep_sign     =  [True, False] # fenomeni di deposizione significativi # pos. 3
S_V_mat_veg_sign =  [True, False] # significativo trasporto di materiale vegetale # pos. 4
S_V_bac_min_500  =  [True, False] # dimensione bacino idrografico <500 kmq # pos. 5
S_V_bac_maj_500  =  [True, False] # dimensione bacino idrografico >500 kmq # pos. 6

# ---- pERICOLOSITà EROSIONE GENERALIZZATA

Y_P_er_gen   =          [1,2,3,4,5]  # pos.0 [1 Alta, 2 Medio-Alta, 3 Media, 4 MB, 5 Bassa] # pos. 7

#
# ---- Definizione delle liste per la V_erosione generalizzata
#

EG_V_super    =  [True, False]  # presenza fondazioni superficiali # pos. 8
EG_V_abb      =  [True, False]  # abbassamento generalizzato alveo # pos. 9
EG_V_curva    =  [True, False]  # alveo su tratto avente sensibile curvatura # pos. 10
EG_V_prof     =  [True, False]  # presenza fondazioni profonde # pos. 11

# ---- pERICOLOSITà EROSIONE localizzata

Y_P_er_loc   =          [1,2,3,4,5]  # pos.0 [1 Alta, 2 Medio-Alta, 3 Media, 4 MB, 5 Bassa] #pos. 12

#
# ---- Definizione delle liste per la V_erosione localizzata
#

# EL_V_super    =  [True, False]  # presenza fondazioni superficiali # pos. 13
# EL_V_abb      =  [True, False]  # abbassamento generalizzato alveo # pos. 14
EL_V_detr     =  [True, False]  # presenza detriti a monte della pila # pos. 15
EL_V_div_plan =  [True, False]  # alveo con tendenza alla divagazione planimetrica ## pos. 16
# EL_V_prof     =  [True, False]  # presenza fondazioni profonde # pos. 16
EL_V_prot     =  [True, False]  # presenza protezione al piede delle pile e delle spalle # pos. 17
EL_V_brig     =  [True, False]  # presenza briglia a valle del ponte # pos. 18

#
# ---- Definizione delle liste per la E_sism
#
Y_tgm         =   [1,2,3] # # pos.7  [1 Alta, 2 Media, 3 Bassa]
Y_L_med       =   [1,2,3] # # pos.8  [1 grande luce, 2 media luce, 3 piccola luce]
Y_persone     =   [1,2]   # # pos.9  [1 frequente passaggio, 2 no passaggio]
Y_alt_strad   =   [1,2]   # # pos.10 [1 assenza, 2 presenza]
Y_scavalc     =   [1,2,3] # # pos.11 [1 Alta, 2 Media, 3 Bassa]
Y_strat       =   [1,2]   # pos.12 [1 Strat; 2 non strat]


Y = [#----------------------- parametri sormonto
     Y_P_sorm, 
     S_V_dep_acc,
     S_V_mat_veg,
     S_V_bac_min_100,
     S_V_dep_sign,
     S_V_mat_veg_sign,
     S_V_bac_min_500,
     S_V_bac_maj_500,
     #----------------------- parametri erosione generalizzata
      Y_P_er_gen,
      EG_V_super,
      EG_V_abb,
      EG_V_curva,
      EG_V_prof,
    #----------------------- parametri erosione localizzata
      Y_P_er_loc,
      # EL_V_super,
      # EL_V_abb,
      EL_V_detr,
      EL_V_div_plan,
      # EL_V_prof,
      EL_V_prot,
      EL_V_brig,
  #-----------------------     parametri esposizione
      Y_tgm, 
      Y_L_med,
      Y_persone,
      Y_alt_strad,
      Y_scavalc,
      Y_strat]

#
# ---- Calcolo delle combinazioni possibili
#

# n_parametri = len(Y)

# sys.exit()
# ---- Con vincoli
combinazioni = []

for combo in product(*Y):
    
    if combo[8] == True:
        if combo[11] == False:
            continue
    elif combo[8] == False:
        pass
    
    
    combinazioni.append(combo)

# combinazioni = list(product(*Y))  #Calcolo delle combinazioni

# sys.exit()


#
# ---- Calcolo della CdA
#
CdA_numero = {5 : 'Low', 4 : 'Medium-Low', 3 :'Medium', 2 : 'Medium-High', 1 : 'High'}
CdA_Hydr = []
Comb     = []

for parametri in combinazioni:
    CdA_Hydr.append(CdA_idraulica(parametri))
    # Per spacchettare X_V_4str e avere in input un vettore di soli numeri
    Comb.append(parametri)

sys.exit()
target    = [ 'CoA Hydraulic']

nomi_parametri_Hydr = ['P_sormonto','dep_acc','bac_min_100', 'dep_signi', 'veg_sign','bac_min_500','bac_maj_500',
                       'P_er_gene', 'fond_super', 'abb_gen','sens_curv','fond_prof',
                       'P_er_loc', 'fond_super', 'abb_gen','pres_detr','div_plani','prot_piede','pres_briglia','fond_prof',
                       'tgm', 'L_med', 'persone', 'alt_strad', 'scavalc', 'strat']


# Database_CdA_stru = pd.DataFrame([Comb + CdA_stru], columns = nomi_parametri_Pstr + nomi_parametri_Vstr + nomi_parametri_Estr + target)

df_features_CdA_hydr = pd.DataFrame(Comb, columns = nomi_parametri_Hydr)

df_target_CdA_hydr = pd.DataFrame(CdA_Hydr, columns = target)

# Salva il DataFrame df_target_CdA_stru come file CSV
nome_file_csv = "stats_CdA_Hydr.csv"
df_target_CdA_hydr.to_csv(nome_file_csv, index=False)

print(f"Il DataFrame df_target_CdA_sism è stato salvato come file CSV: {nome_file_csv}")





