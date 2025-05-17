donnees = input("Entrez une liste d'entiers, séparés par des espaces : ")
donnees = donnees.split("/")  # Sépare les éléments de la chaîne en utilisant l'espace comme séparateur par défaut, Cependant, vous pouvez spécifier un autre séparateur en passant un argument à la méthode split().

liste = []  # Crée une liste vide

for element in donnees:
        # element = (element)  # Convertit chaque élément en entier
    liste.append(element)  # Ajoute l'élément au tableau

print("La liste est :", liste)
