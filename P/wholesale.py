data1 = []
data2 = {}
with open('wholesale.csv','r') as fp:
  header = fp.readline().strip().split(',')
  for i in fp.read().strip().split('\n'):
    data = {}
    w = i.strip().split(',')
    for j in range(len(header)):
      data[header[j]] = int(w[j])
      if header[j] not in data2:
        data2[header[j]] = [int(w[j])]
      else:
        data2[header[j]].append[int(w[j])]
    data1.append(data)