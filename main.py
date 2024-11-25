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

arrayb = [88, 7, 63, 85, 3, 2, 66, 8, 95,55]
def is_sorted(arrayb):
    for i in range(1, len(arrayb)):
        if arrayb[i] < arrayb[i-1]:
            return False
    return True

def bogosort(arrayb):
    count = 0
    while not is_sorted(arrayb):
        random.shuffle(arrayb)
        count += 1
        print(f"Pokus (count): (arrayb)")
    print(f"Seznam seřezan po (count) pokusech.")

bogosort(arrayb)
print("Bogo", arrayb)
