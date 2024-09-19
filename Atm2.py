#input section
money=int(input("Enter money amount to Withdraw : "))

#logic section
money=money-100
num2000=money//2000
money=money%2000

num500=money//500
money=money%500

num200=money//200
money=money%200

num100=money//100

#print section

print("Number of 2000 Rs notes : ",num2000)
print("Number of 500 Rs notes : ",num500)
print("Number of 200 Rs notes : ",num200)
print("Number of 100 Rs notes : ",num100+1)