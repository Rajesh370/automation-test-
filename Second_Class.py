def calculator(a,b): # defining sum function
    sum = a+b
    sub = a-b
    return sum,sub

if __name__ == "__main__":
    a= input("Enter first number")
    b= input("Enter second number")
   sum, sub = calculator(int(a),int(b)) # this will call sum function
    print("The sum result is ", sum)
    print("The subtract result is", sub)

