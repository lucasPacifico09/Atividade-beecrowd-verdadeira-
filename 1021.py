valor = float(input())

notas = [100,50,20,10,5,2]
moedas = [1,0.50,0.25,0.10,0.05,0.01]

print("NOTAS:")

for n in notas:
    qtd = int(valor // n)
        print(qtd,"nota(s) de R$ %.2f" % n)
            valor = valor - qtd*n

            print("MOEDAS:")

            for m in moedas:
                qtd = int(valor // m)
                    print(qtd,"moeda(s) de R$ %.2f" % m)
                        valor = valor - qtd*m