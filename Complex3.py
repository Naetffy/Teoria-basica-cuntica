import Complex2 as CP
import Complex as CPb
from sympy import *

def comp(num):
    return complex(num[0],num[1])

def descomp(num):
    return (complex(num).real,complex(num).imag)

def prob(Data1,pos):
    res = CPb.mod(Data1[pos])/(CP.NorV(Data1))**2
    return round(res,2)

def normalize(Data1):
    res = Data1
    norm = CP.NorV(Data1)
    for i in range(len(Data1)):
        res[i] = (round(res[i][0]/norm,4),round(res[i][1]/norm,4))
    return res

def trans(Data1,Data2):
    Data1 = normalize(Data1)
    Data2 = normalize(Data2)
    res = CP.PriV(Data1,Data2)
    return res

def protrans(Data1,Data2):
    Data1 = normalize(Data1)
    Data2 = normalize(Data2)
    res = CP.PriV(Data1,Data2)
    res = CPb.mod(res)**2
    return round(res,2)

def media(Omega, quet):
    if len(Omega)==len(Omega[0]):
        OmegaQ = CP.AcMV(Omega,quet)
        ExpVal = CP.PriV(OmegaQ,quet)
        return round(ExpVal[0],2)
    else:
        return "Matriz invalida"

def delta(Omega,quet):
    if len(Omega)==len(Omega[0]):
        OmegaQ = CP.AcMV(Omega,quet)
        ExpVal = CP.PriV(OmegaQ,quet)
        ExpVal = round(ExpVal[0],2)
        Ident = []
        for i in range(len(Omega)):
            Fila = []
            for j in range(len(Omega)):
                if i==j:
                    Fila.append((1,0))
                else:
                    Fila.append((0,0))
            Ident.append(Fila)
        Ident = CP.eMat((ExpVal,0),Ident)
        return CP.ResM(Omega,Ident)
    else:
        return "Matriz invalida"

def varince(Omega,quet):
    if len(Omega)==len(Omega[0]):
        Delta = delta(Omega,quet)
        ProDelta = CP.MulM(Delta,Delta)
        Res = media(ProDelta,quet)
        return round(Res,2)
    else:
        return "Matriz invalida"

def valp(Matriz):
    for i in range(len(Matriz)):
        Matriz[i] = list(map(comp,Matriz[i]))
    Matriz = Matrix(Matriz)
    res = []
    for i in Matriz.eigenvals():
        res.append(i)
    return res

def vecp(Matriz):
    for i in range(len(Matriz)):
        Matriz[i] = list(map(comp,Matriz[i]))
    Matriz = Matrix(Matriz)
    res = []
    for i in Matriz.eigenvects():
        for j in i[2]:
            res.append(list(map(descomp,list(j))))
    return res

def transvp(vp,quet):
    res = []
    for i in vp:
        res.append(trans(i,quet))
    return res

def protravp(vp,quet):
    res = []
    for i in vp:
        res.append(round(CPb.mod(trans(i,quet))**2,2))
    return res

pri = prob([(-3,-1),(0,-2),(0,1),(2,0)],2)

nor = normalize([(2,-3),(1,2)])

trasnp = trans([(0,1),(1,0)],[(1,0),(0,-1)])

ptrasnp = protrans([(0,1),(1,0)],[(1,0),(0,-1)])

ExpectedVal = media([[(1,0),(0,-1)],[(0,1),(2,0)]],[(0.707106,0),(0,0.707106)])

Delta = delta([[(1,0),(0,-1)],[(0,1),(2,0)]],[(0.707106,0),(0,0.707106)])

Var = varince([[(1,0),(0,-1)],[(0,1),(2,0)]],[(0.707106,0),(0,0.707106)])

Valoresp = valp([[(-1,0),(0,-1)],[(0,1),(1,0)]])

Vectoresp = vecp([[(-1,0),(0,-1)],[(0,1),(1,0)]])

tranvp = transvp(Vectoresp,[(0.5,0),(0.5,0)])

probvp = protravp(Vectoresp,[(0.5,0),(0.5,0)])

print(pri)
print(nor)
print(trasnp)
print(ptrasnp)
print(ExpectedVal)
print(Delta)
print(Var)
print(Valoresp)
print(Vectoresp)
print(tranvp)
print(probvp)