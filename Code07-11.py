def isQueueFull():
    global SIZE, queue, front, rear
    if ((rear + 1) % SIZE == front):
        return True
    else:
        return False

def isQueueEmpty():
    global SIZE, queue, front, rear
    if rear == front:
        return True
    else:
        return False

def enQueue(data):
    global SIZE, queue, front, rear
    if(isQueueFull()):
        print('큐 꽉')
        return
    rear = (rear + 1) % SIZE
    queue[rear] = data

def deQueue():
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print('큐 텅')
        return
    front = (front + 1) % SIZE
    data = queue[front]
    queue[front] = None
    return data

SIZE = 5
queue = ['화사', None, None, None, None]
front = -1
rear = 0

print(queue)
retData = deQueue()
print('추출 -->', retData)
retData = deQueue()
print('추출 -->', retData)
