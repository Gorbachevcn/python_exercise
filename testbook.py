# -*- coding: cp936 -*-
'''
Ex.3-4 (1)
do_twice����1������������Ϊʵ��������
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
do_twice����2��ʵ�Σ�һ���Ǻ���������һ����һ��ֵ��
do_twice���ú�������2�Σ��������Ǹ�ֵ��Ϊʵ��
'''
def do_twice(f,ch):
    f(ch)
    f(ch)
    '''
f(ch)�ͱ�ʾ��ch����f�������ں������do_twice��ʱ��Ͳ��ܸ������ڵ�print_spam��������
����������Ե�ʣ������ú����ڵ�ǰ��3�������Ŷ��룺
1. Ҫôǰ��������������Ǹ��� ������2. Ҫôǰ������
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
do_four����һ���������� �� һ��ֵ��
�Ǹ�ֵ��Ϊʵ�ε��ú���4�Σ�
�Һ�����Ӧ��ֻ��2�����
'''
def do_four(func,ch):
    func(ch)
    '''
func���治��(ch)�Ļ�����û���βεĴ��ݣ�����������None
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




































