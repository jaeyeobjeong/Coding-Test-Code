def solution(genres, plays):
    answer = []
    genres_time = {}

    for i in range(len(genres)):
        if genres[i] not in genres_time.keys():
            genres_time[genres[i]] = [(i, plays[i])]
        else:
            genres_time[genres[i]].append((i, plays[i]))

    g_lst = list(genres_time.items())
    g_lst.sort(key=lambda x: sum(x[1][1]), reverse=True) # 문제점 : sum은 1개의 value만 있는 경우 Error.

    for g in g_lst:
        g[1].sort(key=lambda x: (x[1], -x[0]), reverse=True)

    for _, p in g_lst:
        for i, _ in p[:2]:
            answer.append(i)

    return answer

def solution(genres, plays):
    answer = []
    d = {} # hash
    dN = {} # for calculating genres rank

    # assigning into dictionary
    for i in range(len(genres)):
        if genres[i] in d:
            d[genres[i]].append((plays[i], i))
            dN[genres[i]] += plays[i]
        else:
            d[genres[i]] = [(plays[i], i)]
            dN[genres[i]] = plays[i]

    # sorting in descending order for genres rank popularity.
    rank = sorted(dN, key=lambda x:dN[x], reverse=True)

    # getting item(genres) in descending order.
    for item in rank:
        # sorting songs based on the number of plays in descending order.
        temp = sorted(d[item], key=lambda x:(x[0],-x[1]), reverse=True)
        # printing twice only.
        for i in range(2):
            answer.append(temp[i][1])
            # if a particular genre has only one song, break the loop.
            if len(d[item])<2: break
    return answer