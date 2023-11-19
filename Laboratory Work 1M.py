Tako = []#Ready stacks
def create():#Thius fucntion serves as the name creation of the stacks
    global Name#name to be called on every stacks
    Name= input(str("Enter the stack name: "))#inputting the name
    print(f"{Name}: {Tako}")#Showing the content of the stack and it's name

def isempty(Tako):#This function serves to check if the stack is empty
    return len(Tako) == 0#Returns the len of tako to zero


def push(Tako):#This function serves as to add a data in a stack
    while True:#A while loop if-else statement if they enter an element or not
        element = input('Enter Item: ')
        if len(element)==0:
            print("Please add an element")
        else:
            Tako.append(element)
            print("pushed item: " + element)
            print(f"{Name}: {Tako}")
            break#breaks the loop and go on the next choice
def pop(Tako):#This function serves as to remove the recently added data
    if(isempty(Tako)):#If-else statement if the stack is empty or not
        print("Stack is empty")
    else:
        print("The Removed Element is " + Tako.pop())
        print(f"{Name}: {Tako}")

def show(Tako):#Serves to show each data in the stack from first added data to the recently added data
    print("the stack elements are: ")
    for cookie in Tako:#Shows each data one by one
        print(cookie)

def peek(Tako):#This function serves to peek the top of the stack which is the recently added data
    print(Tako[-1])


while True:#This program helps to pick what operation after creating a stack
    print("[C] - Create Stack")#This makes the stacks
    print("[A] - Append element to Stack")#this calls to add the data to the stacks
    print("[D] - Remove element on Stack")#Calls the function to remove the recently added data
    print("[P] - Peek the top Element of Stack")#Shows the recently added data
    print("[S] -  Show the Stack Element")#Shows the data in the stacks one by one
    Takodachi = input("enter Element: ").lower()#Input to which operation to use
    if Takodachi == 'c':
        create()
    elif Takodachi == 'a':
        push(Tako)
    elif Takodachi == 'd':
        pop(Tako)
    elif Takodachi == 'p':
        peek(Tako)
    elif Takodachi == 's':
        show(Tako)
#Developer: Kelvin Adam Aninang
#Date of Development: 30/10/2023