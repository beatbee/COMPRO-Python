import json
grades = '''
[{"stdName": "Kun Toto", 
  "enrolledSuject": [
    ["01200101", "1", "A"],["01204111", "3", "A"],["01417167", "3", "B+"],
    ["01420111", "3", "C"],["01420113", "1", "B"],["01355113", "3", "C+"],
    ["01999021", "3", "A"]]},
  {"stdName": "Jane Happy", 
  "enrolledSuject": [
    ["01200101", "1", "B"],["01204111", "3", "C"],["01417167", "3", "D+"],
    ["01420111", "3", "B"],["01420113", "1", "A"],["01355113", "3", "B+"],
    ["01999021", "3", "C+"]]},
  {"stdName": "John Nepjune", 
  "enrolledSuject": [
    ["01200101", "1", "C"],["01204111", "3", "B"],["01417167", "3", "C+"],
    ["01420111", "3", "A"],["01420113", "1", "A"],["01355113", "3", "D+"],
    ["01999021", "3", "B+"]]}
]'''
grade = {'A':4,'B+':3.5,'B':3,'C+':2.5,'C':2,'D+':1.5,'D':1,'F':0}
data = json.loads(grades)
for i in data:
    print(i['stdName'])
    g,w = 0,0
    for j in i['enrolledSuject']:
        print(f'{j[0]} ({float(j[1]):.1f} , {j[2]})')
        g+=grade[j[2]]*int(j[1])
        w+=int(j[1])
    print(f'gpa : {g/w:.2f}')
