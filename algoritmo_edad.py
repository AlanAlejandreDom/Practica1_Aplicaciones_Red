print("*************** Calculo de los días que he ***************")
diaN = int(input("Ingrese el dia en que nacio: "))
mesN = input("Ingrese el mes en el que nacio: ")
mesN = mesN.lower()
yearN = int(input("Ingrese el año en el que nacio: "))
diastilmarzo = 67
diaspormes = [31,28,31,30,31,30,31,31,30,31,30,31]
contador=-1
if mesN=='enero' or mesN=='marzo' or mesN=='mayo' or mesN=='julio' or mesN=='agosto'or mesN=='octubre' or mesN=='diciembre' :
    while diaN <= 31:
        contador = contador + 1
        diaN = diaN + 1
elif mesN=='febrero':
    while diaN <= 28:
        contador = contador + 1
        diaN = diaN + 1
elif mesN=='abril' or mesN=='junio' or mesN=='septiembre' or mesN=='noviembre' :
    while diaN <= 30:
        contador = contador + 1
        diaN = diaN + 1        
if mesN=='enero':
    mes = 1
elif mesN=='febrero':
    mes = 2
elif mesN=='marzo':
    mes = 3
elif mesN=='abril':
    mes = 4
elif mesN=='mayo':
    mes = 5
elif mesN=='junio':
    mes = 6
elif mesN=='julio':
    mes = 7
elif mesN=='agosto':
    mes = 8
elif mesN=='septiembre':
    mes = 9
elif mesN=='octubre':
    mes = 10
elif mesN=='noviembre':
    mes = 11
elif mesN=='diciembre':
    mes = 12
for v in diaspormes[mes:12]:
    contador = contador + v
yearN = yearN + 1
while yearN < 2023:
    if(yearN%4==0):
        contador = contador + 1
    for v in diaspormes:
        contador = contador + v
    yearN = yearN + 1
contador = contador + diastilmarzo
print("Los días que has vivido hasta el 8 de marzo del 2023 son: ",contador)
mod3 = contador%3
if(mod3 == 0):
    print("El modulo 3 de los días es 0 por lo tanto te toca el Buscaminas")
elif(mod3 == 1):
    print("El modulo 3 de los días es 2 por lo tanto te toca el Gato Dummy")
elif(mod3 == 2):
    print("El modulo 3 de los días es 2 por lo tanto te toca el Memorama")

