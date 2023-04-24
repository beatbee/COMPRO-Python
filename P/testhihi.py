file = input('File : ')
D = {}
data = {}
with open(file,'r') as fp:
    header = fp.readline().split(',')
    for i in fp.read().split('\n'):
        if i != '':
            head = ''
            w = i.strip().split(',')
            head = f'{w[0]}   {w[1]}'
            #print(head)
            D[head] = []
            for j in range(2,len(header)-2):
                D[head].append(float(w[j]))
            for k in range(len(header)):
                if header[k] not in data:
                    data[header[k]] = [float(w[k])]
                else:
                    data[header[k]].append(float(w[k]))

print(header)
x= '\"longitude\"'
print(len(D))
#california_housing_test.csv