soma= 0
contatador =0
print("digite os numeros para calcular a média.digite 0 (zero) para terminar.")
while True:
    valor=float(input ("digite um numero"))
    if valor ==0:
        break
    soma +=valor  
    contatador += 1
    if contatador ==0:
        print("nenhum numero foi insirido.")
    else:
        media =soma/contatador
        print("a media dos numeros insiridos é:", media)