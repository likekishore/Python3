for i in range(int(input())):
    S = input()
    T = input()
    ans = ""
    
    for i in range(5):
        if(S[i] == T[i]):
            ans += 'G'
        else:
            ans += 'B'
    
    print(ans)