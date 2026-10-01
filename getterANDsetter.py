class Student:
    def __init__(self):
        self.__age = 20

    # Getter
    def get_age(self):
        return self.__age

    # Setter
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age")
            
s = Student()

print(s.get_age())

s.set_age(25)
print(s.get_age())

s.set_age(-10)
print(s.get_age())