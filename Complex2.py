import math
import Complex as Bas;

def SumV(Data1,Data2):
    res=[]
    if len(Data1)==len(Data2):
        for i in range(len(Data1)):
            res.append(Bas.sum(Data1[i],Data2[i]))
        return res
    else: return res

def InvV(Data1):
    res=[]
    for i in range(len(Data1)):
        res.append(Bas.pro(Data1[i],(-1,0)))
    return res

def eVec(Escalar,Data1):
    res=[]
    for i in range(len(Data1)):
        res.append(Bas.pro(Data1[i],Escalar))
    return res

def SumM(Data1,Data2):
    res=[]
    if len(Data1)==len(Data2) and len(Data1[0])==len(Data2[0]):
        for i in range(len(Data1)):
            columna=[]
            for j in range(len(Data1[i])):
                columna.append(Bas.sum(Data1[i][j],Data2[i][j]))
            res.append(columna)
        return res
    else: return res

def ResM(Data1,Data2):
    res=[]
    if len(Data1)==len(Data2) and len(Data1[0])==len(Data2[0]):
        for i in range(len(Data1)):
            columna=[]
            for j in range(len(Data1[i])):
                columna.append(Bas.res(Data1[i][j],Data2[i][j]))
            res.append(columna)
        return res
    else: return res

def InvM(Data1):
    res=[]
    for i in range(len(Data1)):
        columna=[]
        for j in range(len(Data1[i])):
            columna.append(Bas.pro(Data1[i][j],(-1,0)))
        res.append(columna)
    return res

def eMat(Escalar,Data1):
    res=[]
    for i in range(len(Data1)):
        columna=[]
        for j in range(len(Data1[i])):
            columna.append(Bas.pro(Data1[i][j],Escalar))
        res.append(columna)
    return res

def Tra(Data1):
    res=[]
    for i in range(len(Data1)):
        columna=[]
        for j in range(len(Data1[i])):
            columna.append(Data1[j][i])
        res.append(columna)
    return res

def ConjM(Data1):
    res=[]
    for i in range(len(Data1)):
        columna=[]
        for j in range(len(Data1[i])):
            columna.append(Bas.conj(Data1[i][j]))
        res.append(columna)
    return res

def AdjM(Data1):
    res = []
    for i in range(len(Data1)):
        columna = []
        for j in range(len(Data1[i])):
            columna.append(Bas.conj(Data1[j][i]))
        res.append(columna)
    return res

def AdjV(Data1):
    res = []
    for i in range(len(Data1)):
        res.append(Bas.conj(Data1[i]))
    return res

def MulM(Data1,Data2):
    Matriz = []
    for i in range(len(Data1)):
        Fila = []
        for j in range(len(Data2[0])):
            Rp = 0
            Ip = 0
            for k in range(len(Data1[0])):
                Rp += Bas.pro(Data1[i][k],Data2[k][j])[0]
                Ip += Bas.pro(Data1[i][k],Data2[k][j])[1]
            Fila.append((Rp,Ip))
        Matriz.append(Fila)
    return Matriz

def AcMV(Data1,Data2):
    res=[]
    for i in range(len(Data1)):
        Rp = 0
        Ip = 0
        for k in range(len(Data2)):
            Rp += Bas.pro(Data1[i][k],Data2[k])[0]
            Ip += Bas.pro(Data1[i][k],Data2[k])[1]
        res.append((Rp,Ip))
    return res

def PriV(Data1,Data2):
    Data1 = AdjV(Data1)
    Rp = 0
    Ip = 0
    for i in range(len(Data1)):
        Rp += Bas.pro(Data1[i],Data2[i])[0]
        Ip += Bas.pro(Data1[i],Data2[i])[1]
    return (Rp,Ip)

def NorV(Data1):
    res=0
    for i in range(len(Data1)):
        res += Data1[i][0]**2+Data1[i][1]**2
    return math.sqrt(res)

def DisV(Data1,Data2):
    res = []
    for i in range(len(Data1)):
        res.append(Bas.res(Data1[i],Data2[i]))
    d = 0
    for j in range(len(res)):
        d += Bas.mod(res[j])
    return d

def Unit(Data1):
    res = AdjM(Data1)
    Un = []
    for i in range(len(Data1)):
        col1 = []
        for j in range (len(Data1[i])):
            if i == j:
                col1.append((1,0))
            else: 
                col1.append((0,0))
        Un.append(col1)
    res = MulM(res,Data1)
    if res == Un:return True
    else:return False

def Herm(Data1):
    res = AdjM(Data1)
    if(res==Data1):return True
    else:return False
    
def Prot(Data1,Data2):
    res=[]
    if(type(Data1[0])==list):
        for i in Data1:
            for j in i:
                if (type(Data2[0])==list):
                    res.append(eMat(j,Data2))
                else:
                    res.append(eVec(j,Data2))
    else:
        for i in Data1:
            if (type(Data2[0])==list):
                res.append(eMat(i,Data2))
            else:
                res.append(eVec(i,Data2))
    return res
