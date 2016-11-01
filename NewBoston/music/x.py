# imie = 'Kuba'
# nazwisko = 'Ciężki'
# wiek = 7
#
# print (imie + ' ' + nazwisko + ' ma ' + str(wiek) + ' lat.')
#
a=5
b=1
import sys

try:
    print (a/b)


except ZeroDivisionError:
    print ('not possible!')
else:
    print ('ELSE')
finally:
    print ('FIN')