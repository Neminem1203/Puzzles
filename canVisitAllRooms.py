# https://leetcode.com/explore/featured/card/march-leetcoding-challenge-2021/590/week-3-march-15th-march-21st/3677/
def canVisitAllRooms(rooms):
    """
    :type rooms: List[List[int]]
    :rtype: bool
    """
    # setup
    n = len(rooms)  # amount of rooms
    access = [False for _ in range(n)]  # is the room acessible?
    access[0] = True  # zeroth room always accessible
    keys = [0]  # you access to room 0 in the beginning

    while len(keys) > 0:  # while you still have rooms to visit
        visit = keys[0]  # room key
        keys = keys[1:]  # remove that key
        for i in rooms[visit]:
            if access[i] == False:
                access[i] = True
                keys.append(i)

    for room in access:
        if room == False:
            return False
    return True