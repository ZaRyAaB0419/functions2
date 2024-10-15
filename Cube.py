def cube(num1):
    return num1*num1*num1

def by_three(num1):
    if num1 %3==0:
        return cube(num1)

    else:
        print("Not availabel")

n= int(input("What is your number:"))

print("Cube is:", by_three(n))
