#My Hello World Program
"""
first = 1
second = 2.5
third = "woot"

print("geeksquiz")
print(first)
print(second)
print(third)

#List Creation
nums = []
nums.append(21)
nums.append(40.5)
nums.append("woot")

print(nums)

#First taste of input

combo = input("Enter your name: ")

print("Fuck you",combo)

#Math on inputs

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

num3 = num1 * num2

print("Product Motherfucker", num3)

num = int(input("pick a number motherfucker: "))

if(num < 10):
    print("Smol gang")
elif(num > 10):
    print("Less smol gang")
else:
    print("fuck you")


def hoe():
    print("Fuck")
    print("You")
    print("Hoe")
hoe()

#Call hoe
hoe()
"""

def Main():
    print("Started")
    output = getInteger()
    print(output)

def getInteger():
    result = int(input("Enter integer: "))
    return result

if __name__ == "__main__":
    Main()
