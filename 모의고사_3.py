#itertools.cycle , enumerate 사용 x
#모의고사_itertools.cycle 이용x, enumerate 사용
def solution(answers):
    p1=[1,2,3,4,5]
    p2=[2,1,2,3,2,4,2,5]
    p3=[3,3,1,1,2,2,4,4,5,5]
    scores=[0,0,0]
    result=[]
    index1=0
    for answer in answers:
        if answer==p1[index1%len(p1)]:
            scores[0]+=1
        if answer==p2[index1%len(p2)]:
            scores[1]+=1
        if answer==p3[index1%len(p3)]:
            scores[2]+=1
        index1+=1
    index2=0
    for score in scores:
        if score==max(scores):
            result.append(index2+1)
        index2+=1
    return result
        