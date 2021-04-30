"""
nombre: Carlos Daniel Agamez
código: T00059006
aaunto: caso de estudio hato ganadero 
"""
import random

# deckaramos listas 
nombres=[]
sexo=[]
p_inicial=[]
p_final=[]


# variables --------------
  # peso inciala y final de los machos promedio
sum_pi_m=0
sum_pf_m=0
can_m=0
  # peso incial y final de las hembras promesio
sum_pi_h=0
sum_pf_h=0
can_h=0
#--------------------++++
# datos a utilizar para la entrada 
  # identicadores para los nombres 
names_options=["A","B","C","D","E","F","G","H","I","J","K","M","P","R","S","U","T","Z","Y","W","Q","X","Y","O","LL"]

print("{:^59}".format("datos generales del estudio"))
print("\n ","-"*59)
print("{:^14} {:^14} {:^14} {:^14}".format("nombre","sexo","peso inicial","peso final")) 
print("\n ","-"*59)
for i in range(25):
  # se añaden los datos aleatoriamente
  e_nom=random.choice(names_options)
  nombres.append(e_nom)
  names_options.remove(e_nom)
  # solicitud del sexo 
  e_s=random.randint(1,2)
  sexo.append(e_s)
  # solicitud del oeso inicial 
  e_pi=random.randint(170,190)
  p_inicial.append(e_pi)
  # solicitud del peso final
  e_pf=random.randint(460,500)
  p_final.append(e_pf)
  
  # vamos impriminedo los datos 
  print("{:^14} {:^14} {:^14} {:^14}".format(nombres[i],sexo[i],p_inicial[i],p_final[i]))
  
  # calculamos los ptomedio de los peaos 
  if sexo[i]==1:# evaluamos para los machos
    sum_pi_m+=e_pi
    sum_pf_m+=e_pf
    can_m+=1
    
  elif sexo[i]==2: # evaluamos para las hembras 
    sum_pi_h+=e_pi
    sum_pf_h+=e_pf
    can_h+=1
    
# promedios resultados
  # promedio de peso incial de los machos 
prom_pi_m=sum_pi_m/can_m
prom_pi_m=round(prom_pi_m,2)
  # promedio de peso final de los machos
prom_pf_m=sum_pf_m/can_m
prom_pf_m=round(prom_pf_m,2)
   # promedio de peso incial de las hembras
prom_pi_h=sum_pi_h/can_h
prom_pi_h=round(prom_pi_h,2)
  # promedio de peso final de las hembras
prom_pf_h=sum_pf_h/can_h
prom_pf_h=round(prom_pf_h,2)

# sacamos promedioa totales
prom_t_pi=(sum_pi_h+sum_pi_m)/25 #promedio peso inicial
prom_t_pi=round(prom_t_pi,2)

prom_t_pf=(sum_pf_h+sum_pf_m)/25 # promedio peso final
prom_t_pf=round(prom_t_pf,2)

print("\n ","-"*59)

# imprimimoa los promedios en tablas 
print(" punto 1")
print("promedios")

# machos 
print(" ","-"*26)
print(" {:^29}".format("machos"))
print()
print(" {:^14} {:^14}".format("peso inicila","peso final"))
print()
print(" {:^14} {:^14}".format(prom_pi_m,prom_pf_m))
print(" ","-"*26)

# hembras
print("\n ","-"*26)
print(" {:^29}".format("hembras"))
print()
print(" {:^14} {:^14}".format("peso inicila","peso final"))
print()
print(" {:^14} {:^14}".format(prom_pi_h,prom_pf_h))
print(" ","-"*26)

# totales
print("\n ","-"*26)
print(" {:^29}".format("total"))
print()
print(" {:^14} {:^14}".format("peso inicila","peso final"))
print()
print(" {:^14} {:^14}".format(prom_t_pi,prom_t_pf))
print(" ","-"*26)

# reces con peaos inferiores al promedio general del lote
names_men_p=[]# aqui alamcenos sus nombres
pf_men_p=[]# aqui alamcenos au peso final 

# deckaramos una lista q añmacenara los porcentajes de aumento de peso de laa reces
aumentos=[]
may_aum=0 # deckaramos variable para almacenar el mayor porcentaje de aumento 
terneros_pf_may=0
for i in range(25):
  # calculamos aumentos
  aux=p_final[i] - p_inicial[i]
  aum_p=(aux/p_inicial[i])*100
  aum_p=round(aum_p,2)
  aumentos.append(aum_p)
  # buscamos el mayor aumento con if 
  if aumentos[i]>may_aum:
    # vamos guatdando los datos de la res con mayor aumneto de peso 
    may_aum=aumentos[i]
    nom_aum=nombres[i]
    pi_aum=p_inicial[i]
    pf_aum=p_final[i]
   
   # sacamos las reces que no superaron el promedio del peso final  
  if p_final[i]<prom_t_pf:
    # vamos añadiendo los mombres y pesos finales a las listas anteriormente declaradas 
    names_men_p.append(nombres[i])
    pf_men_p.append(p_final[i])
  
  # sacamos el porcentaje de efectividad del mwtodo  utilizado en los terneros 
  if p_final[i]>=480:
    terneros_pf_may+=1
    
# sacamos porcentaje de efectividad del metodo
por_efc_met=(terneros_pf_may*100)/25   

print("\n punto 2\n aquellas reces que no siperaron el promedio general del peso finao fueron") 
print("\n ","-"*26)
print(" {:^14} {:^14}".format("nombre","peso final"))
print()
for i in range(len(pf_men_p)):
  print(" {:^14} {:^14}".format(names_men_p[i],pf_men_p[i]))
print(" ","-"*26)

print("\n punto 3\n la res con mauor porcentaje de aumento")
print("\n ","-"*59)
print(" {:^14} {:^14} {:^14} {:^14}".format("nombre","peso inicial","peso final","% aumento"))
print()
print(" {:^14} {:^14} {:^14} {:^14}".format(nom_aum,pi_aum,pf_aum,may_aum))
print(" ","-"*59)

print("\n punto 4\nEL METODO TUVO UNA EFECTIVIDAD DEL:",por_efc_met,"%")
