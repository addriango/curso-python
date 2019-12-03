edad=input("cual es tu edad?: ")

while edad.isdigit()==False:
    print("Por favor, Introduce un valor numerico")
    edad=input("cual es tu edad?: ")
    
if int(edad)<18:
    print("no puedes pasar")
else:
    print("puedes pasar")
    