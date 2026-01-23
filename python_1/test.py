print("Hello World")
>>> 7 + 3**6
736 #yes
>>> (3+4)**3
343 #yes
>>> 3**6 - 5
724 #no
>>> (1+2**8)*5
1285 #yes
>>> (2+1**8)**7
2187 #yes

    (1+2)**3 => 27
    "Da" * 4 => DaDaDaDa
    "Da" + 3 = error (#can only concatenate str (not "int") to str)
    ("Pa"+"La") * 2 = PaLaPaLa
    ("Da"*4) / 2 = error (#unsupported operant type(s) for /: 'str' and 'ist')
    5 / 2 = 2.5
    5 // 2 = 2
    5 % 2 = 1

    str(4) * int("3") = 444
    int("3") + float("3.2") = 6.2
    str(3) * float("3.2") = error (can't multiply sequence by non-int of type 'float')

    str(3/4) * 2 = 0.750.75
    
#Affichage
>>> print("Hello") ; print("Joe")
Hello
Joe
>>> print("Hello", end="") ; print("Joe")
HelloJoe
>>> print("Hello", end=" ") ; print("Joe")
Hello Joe
