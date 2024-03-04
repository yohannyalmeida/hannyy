acrs=10
soma=0
i=0
n=int(input("mquantos valores voce quer?/n"))

while i <n:
    i+=1
    soma+= float(input(f"digite o {i}º valor:"))
    if soma <200:
        print("a soma é maior que 200,o valor final com acrecimo de 10% é:", soma*(1+acrs/100))
    else:
        print(" a soma e igual a",soma )
