class Input:
    def __init__(self):
        self.type="text"
        self.name="name"
        self.value="value"
    def createInput(self):
        str="<input type=\""+self.type+"\" name=\""+self.name+"\" value=\""+self.value+"\"/>"
        return str
    def setType(self,type):
        self.type=type

    def setName(self,name):
        self.name=name

    def setValue(self,valye):
        self.value=value
