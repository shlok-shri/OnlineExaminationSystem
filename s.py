s = []
top = None


def isEmpty(stk):
    if stk == []:
        return True
    else:
        return False


def push(stk, item):
    stk.append(item)
    top = len(stk) - 1


def pop(stk):
    if isEmpty(stk):
        return ("Under-Flow!!")
    else:
        i = stk.pop()
        if len(stk) == 0:
            top = None
        else:
            top -= 1
    return i


def peek(stk):
    if isEmpty(stk):
        return ("Underflow")
    else:
        top = len(stk) - 1
        return (stk[top])


def display(stk):
    if isEmpty(stk):
        print("Stack is Empty")
    else:
        top = len(stk) - 1
        print(stk[top], "<---Top")
        for i in range(top - 1, -1, -1):
            print(stk[i])


while True:
    print("STACK IMPLEMENTATION")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    ch = int(input("Enter your choice : "))

    if ch == 1:
        item = input("Enter the item to be pushed : ")
        push(s, item)
        print('%d added successfully' % item)
        input('Press any key to continue....')

    elif ch == 2:
        item.pop(s)
        if item == 'UnderFlow':
            print("UnderFlow! Stack is Empty")
        else:
            print('%d is popped' % item)
        input('Press any key to continue....')

    elif ch == 3:
        item.peek(s)
        if item == 'UnderFlow':
            print("UnderFlow! Stack is Empty")
        else:
            print('%d is popped' % item)
        input('Press any key to continue....')

    elif ch == 4:
        display(s)
        input('Press any key to continue....')

    elif ch == 5:
        break

    else:
        print("Andhe 1-5 tak hi dalna tha...")
        input('Press any key to continue....')