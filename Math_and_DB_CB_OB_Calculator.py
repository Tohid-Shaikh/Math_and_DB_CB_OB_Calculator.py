sum=0
addition=0
substraction=0
division=0
multiplication=0

ch=0
print("for calculator press1")
ch=int(input())
while(ch==1):
    print("|----------------------|")
    print("|1. ADDITION           |")
    print("|2. SUBSTRACTION       |")
    print("|3. MULTIPLICATION     |")
    print("|4. DIVISSON           |")
    print("|5. decimal to binary  |")
    print("|6. char to binary     |")
    print("|7. Octal to binary    |")
    print("|----------------------|")
    print("|ENTER YOUR CHOISE:    |")
    print("|----------------------|")
    st=int(input())
    if(st==1):
        print("ENTER FIRST NUMBER")
        sum1=int(input())
        print("ENTER FIRST NUMBER")
        sum2=int(input())
        ans=sum1+sum2
        print("|----------------------|")
        print("|  the answer is: ",ans, "|")
        print("|----------------------|")
        break
    
    if(st==2):
        print("|----------------------|")
        print("ENTER FIRST NUMBER")
        sum1=int(input())
        print("ENTER FIRST NUMBER")
        sum2=int(input())
        ans=sum1-sum2
        print("|----------------------|")
        print("the answer is: ",ans)
        print("|----------------------|")
        break
    
    if(st==3):
        print("|----------------------|")
        print("ENTER FIRST NUMBER")
        sum1=int(input())
        print("ENTER FIRST NUMBER")
        sum2=int(input())
        ans=sum1*sum2
        print("|----------------------|")
        print("the answer is: ",ans)
        print("|----------------------|")
        break
    
    
    if(st==4):
        print("|----------------------|")
        print("ENTER FIRST NUMBER")
        sum1=int(input())
        print("ENTER FIRST NUMBER")
        sum2=int(input())
        ans=sum1/sum2
        print("the answer is: ",ans)
        print("|----------------------|")
        break
    
    if(st==5):
        print("|----------------------|")
        print("ENTER DECIMAL NUMBER")
        sum1=int(input())
        binary_number = bin(sum1)
        print("BINARY OF GIVEN NUMBER: ")
        print("the answer is:",binary_number)
        # print("the answer is: ",sum1)
        print("|----------------------|")
        break
    
    if(st==6):
        print("|----------------------|")
        print("ENTER STRING NUMBER")
        sum1=str(input())
        binary_str = ""
        for char in sum1:
            binary_str += bin(ord(char))[2:]
            print("BINARY OF GIVEN STRING: ")
            print("Binary representation:", binary_str)
            print("the answer is: ",sum1)
            print("|----------------------|")
        break
    
    if(st==7):
        print("|----------------------|")
        print("ENTER STRING NUMBER")
        sum1=(input())
        binary_str = ""
        for char in sum1:
            binary_number = bin(int(oct(sum1), 8))[2:]
            print("BINARY OF GIVEN STRING: ")
            print("Binary representation:",binary_number)
            print("the answer is: ",sum1)
            print("|----------------------|")
        break

    
    
    



    
