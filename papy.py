import random


def tri_selection(ma_liste):
    for i in range(len(ma_liste)):
        plus_petit = i
        for j in range(i + 1, len(ma_liste)):
            if ma_liste[j] < ma_liste[plus_petit]:
                plus_petit = j
        ma_liste[i], ma_liste[plus_petit] = ma_liste[plus_petit], ma_liste[i]

def tri_bulles(ma_liste):
    taille = len(ma_liste)
    for i in range(taille):
        for j in range(0, taille - i - 1):
            if ma_liste[j] > ma_liste[j + 1]:
                ma_liste[j], ma_liste[j + 1] = ma_liste[j + 1], ma_liste[j]

def tri_insertion(ma_liste):
    for i in range(1, len(ma_liste)):
        valeur = ma_liste[i]
        j = i - 1
        while j >= 0 and valeur < ma_liste[j]:
            ma_liste[j + 1] = ma_liste[j]
            j -= 1
        ma_liste[j + 1] = valeur

def tri_fusion(ma_liste):
    if len(ma_liste) > 1:
        milieu = len(ma_liste) // 2
        gauche = ma_liste[:milieu]
        droite = ma_liste[milieu:]

        tri_fusion(gauche)
        tri_fusion(droite)

        i = j = k = 0
        while i < len(gauche) and j < len(droite):
            if gauche[i] < droite[j]:
                ma_liste[k] = gauche[i]
                i += 1
            else:
                ma_liste[k] = droite[j]
                j += 1
            k += 1

        while i < len(gauche):
            ma_liste[k] = gauche[i]
            i += 1
            k += 1

        while j < len(droite):
            ma_liste[k] = droite[j]
            j += 1
            k += 1

def tri_rapide(ma_liste):
    def rapide(liste, debut, fin):
        if debut < fin:
            pivot = separer(liste, debut, fin)
            rapide(liste, debut, pivot - 1)
            rapide(liste, pivot + 1, fin)

    def separer(liste, debut, fin):
        pivot = liste[fin]
        i = debut - 1
        for j in range(debut, fin):
            if liste[j] <= pivot:
                i += 1
                liste[i], liste[j] = liste[j], liste[i]
        liste[i + 1], liste[fin] = liste[fin], liste[i + 1]
        return i + 1

    rapide(ma_liste, 0, len(ma_liste) - 1)

def tri_tas(ma_liste):
    def faire_tas(liste, taille, i):
        plus_grand = i
        gauche = 2 * i + 1
        droite = 2 * i + 2

        if gauche < taille and liste[gauche] > liste[plus_grand]:
            plus_grand = gauche
        if droite < taille and liste[droite] > liste[plus_grand]:
            plus_grand = droite
        if plus_grand != i:
            liste[i], liste[plus_grand] = liste[plus_grand], liste[i]
            faire_tas(liste, taille, plus_grand)

    n = len(ma_liste)
    for i in range(n // 2 - 1, -1, -1):
        faire_tas(ma_liste, n, i)
    for i in range(n - 1, 0, -1):
        ma_liste[i], ma_liste[0] = ma_liste[0], ma_liste[i]
        faire_tas(ma_liste, i, 0)

def tri_peigne(ma_liste):
    taille = len(ma_liste)
    ecart = taille
    reduire = 1.3
    trie = False

    while not trie:
        ecart = int(ecart / reduire)
        if ecart <= 1:
            ecart = 1
            trie = True
        i = 0
        while i + ecart < taille:
            if ma_liste[i] > ma_liste[i + ecart]:
                ma_liste[i], ma_liste[i + ecart] = ma_liste[i + ecart], ma_liste[i]
                trie = False
            i += 1

#liste aléatoire

def liste_aleatoire(taille):
    return [random.randint(0, 100) for _ in range(taille)]

#boucle principale 

def main():
    taille = 20
    liste_depart = liste_aleatoire(taille)

    mes_tris = [
        ("Sélection", tri_selection),
        ("Bulles", tri_bulles),
        ("Insertion", tri_insertion),
        ("Fusion", tri_fusion),
        ("Rapide", tri_rapide),
        ("Tas", tri_tas),
        ("Peigne", tri_peigne)
    ]

    for nom, tri in mes_tris:
        copie_liste = liste_depart.copy()
        tri(copie_liste)
        print(f"\nTri {nom} :")
        print(copie_liste)

#Lancer le programme

if __name__ == "__main__":
    main()







