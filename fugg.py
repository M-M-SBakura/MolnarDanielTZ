import random
#klubkártya szám#
def kartyaszam ():

    szam1=''.join(random.choice('A' 'B' 'C' 'D' 'Q' 'W' 'E' 'R' 'T' 'Z' 'U' 'I' 'O' 'P' 'S' 'F' 'H' 'J' 'K' 'L' 'y' 'X' 'V' 'N' 'M' '0' '1' '2' '3' '4' '5' '6' '7' '8' '9' ) )
    szam2=''.join(random.choice('A' 'B' 'C' 'D' 'Q' 'W' 'E' 'R' 'T' 'Z' 'U' 'I' 'O' 'P' 'S' 'F' 'H' 'J' 'K' 'L' 'y' 'X' 'V' 'N' 'M' '0' '1' '2' '3' '4' '5' '6' '7' '8' '9' ) )
    szam3=''.join(random.choice('A' 'B' 'C' 'D' 'Q' 'W' 'E' 'R' 'T' 'Z' 'U' 'I' 'O' 'P' 'S' 'F' 'H' 'J' 'K' 'L' 'y' 'X' 'V' 'N' 'M' '0' '1' '2' '3' '4' '5' '6' '7' '8' '9' ) )
    szam4=''.join(random.choice('A' 'B' 'C' 'D' 'Q' 'W' 'E' 'R' 'T' 'Z' 'U' 'I' 'O' 'P' 'S' 'F' 'H' 'J' 'K' 'L' 'y' 'X' 'V' 'N' 'M' '0' '1' '2' '3' '4' '5' '6' '7' '8' '9' ) )
    print(+str(szam1)+str(szam2)+str(szam3)+str(szam4)+'-')
    return

#év szám#
def ev ():

    szam1=''.join(random.choice('1988' '2001' '2006' '2010' '2021' '2022') )
    print(szam1)

    return

#pontszám#
def pont ():


    return 
#neveket#
def nevek ():

    csaladneve=''.join(random.choice('Kovács' 'Molnár' 'Kiss' 'Nagy' 'Horvát' 'Szabó' 'Papp' 'Farkas') )
    kerestneve=''.join(random.choice('József' 'Sándor' 'Katalin' 'Béla' 'Bettina' 'Éva' 'Benedek' 'Péter' 'Erika') )
    print(kerestneve,csaladneve)

    return