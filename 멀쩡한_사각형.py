#멀쩡한 사각형
def solution(w,h):
    import math
    gcd=math.gcd(w,h)
    erase_per_sector=(w/gcd)+(h/gcd)-1
    erase_entire=erase_per_sector*gcd
    return w*h-erase_entire