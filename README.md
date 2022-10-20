PROGRAMA SIMULACIÓN TEORÍA CUÁNTICA BÁSICA, OBSERVABLES Y MEDIDAS
Esta libreria esta desarrollado en python que permite la simulacion de sistemas cuanticos.

Para empezar
Estas librerias desarrolladas para simulaciones de problemas que enrrollan la fisica cuantica, para su uso se debe tener en cuenta:

Prerequesitos:
1.Para el uso de la libreria es necesario tener instalado pyhton y configurado en la carpeta en la cual se quiere llamar a los experimentos.
2.Ser requiere tener instalada la libreria sympy.


Intalacion:
Para la instalacion de esta libreria se puede proceder de dos maneras.
    1.En la carpeta en la que se desea descargar la libreria hacer el uso de git y el comando git clone https://github.com/Naetffy/Teoria-basica-cuntica.git de forma que se obtiene de manera directa la descarga completa de todos los archivos del repositorio dentro de una carpeta llamada VectSpace, dentro de la cual esta la libreria.
    2.En GitHub hacer la instalacion del repositorio descargandolo como un ZIP y extrayendo este en la carpeta en la cual se quiere hacer el uso de la libreria, esto nos creara una carpeta con el nombre "Teoria-basica-cuntica-main", este lo cambiamos a "Teoria-basica-cuntica".

Implemetacion:
Este repositorio se puede trabajar de dos formas, como archivo py o como libreria.

Aclaracion: Todos los numero se tomaran como complejos de la forma (Parte real,Parte imaginaria)

Para usar como un programa .py es de la siguiente forma:

Ejecutar el Experimento(1).
El experimento 1 corresponde al experimento de las posciones y las particulas en el espacio, en este experimento hay dos opciones, la primera se le pide al usuario que digite el numero de posciones donde puede estar la particula y aprtir de esto se pide que se forme el vector ket posterior con una posicion le da la probabilidad de que la particula este en esa posicion, la segunda dados dos vectores ket nos da la probabilidad de transitar de uno  a otro.


Para usar como libreria en un proyecto es de la siguinte forma:
Para implementar la libreria en un proyecto se debe hacer el uso de la siguiente sintaxis import LibreriaComp, posteriormente se puede hacer el uso de cualquiera de las siguientes funciones:
    1.LibreriaComp.prob(Lista,Entero):Es una funcion que dado un vector ket calcula la probabilidad de que la particula se encuentre en una posicion
    Parmetros: como primer parametro recibe una lista que representa el vetor ket y el segundo parametro recibe la posicon donde queremos evaluar la poscion.
    Retorno: Esta funcion retorna un flotante que representa la probabilidad de que la particula se encuentre en dicha posicion

    2.LibreriaComp.protrans(Lista,Lista):Es una funcion que permite determinar la probabilidad de un vector ket de transitar a otro vector ket.
    Parmetros: Esta recibe como primer parametro la lista del vector ket y el segundo parametro es otro vector ket.
    Retorno: Esta funcion retorna un flotante que representa la probabilidad de que la particula se encuentre en dicha posicion

    3.LibreriaComp.media(Matriz,Lista):Es una funcion que calcula la media de una matriz y un vector ket.
    Parmetros: La matriz representa el observable  y es una lista de lista que debe ser cuadrada y hermitanea y el vector ket.
    Retorna: un entero que represnta la amplitud.
    
    4.LibreriaComp.varianza(Matriz,Lista):Es una funcion que calcula la media de una matriz y un vector ket.
    Parmetros: La matriz representa el observable  y es una lista de lista que debe ser cuadrada y hermitanea y el vector ket.
    Retorna: un entero que represnta la varianza.

    5.LibreriaComp.valp(Matriz):Es una funcion que dado una matriz una lista de listas calcula los valores propios.
    Parmetros: La matriz representa el observable  y es una lista de listas.
    Retorna: retorna todos los valores propios.

    6.LibreriaComp.vcp(Matriz):Es una funcion que dado una matriz una lista de listas calcula los vectores propios.
    Parmetros: La matriz representa el observable  y es una lista de listas.
    Retorna: retorna todos los vectores propios.
    
    7.LibreriaComp.QuantSys(Lista,Matriz,Entero):Es una funcion que con la dinamica del sitema calcula el estado final de la matriz
    Parmetros: Lista representa la posicion de la particula, la matriz representa la dinamica del sitema y el entero representa el tiempo.
    Retorna: la posicion final de la particula.
    
    Para ver un ejemplo del uso de la libreria ver Examples.py
Hecho con:
Math - Libreria que nos permite hacer operaciones matematicas como la raiz cuadrada.
matplotlib - Libreria que nos permite graficar informacion relevante del experimento.

Realizado por:
Mateo Sebastian Forero Fuentes
