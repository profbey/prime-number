# Examples: Find whether an entered number is prime or not.

    

print('This app checks if the number is prime or not')
from math import sqrt


def aralik_icin_sayi_al():
    while True:
        try:
            aralik_icin_sayi_al = []

            baslangic = int(input('enter first numb: '))
            bitis = int(input('enter final numb: '))

            if baslangic <= bitis:
                for i in range(baslangic,bitis):
                    aralik_icin_sayi_al = aralik_icin_sayi_al.append([i])
                print(aralik_icin_sayi_al)

            else:
                print("Lütfen belirtilen aralıkta bir sayı giriniz.")
        except ValueError:
            print("Lütfen bir sayı giriniz.")

 
aralik_icin_sayi_al()









'''


try:
    #number = int(input('Enter a number: '))
    number = aralik_icin_sayi_al()
    numberSqrt = int(sqrt(number))
    primeNumber = True

    for i in range(2, numberSqrt + 1):
        if number % i == 0:
            primeNumber = False
            break
        
except ValueError:
    print('try again with numbers.')


if primeNumber:
    print(f"The number {number} is prime.")
else:
    print(f"The number {number} is NOT prime.")
'''