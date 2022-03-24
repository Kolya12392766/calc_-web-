from pywebio import start_server
from pywebio.input import input, FLOAT
from pywebio.output import put_text
def main(what,a,b):
    if what == "+":
        c = a + b
        put_text (str (a) , "+" , str (b) , "=" , str (c))
    elif what == "-":
        c = a - b
        put_text (str (a) , "+" , str (b) , "=" , str (c))
    elif what == "/":
        c = a / b
        put_text (str (a) , "+" , str (b) , "=" , str (c))
    elif what == "*":
        c = a * b
        put_text (str (a) , "+" , str (b) , "=" , str (c))
    else:
        put_text ("is" + what + "not fount")
        exit ()
def print_hi():
    ver = 1.0
    put_text ("calc " + '"web"')
    put_text("ver:" + str(ver))
    a = int (input ("nam1="))
    b = int (input ("nam2="))
    what = input ("what to do(+,-,*,\)=")
    main(what,a,b)



if __name__ == '__main__':
    start_server (print_hi() , port=8080)


