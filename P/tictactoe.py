from mmap import MAP_PRIVATE
import random
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
def print_board(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
def checkwin(board):
    if board['top-L'] == board['top-M'] == board['top-R'] != ' ': return 'win'
    elif board['mid-L'] == board['mid-M'] == board['mid-R'] != ' ': return 'win'
    elif board['low-L'] == board['low-M'] == board['low-R'] != ' ': return 'win'
    elif board['top-L'] == board['mid-L'] == board['low-L'] != ' ': return 'win'
    elif board['top-M'] == board['mid-M'] == board['low-M'] != ' ': return 'win'
    elif board['top-R'] == board['mid-R'] == board['low-R'] != ' ': return 'win'
    elif board['top-L'] == board['mid-M'] == board['low-R'] != ' ': return 'win'
    elif board['top-R'] == board['mid-M'] == board['low-L'] != ' ': return 'win'
"""
def countbot(count):
    win1,win2,win3 = {'top-L': 0 , 'top-M': 0, 'top-R': 0},{'mid-L': 0, 'mid-M': 0, 'mid-R': 0},{'low-L': 0, 'low-M': 0, 'low-R': 0}
    win4,win5,win6 = {'top-L': 0,'mid-L': 0,'low-L': 0},{'top-M': 0,'mid-M': 0,'low-M': 0},{'top-R': 0,'mid-R': 0,'low-R': 0}
    win7,win8 = {'top-L': 0 ,'mid-M': 0,'low-R': 0},{'top-R': 0,'mid-M': 0,'low-L': 0}
    s1,s2,s3,s4,s5,s6,s7,s8=0,0,0,0,0,0,0,0
    for i,j in count.items():
        if i in win1: win1[i] = j
        if i in win2: win2[i] = j
        if i in win3: win3[i] = j
        if i in win4: win4[i] = j
        if i in win5: win5[i] = j
        if i in win6: win6[i] = j
        if i in win7: win7[i] = j
        if i in win8: win8[i] = j
    for i in range(3):
        s1+=win1[i]
        s2+=win2[i]
        s3+=win3[i]
        s4+=win4[i]
        s5+=win5[i]
        s6+=win6[i]
        s7+=win7[i]
        s8+=win8[i]
    if s1 == 2:
        for i,j in win1.items():
            if j == 0: return i
"""
def bot_turn(count,move):
    boards = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
    while(True):
        n = random.choice(list(boards.keys()))
        for i,j in count.items():
            if j == 0 and i == n:
                return n
            elif j==1 and i==n:
                n = random.choice(list(boards.keys()))

sym = ['X','O']
turn = random.choice(sym)
print(f"First turn is : {turn}")
print('Start')
ch = 0
move = ' '
count = {'top-L': 0 , 'top-M': 0, 'top-R': 0, 'mid-L': 0, 'mid-M': 0, 'mid-R': 0, 'low-L': 0, 'low-M': 0, 'low-R': 0}
cnt = list(count.items())
for i in range(9):
    print_board(theBoard)
    print("Player Turn :",turn)
    if turn == 'X':
        move = input()
    else:
        p = bot_turn(count,move)
        move = p
    theBoard[move] = turn
    count[move] += 1
    x = checkwin(theBoard)
    if x == 'win':
        ans = turn
        print_board(theBoard)
        print(f"winner : {ans} !!!!!")
        break
    if turn == 'X':
        p = bot_turn(count,move)
        turn = 'O'
    else:
        turn = 'X'
    ch+=1
    if ch == 9:
        print_board(theBoard)
        ans = 'tie'
        print(ans)
        break


     


