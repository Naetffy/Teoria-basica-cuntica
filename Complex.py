import math

def sum(NUM1,NUM2):
    res = (NUM1[0]+NUM2[0],NUM1[1]+NUM2[1])
    return res

def res(NUM1,NUM2):
    res = (NUM1[0]-NUM2[0],NUM1[1]-NUM2[1])
    return res

def pro(NUM1,NUM2):
    res = (NUM1[0]*NUM2[0]-NUM1[1]*NUM2[1],NUM1[0]*NUM2[1]+NUM2[0]*NUM1[1])
    return res

def div(NUM1,NUM2):
    res = ((((NUM1[0]*NUM2[0])+(NUM1[1]*NUM2[1]))/(NUM2[0]**2+NUM2[1]**2)),(((NUM2[0]*NUM1[1])-(NUM1[0]*NUM2[1]))/(NUM2[0]**2+NUM2[1]**2)))
    return res

def mod(NUM1):
    res = math.sqrt(NUM1[0]**2+NUM1[1]**2)
    return res

def conj(NUM1):
    res = (NUM1[0],(-1)*NUM1[1])
    return res

def ctop(NUM1):
    res = (round(math.sqrt(NUM1[0]**2+NUM1[1]**2),2),round(math.atan(NUM1[1]/NUM1[0])*180/math.pi,2))
    return res

def fase(NUM1):
    res = round(math.atan(NUM1[1]/NUM1[0])*180/math.pi,2)
    return "{}°".format(res)
