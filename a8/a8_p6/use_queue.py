import module_queue
# imports the module module_queue, with all its functions
queue = ["Coca", "Fanta", "Lemonade"]

module_queue.enqueue(queue,"apple")
module_queue.enqueue(queue,"banana")
module_queue.enqueue(queue,"kiwi")
module_queue.printq(queue)
module_queue.dequeue(queue)
module_queue.dequeue(queue)
module_queue.dequeue(queue)
module_queue.printq(queue)
# from module, calls the function with param modified queue and prints it