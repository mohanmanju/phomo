class Input:
    def __init__(self):
        self.type="text"
        self.name="name"
        self.value=""
        self.finalTag=""

    #changing final tag to changed values
    def setFinalTag(self):
        #final string to represent a tag in html
        self.finalTag="<input type=\""+self.type+"\" name=\""+self.name+"\" value=\""+self.value+"\"/>\n"

    #creating input using this methods
    def createInput(self):
        self.setFinalTag()
        fo=open("1.html","a")
        fo.write(self.finalTag)
        return self.finalTag

    #set type of the input field
    def setType(self,type):
        self.type=type

    #set name of the input field
    def setName(self,name):
        self.name=name


    #set value to input field
    def setValue(self,valye):
        self.value=value

    #get string eqivalent of the tags
    def __str__(self):
        return self.createInput()
