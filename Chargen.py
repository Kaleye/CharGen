from random import*
class Character:
    def __init__(self, name, Scorelist=[], level=int(0), stre=1, dex=2, con=3, inte=4, wis=5, cha=6, stremod=0, dexmod=0, conmod=0, intemod=0, wismod=0, chamod=0, profbon=0):
        self.name=name
        self.level=level
        self.stre=stre
        self.dex=dex
        self.con=con
        self.inte=inte
        self.wis=wis
        self.cha=cha
        self.Scorelist=[self.stre, self.dex, self.con, self.inte, self.wis, self.cha]
        self.stremod=stremod
        self.dexmod=dexmod
        self.conmod=conmod
        self.intemod=intemod
        self.wismod=wismod
        self.chamod=chamod

    def RollScore(self):
        a=randint(1,6)
        b=randint(1,6)
        c=randint(1,6)
        d=randint(1,6)
        list=[a,b,c,d]
        list.sort()
        add =sum(list[1:4])
        return add

    def SetAttributes(self):
        a=self.RollScore()
        print("a: ", a)
        b=self.RollScore()
        print("b: ",b)
        c=self.RollScore()
        print("c: ",c)
        d=self.RollScore()
        print("d: ",d)
        e=self.RollScore()
        print("e: ",e)
        f=self.RollScore()
        print("f: ",f)
        list=[a,b,c,d,e,f]
        for i in range(len(self.Scorelist)):
            print("Input letter for", self.Scorelist.__getitem__(i), """
(1=Strength,2=Dexterity, 3=Constitution, 4=Intelligence, 5=Wisdom, 6=Charisma)""")
            x=input()
            if x=="a":
                if a in list:
                    y=a
                    list.remove(a)
                else:
                    print("Stat already used")
                    break
            elif x=="b":
                if b in list:
                    y=b
                    list.remove(b)
                else:
                    print("Stat already used")
                    break
            elif x=="c":
                if c in list:
                    y=c
                    list.remove(c)
                else:
                    print("Stat already used")
                    break
            elif x=="d":
                if d in list:
                    y=d
                    list.remove(d)
                else:
                    print("Stat already used")
                    break
            elif x=="e":
                if e in list:
                    y=e
                    list.remove(e)
                else:
                    print("Stat already used")
                    break
            elif x=="f":
                if f in list:
                    y=f
                    list.remove(f)
                else:
                    print("Stat already used")
                    break
            else:
                print("Not valid")
                break
            if i==0:
                self.stre=y
                print("Strength: ",self.stre)
            elif i==1:
                self.dex=y
                print("Dexterity: ",self.dex)
            elif i==2:
                self.con=y
                print("Constitution: ",self.con)
            elif i==3:
                self.inte=y
                print("Intelligence: ",self.inte)
            elif i==4:
                self.wis=y
                print("Wisdom: ",self.wis)
            elif i==5:
                self.cha=y
                print("Charisma: ",self.cha)
            print(list)
            self.Scorelist=[self.stre, self.dex, self.con, self.inte, self.wis, self.cha]
            print("Scorelist: ", self.Scorelist)

class End:
    def __init__(self):
        pass

    def insert(self, name, score1, score2, add1, add2, prevrace):
        prevrace.nextrace=Race(name, score1, score2, add1, add2, self)
        print(l.search(name))

    def search(self, element):
        return "Race doesn´t exist"

    def searchindex(self,index,i):
        return "Race does not exist. List too short"

    def delete(self, prevrace, preprevrace):
        if preprevrace:
            preprevrace.nextrace=self
            return prevrace.name
        else:
            return "Race already doesn´t exist"

    def deleteindex(self, index, i, prevrace):
        return "Race does not exist. List to short"

    def deletename(self, name, prevrace):
        return "Race does not exist"

class Race:
    def __init__(self, name, score1, score2, add1, add2, nextrace=End()):
        self.name=name
        self.score1=score1
        self.score2=score2
        self.add1=add1
        self.add2=add2
        self.nextrace=nextrace

    def insert(self, name, score1, score2, add1, add2, prevrace):
        self.nextrace.insert(name, score1, score2, add1, add2, self)

    def search(self, name):
        if self.name==name:
            return  self.name
        else:
            return self.nextrace.search(name)

    def searchindex(self, index, i):
        if index==i:
            return self.name
        else:
            i+=1
            return self.nextrace.searchindex(index, i)

    def delete(self, prevrace, preprevrace):
        return self.nextrace.delete(self, prevrace)

    def deleteindex(self, index, i ,prevrace):
        if index==i:
            if prevrace:
                prevrace.nextrace=self.nextrace
                return self.name
        else:
            i+=1
            return self.nextrace.deleteindex(index, i, self)

    def deletename(self,name, prevrace):
        if name==self.name:
            if prevrace:
                prevrace.nextrace=self.nextrace
                return prevrace.name
        else:
            return self.nextrace.deletename(name, self)


class Racelist:
    def __init__(self):
        self.nextrace=End()
        print ("New Racelist created")

    def insert(self, name, score1, score2, add1, add2):
        self.nextrace.insert(name, score1, score2, add1, add2, self)

    def search(self, name):
        return self.nextrace.search(name)

    def searchindex(self, index, i=0):
        return self.nextrace.searchindex(index, i)

    def delete(self):
        return self.nextrace.delete(self,None)

    def deleteindex(self, index, i=0):
        return self.nextrace.deleteindex(index,i, None)

    def deletename(self,name):
        return self.nextrace.deletename(name, None)



class Class:
    def __init__(self, name):
        self.name=name



if __name__ =="__main__":
    c=Character("Kaleye")
    l=Racelist()
    l.insert("Elf","dex", "inte", 2, 1)
    l.insert("Dwarf", "stre", "con", 2, 1)
    print(l.search("Elf"))
    print(l.searchindex(1))
    l.insert("Human","Any","Any",3,3)
    print(l.delete())
    l.insert("Halfling","Cha","Wis",2,1)
    print(l.deleteindex(1))
    print(l.deletename("Elf"))
