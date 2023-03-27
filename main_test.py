import random
import main


def test_main():

    number1 = [0, 2, 3]
    number2 = [1, 4, 5, 6, 9]
    print('Test data')
    print(number1)
    print(number2)
    retlist = main.merge(number1, number2)
    print('After merge', retlist)
    assert retlist[0] == 0
    assert retlist[1] == 1
    assert retlist[2] == 2
    assert retlist[3] == 3
    assert retlist[4] == 4
    assert retlist[5] == 5
    assert retlist[6] == 6
    assert retlist[7] == 9
    # #########################################

    n1 = [random.randint(0, 20) for i in range(5)]
    n2 = [random.randint(0, 20) for i in range(3)]
    n1.sort()
    n2.sort()
    tlist = n1 + n2
    tlist.sort()
    print('Test data')
    print(n1)
    print(n2)
    retlist = main.merge(n1, n2)
    print('After merge', retlist)
    print(tlist)
    print(retlist)
    assert tlist == retlist
# assert v1 == -10, "Min value does not match"
# assert v2 == 5, "Max value does not match"


def test_sort():
    with open('main.py') as f:
        flag = True
        for line in f:
            if 'main()' in line:
                break
            if 'sort' in line:
                flag = False
                break
    assert flag == True
