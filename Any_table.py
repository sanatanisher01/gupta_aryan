#Program to give any table

number=int(input("Enter the number : "))

#Logic & print section

for i in range(1,11):
    print(f"{number:2} X {i:2} = {number*i:4}")