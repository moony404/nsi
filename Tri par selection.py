from random import randint
liste =[]
nelement = 10
borneinf = 0
bornesup = 1000
#Génération de la liste
for i in range(nelement):
    liste.append(randint(borneinf,bornesup))

# Affichage de la liste non triée
print(liste)

# La liste à trier est la se nomme liste
# La boucle s'exécutera jusqu'à l'avant-dernier élément
for i in range(len(liste)):
    # On prend comme valeur minimale le premier élément de la partie non triée de la liste
    index_mini = i
    # On recherche dans la partie non triée le plus petit élément
    for j in range(i+1,len(liste)):
        # Si l’élément regardé est plus petit que celui enregistré
        if liste[j] < liste[index_mini]:
            # On enregistre la position de cet élément
            index_mini = j
    # On enregistre temporairement la première valeur de la partie non triée de la liste
    tmp = liste[i]
    # ON échange la première valeur de la partie non triée de la liste avec la plus valeur valeur de la partie non triée
    liste[i]=liste[index_mini]
    # On replace la valeur enregistrée dans la partie non triée de la liste
    liste[index_mini]=tmp

# Affichage de la liste triée
print(liste)