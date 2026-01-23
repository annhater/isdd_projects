#Exercices
#4.12.1 Prédire la sortie
liste1 = list(range(10, 15))
var = 0
var2 = 10
print(liste1[2]) # => 12
print(liste1[var]) # => 10
print(liste1[var2]) # => error
print(liste1["var"]) # => error

#4.12.2 Jours de la semaine
semaine = ["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
#1
print(semaine[0:5])
print(semaine[5:8])
#2
print(semaine[-7:-2])
print(semaine[5:8])
#3
print(f"{semaine[0:5]:30<},{semaine[6,8]:30>}")

#4.12.3 Saisons
hiver = ["decembre","janvier","fevrier"]
printemps = ["mars", "avril", "mai"]
ete = ["juin", "juillet", "aout"]
automne = ["septembre", "octobre", "novembre"]
saisons = [hiver, printemps, ete, automne]

print(saisons[2]) # => "juin", "juillet", "aout"
print(saisons[1][0]) # => "mars"
print(saisons[1:2]) # => [["mars", "avril", "mai"]] ; toutes les valeurs de listes entre [1] et [2] printemps
print(saisons[:][1]) # => "mars", "avril", "mai"
#4.12.4 Table de multiplication par 9
print(list(range(0,100,9)))

#4.12.5 Nombres pairs
len(list(range(2,10001,2)))

#5.4.1 Boucles de base
#1
vivant = ["vache", "souris", "levure", "bacterie"]
for i in vivant:
    print (i)
#2
for i in range(len(vivant)):
    print(vivant[i])
#3
vivant = ["vache", "souris", "levure", "bacterie"]
i = 0
while i < len(vivant):
        print(vivant[i])
        i += 1 #to close the loop
#5.4.2 Boucles et jours de la semaine
semaine = ["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
for jour in semaine[0:5]:
    print (jour)
jour = 5
while jour < len(semaine):
    print(semaine[jour])
    jour += 1

#5.4.4 Nombres pairs et impairs
impairs = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
pairs = []
for i in impairs:
    pairs.append(i+1)
print(pairs)
        
#5.4.5 Calcul de la moyenne
notes = [14, 9, 6, 8, 12]
moyenne = sum(notes)/len(notes)
print(f"{moyenne:.2f}")

#5.4.6 Produit de nombres consécutifs
entiers = list(range(2,21,2))
liste = [] #create an empty list that we will complete with loop
for i in entiers:
    liste.append(i*i+i*2)) #nombre consecutif est incrementation de 2 => n+2; produit (multilication) des nombres consecutif => n(n+2)
#ou par ex n = 2, produit des nb consec => 2*4 => n*(n+2) => n*n+2*n
print(*liste, sep="\n")

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
#5.4.7 Triangle
triangle = "*"
while triangle != "***********":
    print(triangle)
    triangle += "*"

#5.4.8 Triangle inversé
triangle = "**********"
for i in range (1,11):
    print(triangle)
    triangle = triangle[:-1]
print(triangle)

#5.4.9 Triangle gauche
triangle = "*"
for i in range (0,9):
    print(f"{triangle:>10s}")
    triangle = triangle +"*"
      
#5.4.10 Pyramide
pyramide = "*"
for i in range (0,9):
    print(f"{pyramide:^20s}")
    pyramide = pyramide +"**"

reponse = input("Entrez un nombre de lignes (entier positif): ")
rows = int(reponse)
pyramide = "*"
for i in range(rows):
    print(f"{pyramide:^100s}")
    pyramide = pyramide +"**"