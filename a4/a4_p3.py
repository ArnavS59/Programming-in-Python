#a4_p3

def iswithin_n():
    while True:
        n= int(input("Enter an integer: "))
        if(n>=0 and n<=32):
            return n
        else:
            print("Number should be between 0 and 32")
            continue

def isCapital():
    while True:
        ch= (input("Enter a character: "))
        if(ord(ch) >= 65 and ord(ch)<=90):
            return ord(ch)
        else:
            print("The character should be Capital")
            continue

def main():
    asci=isCapital()
    n=iswithin_n()
    for index in range(n+1):
        print(chr(asci+index), end=" ")
    print()

if __name__ == "__main__":
    main()






