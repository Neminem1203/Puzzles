def minMaxDiff(document, searchTerm, min, max):
    minDiff = len(document)
    maxDiff = len(document)
    srchlen = len(searchTerm)
    for x in range(document.count(searchTerm)):
        found = document.find(searchTerm)
        document = document[:found]+(" "*srchlen)+document[found+srchlen:]
        if found > min and found+srchlen < max:
            return 0
        if found < min and minDiff > min - found:
            minDiff = min-found
        if found+srchlen > max and maxDiff > found+srchlen - max:
            maxDiff = found+srchlen - max
    if maxDiff < minDiff:
        return maxDiff
    else:
        return -minDiff

def newMinMax(document, searchTerms, min, max):
    first = searchTerms[0]
    del searchTerms[0]
    firstlen = len(first)
    returnMin = -1
    returnMax = len(document)
    for i in range(document.count(first)):
        found = document.find(first)
        document = document[:found] + (" " * firstlen) + document[found + firstlen:]
        newMin = found
        newMax = found+firstlen
        for i in (searchTerms):
            print("Before: ",newMin, newMax)
            found = minMaxDiff(document, i, newMin, newMax)
            if found > 0:
                newMax += found
            elif found < 0:
                newMin += found
            print("After: ",newMin, newMax)
        if newMax - newMin  < returnMax - returnMin:
            returnMin = newMin
            returnMax = newMax
            print("Return Min: ", returnMin)
            print("Return Max: ", returnMax)

    return [returnMin, returnMax]

def answer(document, searchTerms):
    n = 0
    lim = len(searchTerms)
    min = len(document)
    max = -1
    while(searchTerms):
        n+=1
        i = searchTerms[0]
        occurences = document.count(i)
        if(occurences > 1):
            print(min, max, searchTerms)
            if min > max:
                if lim > n:
                    searchTerms.append(i)
                    del searchTerms[0]
                else: # all search terms were found multiple times
                    [min, max] = newMinMax(document, searchTerms, min, max)
                    break
            else:
                found = minMaxDiff(document, i, min, max)
                if found > 0:
                    max += found
                elif found < 0:
                    min += found
                else:
                    pass
                del searchTerms[0]

            continue
        found = document.find(i)
        if found > min and found + len(i) < max:
            del searchTerms[0]
            continue
        if(found < min):
            min = found
        if(found+len(i) > max):
            max = found+len(i)
        del searchTerms[0]

    return document[min:max]


document = "many google employees can program"
searchTerms = ["google", "program"]

document = "a b c a d b c"
searchTerms = ["a", "c", "d"]

document = "many a people can hit a many targets and sometimes many are people"
searchTerms = ["many", "people"]

# document = "On September 24, 2008, just before the tobacco-free pharmacy ordinance was to take effect, Philip Morris USA, Inc. filed suit against the City and County of San Francisco in United States District Court.[6] Attorneys for Philip Morris argued unsuccessfully that the ordinance “forced the tobacco company to pull its advertising out of drugstores, interfering with its constitutional right to communicate with its customers”.[7] In addition to the lawsuit from Philip Morris, on September 8, 2008, Walgreens had more success when it sued the City and County of San Francisco in Superior Court of the State of California, claiming “unconstitutional discrimination” because the Walgreens location would not be allowed to sell cigarettes under the new ordinance whereas grocery and big box stores with pharmacies would be allowed to continue to sell.[7] After a number of legal appeals, Walgreens won the upper hand, with San Francisco ultimately deciding not to appeal."
# searchTerms = ["just", "tobacco", "City", "Philip"]

print("Search Terms: ",searchTerms)
print("Answer: ",answer(document,searchTerms))