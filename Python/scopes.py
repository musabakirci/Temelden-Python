name = "Kemal"

def change_name(new_name):
    global name
    name = new_name
    print(name)

change_name("Mustafa")
print(name)    