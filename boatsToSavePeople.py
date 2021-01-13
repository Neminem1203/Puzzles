def numRescueBoats(people, limit):
    """
    :type people: List[int]
    :type limit: int
    :rtype: int
    """
    sorted_people = people
    sorted_people.sort()
    count = 0  # number of boats

    while len(sorted_people) > 0:
        remaining = limit - sorted_people[-1]
        count += 1
        del sorted_people[-1]
        ind = len(sorted_people)-1
        while remaining > 0 and ind >= 0:
            if remaining >= sorted_people[ind]:
                remaining -= sorted_people[ind]
                del sorted_people[ind]
            ind -= 1

    return count


# print(numRescueBoats([1,2], 3))
# print(numRescueBoats([2,49,10,7,11,41,47,2,22,6,13,12,33,18,10,26,2,6,50,10], 50))
print(numRescueBoats([3,2,3,2,2],6))