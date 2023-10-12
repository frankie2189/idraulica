# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 15:17:17 2023

@author: franc
"""
from Dizionari_CdA import *

# =======================================================
# CdA_stru = 
# Calcolo CdA strutturale
# =======================================================

# elenco_parametri_idraulica
def calcolo_CdA_sism(parametri):
        
    # ---- Calcolo della pericolosità fenomeno di soromnto
    # Ottengo il valore del parametro per P_sormonto
    nomi_parametri_Psorm = ['P_sormonto']
    # Valuto la pericolosità sfenomeno sormonto
    # lista delle posizioni dei parametri all'interno di X[V_stru]
    pos_Y_Psorm = [elenco_parametri_idraulica.get(i) for i in nomi_parametri_Psorm]
    # Valuto la pericolosità sormonto
    Psorm = tuple([parametri[i] for i in pos_Y_Psorm]) 
#   

#     # ---- Calcolo vulnerabilità sormonto
#     # Elenco dei parametri per v_sormonto
    nomi_parametri_Vsorm = ['dep_acc','bac_min_100', 'dep_signi', 'veg_sign','bac_min_500','bac_maj_500']
#     # lista delle posizioni dei parametri all'interno di X[V_stru]
    pos_Y_Vsorm = [elenco_parametri_idraulica.get(i) for i in nomi_parametri_Vsorm]
#     # estraggo i parametri necessari per Vsorm
    par_Vsorm = tuple([parametri[i] for i in pos_Y_Vsorm]) 
#     # Valuto la pericolosità strutturale
    Vsorm = V_sorm(*par_Vsorm)
    
    # ---- Calcolo della pericolosità erosione generalizzata
    # Ottengo il valore del parametro per P_generalizzata
    nomi_parametri_Per_gen = ['P_er_gene']
    # Valuto la pericolosità sfenomeno erosione generalizzata
    # lista delle posizioni dei parametri all'interno di X[V_stru]
    pos_Y_Per_gen = [elenco_parametri_idraulica.get(i) for i in nomi_parametri_Per_gen]
    # Valuto la pericolosità erosione generalizzata
    Per_er_gen = tuple([parametri[i] for i in pos_Y_Per_gen]) 
#      

#     # ---- Calcolo vulnerabilità erosione generalizzata
#     # Elenco dei parametri per v_generalizzata
    nomi_parametri_V_er_gen = ['fond_super', 'abb_gen','sens_curv','fond_prof']
#     # lista delle posizioni dei parametri all'interno di X[V_stru]
    pos_Y_V_er_gen = [elenco_parametri_idraulica.get(i) for i in nomi_parametri_V_er_gen]
#     # estraggo i parametri necessari per Vsorm
    par_V_er_gen = tuple([parametri[i] for i in pos_Y_V_er_gen]) 
#     # Valuto la pericolosità strutturale
    V_er_gen = V_er_general(*par_V_er_gen)
    
    # ---- Calcolo della pericolosità erosione localizzata
    # Ottengo il valore del parametro per P_localizzata
    nomi_parametri_Per_loc = ['P_er_loc']
    # Valuto la pericolosità sfenomeno erosione localizzata
    # lista delle posizioni dei parametri all'interno di X[V_stru]
    pos_Y_Per_loc = [elenco_parametri_idraulica.get(i) for i in nomi_parametri_Per_loc]
    # Valuto la pericolosità erosione localizzata
    Per_er_loc = tuple([parametri[i] for i in pos_Y_Per_loc]) 
  
    
    
#     # ---- Calcolo vulnerabilità erosione generalizzata
#     # Elenco dei parametri per v_generalizzata
    nomi_parametri_V_er_loc = ['fond_super', 'abb_gen','pres_detr','div_plani','prot_piede','pres_briglia','fond_prof']
#     # lista delle posizioni dei parametri all'interno di X[V_stru]
    pos_Y_V_er_loc = [elenco_parametri_idraulica.get(i) for i in nomi_parametri_V_er_loc]
#     # estraggo i parametri necessari per Vsorm
    par_V_er_loc = tuple([parametri[i] for i in pos_Y_V_er_loc]) 
#     # Valuto la pericolosità strutturale
    V_er_loc = V_er_local(*par_V_er_loc)
    
#     # ---- Calcolo dell'esposizione sismica
#     # Elenco dei parametri per E_sism
    nomi_parametri_Esism = ['tgm', 'L_med', 'persone', 'alt_strad', 'scavalc', 'strat']
#     # lista delle posizioni dei parametri all'interno di X[E_stru]
    pos_Y_Eidr = [elenco_parametri_idraulica.get(i) for i in nomi_parametri_Esism]
#     # estraggo i parametri necessari per Pstr
    par_Eidra = tuple([parametri[i] for i in pos_Y_Eidr]) 
#     # Valuto la pericolosità strutturale
    Eidra = E_sismica(*par_Eidra)    
    
    
#     # ---- Calcolo cda sormonto
    # CdA_stru = 0
    CdA_sorm = CdA_sismi(Psorm, Vsorm, Eidra)
    
    
    return Psism,Vsism,Esism,CdA_sism

#---------------------------------------
#CDA sismica   
#---------------------------------------

#---------------------------------------
#---- Vulnerabilità sormonto
#---------------------------------------

def V_sorm(S_V_dep_acc, S_V_mat_veg, S_V_bac_min_100, S_V_dep_sign,
           S_V_mat_veg_sign, S_V_bac_min_500, S_V_bac_maj_500):

    # Conta le condizioni sussistenti per le prime 3 classi
    count_condizioni_1_3 = sum([S_V_dep_acc, S_V_mat_veg, S_V_bac_min_100])
    count_condizioni_med = sum([S_V_dep_sign, S_V_mat_veg_sign, S_V_bac_min_500])

    V_sormonto = []

    # Classe 1
    if count_condizioni_1_3 >= 2:
        V_sormonto.append(1)

    # Classe 2
    if count_condizioni_1_3 >= 1:
        V_sormonto.append(2)

    # Classe 3
    if count_condizioni_med >= 1:
        V_sormonto.append(3)

    # Classe 4
    condizioni_4 = [not S_V_dep_sign, not S_V_mat_veg_sign, S_V_bac_maj_500]
    if sum(condizioni_4) >= 2:
        V_sormonto.append(4)

    # Classe 5
    if not S_V_dep_sign and not S_V_mat_veg_sign and S_V_bac_maj_500:
        V_sormonto.append(5)

    # Se c'è ambiguità, restituisci la classe più alta tra le possibili
    if len(V_sormonto) > 1:
        return min(V_sormonto)

    # Se non c'è corrispondenza, restituisci la classe media
    elif len(V_sormonto) == 0:
        return [3]

    return V_sormonto

#---------------------------------------
#---- Vulnerabilità erosione generalizzata
#---------------------------------------
def V_er_general(EG_V_super, EG_V_abb, EG_V_curva, EG_V_prof):

    # Conta le condizioni sussistenti per le prime 3
    count_sussistenti = sum([EG_V_super, EG_V_abb, EG_V_curva])

    V_eros_gen = []
    # Classe 1
    if count_sussistenti == 3:
        V_eros_gen.append(1)
    # Classe 2
    if count_sussistenti == 2:
        V_eros_gen.append(2)
    # Classe 3
    if count_sussistenti == 1:
        V_eros_gen.append(3)
    # Classe 4
    if EG_V_prof and sum([EG_V_abb, EG_V_curva]) >= 1:
        V_eros_gen.append(4)
    # Classe 5
    if EG_V_prof and not (EG_V_abb or EG_V_curva):
        V_eros_gen.append(5)
    # Se c'è ambiguità, restituisci la classe più alta tra le possibili
    if len(V_eros_gen) > 1:
        return min(V_eros_gen)
    # Se non c'è corrispondenza, restituisci la classe media
    elif len(V_eros_gen) == 0:
        return 3
    return V_eros_gen[0] 
        
#---------------------------------------
#---- Vulnerabilità erosione localizzata
#---------------------------------------
def V_er_local(EL_V_super, EL_V_abb, EL_V_detr, EL_V_div_plan, EL_V_prof, EL_V_prot, EL_V_brig):

    # Conta le condizioni sussistenti per le prime 4
    count_sussistenti = sum([EL_V_super, EL_V_abb, EL_V_detr, EL_V_div_plan])

    V_eros_loc = []
    
    # Classe alta
    if count_sussistenti >= 3:
        V_eros_loc.append(1)
    # Classe medio-alta
    if count_sussistenti == 2:
        V_eros_loc.append(2)
    # Classe media
    if count_sussistenti == 1:
        V_eros_loc.append(3)
    # Classe medio bassa
    if EL_V_prof and sum([EL_V_prot, EL_V_brig]) >= 2:
        V_eros_loc.append(4)
    # Classe bassa
    if EL_V_prof and EL_V_prot:
        V_eros_loc.append(5)
    if possibili_classi:
        return min(V_eros_loc)  # restituisce la classe più alta tra le possibili
    else:
        return 3  # ritorna la classe media in caso non ci sia corrispondenza

    return V_eros_loc
#---------------------------------------
#---- Esposizione sismica
# #---------------------------------------
def E_sismica(tgm, L_med, persone, alt_strad, scavalc, strat):
    
    E10 = E_1_0str[(tgm, L_med)]
    E1  = E_1str[(persone, E10)]
    E2  = E_2str[(alt_strad,E1)]
    Estr = E_str[(E2, scavalc)]
    Esism = E_sism [(Estr, strat)]
    
    # Estr = E_str[(Estr0, merci_per)]
    
    return Esism
#---------------------------------------
#Classe di attenzione sormonto 
#---------------------------------------
def CdA_sorm (Psorm, Vsorm, Eidra):
    
    CdAsorm = Tabella_CdA[(Psorm, Vsorm, Eidra)]
    
    return CdAsorm

def CdA_eros_gen (Per_er_gen, V_er_gen, Eidra):
    
    CdA_ero_gen = Tabella_CdA[(Per_er_gen, V_er_gen, Eidra)]
    
    return CdA_ero_gen 

def CdA_eros_local (Per_er_loc, V_er_loc, Eidra):
    
    CdA_ero_loc = Tabella_CdA[(Per_er_loc, V_er_loc, Eidra)]
    
    return CdA_ero_loc 

def CdA_erosione (CdA_ero_gen, CdA_ero_loc):
    
    CdA_erosione = CdA_erosione_dict[(CdA_ero_gen, CdA_ero_loc)]
    
    return CdA_erosione 

def CdA_idraulica (CdAsorm, CdA_erosione):
    if CdAsorm >= CdA_erosione:
        CdA_idra = CdAsorm
    else:
        CdA_idra = CdA_erosione
    return CdA_idra




