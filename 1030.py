t = int(input())

for i in range(1,t+1):

    n,k = map(int,input().split())

        pessoas = list(range(1,n+1))

            pos = 0

                while len(pessoas) > 1:
                        pos = (pos + k -1) % len(pessoas)
                                pessoas.pop(pos)

                                    print("Case",i,":",pessoas[0])