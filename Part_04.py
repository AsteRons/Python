
'''
        Stringi - wprowadzenie
'''

atext = 'This is a text.'


#czy konczy sie slowami ext
atext.endswith('ext') 
# czytekst jest napisany malymi literami
atext.islower() 
# zmienia tekst na duze litery
atext.upper()  
#sprawdza czy tekst jest napisany tylko malywmi literami
atext.upper().isupper()
# czy wystepuje w tekscie wyraz is, jesli tak to pokazuje znaku i (pierwsze wystapienie)
atext.find('is')
#na którym miejscy wystepuje pierwszy znak zaczynajac od 3 wyrazu
atext.find('is',  3)
#Zamienia ciag znakow string a na 4
atext.replace('a',  '4')
# Dzieli tekst spacjami, wynikiem jest tablica podzielonych wyrazow
atext.split(' ') 

somethingsLikeNumber='10000'

#sprawdza czy ten string wyglada jak liczba
somethingsLikeNumber.isdigit()
#sprawdza czy sa same literki
somethingsLikeNumber.isalpha()
#israwdza czy sa tylko literki i cyferki
somethingsLikeNumber.isalnum()

