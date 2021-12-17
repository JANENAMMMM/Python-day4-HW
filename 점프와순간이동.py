#점프와 순간 이동
def solution(n):
    battery=0
    while True:
        if n%2==0:
            n=n/2
        else:
            n=n-1
            battery+=1
        if n==0:
            break
    return battery