a = input().split()
b = input().split()
total = int(a[1])*float(a[2]) + int(b[1])*float(b[2])
print("VALOR A PAGAR: R$ {:.2f}".format(total))