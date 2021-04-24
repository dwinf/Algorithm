katok = ['다현', '정현', '쯔위', '사나', '지효']

def delete_data(position) :

    if position < 0 or position > len(katok) :
        print('데이터를 삽입할 범휘를 벗어났습니다.')
        return

    kLen = len(katok)
    katok[position] = None

    for i in range(position+1, kLen) :
        katok[i-1] = katok[i]
        katok[i] = None

    del(katok[kLen-1])

delete_data(1)
print(katok)
delete_data(3)
print(katok)