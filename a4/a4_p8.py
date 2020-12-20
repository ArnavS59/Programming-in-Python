#a4_p8

def convert ( miles ) :
    conversionfactor=1.609344
    return miles*conversionfactor

def main ():
    miles = float ( input ("Enter the number of miles: ") )
    result = convert ( miles )
    print ("The conversion of, {} is {:.2f} kms".format(miles,result) )

# The entry point for program execution
if __name__ == "__main__":
    main()