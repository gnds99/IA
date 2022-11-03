import random
import math 

def mostrarPoblacion(arr = []): # FUNCION QUE MUESTRA LA POBLACION
    new_generation = arr[:]
    for i in range(len(new_generation)):
        print(new_generation[i])

def mostrarValores(arr = []): # FUNCION QUE MUESTRA LOS VALORES

    for i in range(len(arr)):
        for j in range(len(arr[i])-1):
            print(arr[i][j], " ", arr[i][j+1], " = ", f(arr[i][j], arr[i][j+1]))

# ESTA ES LA FUNCION DE ACTIVACIÓN (SE DEBE CAMBIAR SEGUN EL EJERCICIO)
def f(x,y):
    return x*y-x+y

def randomSelection(arr = []): # ASGINANDO POSICIONES PARA EL TORNEO
    copy_arr = arr[:]
    arr2 = []
    while(len(copy_arr) != 0):
        rnd = random.choice(copy_arr)
        arr2.append(rnd)
        indice = copy_arr.index(rnd)
        copy_arr.pop(indice)
    return arr2
    
def tournament(arr = []):  # FUNCION DE SELECCION POR TORNEO
    arr2 = arr[:] # COPIANDO EL ARREGLO
    mejores = [] # GUARDA A LOS MEJORES

    contador = 0

    while(len(arr2) != 0): # REALIZANDO EL TORNEO

        if(len(arr2) == 1): # EN CASO DE SER UNA POBLACION IMPAR 

            #print("IMPRIMIENDO LOS MEJORES TEMPORALES")
            #print(mejores)
            tempMejor = random.choice(mejores)
            #print("ELEMENTO REMOVIDO")
            #print(tempMejor)
            mejores.pop(mejores.index(tempMejor))

            mejores.append(arr2[0])
           # print("IMPRIMIENDO EL SOBRANTE")
          #  print(arr2[0])
            break


        else:
            opcion1 = arr2[0]
            opcion2 = arr2[1]
            # COMPARANDO LOS PRIMEROS DOS LUGARES DEL ARREGLO Y ALMACENANDO AL MAYOR
            mejores.append(opcion1 if f(arr2[contador][contador], arr2[contador][contador+1]) > f(arr2[contador+1][contador],arr2[contador+1][contador+1]) else opcion2)
            # REMOVIENDO LOS VALORES COMPARADOS
            arr2.pop(arr2.index(arr2[contador])) 
            arr2.pop(arr2.index(arr2[contador]))

  
   # print("MOSTRANDO LOS VALORES FINALES")
    return(mejores)

    #mostrarValores(arr)

def helper(arr = []): # SEGUNDO TORNEO (SE UTILIZA SI EN EL PRIMERO HUBO MAS DE DOS FINALISTAS)
    arr2 = arr[:] # COPIANDO EL ARREGLO ENVIADO
    mejores = [] # ALMACENA A LOS MEJORES DEL TORNEO
    contador = 0 

    opcion1 = arr2[contador]
    opcion2 = arr2[contador+1]

    # SELECIONANDO AL MENOR
    menor = opcion1 if f(arr2[contador][contador], arr2[contador][contador+1]) < f(arr2[contador+1][contador],arr2[contador+1][contador+1]) else opcion2

    mejores.append(menor) # APARTANDO AL MENOR
       
    if((menor in mejores) & (menor in arr2)): 
        arr2.pop(arr2.index(menor)) # REMOVIENDO AL MENOR

    mejores = arr2[:] # ALMACENANDO A LOS MEJORES
 
    return mejores # RETORNANDO A LOS MEJORES

def mutation(arr=[]): # FUNCIÓN DE MUTACION
    rnd = random.random() 
    condicional = 0.4 # PROBABILIDAD DE MUTACIÓN (CAMBIAR SI LO DESEAS)
    if(rnd >= condicional ):
        rnd2 = random.random() # LO DEJE EN 50 - 50 PARA SUMA O RESTA (CAMBIAR SI LO DESEAS)
        if(rnd2 >= 0.5 ):
            return math.ceil(arr+ rnd2*3)
        else:
            return math.floor(arr+ rnd2*7)
    else:
        return arr
        



def crossOver(arr = []):
    new_population = arr[:] # COPIANDO EL ARREGLO ENVIADO
    child1 = [mutation(arr[0][0]), mutation(arr[1][1])] # CREANDO EL PRIMER HIJO
    child2 = [mutation(arr[0][1]), mutation(arr[1][0])] # CREANDO EL SEGUNDO HIJO

    new_population.append(child1) # AGREGANDO AL PRIMER HIJO
    new_population.append(child2) # AGREGANDO AL SEGUNDO HIJO
    return new_population # RETORNANDO LA NUEVA GENERACIÓN
    


# n = numero de generaciones deseadas
# main (funcion principal)
def generation(n): # funcion para crear generaciones
        #population = [ [-1,4],[2,5],[0,3]] # funcionara para 3 -> 1 no funciona para tres
    population = [ [-1,4],[2,5],[0,3],[4,-3]] # funciona para 4 -> 2 *
        #population = [ [-1,4],[2,5],[0,3],[4,-3],[1,4]] # funciona para 5 -> 2 *
    
    # ESTA LA POBLACIÓN INICIAL
   # population = [ [-1,4],[2,5],[0,3],[4,-3],[1,4],[6,4]]  # funciona para 6 -> 3 -> 1
        #population = [ [-1,4],[2,5],[0,3],[4,-3],[1,4],[6,4], [3,1]] # funciona para 7 -> 3 -> 1
        #population = [ [-1,4],[2,5],[0,3],[4,-3],[1,4],[6,4], [3,1], [5,1]] # funciona para 8 -> 3 -> 1
        #population = [ [-1,4],[2,5],[0,3],[4,-3],[1,4],[6,4], [3,1], [5,1], [3,4]] # funciona para 9 -> 3 -> 1
    for i in range(n):

        print("########## GENERACIÓN ANTERIO ############")
        mostrarPoblacion(population) # MOSTRANDO LA POLBACIÓN INICIAL

        aleatorio = randomSelection(population) # RIFANDO LAS POSICIONES PARA EL TORNEO
        #print(aleatorio)
        mejores = tournament(aleatorio) # REALIZANDO SELECCION POR TORNEO
        
        if(len(mejores) != 2): # CONDICIONAL PARA ESTAR SEGURO QUE SOLO TENEMOS DOS ARREGLOS
            temp = mejores[:] # REALIZANDO COPIA
            mejores2 = helper(temp) # LLAMANDO A LA FUNCION HELPER PARA REALIZAR UN SEGUNDO TORNEO
            mejores = mejores2[:] # COPIANDO EL RESULTADO A LA VARIABLE ORIGINAL DE TORNEO
        #   print(mejores2)

        new_generation = crossOver(mejores) # CRUZANDO LOS VALORES 

        print("########## NUEVA GENERACION ############", i)
        mostrarPoblacion(new_generation) # MOSTRANDO LA NUEVA GENERACIÓN
        
        
        population = new_generation[:] # REEMPLAZANDO A LA GENERACION ANTERIOR

# FUNCION PRINCIPAL
def main():
    n = 100# NUMERO DE GENERACIONES DESEADAS
    generation(n)

main()
