
def in2cm_table(first, last, step):
    print("{0:>6}  {1:>6}".format("inch", "cm"))  
    for it in range(first, last, step):
        print("{0:>6.1f}  {1:>6.1f}".format(it, 2.54 * it))
        # since 1 in = 2.54 cm
    return ""

