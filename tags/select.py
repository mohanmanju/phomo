class Option:

    def getOption(name,value):
        return "<option"+" name=\""+name+"\"> "+value+"</option>\n"



class Select:
    def __init__(self):
        self.name=""


        self.items=[]
        self.finalTag="<select>\n</select>"

    def createSelect(self):
        self.setFinalTag()
        fo=open("1.html","a")
        fo.write(self.finalTag)

    def setFinalTag(self):
        result="<select"+" name=\""+self.name+"\" >\n"
        for i in range(len(self.items)):
            result+=self.items[i]

        result+="</select>\n"

        self.finalTag=result
        #print(self.finalTag)

    def setName(self,name):
        self.name=name

    def addOption(self,name,value):
        self.items.append(Option.getOption(name,value))

    def __str__(self):
        return self.createSelect()
