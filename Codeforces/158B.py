def taxi():
    n = int(raw_input())
    s = raw_input().split(" ")
    s.sort(reverse = True)
    ans = 0
    i = 0
    j = len(s) - 1
 
    while i <= j:
        ans += 1
        four = 4 - int(s[i])
        while (int(s[j]) <= four) and (j >= i):
            four -= int(s[j])
            j -= 1
        i += 1
 
    print ans

taxi()
