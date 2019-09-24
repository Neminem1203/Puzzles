'''
Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a starting airport, compute the person's itinerary. If no such itinerary exists, return null. If there are multiple possible itineraries, return the lexicographically smallest one. All flights must be used in the itinerary.

For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] and starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', you should return null.

Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A', you should return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. However, the first one is lexicographically smaller.
'''

def flightItinerary(flights, origin):
    def bestRoute(tripSoFar, remainingFlights):
        if(remainingFlights == []):
            return tripSoFar
        for path_num, flight in enumerate(remainingFlights):
            if(flight[0] == tripSoFar[-1]):
                testRoute = bestRoute(tripSoFar+[flight[1]], remainingFlights[:path_num] + remainingFlights[path_num+1:])
                if(testRoute != []):
                    return testRoute
        return []

    for path_num, flight in enumerate(flights):
        if(flight[0] == origin):
            returnRoute = bestRoute([flight[1]], flights[:path_num] + flights[path_num + 1:])
            if(returnRoute != []):
                return [origin]+returnRoute
    return None


print(flightItinerary([('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')], 'YUL'))
print(flightItinerary([('SFO', 'COM'), ('COM', 'YYZ')], 'COM'))
print(flightItinerary([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')], 'A'))