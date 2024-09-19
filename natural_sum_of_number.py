#To find the natural sum of the number

#input Section
number=int(input("Enter the number for natural sum : "))
sum=0
#logic section & print Section

for i in range(1,number+1):
    sum=sum+i
print("Natural sum of ",number,"=",sum)