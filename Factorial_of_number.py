#Program to find Factorial of any number

number=int(input("Enter the number : "))
factorial=1


#logic section 

for i in range(1,number+1):
    factorial *= i

#print Section

print("Factorial of", number, "is :", factorial)