from django.shortcuts import render
from home.precio_bcv import*
from home.extraccion_tuazar import*


def home (request):
     x=valorDolar()
     y=capture_resultados()
     a1=len(y)
     a=0
     while a<12:          
          if a>a1:
               y.append('No disponible')
          a=a+1            
     # for q in y:
     #      print(y)
     z=capture_granja()
     a1g=len(z)
     ag=0
     while ag<13:
          if ag>a1g:
               z.append('No disponible')
          ag=ag+1
          
          
          
          
     ml=maximo_loto()
     salidor_loto=ml[0]
     cantidad_loto=ml[1]
     menos_salidor_loto=ml[2]
     cantidad_menor_loto=ml[3]
     cantidad_loto=int(cantidad_loto)
     salidor_loto=int(salidor_loto)
     menos_salidor_loto=int(menos_salidor_loto)
     cantidad_menor_loto=int(cantidad_menor_loto)
    
     mlg=maximo_granja()
     salidor_granja=mlg[0]
     cantidad_granja=mlg[1]
     menos_salidor_granja=mlg[2]
     cantidad_menor_granja=mlg[3]
     salidor_granja=int(salidor_granja)
     cantidad_granja=int(cantidad_granja)
     menos_salidor_granja=int(menos_salidor_granja)
     cantidad_menor_granja=int(cantidad_menor_granja)
     
     
        
     datos=datos_excel()
     dato1=datos[0]
     dato2=datos[1]    
     if dato1==38:
          nombre_dato1='Ballena'
          dato1='00'          
     elif dato1==37:
          nombre_dato1='Delfin'
          dato1=0         
     else:
          nombre_dato1=capture_nombre(dato1)
     
     if dato2==38:
          nombre_dato2='Ballena'
          dato2='00'
          
     elif dato2==37:
          nombre_dato2='Delfin'
          dato2==0
          
     else:
          nombre_dato2=capture_nombre(dato2)
          
     
   
     
     
     
     nombres_loto=[] 
     contador_nombresloto=0
     while contador_nombresloto!=a1:          
          nombre_temp='' 
          if  ((y[contador_nombresloto])=='00'):               
               nombre_temp="Ballena"
          else:                        
               nombre_temp=capture_nombre(y[contador_nombresloto])          
          contador_nombresloto=contador_nombresloto + 1
          nombres_loto.append(nombre_temp)
     
     anombreloto=0
     while anombreloto<12:                    
          if anombreloto>a1:
               nombres_loto.append('')
          anombreloto=anombreloto+1
     # print(nombres_loto)
     
     
     
     nombre_granja=[]
     contador_nombresgranja=0
     while contador_nombresgranja!=a1g:          
          nombre_temp=''
          
          if  ((z[contador_nombresgranja])=='00'):
               
               nombre_temp="Ballena"
          else:               
               nombre_temp=capture_nombre(z[contador_nombresgranja])          
          contador_nombresgranja=contador_nombresgranja + 1
          nombre_granja.append(nombre_temp)
          
     anombregranja=0
     while anombregranja<13:          
          if anombregranja>a1g:
               nombre_granja.append('')
          anombregranja=anombregranja+1
     
         
     nombre_salidor_loto=capture_nombre(salidor_loto)
     nombre_salidor_granja=capture_nombre(salidor_granja)
     nombre_menor_salidor_lotto= capture_nombre(menos_salidor_loto)
     nombre_menor_salidor_granja= capture_nombre(menos_salidor_granja)
     
         
              
         
  
     a=x[0]
     b=x[1]
     c=x[2]
     l9=y[0]
     l10=y[1]
     l11=y[2]
     
     l12=y[3]
     l13=y[4]
     l14=y[5]
     l15=y[6]
     l16=y[7]
     l17=y[8]
     l18=y[9]
     l19=y[10]
     
     z8=z[0]
     z9=z[1]
     z10=z[2]
     
     z11=z[3]
     z12=z[4]
     z13=z[5]
     z14=z[6]
     z15=z[7]
     z16=z[8]
     z17=z[9]
     z18=z[10]
     z19=z[11]
     nloto9=nombres_loto[0]
     nloto10=nombres_loto[1]
     nloto11=nombres_loto[2]
     nloto12=nombres_loto[3]
     nloto13=nombres_loto[4]
     nloto14=nombres_loto[5]
     nloto15=nombres_loto[6]
     nloto16=nombres_loto[7]
     nloto17=nombres_loto[8]
     nloto18=nombres_loto[9]
     nloto19=nombres_loto[10]
     
     ngranja8=nombre_granja[0]
     ngranja9=nombre_granja[1]
     ngranja10=nombre_granja[2]
     ngranja11=nombre_granja[3]
     ngranja12=nombre_granja[4]
     ngranja13=nombre_granja[5]
     ngranja14=nombre_granja[6]
     ngranja15=nombre_granja[7]
     ngranja16=nombre_granja[8]
     ngranja17=nombre_granja[9]
     ngranja18=nombre_granja[10]
     ngranja19=nombre_granja[11]
     
     acierto1=aciertos(dato1,dato2)
     acierto=acierto1
     acumulador_indicaciones1=open("acumulador_indicaciones_semana.txt","r")
     acumulador_indicaciones=acumulador_indicaciones1.read()
     acumulador_indicaciones1.close()
     indicaciones=int(acumulador_indicaciones)
     if dato1==dato2:
          indicaciones=indicaciones+1
     else:
          indicaciones=indicaciones+2
          
     if acierto1==0:
          efectividad=0
     else:
          efectividad=(acierto1*100)/indicaciones
          efectividad=format(efectividad,'.2f')

     

     dia_semana=(datetime.today().weekday())
     if dia_semana==0:
          indicaciones=indicaciones - 14
     
     
        
     
     context={'valordolar':a, 'valoreuro':b, 'fecha': c, 
              'loto9':l9,'loto10':l10,'loto11':l11,'loto12':l12,
              'loto13':l13,'loto14':l14, 'loto15':l15,'loto16':l16, 'loto17':l17,'loto18':l18,
              'loto19':l19, 'granja8':z8,'granja9':z9, 'granja10':z10, 'granja11':z11, 'granja12':z12,
              'granja13':z13,
              'granja14':z14, 'granja15':z15, 'granja16':z16, 'granja17':z17, 'granja18':z18, 
              'granja19':z19 , 'nombre_loto9':nloto9,
              'nombre_loto10':nloto10, 'nombre_loto11':nloto11, 'nombre_loto12':nloto12, 
              'nombre_loto13':nloto13, 'nombre_loto14':nloto14,
              'nombre_loto15':nloto15, 'nombre_loto16':nloto16, 'nombre_loto17':nloto17, 
              'nombre_loto18':nloto18, 'nombre_loto19':nloto19,
              'ngranja8': ngranja8, 'ngranja9': ngranja9, 'ngranja10': ngranja10, 'ngranja11': ngranja11,
              'ngranja12': ngranja12, 
              'ngranja13': ngranja13, 'ngranja14': ngranja14, 'ngranja15': ngranja15,'ngranja16': ngranja16, 
              'ngranja17': ngranja17, 'ngranja18': ngranja18, 'ngranja19': ngranja19,
              'salemasloto':salidor_loto, 'cantidadsalidorloto':cantidad_loto,
              'menorsalidorloto': menos_salidor_loto, 'mayorsalidorgranja': salidor_granja,
              'cantidad_menor_loto':cantidad_menor_loto,
              'cantidadmayorsalidorgranja':  cantidad_granja, 'menorsalidorgranja': menos_salidor_granja,
              'cantidadmenorsalidorgranja': cantidad_menor_granja,
              'nombresalidorloto':nombre_salidor_loto, 'nombresalidorgranja':nombre_salidor_granja,
              "nombre_menor_salidor_lotto":nombre_menor_salidor_lotto,
              "nombre_menor_salidor_granja":nombre_menor_salidor_granja,
              'dato1':dato1, 'dato2': dato2, 'nombre_dato1':nombre_dato1, 'nombre_dato2':nombre_dato2, 'acierto':acierto,
              'indicaciones': indicaciones, 'efectividad':efectividad}              
     return render (request, 'index.html', context)

def contacto (request):
     x=valorDolar()
     y=capture_resultados()
     a1=len(y)
     a=0
     while a<12:          
          if a>a1:
               y.append('No disponible')
          a=a+1            
     # for q in y:
     #      print(y)
     z=capture_granja()
     a1g=len(z)
     ag=0
     while ag<13:
          if ag>a1g:
               z.append('No disponible')
          ag=ag+1
          
      
          
          
     ml=maximo_loto()
     salidor_loto=ml[0]
     cantidad_loto=ml[1]
     menos_salidor_loto=ml[2]
     cantidad_menor_loto=ml[3]
     cantidad_loto=int(cantidad_loto)
     salidor_loto=int(salidor_loto)
     menos_salidor_loto=int(menos_salidor_loto)
     cantidad_menor_loto=int(cantidad_menor_loto)
    
     mlg=maximo_granja()
     salidor_granja=mlg[0]
     cantidad_granja=mlg[1]
     menos_salidor_granja=mlg[2]
     cantidad_menor_granja=mlg[3]
     salidor_granja=int(salidor_granja)
     cantidad_granja=int(cantidad_granja)
     menos_salidor_granja=int(menos_salidor_granja)
     cantidad_menor_granja=int(menos_salidor_granja)
     
     
        
     datos=datos_excel()
     dato1=datos[0]
     dato2=datos[1]    
     if dato1==38:
          nombre_dato1='Ballena'
          dato1='00'          
     elif dato1==37:
          nombre_dato1='Delfin'
          dato1=0         
     else:
          nombre_dato1=capture_nombre(dato1)
     
     if dato2==38:
          nombre_dato2='Ballena'
          dato2='00'
          
     elif dato2==37:
          nombre_dato2='Delfin'
          dato2==0
          
     else:
          nombre_dato2=capture_nombre(dato2)
          
     
   
     
     
     
     nombres_loto=[] 
     contador_nombresloto=0
     while contador_nombresloto!=a1:          
          nombre_temp='' 
          if  ((y[contador_nombresloto])=='00'):               
               nombre_temp="Ballena"
          else:                        
               nombre_temp=capture_nombre(y[contador_nombresloto])          
          contador_nombresloto=contador_nombresloto + 1
          nombres_loto.append(nombre_temp)
     
     anombreloto=0
     while anombreloto<12:                    
          if anombreloto>a1:
               nombres_loto.append('')
          anombreloto=anombreloto+1
     # print(nombres_loto)
     
     
     
     nombre_granja=[]
     contador_nombresgranja=0
     while contador_nombresgranja!=a1g:          
          nombre_temp=''
          
          if  ((z[contador_nombresgranja])=='00'):
               
               nombre_temp="Ballena"
          else:               
               nombre_temp=capture_nombre(z[contador_nombresgranja])          
          contador_nombresgranja=contador_nombresgranja + 1
          nombre_granja.append(nombre_temp)
          
     anombregranja=0
     while anombregranja<13:          
          if anombregranja>a1g:
               nombre_granja.append('')
          anombregranja=anombregranja+1
     
         
     nombre_salidor_loto=capture_nombre(salidor_loto)
     nombre_salidor_granja=capture_nombre(salidor_granja)
     nombre_menor_salidor_lotto= capture_nombre(menos_salidor_loto)
     nombre_menor_salidor_granja= capture_nombre(menos_salidor_granja)
     
         
              
         
  
     a=x[0]
     b=x[1]
     c=x[2]
     l9=y[0]
     l10=y[1]
     l11=y[2]
     
     l12=y[3]
     l13=y[4]
     l14=y[5]
     l15=y[6]
     l16=y[7]
     l17=y[8]
     l18=y[9]
     l19=y[10]
     
     z8=z[0]
     z9=z[1]
     z10=z[2]
     
     z11=z[3]
     z12=z[4]
     z13=z[5]
     z14=z[6]
     z15=z[7]
     z16=z[8]
     z17=z[9]
     z18=z[10]
     z19=z[11]
     nloto9=nombres_loto[0]
     nloto10=nombres_loto[1]
     nloto11=nombres_loto[2]
     nloto12=nombres_loto[3]
     nloto13=nombres_loto[4]
     nloto14=nombres_loto[5]
     nloto15=nombres_loto[6]
     nloto16=nombres_loto[7]
     nloto17=nombres_loto[8]
     nloto18=nombres_loto[9]
     nloto19=nombres_loto[10]
     
     ngranja8=nombre_granja[0]
     ngranja9=nombre_granja[1]
     ngranja10=nombre_granja[2]
     ngranja11=nombre_granja[3]
     ngranja12=nombre_granja[4]
     ngranja13=nombre_granja[5]
     ngranja14=nombre_granja[6]
     ngranja15=nombre_granja[7]
     ngranja16=nombre_granja[8]
     ngranja17=nombre_granja[9]
     ngranja18=nombre_granja[10]
     ngranja19=nombre_granja[11]
     
     
     acierto1=aciertos(dato1,dato2)
     acierto=acierto1
     acumulador_indicaciones1=open("acumulador_indicaciones_semana.txt","r")
     acumulador_indicaciones=acumulador_indicaciones1.read()
     acumulador_indicaciones1.close()
     indicaciones=int(acumulador_indicaciones)
     if acierto1==0:
          efectividad=0
     else:
          efectividad=(acierto1*100)/indicaciones
          efectividad=format(efectividad,'.2f')
     
        
     
     context={'valordolar':a, 'valoreuro':b, 'fecha': c, 
              'loto9':l9,'loto10':l10,'loto11':l11,'loto12':l12,
              'loto13':l13,'loto14':l14, 'loto15':l15,'loto16':l16, 'loto17':l17,'loto18':l18,
              'loto19':l19, 'granja8':z8,'granja9':z9, 'granja10':z10, 'granja11':z11, 'granja12':z12,
              'granja13':z13,
              'granja14':z14, 'granja15':z15, 'granja16':z16, 'granja17':z17, 'granja18':z18, 
              'granja19':z19 , 'nombre_loto9':nloto9,
              'nombre_loto10':nloto10, 'nombre_loto11':nloto11, 'nombre_loto12':nloto12, 
              'nombre_loto13':nloto13, 'nombre_loto14':nloto14,
              'nombre_loto15':nloto15, 'nombre_loto16':nloto16, 'nombre_loto17':nloto17, 
              'nombre_loto18':nloto18, 'nombre_loto19':nloto19,
              'ngranja8': ngranja8, 'ngranja9': ngranja9, 'ngranja10': ngranja10, 'ngranja11': ngranja11,
              'ngranja12': ngranja12, 
              'ngranja13': ngranja13, 'ngranja14': ngranja14, 'ngranja15': ngranja15,'ngranja16': ngranja16, 
              'ngranja17': ngranja17, 'ngranja18': ngranja18, 'ngranja19': ngranja19,
              'salemasloto':salidor_loto, 'cantidadsalidorloto':cantidad_loto,
              'menorsalidorloto': menos_salidor_loto, 'mayorsalidorgranja': salidor_granja,
              'cantidad_menor_loto':cantidad_menor_loto,
              'cantidadmayorsalidorgranja':  cantidad_granja, 'menorsalidorgranja': menos_salidor_granja,
              'cantidadmenorsalidorgranja': cantidad_menor_granja,
              'nombresalidorloto':nombre_salidor_loto, 'nombresalidorgranja':nombre_salidor_granja,
              "nombre_menor_salidor_lotto":nombre_menor_salidor_lotto,
              "nombre_menor_salidor_granja":nombre_menor_salidor_granja,
              'dato1':dato1, 'dato2': dato2, 'nombre_dato1':nombre_dato1, 'nombre_dato2':nombre_dato2, 'acierto':acierto,
              'indicaciones': indicaciones, 'efectividad':efectividad}              
     return render (request, 'contacto.html', context)


def soporte (request):
     x=valorDolar()
     y=capture_resultados()
     a1=len(y)
     a=0
     while a<12:          
          if a>a1:
               y.append('No disponible')
          a=a+1            
     # for q in y:
     #      print(y)
     z=capture_granja()
     a1g=len(z)
     ag=0
     while ag<13:
          if ag>a1g:
               z.append('No disponible')
          ag=ag+1
          
          
          
          
     ml=maximo_loto()
     salidor_loto=ml[0]
     cantidad_loto=ml[1]
     menos_salidor_loto=ml[2]
     cantidad_menor_loto=ml[3]
     cantidad_loto=int(cantidad_loto)
     salidor_loto=int(salidor_loto)
     menos_salidor_loto=int(menos_salidor_loto)
     cantidad_menor_loto=int(cantidad_menor_loto)
    
     mlg=maximo_granja()
     salidor_granja=mlg[0]
     cantidad_granja=mlg[1]
     menos_salidor_granja=mlg[2]
     cantidad_menor_granja=mlg[3]
     salidor_granja=int(salidor_granja)
     cantidad_granja=int(cantidad_granja)
     menos_salidor_granja=int(menos_salidor_granja)
     cantidad_menor_granja=int(menos_salidor_granja)
     
     
        
     datos=datos_excel()
     dato1=datos[0]
     dato2=datos[1]    
     if dato1==38:
          nombre_dato1='Ballena'
          dato1='00'          
     elif dato1==37:
          nombre_dato1='Delfin'
          dato1=0         
     else:
          nombre_dato1=capture_nombre(dato1)
     
     if dato2==38:
          nombre_dato2='Ballena'
          dato2='00'
          
     elif dato2==37:
          nombre_dato2='Delfin'
          dato2==0
          
     else:
          nombre_dato2=capture_nombre(dato2)
          
     
   
     
     
     
     nombres_loto=[] 
     contador_nombresloto=0
     while contador_nombresloto!=a1:          
          nombre_temp='' 
          if  ((y[contador_nombresloto])=='00'):               
               nombre_temp="Ballena"
          else:                        
               nombre_temp=capture_nombre(y[contador_nombresloto])          
          contador_nombresloto=contador_nombresloto + 1
          nombres_loto.append(nombre_temp)
     
     anombreloto=0
     while anombreloto<12:                    
          if anombreloto>a1:
               nombres_loto.append('')
          anombreloto=anombreloto+1
     # print(nombres_loto)
     
     
     
     nombre_granja=[]
     contador_nombresgranja=0
     while contador_nombresgranja!=a1g:          
          nombre_temp=''
          
          if  ((z[contador_nombresgranja])=='00'):
               
               nombre_temp="Ballena"
          else:               
               nombre_temp=capture_nombre(z[contador_nombresgranja])          
          contador_nombresgranja=contador_nombresgranja + 1
          nombre_granja.append(nombre_temp)
          
     anombregranja=0
     while anombregranja<13:          
          if anombregranja>a1g:
               nombre_granja.append('')
          anombregranja=anombregranja+1
     
         
     nombre_salidor_loto=capture_nombre(salidor_loto)
     nombre_salidor_granja=capture_nombre(salidor_granja)
     nombre_menor_salidor_lotto= capture_nombre(menos_salidor_loto)
     nombre_menor_salidor_granja= capture_nombre(menos_salidor_granja)
     
         
              
         
  
     a=x[0]
     b=x[1]
     c=x[2]
     l9=y[0]
     l10=y[1]
     l11=y[2]
     
     l12=y[3]
     l13=y[4]
     l14=y[5]
     l15=y[6]
     l16=y[7]
     l17=y[8]
     l18=y[9]
     l19=y[10]
     
     z8=z[0]
     z9=z[1]
     z10=z[2]
     
     z11=z[3]
     z12=z[4]
     z13=z[5]
     z14=z[6]
     z15=z[7]
     z16=z[8]
     z17=z[9]
     z18=z[10]
     z19=z[11]
     nloto9=nombres_loto[0]
     nloto10=nombres_loto[1]
     nloto11=nombres_loto[2]
     nloto12=nombres_loto[3]
     nloto13=nombres_loto[4]
     nloto14=nombres_loto[5]
     nloto15=nombres_loto[6]
     nloto16=nombres_loto[7]
     nloto17=nombres_loto[8]
     nloto18=nombres_loto[9]
     nloto19=nombres_loto[10]
     
     ngranja8=nombre_granja[0]
     ngranja9=nombre_granja[1]
     ngranja10=nombre_granja[2]
     ngranja11=nombre_granja[3]
     ngranja12=nombre_granja[4]
     ngranja13=nombre_granja[5]
     ngranja14=nombre_granja[6]
     ngranja15=nombre_granja[7]
     ngranja16=nombre_granja[8]
     ngranja17=nombre_granja[9]
     ngranja18=nombre_granja[10]
     ngranja19=nombre_granja[11] 
     
     acierto1=aciertos(dato1,dato2)
     acierto=acierto1
     acumulador_indicaciones1=open("acumulador_indicaciones_semana.txt","r")
     acumulador_indicaciones=acumulador_indicaciones1.read()
     acumulador_indicaciones1.close()
     indicaciones=int(acumulador_indicaciones)     
     if acierto1==0:
          efectividad=0
     else:
          efectividad=(acierto1*100)/indicaciones
          efectividad=format(efectividad,'.2f')
     
               
          
          
          
   
          
     
     
     
     
        
     
     context={'valordolar':a, 'valoreuro':b, 'fecha': c, 
              'loto9':l9,'loto10':l10,'loto11':l11,'loto12':l12,
              'loto13':l13,'loto14':l14, 'loto15':l15,'loto16':l16, 'loto17':l17,'loto18':l18,
              'loto19':l19, 'granja8':z8,'granja9':z9, 'granja10':z10, 'granja11':z11, 'granja12':z12,
              'granja13':z13,
              'granja14':z14, 'granja15':z15, 'granja16':z16, 'granja17':z17, 'granja18':z18, 
              'granja19':z19 , 'nombre_loto9':nloto9,
              'nombre_loto10':nloto10, 'nombre_loto11':nloto11, 'nombre_loto12':nloto12, 
              'nombre_loto13':nloto13, 'nombre_loto14':nloto14,
              'nombre_loto15':nloto15, 'nombre_loto16':nloto16, 'nombre_loto17':nloto17, 
              'nombre_loto18':nloto18, 'nombre_loto19':nloto19,
              'ngranja8': ngranja8, 'ngranja9': ngranja9, 'ngranja10': ngranja10, 'ngranja11': ngranja11,
              'ngranja12': ngranja12, 
              'ngranja13': ngranja13, 'ngranja14': ngranja14, 'ngranja15': ngranja15,'ngranja16': ngranja16, 
              'ngranja17': ngranja17, 'ngranja18': ngranja18, 'ngranja19': ngranja19,
              'salemasloto':salidor_loto, 'cantidadsalidorloto':cantidad_loto,
              'menorsalidorloto': menos_salidor_loto, 'mayorsalidorgranja': salidor_granja,
              'cantidad_menor_loto':cantidad_menor_loto,
              'cantidadmayorsalidorgranja':  cantidad_granja, 'menorsalidorgranja': menos_salidor_granja,
              'cantidadmenorsalidorgranja': cantidad_menor_granja,
              'nombresalidorloto':nombre_salidor_loto, 'nombresalidorgranja':nombre_salidor_granja,
              "nombre_menor_salidor_lotto":nombre_menor_salidor_lotto,
              "nombre_menor_salidor_granja":nombre_menor_salidor_granja,
              'dato1':dato1, 'dato2': dato2, 'nombre_dato1':nombre_dato1, 'nombre_dato2':nombre_dato2, 'acierto':acierto,
              'indicaciones': indicaciones, 'efectividad':efectividad}              
     return render (request, 'soporte.html', context)


