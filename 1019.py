tempo = int(input())

h = tempo // 3600
tempo %= 3600
m = tempo // 60
s = tempo % 60

print(f"{h}:{m}:{s}")