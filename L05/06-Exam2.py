n = int(input("Number of inputs: "))
score = {}
ch = {}
for i in range(n):
    x = input("Input name: ")
    y = float(input("Input score: "))
    if x in score.keys():
        score[x]+=y
        ch[x]+=1
    else:
        score.setdefault(x,y)
        ch[x] = 1
for i in score.keys():
    score[i]/=ch[i]
mx = max(score.values())
for i,j in score.items():
    if j == mx:
        print(f"Top score is {i}: {j:.2f}")
    
