import csv
import codecs
fichier = codecs.open("prix-des-carburants-en-france-flux-instantane-v2.csv",'r','utf-8')
lecteur = list(csv.DictReader(fichier,delimiter=";"))
# select, annee, ponct, ponctPC, nbtrain, nbtrainPC=([] for i in range(6))
select=[]
moyenne=0
nb_a_afficher=5
a=0
b=0
def printab(a,b):
    print("###############################")
    print("# Gazole prix moy. = ",a,"€ #")
    print("# E85 prix moy. = ",b,"€    #")
    print("###############################\n")
def tri_insertion(liste):
    for j in range(len(liste)):
        cle = liste[j]
        i = j-1
        while i >=0 and liste[i]["Prix Gazole"]>cle["Prix Gazole"]:
            liste[i+1] = liste[i]
            i=i-1
        liste[i+1]=cle
    return liste
def recherche_station_moins_cher(liste_station,carburant):
    for i in range(len(lecteur)):
        if ((lecteur[i]["code_departement"])=="63") and (lecteur[i]["Prix "+carburant])!="":
            select.append(lecteur[i]) # Pour la Q3
    tri_insertion(liste_station)
    if carburant=="Gazole":
        print("\n\nGAZOLE :")
        for i in range(nb_a_afficher):
            print(i+1,select[i]["Ville"],"à l'adresse",select[i]["Adresse"],"à",select[i]["Prix Gazole"],"€")
    elif carburant=="E85":
        print("E85 :")
        for i in range(nb_a_afficher):
            print(i+1,select[i]["Ville"],"à l'adresse",select[i]["Adresse"],"à",select[i]["Prix Gazole"],"€")
            
            
            
def calcul_moy_carburant(liste_station,carburant):
    '''
    qui calculera sur une liste de stations donnée en
    paramètre le prix moyen d’un carburant donné en paramètre
    '''
    for i in range(len(liste_station)):
        if ((lecteur[i]["code_departement"])=="63") and (lecteur[i]["Prix "+carburant])!="":
            select.append(lecteur[i]) # Pour la Q3
    tri_insertion(liste_station)
    return r
# for i in range (len(lecteur)):
#     if ((lecteur[i]["code_departement"])=="63") and (lecteur[i]["Prix Gazole"])!="":
#         select.append(lecteur[i]) # Pour la Q3
#         a=a+float(lecteur[i]["Prix Gazole"])
#     if (lecteur[i]["code_departement"])=="63" and (lecteur[i]["Prix E85"])!="":
#         select2.append(lecteur[i]) # Pour la Q3
#         b=b+float(lecteur[i]["Prix E85"])
# printab(f"{a/len(select):.3f}",f"{b/len(select2):.3f}")
# print("GAZOLE :\n")
# for i in range(5):
#     print(i+1,select[i]["Ville"],"à l'adresse",select[i]["Adresse"])
# print("E85 :")
# for i in range(5):
#     print(i+1,select2[i]["Ville"],"à l'adresse",select2[i]["Adresse"])
recherche_station_moins_cher(select,"Gazole")
recherche_station_moins_cher(select,"E85")