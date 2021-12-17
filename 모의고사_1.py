#모의고사_itertools.cycle이용
def solution(answers):
    import itertools
    inf_m1=iter(itertools.cycle([1,2,3,4,5]))
    inf_m2=iter(itertools.cycle([2,1,2,3,2,4,2,5]))
    inf_m3=iter(itertools.cycle([3,3,1,1,2,2,4,4,5,5]))
    inf_answers=iter(answers)
    scores=[0,0,0]
    for i in range(len(answers)):
        value=next(inf_answers)
        if value==next(inf_m1):
            scores[0]+=1
        if value==next(inf_m2):
            scores[1]+=1
        if value==next(inf_m3):
            scores[2]+=1
    if max(scores)==scores[0]==scores[1]==scores[2]:
        return([1,2,3])
    elif max(scores)==scores[0]==scores[1]:
        return([1,2])
    elif max(scores)==scores[0]==scores[2]:
        return([1,3])
    elif max(scores)==scores[1]==scores[2]:
        return([2,3])
    elif max(scores)==scores[0]:
        return([1])
    elif max(scores)==scores[1]:
        return([2])
    elif max(scores)==scores[2]:
        return([3])