
import  tkinter as tk
from tkinter import filedialog 
import numpy as np
import pandas as pd

def rendimiento(sumaitem_,bajo,medio,alto):
  r="fuera de rango"
  #for i in range(len(sumaitem_)):
  if sumaitem_ <= bajo[0]:
    print("Despreciable"+" "+ str(sumaitem_))
    r="Despreciable"
  elif sumaitem_ >=bajo[0] and sumaitem_ <= bajo[1]:
    print("Bajo"+" "+ str(sumaitem_))
    r="Bajo"
  elif sumaitem_ >=medio[0] and sumaitem_ <= medio[1]:
    print("Medio"+" "+ str(sumaitem_))
    r="Medio"
  elif sumaitem_ >=alto[0] and sumaitem_ <=alto[1]:
    print("Alto"+" "+ str(sumaitem_))
    r="Alto"
  elif sumaitem_ >= alto[1]:
    print("Muy Alto"+" "+ str(sumaitem_))
    r="Muy Alto"
  else:
    print(sumaitem_)
  return r

rangos_Dominio = [[[5,  9],[9, 11],[11,14]],
                  [[5,  9],[9, 11],[11,14]],
                  [[5,  9],[9, 11],[11,14]],
                  [[15,21],[21,27],[27,37]],
                  [[15,21],[21,27],[27,37]],
                  [[15,21],[21,27],[27,37]],
                  [[15,21],[21,27],[27,37]],
                  [[15,21],[21,27],[27,37]],
                  [[15,21],[21,27],[27,37]],
                  [[11,16],[16,21],[21,25]],
                  [[11,16],[16,21],[21,25]],
                  [[11,16],[16,21],[21,25]],
                  [[11,16],[16,21],[21,25]],
                  [[1,  2],[2,  4],[4,  6]],
                  [[4,  6],[6,  8],[8, 10]],
                  [[4,  6],[6,  8],[8, 10]],
                  [[9, 12],[12,16],[16,20]],
                  [[9, 12],[12,16],[16,20]],
                  [[10,13],[13,17],[17,21]],
                  [[10,13],[13,17],[17,21]],
                  [[7, 10],[10,13],[13,16]],
                  [[6, 10],[10,14],[14,18]],
                  [[6, 10],[10,14],[14,18]],
                  [[4,  6],[6,  8],[8, 10]],
                  [[4,  6],[6,  8],[8, 10]]]



resultadosPorCategoria=[[[5,  9],[9, 11],[11,14]],
                        [[5,  9],[9, 11],[11,14]],
                        [[5,  9],[9, 11],[11,14]],
                        [[15,30],[30,45],[45,60]],
                        [[15,30],[30,45],[45,60]],
                        [[15,30],[30,45],[45,60]],
                        [[15,30],[30,45],[45,60]],
                        [[15,30],[30,45],[45,60]],
                        [[15,30],[30,45],[45,60]],
                        [[15,30],[30,45],[45,60]],
                        [[15,30],[30,45],[45,60]],
                        [[15,30],[30,45],[45,60]],
                        [[15,30],[30,45],[45,60]],
                        [[5,  7],[7, 10],[10,13]],
                        [[5,  7],[7, 10],[10,13]],
                        [[5,  7],[7, 10],[10,13]],
                        [[14,29],[29,42],[42,58]],
                        [[14,29],[29,42],[42,58]],
                        [[14,29],[29,42],[42,58]],
                        [[14,29],[29,42],[42,58]],
                        [[14,29],[29,42],[42,58]],
                        [[10,14],[14,18],[18,23]],
                        [[10,14],[14,18],[18,23]],
                        [[10,14],[14,18],[18,23]],
                        [[10,14],[14,18],[18,23]]]


#####################################
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
df = pd.read_pickle(file_path)

respuestas = df[['Siempre', 'Casi siempre','Algunas veces','Casi nunca','Nunca']]

vector = []
x=0
for i in range(0,len(respuestas)):
    for j in range(0,len(respuestas.iloc[i])):
        if respuestas.iloc[i][j] == 1:
            x+=1
            #print(x)
            vector.append(j+1)
            break

itemsNormals=[1, 4, 23, 24, 25, 26, 27, 28, 30, 31,32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42,43, 44, 45, 46, 47, 48, 49,50, 51, 52, 53, 55, 56, 57]
itemsInvert=[2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,16, 17, 18, 19, 20, 21, 22, 29, 54, 58,59, 60, 61, 62, 63, 64, 65,66, 67, 68, 69, 70, 71, 72]
for i in range(len(itemsNormals)):
  itemsNormals[i] = itemsNormals[i]-1
for i in range(len(itemsInvert)):
  itemsInvert[i] = itemsInvert[i]-1

respuetasnumericas= np.zeros(len(vector),dtype=int)
b= vector
max_=0
for i in range(len(itemsNormals)):
    if itemsInvert[i] >= len(b):
      max_=i
      #print(max_)
      break

for i in range(len(itemsNormals)):
  if b[itemsNormals[i]] == 1:
    respuetasnumericas[itemsNormals[i]]=0
  elif b[itemsNormals[i]] ==2:
    respuetasnumericas[itemsNormals[i]]=1
  elif b[itemsNormals[i]] == 3:
    respuetasnumericas[itemsNormals[i]] = 2
  elif b[itemsNormals[i]] == 4:
    respuetasnumericas[itemsNormals[i]] = 3
  elif b[itemsNormals[i]] == 5:
    respuetasnumericas[itemsNormals[i]] = 4

print(respuetasnumericas)

max_=0
for i in range(len(itemsInvert)):
    if itemsInvert[i] >= len(b):
      max_=i
      #print(max_)
      break

for i in range(max_):
  if b[itemsInvert[i]] == 1:
    respuetasnumericas[itemsInvert[i]]=4
  elif b[itemsInvert[i]] ==2:
    respuetasnumericas[itemsInvert[i]]=3
  elif b[itemsInvert[i]] == 3:
    respuetasnumericas[itemsInvert[i]] = 2
  elif b[itemsInvert[i]] == 4:
    respuetasnumericas[itemsInvert[i]] = 1
  elif b[itemsInvert[i]] == 5:
    respuetasnumericas[itemsInvert[i]] = 0

print(respuetasnumericas)

Csum=0
for i in range(len(respuetasnumericas)):
    Csum += respuetasnumericas[i]


print("Calificaci??n final del cuestionario")
if Csum <= 50:
  print("Despreciable"+" "+ str(Csum))
elif Csum >50 and Csum <= 75:
  print("Bajo"+" "+ str(Csum))
elif Csum >75 and Csum <= 99:
  print("Medio"+" "+ str(Csum))
elif Csum >99 and Csum <=140:
  print("Alto"+" "+ str(Csum))
elif Csum >140:
  print("Muy Alto"+" "+ str(Csum))

analisis = df.iloc[:,:0].assign(Respuestas = list(respuetasnumericas))

print(analisis)
analisis.to_csv("Respuesta_Analisis_Prueba.csv")

tabla3 = pd.read_csv("Templates/Tabla3_Guia3.csv", encoding= 'ISO-8859-1', low_memory=False)
#itemTabla2Sums=[[2],[1],[3],[4, 9],[5, 6],[7,8],[41,42,43],[10, 11],[12,13],[20, 21, 22],[18, 19],[26, 27],[14,15],[16],[17],[23,24,25],[28,29],[30,31,32],[44,45,46],[33, 34, 35, 36, 37, 38, 39, 40]]
itemTabla3Sums = [[1,3],[2,4],[5],[6,12],[7,8],[9,10,11],[65,66,67,68],[13,14],[15,16],[25,26,27,28],[23, 24],[29, 30],[35, 36],[17, 18],[19, 20],[21, 22],[31, 32, 33, 34],[37, 38, 39, 40, 41],[42, 43, 44, 45, 46],[69, 70, 71, 72],[57, 58, 59, 60, 61, 62,63, 64],[47, 48],[49, 50, 51, 52],[55, 56],[53, 54]]

sumaitems = []

for i in range(len(itemTabla3Sums)):
    total = 0
    for j in range(len(itemTabla3Sums[i])):
        
        if (itemTabla3Sums[i][j]-1) > len(analisis)-1:
            
            total=0
        else:
            #print(itemTabla3Sums[i][j]-1)
            total = total+ respuetasnumericas[itemTabla3Sums[i][j]-1]
    #print(total)        
    sumaitems.append(total)

tabla3["Resultados de dimenciones"]=sumaitems
print(tabla3)

resultados_dominios=[]
resultados_competencias=[]
for i in range(len(sumaitems)):
    resultados_dominios.append(rendimiento(sumaitems[i],rangos_Dominio[i][0],rangos_Dominio[i][1],rangos_Dominio[i][2]))

tabla3["Resultados Dominios"]=resultados_dominios
print(tabla3)

indices_Categoria=[[0,2],[3,12],[13,15],[16,20],[20,24]]
for i in range(len(indices_Categoria)):
    sumaCategoria=0
    for j in range(indices_Categoria[i][0],indices_Categoria[i][1]+1):
        #print(j)
        sumaCategoria += sumaitems[j]
    resultados_competencias.append(sumaCategoria)

rango_Competencias = []
for i in range (len(resultados_competencias)):
    rango_Competencias.append(rendimiento(resultados_competencias[i],resultadosPorCategoria[i][0],resultadosPorCategoria[i][1],resultadosPorCategoria[i][2]))  
print(rango_Competencias)  

categoriaResultados=pd.read_csv("Templates/Tabla3_Guia3_Categoria.csv")
categoriaResultados["Resultados Categorias"]=rango_Competencias

print(categoriaResultados)


categoriaResultados.to_csv("Resultados_de_Categoria.csv")
tabla3.to_csv("Resultados_Tabla_3_.csv")