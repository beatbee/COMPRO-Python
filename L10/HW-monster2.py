import numpy as np
class Game:
    def __init__(self,meh,monster):
        self.meh = meh ; self.monh = monster ; self.ch = 0 ; self.turn = 1 ; self.combo = 0 ; self.ms1 = []
    def player_attack(self):
        if self.ch == 0:
            self.combo = 10
            self.ch = 1
        elif self.ch == 1:
            self.combo+=2
        mx = -1
        for i in self.ms:
            if i[1] > mx and i[0] != 'me' and i[0] not in self.ms1:
                mx = i[1]
        for i in self.ms:
            if i[1] == mx and i[0] not in self.ms1:
                self.monh[i[0]]-=self.combo
                if self.monh[i[0]] <= 0:
                    self.ms1.append(i[0])
                    self.monh[i[0]] = 0
                print(f'Monster {i[0]} HP left {self.monh[i[0]]}')
    def player_health(self):
        self.ch = 0
        self.meh+=20*n
        self.combo = 10
        print(f'Your HP left {self.meh}')
    def mon_attack(self):
        self.a = X.randint(1, 40) 
        self.meh-=self.a
        if self.meh <= 0:
            self.meh = 0
        print(f'Your HP left {self.meh}')
    def play(self):
        self.ms = sorted(speed.items(), key=lambda x: x[1],reverse=True)
        while True:
            print('=========================')
            print(f'Turn {self.turn}')
            print('-------------------------')
            for i in self.ms:
                if i[0] == 'me':
                    print('- Your Turn -')
                    myTurn = input('Attack(a) or Heal(h): ')
                    if myTurn == 'a':
                        self.player_attack()
                    else:
                        self.ch = 0
                        self.player_health()
                else:
                    if i[0] in self.ms1:
                        continue
                    print(f'- Monster {i[0]} Turn -')
                    self.mon_attack()
                t = 0
                for i in self.monh:
                    if self.monh[i] <= 0:
                        t+=1  
                if t == n:
                    print('You win.(^_^)') 
                    exit(0)
                if self.meh == 0:
                    print('You lose and die.(T_T)')
                    exit(0)
            self.turn+=1       
bs = int(input('Blood Start: '))
mySpeed = int(input('Your speed: '))
n = int(input('Number of monsters: '))
X = np.random.RandomState(1)
meh = bs
monh = bs//n
speed = {}
monster = {}
speed['me'] = mySpeed
for i in range(n):
    x = int(input(f'Monster {i+1} speed: '))
    speed[f'{i+1}'] = x
    monster[f'{i+1}'] = monh
play = Game(meh,monster)
play.play()


    
    


