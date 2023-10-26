
def szepnapvan(szoveg):

    """ Írd ki a szöveg első karakterét! """

    print("1. karaketer:",szoveg[0])
    print("2. karaketer:",szoveg[1])
    print("utolso karaketer:",szoveg[len(szoveg)-1])

    i=0
    while i<len(szoveg):
        print(szoveg[i],end="")
        i+=1






def szovegkezeles(szoveg):
    print(szoveg.upper())


    torpedo = szoveg.find("jegesmedve")
    print("A 'jegesmedve' szó ennél a karakternél kezdődik:", torpedo if torpedo>=0 else "nincs ilyen szó a szövegben")

    print("Az első 's' betű karakter helye:",end=" ")
    print(szoveg.index("s"))

    print("Minden szó kezdőbetűje nagy lesz:",end=" ")
    print(szoveg.title())

    print("A 'hegedül' szót kicseréljük a 'proba' szóra:",end=" ")
    print(szoveg.replace("hegedül","proba"))







def aszoveg_visszafele(szoveg):
    i=len(szoveg)
    while i!=0:
        print(szoveg[i-1],end="")
        i-=1






def a_betuk_szama(szoveg):
    i=0
    db=0
    while i!=len(szoveg):
        if szoveg[i]=="e":
            db+=1
        i+=1
    print("\n'e' betűk száma:",db)





