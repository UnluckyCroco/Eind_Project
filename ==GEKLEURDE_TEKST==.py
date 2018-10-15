# Om kleuren aan text toe te voegen typ je na de ', \033[. vervolgens een getal (zie lijst) en dan m. dit kunnen ook meerdere getallen zijn gescheiden met een ;.

#Tekst Kleur
    # - 0 standaard
    # - 31 rood
    # - 32 geel
    # - 33 oranje
    # - 34 blauw
    # - 35 roze
    # - 36 cyaan
    # - 37 grijs
    # - 38 wit (standaard)

#Tekst stijl
    # - 0 standaard
    # - 1 bold
    # - 4 underline
    # - 7 negatief

#Achtergrond kleur
    # - 40 wit
    # - 41 rood
    # - 42 groen
    # - 43 geel
    # - 44 blauw
    # - 45 roze
    # - 46 cyaan
    # - 47 grijs
    # - 48 zwart (standaard)

#Voorbeelen
print('\033[31mHello world\033[0m')
print('\033[34mHello world\033[0m')
print('\033[4mHello world\033[0m')
print('\033[1mHello world\033[0m')
print('\033[31;4mHello world\033[0m')
print('\033[1;31;7mHello world\033[0m')
print('\033[31mH\033[32mA\033[34mL\033[35mL\033[33mO\033[0m')
#Je typt dus 'print(\033[(kleurcodes gescheiden door ; en gevolt door m)TEKST(geen spaties tussen de m en je tekst)\033[0m(hier zorg je ervoor dat het niet verder gaat in je code door de kleuren af te sluiten, of je moet dit willen verwijder dan gewoon de \033[0m.')