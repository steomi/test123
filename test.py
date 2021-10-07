def make_joust(arr):
    arr2 = []
    knight = arr[0]
    k = 0
    pos = 0
    for i in range(0, len(arr)):
        if arr[i] == knight:
            k += 1
        else:
            if k <= 1:
                pos = i
                knight = arr[i]

    for i in range(0, len(arr)):
        if i < pos or i > pos+k:
            arr2.append(arr[i])

    if k > 1:
        arr2.append(arr[pos]+1)
    else:
        arr2.append(arr[pos])
        return len(arr2)

    return arr2


n = int(input("кол-во рыцарей без Галахада: "))
r = str(input("ранги рыцарей: ")).split()
g = str(input("место и ранг Галахада: ")).split()


r2 = []
for i in range(len(r)):
    t = int(r[i])
    r2.append(t)


flag = True
gm = 0
gr = 0
for i in range(0, len(g)):
    if flag:
        flag = False
        gm = int(g[i])
    else:
        gr = int(g[i])


r3 = []
for i in range(0, len(r2)):
    if i == (gm-1):
        r3.append(r2[i])
        r3.append(gr)
    else:
        r3.append(r2[i])

p = sorted(r3)

for i in range(0, 20):
    p = make_joust(p)
    if not(isinstance(p, list)):
        print(p)
        break
