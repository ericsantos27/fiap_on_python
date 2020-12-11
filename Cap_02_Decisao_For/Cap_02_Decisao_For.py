value = int(input("Valor da tabuada: "))
print("Tabuada do número ", value)
for i in range(1, 11, 1):
    print(str(value) + " x " + str(i) + " = " + str(value * i))

