'''
Daily Coding Problem: Problem #68
On our special chessboard, two bishops attack each other if they share the same diagonal. This includes bishops that have another bishop located between them, i.e. bishops can attack through pieces.

You are given N bishops, represented as (row, column) tuples on a M by M chessboard. Write a function to count the number of pairs of bishops that attack each other. The ordering of the pair doesn't matter: (1, 2) is considered the same as (2, 1).

For example, given M = 5 and the list of bishops:

    (0, 0)
    (1, 2)
    (2, 2)
    (4, 0)

The board would look like this:

[b 0 0 0 0]
[0 0 b 0 0]
[0 0 b 0 0]
[0 0 0 0 0]
[b 0 0 0 0]

You should return 2, since bishops 1 and 3 attack each other, as well as bishops 3 and 4.
'''

def bishopsOnBoard(bishops):
    count = 0
    for first in range(len(bishops)):
        first_bishop = bishops[first]
        for second in range(first, len(bishops)):
            second_bishop = bishops[second]
            x, y = first_bishop[0] - second_bishop[0], first_bishop[1] - second_bishop[1]
            # print(first_bishop, second_bishop, x, y, end=" ")
            if (y != 0 and (x / y == 1 or x / y == -1)) or (x != 0 and (y / x == 1 or y / x == -1)):
                # print("True")
                count += 1
            else:
                pass
                # print()
    return count

print(bishopsOnBoard([(4,0),(0,0), (1,2), (2,2), (4,4), (3,3),(2,3)]))

'''
[(4,0), (0,0), (1,2), (2,2), (4,4), (3,3), (2,3)]
[b 0 0 0 0]
[0 0 b 0 0]
[0 0 b b 0]
[0 0 0 b 0]
[b 0 0 0 b]

(4,0) (2,2)
(0,0) (2,2)
(0,0) (4,4)
(0,0) (3,3)
(1,2) (2,3)
(2,2) (4,4)
(2,2) (3,3)
(4,4) (3,3)
count == 8
'''