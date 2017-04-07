from tags.input import *
from tags.div import *
from tags.para import *
from tags.form import *

f=Div()
i=Input()
i.setType("username")
p=Input()
p.setType("password")

i.createInput()
p.createInput()

f.setHeight("345")
f.setWidth("567")
f.add(i)
f.add(p)
f.createDiv()
