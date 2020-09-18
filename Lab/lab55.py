# item : 5 - วาดภาพแสนสุข

"""
TEST
input : 3
output :
__#
_##
###

input : 7
output :
______#
_____##
____###
___####
__#####
_######
#######

input : -8
output :
########
_#######
__######
___#####
____####
_____###
______##
_______#

"""
def staircase(n):
    #Code
    if n > 0:
        if n == 1 or n == -1:
            print('#'*inp)
            return 1
        elif n > 1:
            print('_'*(n-1),end='')
            print('#'*(inp-n+1))
            return staircase(n-1)
    else:
        if n == -1:
            print('_'*(abs(inp)-1),end='')
            print('#')
            return 1
        else:
            print('_'*(abs(inp)-abs(n)),end='')
            print('#'*(abs(n)))
            return staircase(n+1)


if __name__ == '__main__':
    global inp
    inp = int(input("Enter Input : "))
    if inp == 0:
        print('Not Draw!')
    else:
        staircase(inp)