caso = 1

while True:

    n,q = map(int,input().split())

        if n == 0 and q == 0:
                break

                    numeros = []

                        for i in range(n):
                                numeros.append(int(input()))

                                    numeros.sort()

                                        print("CASE#",caso)

                                            for i in range(q):
                                                    x = int(input())

                                                            if x in numeros:
                                                                        print(x,"found")
                                                                                else:
                                                                                            print(x,"not found")

                                                                                                caso += 1