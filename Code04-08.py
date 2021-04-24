# 클래스와 함수 선언부
class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):
    current = start
    if current == None:
        return
    print(current.data, end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()

def insertNode(findData, insertData):
    global memory, head, pre, current # 전역변수를 가져다 쓰는 파이썬 문법

    if head.data == findData: # 첫 노드 앞에 삽입
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return

    current = head
    while current.link != None: # 중간 노드 앞에 삽입
        pre = current
        current = current.link
        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return

    node = Node() # 마지막 노드로 삽입
    node.data = insertData
    current.link = node

def deleteNode(deleteData):
    global memory, head, pre, current  # 전역변수를 가져다 쓰는 파이썬 문법

    if head.data == deleteData:
        current = head
        head = current.link
        del(current)
        return

    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == deleteData:
            pre.link = current.link
            del(current)
            return

def findNode(findData):
    global memory, head, pre, current  # 전역변수를 가져다 쓰는 파이썬 문법

    current = head
    if current.data == findData:
        return current
    while current.link != None:
        current = current.link
        if current.data == findData:
            return current
        return Node()


## 전역 변수부
memory = []
head, current, pre = None, None, None
dataArray = ['다현', '정현', '쯔위', '사나', '지효']

## 메인 코드부
# 첫 노드
node = Node()
node.data = dataArray[0]
head = node
memory.append(node)

for data in dataArray[1:]:
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)

printNodes(head)
insertNode('다현', '화사')
printNodes(head)
insertNode('사나', '솔라')
printNodes(head)
insertNode('재남', '문별')
printNodes(head)
print()

deleteNode('화사')
printNodes(head)
deleteNode('쯔위')
printNodes(head)
deleteNode('문별')
printNodes(head)
deleteNode('모모')
printNodes(head)
print()

fNode = findNode('다현')
print(fNode.data)
fNode = findNode('정현')
print(fNode.data)
fNode = findNode('대찬')
print(fNode.data)