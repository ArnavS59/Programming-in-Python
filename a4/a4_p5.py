#a4_p5

def print_rectangle( n,m,c ) :
    for i in range(0,n):
        for j in range(0,m):
            print(c, end= '')
        print()
    return

def main ():
    n = int ( input ("") )# number of rows
    m = int ( input ("") )# number of columns
    c = ( input ("") ) #character 
    print_rectangle( n,m,c )


# The entry point for program execution
if __name__ == "__main__":
    main()

