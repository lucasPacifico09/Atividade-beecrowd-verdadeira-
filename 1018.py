valor = int(input())
print(valor)

notas = [100,50,20,10,5,2,1]

for n in notas:
    qtd = valor // n
        print(f"{qtd} nota(s) de R$ {n},00")
            valor %= n