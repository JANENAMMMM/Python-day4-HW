#오픈채팅방
def solution(record):
    answer = []
    status={}
    for event in record:
        list=event.split(" ")
        if (list[0]=="Enter") or (list[0]=="Change"):
            status[list[1]]=list[2]
    for event in record:
        list=event.split(" ")
        if list[0]=="Enter":
            answer.append(status[list[1]]+"님이 들어왔습니다.")
        elif list[0]=="Leave":
            answer.append(status[list[1]]+"님이 나갔습니다.")
    return answer
