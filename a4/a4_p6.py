#a4_p6

def print_frame(n,m,c):
    for i in range(n):
        for j in range(m):
            if(i == 0 or i == n - 1 or j == 0 or j == m- 1):
                print(c ,end="")
            else:
                print(' ', end="")
        print()


def main ():
    n = int(input(""))#number of rows
    m = int(input(""))# numebr of columns
    c=input("")
    print_frame(n,m,c)

if __name__ == "__main__":
    main()




