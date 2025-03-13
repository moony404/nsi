import csv
import codecs
import tkinter as tk
from tkinter import font as tkFont
from tkinter import *
from tkinter import ttk

fichier = codecs.open("prix-des-carburants-en-france-flux-instantane-v2.csv",'r','utf-8')
lecteur = list(csv.DictReader(fichier,delimiter = ";"))
pdd =[]
a=0
b=0
carburant=""

for i in lecteur:
    if i["code_departement"] == "63":
        pdd.append(i)


def tri_selection(liste,critere):
    for i in range(len(liste)):
        index_mini = i
        for j in range(i+1,len(liste)):
            if float(liste[j][critere]) < float(liste[index_mini][critere]):
                index_mini = j
        tmp = liste[i]
        liste[i]=liste[index_mini]
        liste[index_mini]=tmp
    return liste


def stationlemoinschere(liste,carburant):
    listeCarbuOK = []
    for i in liste:
        if i["Prix " + carburant] != "":
            listeCarbuOK.append(i)
    return tri_selection(listeCarbuOK,"Prix " + carburant)


def calcul_moy_carburant(liste,carburant):
    a=0
    compt = 0
    for i in range(len(liste)):
        if liste[i]["Prix "+carburant] != "":
            a=a+float(liste[i]["Prix "+carburant])
            compt +=1
    return a/compt


gazole = stationlemoinschere(pdd, "Gazole")
E85 = stationlemoinschere(pdd, "E85")


for liste in [gazole,E85]:
    for j in range(5):
        print(j,liste[j]["Adresse"])
    print("\n")
print("Gazole :",calcul_moy_carburant(pdd,"Gazole"),"€")
print("E85 :",calcul_moy_carburant(pdd,"E85"),"€")


fenetre = tk.Tk()
fenetre.geometry("600x400")
# root.resizable(False, False)
fenetre.title("Essencéo")
# fenetre.iconbitmap("icon.ico")

Font14 = tkFont.Font(family="Arial", size=14)
Font20 = tkFont.Font(family="Arial", size=20, weight="bold", underline=1)

label1 = tk.Label(fenetre,text="Essenthéo")
label1.pack(side="top")

buttonquit =tk.Button(fenetre,text="Quitter",bg="red",fg="white",font=Font14,command=fenetre.destroy)
#Le bouton se positionnera à droite dans la fenêtre
buttonquit.pack(side="bottom")

def action(event):
    select = listeCombo.get()
    print(select)
 
labelChoix = tk.Label(fenetre, text = "Elle roule a quoi ta bécane ?")
labelChoix.pack()

listeProduits=["Gazole", "E85"]

listeCombo = ttk.Combobox(fenetre, values=listeProduits)

listeCombo.current(0)
 
listeCombo.pack()
listeCombo.bind("<<ComboboxSelected>>", action)

 
listeCombo.pack()

fenetre.mainloop()