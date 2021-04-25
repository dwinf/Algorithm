def isQueueFull():
    global SIZE, queue, front, rear
    if rear != SIZE - 1:
        return False
    elif (rear == SIZE-1) and (front == -1):
        return True
    else:
        for i in range(front+1, SIZE):
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
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

def peek():
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print('큐 텅')
        return
    return queue[front+1]


SIZE = 5
queue = [None, None, '문별', '휘인', '선미']
front = 1
rear = 4


#print('큐 꽉?', isQueueFull())
enQueue("대찬")
enQueue("대찬")
print(queue)