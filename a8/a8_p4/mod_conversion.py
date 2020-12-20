
def in2cm_table(first, last, step):
    print("{0:>6}  {1:>6}".format("inch", "cm"))  # since 1 in = 2.54 cm
    for it in range(first, last, step):
        print("{0:>6.1f}  {1:>6.1f}".format(it, 2.54 * it))
        # since 1 in = 2.54 cm
    return ""

def in2cm_table_html(first, last, step):
    msg = "<html>"
    msg += '<table border="1">' 
    msg += '<tr style="color: blue; background-color: orange;">'
    msg += "<th>inch</th><th>cm</th>"
    msg += "</tr>"  # closing the 'container'
    for it in range(first, last, step):
        msg += '<tr style="background-color: yellow;">'
        msg += "<td>{0:>6.1f}</td><td>{1:>6.1f}</td>".format(it, 2.54 * it)
        msg += "</tr>"
    msg += "</table>"
    msg += "</html>" 
    return msg
