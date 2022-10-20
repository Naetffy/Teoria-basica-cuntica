import LibreriaComp as LC

def main():
    print("OPCIONES:")
    print("1.calcular la probabilidad de encontrarlo en una posición en particular.")
    print("2.vector Ket debe buscar la probabilidad de transitar del primer vector al segundo.")
    op = int(input("Dame la opcion: "))
    if op==1:
        posiciones = int(input("Dame el numero de posciones donde puede estar la particula: "))
        quet = []
        for i in range(posiciones):
            Rp = int(input("Dame la parte real que representa la posibilidad de que la particula este en esa posicion: "))
            Ip = int(input("Dame la parte imaginaria que representa la posibilidad de que la particula este en esa posicion: "))
            quet.append((Rp,Ip))
        pos = int(input("Dame la posicion para calcular la probabilidad: "))
        print(LC.prob(quet,pos))
    elif op==2:
        posiciones = int(input("Dame el numero de posciones donde puede estar la particula: "))
        quet = []
        for i in range(posiciones):
            Rp = int(input("Dame la parte real que representa la posibilidad de que la particula este en esa posicion: "))
            Ip = int(input("Dame la parte imaginaria que representa la posibilidad de que la particula este en esa posicion: "))
            quet.append((Rp,Ip))
        posiciones1 = int(input("Dame el numero de posciones donde puede estar la particula: "))
        quet1 = []
        for i in range(posiciones):
            Rp = int(input("Dame la parte real que representa la posibilidad de que la particula este en esa posicion: "))
            Ip = int(input("Dame la parte imaginaria que representa la posibilidad de que la particula este en esa posicion: "))
            quet1.append((Rp,Ip))
        print(LC.protrans(quet,quet1))
main()