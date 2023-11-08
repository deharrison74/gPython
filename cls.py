class people:
    def __init__(selp,name,age):
        selp.name = name
        selp.age = age

    def methods(selp):
        print("Hi my name is " + selp.name)

h1= people("Muki",22)
h2= people(name="Todi", age= 25)


h2.methods()