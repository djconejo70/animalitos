import pandas as pd
from datetime import datetime
rv=1
rvb=2
numero_datos=0    
numero=pd.read_excel('D:/ia_animalitos/animalitos/numero_indicaciones_semana.xlsx', header=None, names=['Numero']) 
df = pd.DataFrame(numero)
lista1 = df['Numero'].tolist()

acumulador=lista1[0]
print(acumulador, type(acumulador))

# if rv==rvb:
#     numero_datos=+1
# else:
#     numero_datos=+2
    
# dia_semana=(datetime.today().weekday())
# if dia_semana==0:
#     acumulador=0
# else:
#     acumulador=acumulador+numero_datos