#listes
liste_1 = [1, 4, 2, 7, 35, 84]
villes = ['Paris', 'Berlin', 'Londres', 'Bruxelles']
liste_2 = [liste_1, villes]
liste_3 = []  #liste vide

#tuple
tuple_1 = (1, 2, 6, 1, 7)

#string
prénom = 'Nicolas'


#indexing sur une liste
print (villes[0])   #1er élément = index 0
print (villes[1])   #2eme élément = index 1
print (villes[-1])  #dernier élément = index -1
print (villes[-2])  #avant dernier élément = index -2

#slicing sur une liste: liste[début : fin : pas]
print(villes[0:3])   #de l'index 0 jusqu'à l'index 2 
print(villes[:3])    #de l'index 0 jusqu'à l'index 2
print(villes[2:])    #de l'index 2 jusqu'à la fin de la liste
print(villes[1:3])   #de l'index 1 jusqu'à l'index 2
print(villes[::2])   #du début jusqu'à la fin avec un pas = 2
print(villes[::-1])  #extraire tous les éléments de la liste à l'envers

#slicing sur une string: string[début : fin : pas]
print(prénom[0:3])   #de l'index 0 jusqu'à l'index 2
print(prénom[:3])   #de l'index 0 jusqu'à l'index 2

#remplacer un élément dans une liste
villes[0] = 'Dublin'
print (villes)
