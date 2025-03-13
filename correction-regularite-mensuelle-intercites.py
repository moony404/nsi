# -*- coding: utf-8 -*-
import csv
import codecs
import matplotlib.pyplot as plt
 
def affiche_graphique(liste,cle,titre):
    date =[]
    taux=[]
    for i in range(len(liste)):
        date.append(liste[i]["Date"])
        taux.append(liste[i][cle])
    fig, ax = plt.subplots()
    ax.plot(date, taux)
    ax.set_title(titre)
    plt.show()
    
def trie(liste,critere):
    for j in range(1,len(liste)):
        cle = liste[j]
        i = j-1
        while i >=0 and liste[i][critere]<cle[critere] :
            liste[i+1] = liste[i]
            i=i-1
        liste[i+1]=cle
    return liste

def nouveau_fichier(liste, nom_fichier):
    fichier_new = codecs.open(nom_fichier+".csv",'w','utf-8')
    ecriture = csv.DictWriter(fichier_new,list(liste[0]))
    ecriture.writeheader()
    ecriture.writerows(liste)
    fichier_new.close()
       
fichier = codecs.open("regularite-mensuelle-intercites.csv","r","utf-8")
données = list(csv.DictReader(fichier,delimiter = ";"))
fichier.close()

aller = []
retour = []
for donnée in données :
    donnée["Nombre de trains annulés"]=int(donnée["Nombre de trains annulés"])
    donnée["Nombre de trains ayant circulé"]=int(donnée["Nombre de trains ayant circulé"])
    donnée["Nombre de trains en retard à l'arrivée"]=int(donnée["Nombre de trains en retard à l'arrivée"])
    donnée["Nombre de trains programmés"]=int(donnée["Nombre de trains programmés"])
    donnée["Nombre de trains à l'heure pour un train en retard à l'arrivée"]=float(donnée["Nombre de trains à l'heure pour un train en retard à l'arrivée"])
    donnée["Taux de régularité"]=float(donnée["Taux de régularité"])
    donnée["Date"]=int(donnée["Date"][:4])+(int(donnée["Date"][5:])-1)/12
    if donnée["Départ"]=="CLERMONT-FERRAND" and donnée["Arrivée"]=="PARIS-BERCY":
        aller.append(donnée)
    elif donnée["Départ"]=="PARIS-BERCY" and donnée["Arrivée"]=="CLERMONT-FERRAND":
        retour.append(donnée)  
    
# date =[]
# taux=[]
# for i in range(len(aller)):
#     date.append(aller[i]["﻿Date"])
#     taux.append(aller[i]["Taux de régularité"])
# fig, ax = plt.subplots()
# ax.plot(date, taux)
# ax.set_title("Taux de régularité CLERMONT-FERRAND->PARIS-BERCY")
# plt.show()

# date =[]
# taux=[]
# for i in range(len(retour)):
#     date.append(retour[i]["﻿Date"])
#     taux.append(retour[i]["Taux de régularité"])
# fig, ax = plt.subplots()
# ax.plot(date, taux)
# ax.set_title("Taux de régularité PARIS-BERCY->CLERMONT-FERRAND")
# plt.show()

affiche_graphique(aller,"Taux de régularité","Taux de régularité CLERMONT-FERRAND->PARIS-BERCY")
affiche_graphique(retour,"Taux de régularité","Taux de régularité PARIS-BERCY->CLERMONT-FERRAND")
affiche_graphique(aller,"Nombre de trains annulés","Nombre de trains annulés CLERMONT-FERRAND->PARIS-BERCY")
affiche_graphique(retour,"Nombre de trains annulés","Nombre de trains annulés PARIS-BERCY->CLERMONT-FERRAND")

nouveau_fichier(trie(aller,"Taux de régularité"),"trie_ponctu")
nouveau_fichier(trie(aller,"Nombre de trains annulés"),"trie_annul")
nouveau_fichier(trie(aller,"Nombre de trains en retard à l'arrivée"),"trie_retard")