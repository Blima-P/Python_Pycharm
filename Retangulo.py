import math

base = float(input("Base do Retangulo: "))
altura = float(input("Altura do retngulo: "))

area = base * altura
perimetro = 2 * (base + altura)
diagonal = math.sqrt(base ** 2 + altura ** 2)

print(f"Area = {area:.4F}")

print(f"Perimetro = {perimetro:.4f}")

print(f"diagonal = {diagonal:.4f}")