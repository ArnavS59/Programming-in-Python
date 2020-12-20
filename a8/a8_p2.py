
def main():
    m = int(input("enter starting: "))
    n = int(input("enter end point: "))
    step = int(input("enter step: "))

    f = open("table.txt", "w")
    headings = "{0:>10}{1:>12}{2:>12}{3:>12}".format("inch", "cm", "meters","kilometers")
    f.write(headings)
    # same loop but adding new entry points and a newline for the file
    for i in range(m, n, step):
        data = "{0:>10.1f}{1:>12.1f}{2:>12.4f}{3:>12.7f}".format(i, i*2.54,i/39.37, i/39370)
        f.write("\n")
        f.write(data)
    f.close()

main()