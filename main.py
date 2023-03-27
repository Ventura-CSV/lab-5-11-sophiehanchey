import random


def merge(number1, number2):
    #################
    # Make your code
    #################
    mlist = []

    #################
    # Do not delete return statement
    # You should return 'mlst" as a merged result
    return mlist


def main():
    number1 = [0, 2, 3]
    number2 = [1, 4, 5, 6, 9]
    retlist = merge(number1, number2)
    print(retlist)
    # #########################################

    n1 = [random.randint(0, 20) for i in range(5)]
    n2 = [random.randint(0, 20) for i in range(3)]
    n1.sort()
    n2.sort()
    print(n1)
    print(n2)
    retlist = merge(n1, n2)
    print(retlist)


if __name__ == '__main__':
    main()
