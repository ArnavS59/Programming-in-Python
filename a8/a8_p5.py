
#funtion for adding at the end of the queue    
def enqueue(queue,elem):
    queue.append(elem)

#function for removing the front element of the queue     FIFO FIRST IN FIRST OUT    
def dequeue(queue):
    queue.pop(0)

#function for  printing the final content of queue
def printq(queue):
    print("elements of queue are", queue)


def main():
    queue=["Coca", "Fanta", "Lemonade"]
    #calling the 3 functions  
    enqueue(queue,"apple")
    enqueue(queue,"banana")
    enqueue(queue,"kiwi")
    printq(queue)
    dequeue(queue)
    dequeue(queue)
    dequeue(queue)
    printq(queue)

main()