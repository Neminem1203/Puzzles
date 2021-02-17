# https://leetcode.com/problems/combination-sum/

def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """

    candidate_search = {0: []}
    ind = 0
    while ind < len(candidates):

        candidate = candidates[ind] # candidate we are looking at
        for search_ind in list(candidate_search): # need to turn into list so compiler doesnt complain about changing dict size
            multiple = 1 # multiple to check against the already established candidate_search
            limit = search_ind - (multiple * candidate)
            while limit >= 0: # checking to see if we go over the limit
                if limit not in candidate_search:
                    candidate_search[limit] = [] # initializing list
                for lst in candidate_search[search_ind]:                        # for each list
                    candidate_search[limit] += [lst + ([candidate]*multiple)]   # add that new list to new ind with [candidate]*multiple
                multiple += 1 # next multiple of the candidate
                limit = search_ind - (multiple * candidate) # new limit

        multiple = 1 # multiple to add to candidate_search
        while multiple * candidate <= target:
            new_candidate = candidate*multiple
            if target-new_candidate not in candidate_search:
                candidate_search[target-new_candidate] = [] # initializing list
            candidate_search[target-new_candidate] += [[candidate]*multiple] # adds multiple copies of candidate as long as its under target
            multiple += 1 # increment multiple
        ind += 1 # next candidate
    # print(candidate_search) # debugging
    return candidate_search[0] # return all candidate_searches that hit the target of 0


print(combinationSum([2,3,6,7], 7)) # [[2,2,3], [7]]
print(combinationSum([2,3,5], 8)) # [[2,2,2,2],[2,3,3],[3,5]]