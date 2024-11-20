import random

#1. Vytvořte jednorozměrné pole, které bude mít 10 náhodných hodnot (0-100).
pole = [random.randint(0, 100) for _ in range(10)]
print("Jednorozměrné pole:", pole)

#2. Vytvořte jednoduchý sort.
serazeno = sorted(pole)
print("Seřazené pole (standartní sort):", serazeno)

#3. Přemýšlejte nad tím jak implementovat bubble sort.
