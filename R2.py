# a function that prints true for an even number using an is_even function
# should not use division, modulo, multiplication

print('easy stuff')
print('even number checker')
k=int(input('Enter number k:'))


def is_even(k):
    while k>0:
        k=k-2
    if k==0:
        return True
    else:
        return False

print(is_even(k))
