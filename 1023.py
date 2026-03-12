n = int(input())

while n != 0:

    casas = []
        consumo = []

            for i in range(n):
                    x,y = map(int,input().split())
                            casas.append(x)
                                    consumo.append(y//x)

                                        for i in range(n):
                                                print(casas[i],"-",consumo[i])

                                                    media = sum(consumo)/len(consumo)

                                                        print("Consumo medio: %.2f m3." % media)

                                                            n = int(input())