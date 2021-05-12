class Fra:              #Fra is the shortage for Fraction
    def __init__(self,top=1,bottom=1):
        self.num = top
        self.den = bottom
        if bottom<=0:
            print("给爷爬")

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def gcd(m,n):
        while m%n!=0:
            oldm = m
            oldn = n
            m = oldn
            n = oldm%oldn
        return n
    
    def __add__(self,otherfra):
        newnum = self.num*otherfra.den+self.den*otherfra.num
        newden = self.den*otherfra.den
        common = Fra.gcd(newnum,newden)
        if newnum!=0:
            return Fra(newnum//common, newden//common)
        else:
            return 0

    def __sub__(self,otherfra):
        newnum = self.num*otherfra.den-self.den*otherfra.num
        newden = self.den*otherfra.den
        common = Fra.gcd(newnum,newden)
        if newnum!=0:
            return Fra(newnum//common, newden//common)
        else:
            return 0

    def __mul__(self,otherfra):
        newnum = self.num*otherfra.num
        newden = self.den*otherfra.den
        common = Fra.gcd(newnum,newden)
        if newnum!=1:
            return Fra(newnum//common, newden//common)
        else:
            return 1
    
    def __truediv__(self,otherfra):
        newnum = self.num*otherfra.den
        newden = self.den*otherfra.num
        common = Fra.gcd(newnum,newden)
        if newnum!=1:
            return Fra(newnum//common, newden//common)
        else:
            return 1    

    def __eq__(self,other):
        firstnum = self.num*other.den
        secondnum = self.den*other.num
        return firstnum==secondnum


class Vec:
    def __init__(self,lis):
        if type(lis)==list:
            self.detail = lis
            self.dimension = len(lis)
        else:
            print("戳啦,极霸矛(指列表)嘛")

    def __str__(self):
        return str(self.detail)

    def show(self):
        print("{},事{}维向量".format(self.detail, self.dimension))

    def __mul__(self,other):           #内积数乘不分的屑程序,,,
        newdet = []
        ipro = 0
        if type(other)==int:            #你麻麻的只能把数放在后边[流汗黄豆]
            for i in self.detail:
                newdet.append(other*i)
            return Vec(newdet)
        elif type(other)==Vec and self.dimension==other.dimension:
            for i in range(self.dimension):
                ipro += (self.detail[i]*other.detail[i])
            return ipro
        else:
            print("MarkErrorVecMul")

    def moudle(self):
        ms = 0
        for i in self.detail:
            ms += i**2
        return pow(ms,0.5)

    def __add__(self,other):
        addet = []
        if type(other)==Vec and self.dimension==other.dimension:
            for i in range(self.dimension):
                addet.append(self.detail[i]+other.detail[i])
            return Vec(addet)
        else:
            print("爪巴")

    def __truediv__(self,other):
        divdet = []
        for i in self.detail:
            divdet.append(i/other)
        return Vec(divdet)

    def outP(vec1,vec2):
        outl=[]
        if vec1.dimension==3 and vec2.dimension==3:
            outl.append(vec1.detail[1]*vec2.detail[2]-vec1.detail[2]*vec2.detail[1])
            outl.append(vec1.detail[2]*vec2.detail[0]-vec1.detail[0]*vec2.detail[2])
            outl.append(vec1.detail[0]*vec2.detail[1]-vec1.detail[1]*vec2.detail[0])
        else:
            print("爪巴")
        return Vec(outl)

class Mat:
    def __init__(self,matr):    #猜测对继承有偏见,那就不用继承了
        #Vec.__init__(self,lis)    #输入的是一行一行的行向量,,,
        if type(matr)==list and type(matr[0])==Vec:
            self.detail = matr
            self.slen = len(matr)
            self.nlen = len(matr[0].detail)
        else:
            print("Element is Vec,input is list.")

    def __sum__(self, other):
        nMats = []
        if self.slen==other.slen and self.nlen==other.nlen:
            for i in range(self.slen):
                nVec = self.detail[i]+other.detail[i]
                nMats.append(nVec)
            return Mat(nMats)
        else:
            print("爪巴")
            return None

    def nVofMat(self, n):
        pvec = []
        for i in range(self.slen):
            pvec.append(self.detail[i].detail[n])
        return Vec(pvec)

    def __mul__(self, other):
        nMatm = []
        pVec = []
        if type(other)==int:
            for item in self.detail:
                nMatm.append(item*other)
            return Mat(nMatm)
        elif type(other)==Vec:
            for item in self.detail:
                pVec.append(item*other)
            return Vec(pVec)
        elif type(other)==Mat:
            if self.slen==other.nlen and self.nlen==other.slen:
                for i in range(self.slen):
                    pVec = [self.detail[i]*other.nVofMat(j) for j in range(other.nlen)]
                    nMatm.append(Vec(pVec))
                    pVec = []
                    continue
                return Mat(nMatm)
            else:
                print("MarkErrorMatMul")
        else:
            print("[流汗黄豆]")

    '''def __str__(self):
        for i in self.detail:
            return str(i)'''

    def alcomMat(self,i,j):     #i,j仍是直接数的那种
        amm = []
        vecAm = []
        for k in range(self.slen):
            if k!=(i-1):
                vecAm = [self.detail[k].detail[l] for l in range(self.nlen) if l!=(j-1)]
                amm.append(Vec(vecAm))
                vecAm = []
                continue
        return Mat(amm)

    def transSet(self):
        trmat = []
        for i in range(self.nlen):
            trmat.append(self.nVofMat(i))
        return Mat(trmat)

    '''def assistSum():
        d = 0
            for i in range(self.nlen):
                d += self.detail[0].detail[i]*((-1)**i)*Mat.det(self.alcomMat(0,i))
            return d

    def det(self):        
        if type(self)==Mat and self.slen==self.nlen:
            if self.slen==1:
                return det.detail[0].detail[0]
            else:
                d = 0
                for i in range(self.nlen):
                    d += self.detail[0].detail[i]*((-1)**i)*Mat.det(self.alcomMat(0,i))
                return d
        else:
            print("Input 方阵,Plz")'''#听说算法很鸡肋,弃坑了弃坑了
        
    
    def show(self):
        for item in self.detail:
            print(item)
        print("\n")

            

'''v1 = Vec([1,1,4,5,1,4])
v2 = Vec([3,6,4,3,6,4])
v19 = Vec([1,9,1,9,8,1,0])
print(v1)
v1.show()
print(type(v1))
v3 = v1*2
print(v3)
v3.show()
v4=v1+v2
print(v4)
v4.show()
print(v1.moudle())
a = Vec(114514)'''
v1 = Vec([1,1,4])
v2 = Vec([5,1,4])
v3 = Vec([3,6,4])
m1 = Mat([v1,v2])
#print(m1.det())
m1.show()
m2 = m1.transSet()
m2.show()









        
