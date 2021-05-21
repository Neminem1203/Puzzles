def findJudge(n, trust):
    trusted_by = {}
    trust_someone = [False for _ in range(n)]
    for truster, trustee in trust:
        trust_someone[truster - 1] = True
        if trustee not in trusted_by:
            trusted_by[trustee] = []
        trusted_by[trustee].append(truster)

    for truster in range(1, n + 1):
        if trust_someone[truster - 1] == False:
            if truster in trusted_by and len(trusted_by[truster]) == n - 1:
                return truster
            elif n == 1:
                return truster
    return -1