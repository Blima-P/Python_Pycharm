print("Digite dois numeros")
x = int(input())
y = int(input())

while x != y:
    if x < y: 
        print("Crescente!")
    else:
        print("Descrescente!")

    print ("digite outros dois numeros")
    x = int(input())
    y = int(input())