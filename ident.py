# Identities mod p

import math

''' Useful functions '''
def fact(n):
    return math.factorial(n)
def bin(n,k):
    return math.comb(n,k)
def factmod(n):
    global p
    return math.factorial(n) % p

p = int(input('Enter prime p: '))
a = int(input('Enter positive integer a: '))
b = int(input('Enter positive integer b: '))
c = int(input('Enter positive integer c: '))
'''
p=7
a=4
b=3
c=1
'''
def valid_quadraple(p,a,b,c):
    is_valid=False
    if (a+2*c<p) and (b+2*c<p) and (p-1<=a+b+c) and (a+b+2*c+1<2*p):
        is_valid = True
    return is_valid

def P_3is_valid(p,a,b,c):
    is_valid=True
    if (a+b+4*c-p+1<0) or (a+b+4*c-p+1>=p):
        is_valid=False
    elif (a+b+2*c-p+1<0) or (a+b+2*c-p+1>=p):
        is_valid=False
    elif (a+b+3*c-p+1<0) or (a+b+3*c-p+1>=p):
        is_valid=False
    return is_valid

def P_3(p,a,b,c):
    if not P_3is_valid(p,a,b,c):
        return 'The denominator of P_3({},{},{}) contains zero or factorial of a negative number'.format(a,b,c)
    topmod = (factmod(2*c)*factmod(3*c)*factmod(a)*factmod(a+c)*factmod(a+2*c)*factmod(b)*factmod(b+c)*factmod(b+2*c)) % p
    botmod = (factmod(c)*factmod(c)*factmod(a+b+4*c-p+1)*factmod(a+b+2*c-p+1)*factmod(a+b+3*c-p+1)) % p
    for i in range(1,p):
        if botmod*i % p == 1:
            inv = i
            continue
    res = (topmod*inv) % p
    return 'P_3({},{},{}) = {} in F_{}'.format(a,b,c, res, p)

def Q_3_den_is_valid(p,a,b,c, x,y,z):
    is_valid=True
    if (a+x+z+b-p+1<0) or (a+x+z+b-p+1>=p):
        is_valid=False
    elif (a+2*c-x+y+b-p+1<0) or (a+2*c-x+y+b-p+1>=p):
        is_valid=False
    elif (a+4*c-z-y+b-p+1<0) or (a+4*c-z-y+b-p+1>=p):
        is_valid=False
    return is_valid

def Q_3(p,a,b,c):
    partial_sum_x=0
    count=0
    for x in range(2*c+1):
        partial_sum_y=0
        for y in range(2*c+1):
            partial_sum_z=0
            for z in range(2*c+1):
                if not Q_3_den_is_valid(p,a,b,c, x,y,z):
                    count+=1
                    continue
                topmod=(factmod(a+x+z)*factmod(a+2*c-x+y)*factmod(a+4*c-z-y)*(factmod(b)**3)) % p
                botmod=(factmod(a+x+z+b-p+1)*factmod(a+2*c-x+y+b-p+1)*factmod(a+4*c-z-y+b-p+1)) % p
                for i in range(1,p):
                    if botmod*i % p == 1:
                        inv = i
                        continue
                pre_summand = (topmod*inv) % p
                summand = ((-1)**(x+y+z))*bin(2*c,x)*bin(2*c,y)*bin(2*c,z)*pre_summand
                #print(summand)
                partial_sum_z += summand
                #print('           x={}, y={}, z={},  partial sum z ={} '.format(x,y,z,partial_sum_z))
            partial_sum_y += partial_sum_z
            #print('   partial sum y =', partial_sum_y)
        partial_sum_x += partial_sum_y
        #print('partial sum x =', partial_sum_x)
    sum = partial_sum_x  % p
    return 'Q_3({},{},{}) = {} in F_{}; {} summand(s) undefined'.format(a,b,c, int(sum), p, count)


def results(p,a,b,c):
    #if valid_quadraple(p,a,b,c):
    print()
    print('p={}, a={}, b={}, c={}'.format(p,a,b,c))
    print()
    print(P_3(p,a,b,c))
    print()
    print(Q_3(p,a,b,c))
    print()

results(p,a,b,c)


#print(factmod(7))
