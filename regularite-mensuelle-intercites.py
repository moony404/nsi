import matplotlib.pyplot as plt
import csv
import codecs
fichier = codecs.open("regularite-mensuelle-intercites.csv",'r','utf-8')
lecteur = list(csv.DictReader(fichier,delimiter=";"))
date, annee, ponct, ponctPC, nbtrain, nbtrainPC=([] for i in range(6))
def graph(x, y, label, color):
    fig, ax = plt.subplots()
    ax.plot(x, y, label=label, color=color)
    ax.legend()
    plt.show()
def tri_insertion(liste):
    for j in range(1,len(liste)):
        cle = liste[j]
        i = j-1
        while i >=0 and liste[i]>cle :
            liste[i+1] = liste[i]
            i=i-1
        liste[i+1]=cle
    return liste
a={}
for i in range (1,len(lecteur)):
    if ((lecteur[i]["Départ"])=="CLERMONT-FERRAND") and ((lecteur[i]["Arrivée"])=="PARIS-BERCY"):
        a=a+float(lecteur[i]["Taux de régularité"])
        date.append(lecteur[i]["Date"])
        ponct.append(float(lecteur[i]["Taux de régularité"]))
        nbtrain.append(int(lecteur[i]["Nombre de trains annulés"]))
    if ((lecteur[i]["Départ"])=="PARIS-BERCY") and ((lecteur[i]["Arrivée"])=="CLERMONT-FERRAND"):
        ponctPC.append(float(lecteur[i]["Taux de régularité"]))
        nbtrainPC.append(int(lecteur[i]["Nombre de trains annulés"]))
for i in range(len(date)):
    annee.append(int(date[i][0:4])+int(date[i][5:7])/12)
graph(annee, ponct, "ponctualité C-P", None)
graph(annee, ponctPC, "ponctualité P-C", "red")
graph(annee, nbtrain, "Nombre de trains annulés C-P", None)
graph(annee, nbtrainPC, "Nombre de trains annulés P-C", "orange")
fichier = codecs.open("nom.csv","w","utf-8")
ecriture = csv.DictWriter(fichier, list(lecteur[0]))
ecriture.writeheader()
ecriture.writerows()
# reversed(tri_insertion(ponct))