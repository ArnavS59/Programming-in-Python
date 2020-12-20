
def main():

    start = int(input("Enter a starting value: "))
    end = int(input("Enter an ending value : "))
    step = int(input("Enter a step          : "))
    print("{0:>6}  {1:>6}".format("inch", "cm"))  # header of the table
    for it in range(start, end, step):
        print("{0:>6.1f}  {1:>6.1f}".format(it, 2.54*it))
        # since 1 in = 2.54 cm

main()