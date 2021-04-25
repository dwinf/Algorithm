def isQueueFull():
    global SIZE, queue, front, rear
    if rear == SIZE - 1:
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
    rear += 1
    queue[rear] = data

def deQueue():
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print('큐 텅')
        return
    front += 1
    data = queue[front]
    queue[front] = None
    return data

SIZE = 5
queue = ['화사', '솔라', '문별', '휘인', None]
front = -1
rear = 3

print(queue)
enQueue('선미')
print(queue)
enQueue('대찬')
print(queue)