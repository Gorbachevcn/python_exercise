# -*- coding: cp936 -*-
'''
Ex.3-4 (1)
do_twice接受1个函数对象作为实参来传递
'''
def do_twice(f):
    f
    f
    return None

def print_spam(ch):
    print ch
    return None
ch = 'Spam '*3

do_twice(print_spam(ch))
print 'Ex.3-4 (1) Terminated'


'''
Ex.3-4 (2,3,4)
do_twice接受2个实参，一个是函数对象，另一个是一个值，
do_twice调用函数对象2次，并传入那个值作为实参
'''
def do_twice(f,ch):
    f(ch)
    f(ch)
    '''
f(ch)就表示把ch传给f，所以在后面调用do_twice的时候就不能给括号内的print_spam赋参数；
由于缩进的缘故，不能让函数内的前后3个单引号对齐：
1. 要么前面缩进而后面的那个不 缩进；2. 要么前后都缩进
'''
    return None

def print_spam(ch):
    print ch
    return None
ch = 'Spam '*3

do_twice(print_spam,ch)
print 'Ex.3-4 (2,3,4) Terminated'


'''
Ex.3-4 (5)
do_four接受一个函数对象 和 一个值，
那个值作为实参调用函数4次，
且函数体应该只有2个语句
'''
def do_four(func,ch):
    func(ch)
    '''
func后面不加(ch)的话，会没有形参的传递，输出结果会是None
'''
    func(ch)
    return None

def print_twice(ch):
    print ch
    print ch
    return print_twice

ch = 'Spam'*3
do_four(print_twice,ch)
print 'Ex.3-4 (5) Terminated'




































