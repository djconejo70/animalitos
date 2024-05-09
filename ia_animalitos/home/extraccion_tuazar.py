import requests 
from bs4 import BeautifulSoup
import re
import pandas as pd
from collections import Counter
from datetime import datetime, date



def capture_resultados():
    
    url=requests.get('https://www.tuazar.com/loteria/animalitos/resultados/')
    soup = BeautifulSoup(url.content, "html.parser")
    resultado_loto=[]
    resultado_granja=[]
    resultado_loto_numerico=[]
    elementos=soup.find_all('div', class_="col-xs-6 col-sm-3")
    c=0
    for elementos_div in elementos:
        x = elementos_div.find('span')
        c=c+1
        if x and (c>12 and c<24):
            resultado_loto.append(x.text.strip())
    for animales in resultado_loto:   
        resultado_loto_numerico.append(re.findall('\d+', animales))
    lista=[]   
    for valores in resultado_loto_numerico:
        for numeros in valores:
            lista.append(numeros)    
    # df=pd.DataFrame(lista)
    # a=pd.concat([datos, df], axis=0)
    # a.to_excel('lotoactivo.xlsx', sheet_name='Hoja1', index=None)   
    return (lista)


def capture_granja():
    
    url=requests.get('https://www.tuazar.com/loteria/animalitos/resultados/')
    soup = BeautifulSoup(url.content, "html.parser")    
    resultado_granja=[]
    elementos=soup.find_all('div', class_="col-xs-6 col-sm-3")
    c=0
    for elementos_div in elementos:
        x = elementos_div.find('span')
        c=c+1
        if x and (c>23 and c<36):
            resultado_granja.append(x.text.strip())  

    
    resultado_granja_numerico=[]
    for animales in resultado_granja:   
        resultado_granja_numerico.append(re.findall('\d+', animales))
    lista_granja=[]   
    for valores in resultado_granja_numerico:
        for numeros in valores:
            lista_granja.append(numeros)    
    # df=pd.DataFrame(lista_granja)
    # a=pd.concat([datos_granja, df], axis=0)
    # a.to_excel('Granja.xlsx', sheet_name='Hoja1', index=None)
    # print('Granja')
    # print(lista_granja)
    return (lista_granja)

def capture_nombre(entrada):
    df = pd.read_excel('D:/ia_animalitos/animalitos/animalitos.xlsx', header=None, names=['Numero','Nombre']) 
    nombre=1
    entrada=int(entrada)
    if entrada in df.Numero.values:
        nombre=df[df.Numero==entrada]['Nombre'].values[0]
        # print(nombre)    
    return(nombre)

def maximo_loto():
    datos=pd.read_excel('D:/ia_animalitos/animalitos/lotoactivo.xlsx', header=None, names=['Numero'])
    df = pd.DataFrame(datos)
    lista1 = df['Numero'].tolist()
    c=Counter(lista1)
    comun=(Counter(lista1).most_common())
    a1=(comun[0][0])
    a2=(comun[0][1])    
    b1=(comun[-1][0])    
    b2=(comun[-1][1])
    # print(b1,b2)
    return(a1,a2,b1,b2)

def datos_excel():
    datos=pd.read_excel('D:/ia_animalitos/animalitos/dato.xlsx', header=None, names=['Numero'])
    df = pd.DataFrame(datos)
    lista1 = df['Numero'].tolist()
    # print(lista1,'lista1')
    dato1=lista1[1]
    if dato1==00 or dato1==38:
        dato1=38
    dato2=lista1[2] 
    if dato2==00 or dato2==38:
        dato2=38
    # print('dato1', dato1, dato2)
    return(dato1,dato2)



def maximo_granja():
    datos=pd.read_excel('D:/ia_animalitos/animalitos/Granja.xlsx', header=None, names=['Numero'])
    df = pd.DataFrame(datos)
    lista2 = df['Numero'].tolist()
    c=Counter(lista2)
    comun=(Counter(lista2).most_common())
    ag1=(comun[0][0])
    ag2=(comun[0][1])    
    bg1=(comun[-1][0])    
    bg2=(comun[-1][1])
    # print(ag1,ag2,bg1,bg2)
    return(ag1,ag2,bg1,bg2)



def capture_temp_granja():
    
    url=requests.get('https://www.tuazar.com/loteria/animalitos/resultados/')
    soup = BeautifulSoup(url.content, "html.parser")    
    resultado_granja=[]
    elementos=soup.find_all('div', class_="col-xs-6 col-sm-3")
    c=0
    for elementos_div in elementos:
        x = elementos_div.find('span')
        c=c+1
        if x and (c>23 and c<36):
            resultado_granja.append(x.text.strip())  

    
    resultado_granja_numerico=[]
    for animales in resultado_granja:   
        resultado_granja_numerico.append(re.findall('\d+', animales))
    lista_granja=[]   
    for valores in resultado_granja_numerico:
        for numeros in valores:
            lista_granja.append(numeros)    
    df=pd.DataFrame(lista_granja)
    return (lista_granja)


def capture_temporal_loto():    
    url=requests.get('https://www.tuazar.com/loteria/animalitos/resultados/')
    soup = BeautifulSoup(url.content, "html.parser")
    resultado_loto=[]
    resultado_granja=[]
    resultado_loto_numerico=[]
    elementos=soup.find_all('div', class_="col-xs-6 col-sm-3")
    c=0
    for elementos_div in elementos:
        x = elementos_div.find('span')
        c=c+1
        if x and (c>12 and c<24):
            resultado_loto.append(x.text.strip())
    for animales in resultado_loto:   
        resultado_loto_numerico.append(re.findall('\d+', animales))
    lista=[]   
    for valores in resultado_loto_numerico:
        for numeros in valores:
            lista.append(numeros)    
    df=pd.DataFrame(lista)    
    #df.to_excel('D:/ia_animalitos/animalitos/resultados_temporal_loto.xlsx', index=None)   
    return (lista)






def aciertos(dato1, dato2):
    dato1=str(dato1)
    dato2=str(dato2)
    contador_aciertos=0
    temporal_loto=capture_temporal_loto()
    for animalitos in temporal_loto:
        if dato1==animalitos:
            contador_aciertos=contador_aciertos+1
        if dato2==animalitos:
            contador_aciertos=contador_aciertos+1
    temporal_granja=capture_temp_granja()
    for animalitos in temporal_granja:
        if dato1==animalitos:
            contador_aciertos=contador_aciertos+1
        if dato2==animalitos:
            contador_aciertos=contador_aciertos+1    
    dia_semana=(datetime.today().weekday())
    if dia_semana==0:
        acumulador_aciertos=contador_aciertos
    else:
        acumulador_aciertos1=open("acumulador_aciertos_semana.txt","r")
        acumulador_aciertos=acumulador_aciertos1.read()
        acumulador_aciertos1.close()
        acumulador_aciertos=int(acumulador_aciertos)+contador_aciertos
    return(acumulador_aciertos)
    
        



        
    
        
                
        

    
    
    
    

