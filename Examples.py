import LibreriaComp as Lib

pri = Lib.prob([(-3,-1),(0,-2),(0,1),(2,0)],2)

nor = Lib.normalize([(2,-3),(1,2)])

trasnp = Lib.trans([(0,1),(1,0)],[(1,0),(0,-1)])

ptrasnp = Lib.protrans([(0,1),(1,0)],[(1,0),(0,-1)])

ExpectedVal = Lib.media([[(1,0),(0,-1)],[(0,1),(2,0)]],[(0.707106,0),(0,0.707106)])

Delta = Lib.delta([[(1,0),(0,-1)],[(0,1),(2,0)]],[(0.707106,0),(0,0.707106)])

Var = Lib.varince([[(1,0),(0,-1)],[(0,1),(2,0)]],[(0.707106,0),(0,0.707106)])

Valoresp = Lib.valp([[(-1,0),(0,-1)],[(0,1),(1,0)]])

Vectoresp = Lib.vecp([[(-1,0),(0,-1)],[(0,1),(1,0)]])

tranvp = Lib.transvp(Vectoresp,[(0.5,0),(0.5,0)])

probvp = Lib.protravp(Vectoresp,[(0.5,0),(0.5,0)])

Laste = Lib.QuantSys([1,0,0,0],[[(0,0),(0.707,0),(0.707,0),(0,0)],[(0,0.707),(0,0),(0,0),(0.707,0)],[(0.707,0),(0,0),(0,0),(0,0.707)],[(0,0),(0.707,0),(-0.707,0),(0,0)]],3)

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
print(Laste)