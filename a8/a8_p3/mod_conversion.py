
def in2cm_table(first, last, step):
    print("{0:>6}  {1:>6}".format("inch", "cm"))  # since 1 in = 2.54 cm
    for it in range(first, last, step):
        print("{0:>6.1f}  {1:>6.1f}".format(it, 2.54 * it))
        # since 1 in = 2.54 cm
    return ""


















# For floating

# #enter variables for start length, end length and step size
# start=float(input("Enter start length:"))
# end=float(input("Enter end length:"))
# step=float(input("Enter step size:"))
# length=start

# #print the table names "inch" and "cm" with a width for the latter of 10
# #and aligned to the right
# print("{0:>}{1:>10}".format("inch","cm"))
# #for x in my prevoiusly defined range 
# # for x in range (start,end+1,step):
# #     #print x with first format
# #     #and the second format for x*2.54 as conversion into cm
# #     #both floats with precision of 1
# #     #cm line with width of 9, aligned to right 
# #     print("{0:>.1f} {1:>9.1f}".format(x, x*2.54))


# # while length<=end:
# #     print("{0:>.1f} {1:>9.1f}".format(length, length*2.54))
# #     length+=step
