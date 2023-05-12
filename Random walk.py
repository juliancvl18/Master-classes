
import random
import matplotlib.pyplot as plt

#Fuente de letra Times
plt.rcParams["font.family"] = "Times New Roman"

#Función de random walk
def random_walk(steps, Z0, p):
    #Se inicia el random walk con la posición inicial definida 
    Z = Z0
    walk = [Z0]
    #Iteraciones por el número de time steps definido
    for i in range(1, steps):
        #Si el núm. aleatorio es mayor a p, entonces...
        if random.random() > p:
            #moverse hacia arriba según p 
            Z += p
        else:
            #si es menor a p, entonces mover hacia abajo según p
            Z -= p
            #Añade la nueva posición a variable Walk
        walk.append(Z)
        #Regresa a la lista de la variable walk
    return walk

#Definir número de pasos, posición inicial y probabilidad del paso
steps = 300
Z0 = 0.5
p = 0.5

#Cálculo de dos walks a partir de la misma función con fines comparativos
walk_1 = random_walk(steps, Z0, p)
walk_2 = random_walk(steps, Z0, p)

#Graficación de los walks
plt.plot(walk_1, color= "black" , label="One horn")
plt.plot(walk_2, color= "red" , label="Two horns")
plt.title("Evolution of allele frequency over time")
plt.xlabel("Time (Generations)")
plt.ylabel("Frequency")
plt.legend()
plt.show()
#%%%%

plt.plot(walk_1, color= "black" , label="Brown color")
plt.plot(walk_2, color= "red" , label="Green color")
plt.title("Evolution of allele frequency over time")
plt.xlabel("Time (Generations)")
plt.ylabel("Frequency")
plt.legend()
plt.show()
