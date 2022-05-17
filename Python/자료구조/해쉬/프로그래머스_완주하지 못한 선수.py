import collections

participant = ['a','b','a','c','d']
completion = ['a','b','c','d']

print(collections.Counter(participant), collections.Counter(completion))

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    print(answer)
    return list(answer.keys())[0]

print(solution(participant, completion))