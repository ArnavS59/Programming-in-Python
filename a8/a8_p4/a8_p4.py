from mod_conversion import in2cm_table_html 
from mod_conversion import in2cm_table # import the other file
# import mod_conversion

def main():
    start = int(input("Enter a starting value: "))
    end = int(input("Enter an ending value : "))
    step = int(input("Enter a step          : "))
    output_decision = (input("Enter 's' to print on the screen,else in another file: "))
    if output_decision == 's':
        in2cm_table(start, end, step)
    else:  # call a different function
        f = open('in2cm.html', 'w')
        f.write(in2cm_table_html(start, end, step))
        # call the function from the other file
#
main()
