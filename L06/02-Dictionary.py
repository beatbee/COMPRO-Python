D = {'arm' : ['n','แขน'] , 'hello' : ['v','สวัสดี'] , 'beautiful' : ['adj','สวย'] , 'toilet' : ['n','ห้องน้ำ'] , 'kick' : ['v','เตะ'] , 'handsome' :['adj','หล่อ']}
while(True):
    word = input()
    if word == '0':
        break
    if word not in D:
        print("Word not in dictionary.")
    else:
        while(True):
            num = input()
            if num == '1' :
                print(D[word][0])
                break
            elif num == '2' :
                print(D[word][1])
                break
            else:
                print('Invalid option.')
"""
test:
beautiful
1
adj
beautiful
2
สวย
kick
3
Invalid option.
p 
Invalid option.
2
เตะ
0
"""