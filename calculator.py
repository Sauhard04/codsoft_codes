print("\n\n    ****  THIS IS A SIMPLE CALCULATOR THAT CAN PERFORM BASIC ARITHMATIC OPERATIONS  ****    \n")
print("\nTHIS CALCULATOR CAN PERFORM FOLLOWING TASKS--")
print("\t-->ADDITION (+)\n")
print("\t-->SUBTRACTION (-)\n")
print("\t-->MULTIPLICATION (*)\n")
print("\t-->DIVISION (/)\n\n")
num1=float(input("ENTER THE FIRST NUMBER AND PRESS ENTER KEY: "))
print("\n    ----    ****    ----    \n")
op=input("ENTER THE OPERATION TO BE PERFORMED: ")
print("\n    ----    ****    ----    \n")
num2=float(input("ENTER THE SECOND NUMBER AND PRESS THE ENTER KEY: "))
print("\n    ----    ****    ----    \n")
if op=='+':
    print("ON ADDING",num1,"AND",num2," ",num1+num2)
elif op=='-':
    print("ON SUBTRACTING",num1,"FROM",num2," ",num1-num2)
elif op=='*':
    print("ON MULTIPLYING",num1,"AND",num2," ",num1*num2)
elif op=='/':
    if num2==0:
        print("ON DIVIDING",num1,"BY",num2," 0")
    else:
        print("ON DIVIDING",num1,"BY",num2," ",num1/num2)
print("\n    ----    ****    ----    \n\n")