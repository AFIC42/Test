#Efecto Talbot

from visual import *
from visual.graph import gdisplay, gdots


m = 1. #cte.
L = 1.e-3 #Frecuencia espacial de la red de difraccion en m
D = 10.*L #Longitud de la red en m
lamb = 520e-9 #Longitud de onda del verde en m

dx = L/30. #Paso

escena = gdisplay(height=500,width=500,
                  xmin=-0.5*D,xmax=0.5*D,ymin=-0.5*D,ymax=0.5*D)
puntos = []


def Intensidad(x,z):

    I = 0.25*(1.+2.*m*cos(pi*lamb*z/(L*L))*cos(2.*pi*x/L)
              +m*m*cos(2.*pi*x/L)**2)

    return I

j=0
for i in arange(-0.5*D,0.5*D,dx):

    puntos.append(gdots())

    puntos[j].radius=dx/2
    j+=1

j=0

#------------
#GRAFICACION
#------------

#Plano de observacion:

z=(2.*L*L/lamb)*1. #Primera auto-imagen

#(3.*L*L/lamb) --> Auto-imagen con desfase espacial pi

for x in arange(-0.5*D,0.5*D,dx):

    I = Intensidad(x,z)
    puntos[j].color=(0,I,0)
   
    for y in arange(-0.5*D,0.5*D,dx):

        puntos[j].plot(pos=(x,y))

    j+=1
    

# Un cambio

