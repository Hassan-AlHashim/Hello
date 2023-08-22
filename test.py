msg = "Hello World!!"
print (msg)


#a function that will ask as many numbers as possible and then it will add them together and print the average of the numbers
def average():
    total = 0
    count = 0
    while True:
        try:
            x = input("Enter a number, write done when you're satisfied: ")
            if x == "done":
                break
            else:
                total = total + int(x)
                count = count + 1
        except:
            print("Invalid input")
            continue
    print(total/count)
average()