photo = []
album = []
def isPhotobook(str):
    if str[0].isalpha() and str[-1].isalpha():
        return True
    else:
        return False
def hash(a,b):
    if ord(a) >= ord(b):
        return ord(b)+10
    else:
        return ord(a)-7
def calKey(s):
    ans = 0
    for j in range(len(s)-1):
        ans += hash(s[j],s[j+1])
    if isPhotobook(s) == True:
        photo.append(ans)
    else:
        album.append(ans)
    return ans
def isPhotobookGenuine(a):
    if a in album:
        return 'Incorrect Type'
    elif a %2 == 0:
        return True
    elif a%2 == 1:
        return False
def isAlbumGenuine(a):
    if a in photo:
        return 'Incorrect Type'
    elif a %2 == 1:
        return True
    elif a%2 == 0:
        return False
def solve():
    p = 0
    a = 0
    n = int(input())
    for i in range(n):
        s = input()
        x = calKey(s)
        if isPhotobookGenuine(x) == True:
            p+=1
        if isAlbumGenuine(x) == True:
            a+=1
    print(p)
    print(a)
   