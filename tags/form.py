class Form:

    def __init__(self):
        self.action=""
        self.method="post"
        self.finalTag="<form"+" method=\""+self.method+"\" action=\""+self.action+"\" >\n</form>"

        self.items=[]

    def createForm(self):
        self.setFinalTag()
        return self.finalTag



    def setFinalTag(self):
        self.finalTag="<form"+" method=\""+self.method+"\" action=\""+self.action+"\" >\n</form>"
        idx=self.finalTag.rfind("</form>")
        self.finalTag=self.finalTag[:idx]

        itemList=""
        for i in range(len(self.items)):
            itemList+=str(self.items[i])+"\n"

        self.finalTag+=itemList+"</form>\m"
        #self.finalTag=""
        #print(self.finalTag)
        fo=open("1.html","a")
        fo.write(self.finalTag)

    def add(self,item):
        self.items.append(item)
        #print(len(self.items))

    def __str__(self):
        return self.finalTag

    def setMethod(self,method):
        self.method=method

    def setAction(self,action):
        self.action=action

    def write(self,text):
        self.items.append(text)

    def __str__(self):
        return self.createForm()
