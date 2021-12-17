#키패드 누르기
def solution(numbers, hand):
    def closer(L,R,target):
        def indexing(a):
            if a==1:
                return [0,0]
            elif a==2:
                return [0,1]
            elif a==3:
                return [0,2]
            elif a==4:
                return [1,0]
            elif a==5:
                return [1,1]
            elif a==6:
                 return [1,2]
            elif a==7:
                return [2,0]
            elif a==8:
                return [2,1]
            elif a==9:
                return [2,2]
            elif a=="*":
                return [3,0]
            elif a==0:
                return [3,1]
            elif a=="#":
                return [3,2]
        Ldistance=abs(indexing(L)[0]-indexing(target)[0])+abs(indexing(L)[1]-indexing(target)[1])
        Rdistance=abs(indexing(R)[0]-indexing(target)[0])+abs(indexing(R)[1]-indexing(target)[1])
        if Ldistance<Rdistance:
            return "L"
        elif Ldistance>Rdistance:
            return "R"
        elif Ldistance==Rdistance:
            if hand=="right":
                return "R"
            elif hand=="left":
                return "L"     
    Rhand="#"
    Lhand="*"
    answer=[]
    for i in numbers:
        if i in [1,4,7,"*"]:
            Lhand=i
            answer.append("L")
        elif i in [3,6,9,"#"]:
            Rhand=i
            answer.append("R")
        elif i in [2,5,8,0]:
            if closer(Lhand,Rhand,i)=="L":
                Lhand=i
                answer.append("L")
            else:
                Rhand=i
                answer.append("R")
    return("".join(answer))