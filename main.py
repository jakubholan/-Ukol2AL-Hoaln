import random

#1. Vytvořte jednorozměrné pole, které bude mít 10 náhodných hodnot (0-100).
pole = [random.randint(0, 100) for _ in range(10)]
print("Jednorozměrné pole:", pole)

#2. Vytvořte jednoduchý sort.
serazeno = sorted(pole)
print("Seřazené pole (standartní sort):", serazeno)

#3. Přemýšlejte nad tím jak implementovat bubble sort.
def bubble_sort(pole):
    n = len(pole)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if pole[j] > pole[j+1]:
                pole[j], pole[j+1] = pole[j+1], pole[j]
            print(pole)
    return pole
    
print(bubble_sort)

