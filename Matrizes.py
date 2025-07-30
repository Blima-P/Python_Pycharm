M = int(input("Quantas linhas vai ter a matriz? "))
N = int(input("Quantas colunas vai ter a matriz? "))

Mat: [[int]] = [[0 for x in range (N)]for x in range (M)]

for i in range (0, M) :
    for j in range (0, N):
        Mat [i][j] = int(input(f"Elemento [{i},{j}]: "))

print()
print("Matriz digitada")
for i in range(0, M):
    for j in range(0, N):
        print(F"{Mat[i][j]} ", end ="")
    print()