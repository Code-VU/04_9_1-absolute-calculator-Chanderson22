def calculateAbsolute():
    
    # This first line is provided for you
    in_num  = input("Enter a number: ")
    n = int(in_num)
    if n > 21:
        print("Result: "+str(abs(2*(n-21))))
    elif n < 21:
        print("Result: "+str(abs(n-21)))
    # end assignment

## If you want to test locally run > python payCalculator.py

if __name__ == "__main__":
    calculateAbsolute()
