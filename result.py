# 1.jautajums

vertiba=[]
list=[]

with open("data.txt","r") as f:
    next(f)
    for line in f:
        row=line.rstrip().split(",")
        list.append(row)

for row in list:
    if (row[4]=="Oman"):
        vertiba.append(int(row[6]))

print(min(vertiba))


# 2.jautajums

vertiba=[]
list=[]
darbinieki=0

with open("data.txt","r") as f:
    next(f)
    for line in f:
        row=line.rstrip().split(",")
        list.append(row)

for row in list:
    if (row[4]=="Latvia"):
        vertiba.append(int(row[8]))

print(len(vertiba))


# 3.jautajums

vertiba=[]
list=[]
darbinieki=0

with open("data.txt","r") as f:
    next(f)
    for line in f:
        row=line.rstrip().split(",")
        list.append(row)

for row in list:
    if (row[7]=="Telecommunications") and (row[4]=="Latvia"):
        darbinieki=darbinieki+1

print(darbinieki)


# 4.jautajums

vertiba=[]
list=[]
kompanijas=0

with open("data.txt","r") as f:
    next(f)
    for line in f:
        row=line.rstrip().split(",")
        list.append(row)

for row in list:
    if (row[4]=="Latvia") and (row[3].startswith('https://')):
        kompanijas=kompanijas+1

print(kompanijas)


# 5.jautajums

vertiba = []
list = []
kompanijas = 0

with open("data.txt", "r") as f:
    next(f)
    for line in f:
        row = line.rstrip().split(",")
        list.append(row)

for row in list:
    if row[4] == "Latvia" and (row[3].endswith('.org/')):
        kompanijas=kompanijas+1

print(kompanijas)
