import multiprocessing 
  
def people(li, q): 

    for name in li: 
        q.put("Welcome "+ str(name)) 
  
def welcome_people(q): 

    print("Welcoming People: \n") 
    while not q.empty(): 
        print(q.get()) 

  
if __name__ == "__main__": 
    # input list 
    li = ['Ram','Geeta'] 
  
    # creating multiprocessing Queue 
    q = multiprocessing.Queue() 
  
    # creating new processes 
    p1 = multiprocessing.Process(target=people, args=(li, q)) 
    p2 = multiprocessing.Process(target=welcome_people,  args=(q,)) 
  
    # running process p1 to square list 
    p1.start() 
    p1.join() 
  
    # running process p2 to get queue elements 
    p2.start() 
    p2.join()
    print("hello", "hi")


