def getusergae():
    while True:
    try:
        age = int(input("Please put your age: "))
        if age <= 0:
            print("Invalid age, please try again.")
    return age
except ValueError:
    print("Invalid input, please try again.")

getuserage()