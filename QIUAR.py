class Queue:
  
  
  def __init__(self):
 
    self.queue = list()
    
  
  def enqueue(self, data):
    if data not in self.queue:
      self.queue.insert(0, data)
      return True
    else:
      return False
   
  def dequeue(self):
    
    if len(self.queue) > 0:
      return self.queue.pop()
    else:
      return False
   
  
  def isEmpty(self):
    if len(self.queue) > 0:
      return False
    else:
      return True
 
  def size(self):
    return len(self.queue)
   
  def show(self):
    print(self.queue)
    
myQueue = Queue()
print(myQueue.enqueue(10)) 
print(myQueue.enqueue(5)) 
print(myQueue.enqueue("Hello")) 

print(myQueue.size()) 

print(myQueue.isEmpty())

myQueue.show() 

print(myQueue.dequeue()) 

myQueue.show() 
