import multiprocessing 
  
def coming_people(conn, peoples): 

    for people in peoples: 
        conn.send(people) 
    conn.close() 
  
def welcoming_people(conn): 

    while True: 
        people = conn.recv()
        print("Welcome: {}".format(people)) 
  
if __name__ == "__main__": 
    # People to be welcome
    peoples = ["Ram", "Geeta", "Rajesh"] 
  
    # creating a pipe 
    parent_conn, child_conn = multiprocessing.Pipe() 
  
    # creating new processes 
    p1 = multiprocessing.Process(target=coming_people, args=(parent_conn,peoples)) 
    p2 = multiprocessing.Process(target=welcoming_people, args=(child_conn,)) 
  
    # running processes 
    p1.start() 
    p2.start() 
  
    # wait until processes finish 
    p1.join() 
    p2.join() 
