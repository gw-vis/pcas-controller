class MyClass():
    def __init__(self,message):
        self.value = message

    def set_value(self,message):
        self.value = message

    def print_value(self):
        print(self.value)

myins = MyClass("Hello!")
print(myins.value)

print("--------------------------")

myins.print_value()

print("--------------------------")

myins.set_value("abc")
myins.print_value()

