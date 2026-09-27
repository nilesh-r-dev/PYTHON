# def start():
#     print("hello")
# start() 


def decorator(func):
     
     def wrapper():
          print("hello")
          func()
     return wrapper

@decorator

def start():
     print("world")
start()     

def start(func):

    def wrapper():
        print("Program Started")
        func()

    return wrapper

@start
def add():
    print("Addition")

@start
def subtract():
    print("Subtraction")

add()
subtract()






is_logged_in = True

def login_required(func):
    def wrapper():
        if is_logged_in:
            print("welcome")
        else:
            print("login first")
    func()
    return wrapper

@login_required            


@login_required
def view_profile():
    print("Welcome to your profile")

@login_required
def edit_profile():
    print("Profile updated")

view_profile()
edit_profile()



def positive_number(func):
    def wrapper(num):
        if num > 0:
            print("enter positive number")
            func(num)
        else:
            print("num must be a positive number")
    return wrapper

@positive_number

def square(num):
    print(num * num)


square(5)
square(3)

            