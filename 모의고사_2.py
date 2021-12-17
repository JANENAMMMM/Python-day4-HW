#모의고사_itertools.cycle 이용x, enumerate 사용
#나머지(%)로 인덱스 표현해주기
def solution(answers):
    p1=[1,2,3,4,5]
    p2=[2,1,2,3,2,4,2,5]
    p3=[3,3,1,1,2,2,4,4,5,5]
    scores=[0,0,0]
    result=[]
    for index,answer in enumerate(answers):
        if answer==p1[index%len(p1)]:
            scores[0]+=1
        if answer==p2[index%len(p2)]:
            scores[1]+=1
        if answer==p3[index%len(p3)]:
            scores[2]+=1
    for index,score in enumerate(scores):
        if score==max(scores):
            result.append(index+1)
    return result
        