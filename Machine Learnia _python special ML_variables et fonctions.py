x = 1
print (x)

x = 2
print (x)

x +=1
print (x)

x = 1
y=2.5



#arithmetique
print (x+y)
print (x*y)
print (x-y)
print (x/y)
print (x**y)
#comparaison
print (x<=y)
print (x>=y)
print (x==y)
print (x!=y)

a=True

#logique
print (False & True) # AND
print (False | True) # OR
print (False ^ True) # XOR

#string
prenom = 'Guillaume 0'
print (prenom)


x,y = 1, 2.5
print (x)
print (y)
print (x,y)


#creer une fonction
f = lambda x: x**2

print(f(3))
print(f(4))
print(f(5))


f = lambda x,y: x**2 + y
print(f(3,5))

#utiliser une fonction
def i_potentielle (m,h,g):
    E = m*g*h
    print (E, 'Joules')

print ('Bonjour')

i_potentielle(80, 5, 9.81)


#les vaiables internes et les arguments
##la commande return et la variable interne
def i_potentielle (m,h,g):
    E = m*g*h
    print (E, 'Joules')
    return E
print ('Bonjour')

resultat = i_potentielle(80, 5, 9.81)


##les arguments
###exemple 1
def i_potentielle (m,h,g):
    E = m*g*h
    print (E, 'Joules')
    return E
print ('Bonjour')

resultat_2 = i_potentielle(m=80, h=5, g=9.81)


###exemple 2
def i_potentielle (m,h,g=9.81):
    E = m*g*h
    print (E, 'Joules')
    return E
print ('Bonjour')

resultat_3 = i_potentielle(m=80, h=5)

###exemple 3
def i_potentielle (m,h,g=9.81):
    E = m*g*h
    print (E, 'Joules')
    return E
print ('Bonjour')

resultat_4 = i_potentielle(m=80, h=5, g=6.52)











