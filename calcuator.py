print("*****Python Calculator!*****")
question = input("What operation would you like to perform? (add, subtract, multiply, divide) ")
question2= input("What is your first value? ")
question3= input("What is your second value? ")
if question == "add":
    print("The result is: ", float(question2) + float(question3))
elif question == "subtract":
    print("The result is: ", float(question2) - float(question3))
elif question == "multiply":
    print("The result is: ", float(question2) * float(question3))
elif question == "divide":
    print("The result is: ", float(question2) / float(question3))
