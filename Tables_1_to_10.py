#writing tables 1 to 10

for i in range(1, 11):
    print(end="\n")
    for j in range(1, 11):
        print(f"{i:2} x {j:2} = {i*j:3}")