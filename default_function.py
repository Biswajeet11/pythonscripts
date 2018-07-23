def simple(num1,num2):
    pass

def simple(num1,num2=5):
    print(num1,num2)
    '''default parameter num2 it will always print 5'''

simple(2)

def basic_window(width,height,font='TNR',bgc='w',scrollbar=True):
    print(width,height,font,bgc,scrollbar)

basic_window(1000,343)
basic_window(1000,343,bgc='rr')