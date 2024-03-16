def rainaverage(l):
    a=[]
    res=[]
    ret=[]
    for i in l:
        l3=i[0]
        a.append(l3)
    b=list(set(a))
    for y in b:
        cun=0
        sum=0
        result=0
        for z in l:
            if (y==z[0]):
                sum=sum+z[1]
                cun+=1
        result=sum/cun
        res.append(result)
    for j in range (len(b)):
        to = (b[j],res[j])
        ret.append(to)
    return (sorted(ret))

def listtype(l):
    return (type(l) == type([]))
def flatten(l):
    a=[]
    l2=[]
    def flat(l1):
        for i in l1:
            if (listtype(i) == True):
                flat(i)
            else:
                a.append(i)
        return a
    l2=flat(l)
    return (l2)
import ast

def parse(inp):
  inp = ast.literal_eval(inp)
  return (inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "rainaverage":
  arg = parse(farg)
  print(rainaverage(arg))

if fname == "flatten":
  arg = parse(farg)
  print(flatten(arg))

