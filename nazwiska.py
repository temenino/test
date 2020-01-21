def all(names):
    n = sum(1 for x in names)
    return [n, len(names)]

try:
    f = open("nazwiska.txt", "r")
except FileNotFoundError:
    print('Nie znaleziono pliku nazwiska.txt')
    #nalezoloby obiac tym reszte kodu.....

lines = []
for line in f:
    lines.append(line.split(' '))

print(all(lines))

all_names = len(lines)
still_alive = len([x for x in lines if int(x[0]) > 0])
all_people = sum([int(x[0]) for x in lines])
print(all_names, still_alive, all_people)  #pkt a

avg_len_name = sum([int(x[0]) * (len(x[1]) - 1) for x in lines]) / all_people
print(avg_len_name) #pkt b


# alpha = 'abcdefghijklmnopqrstuvwxyz'
# alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

alpha = set(x[1][0] for x in lines)
alpha = sorted(list(alpha))

dic = {c : 0 for c in alpha}
print(dic)

for x in lines:
    dic[x[1][0]] += int(x[0])

for d in dic:
    print(d, ' : ', dic[d])  #pkt c

#raport
print("RAPORT:")
print("------------------------------------------------------------")
print('Liczba nazwisk w pliku :                            {:8}'.format(all_names))
print('Liczba nazwisk o liczbie wystąpień różnej od zera : {:8}'.format(still_alive))
print('Całkowita liczba ludności :                         {:8}'.format(all_people))
print("------------------------------------------------------------")
print('Średnią długość nazwiska ważona liczbą wystąpień :  {:8.4f}'.format(avg_len_name))
print("------------------------------------------------------------")
print('Liczba osób w zależności od pierwszej litery nazwiska : ')

for d in dic:
    print('{} : {:8}'.format(d, dic[d]))
print("------------------------------------------------------------")
f.close()