from mod_conversion import in2cm_table  # import the other file
import sys

def main():
    start = int(input("Enter a starting value: "))
    end = int(input("Enter an ending value : "))
    step = int(input("Enter a step          : "))
    in2cm_table(start,end,step)

main()
