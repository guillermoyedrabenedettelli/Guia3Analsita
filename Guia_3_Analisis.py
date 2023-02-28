from matplotlib.pyplot import xticks
import pickle
import numpy as np
import pandas as pd


df = pd.read_pickle("gordo_Data.pkl")

respuestas = df[['Siempre', 'Casi siempre','Algunas veces','Casi nunca','Nunca']]

vector = []
x=0
for i in range(0,len(respuestas)):
    for j in range(0,len(respuestas.iloc[i])):
        if respuestas.iloc[i][j] == 1:
            x+=1
            print(x)
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
      print(max_)
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
      print(max_)
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
Csum

print("Calificación final del cuestionario")
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

tabla3 = pd.read_csv("Tabla3_Guia3.csv", encoding= 'ISO-8859-1', low_memory=False)
itemTabla3Sums=[[2],[1],[3],[4, 9],[5, 6],[7,8],[41,42,43],[10, 11],[12,13],[20, 21, 22],[18, 19],[26, 27],[14,15],[16],[17],[23,24,25],[28,29],[30,31,32],[44,45,46],[33, 34, 35, 36, 37, 38, 39, 40]]

sumaitems = []
for i in range(len(itemTabla3Sums)):
    total = 0
    for j in range(len(itemTabla3Sums[i])):
        total += respuetasnumericas[itemTabla3Sums[i][j]-1]
        #print(total)
    sumaitems.append(total)

tabla3["Item"]=sumaitems

print(tabla3)
tabla3.to_csv("Resultados_Tabla_3_Prueba.csv")