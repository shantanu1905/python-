from datetime import date
today = date.today()
program_info="""Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics
$ ./todo exit             # Exit program"""
print(program_info)
#File_object = open(r"File_Name","Access_Mode")
while(True):
     #to count elements in todo.txt
    file = open("todo.txt","r")
    Counter = 0
    # Reading from file
    Content = file.read()
    CoList = Content.split("\n")
    for i in CoList:
        if i:
            Counter += 1
    #print("no of task todo")
    #print(Counter)
    todo_task=Counter



     #to count elements in done.txt
    file = open("done.txt","r")
    Counter = 0
    # Reading from file
    Content = file.read()
    CoList = Content.split("\n")
    for i in CoList:
        if i:
            Counter += 1
    #print("no of task done")
    #print(Counter)
    done_task=Counter

    

    
    
    user_input=input("./todo ")
## to add data to file    
    if(user_input=='add'):
        user=input("Add:")
        todo = open("todo.txt","a")
        todo.write(user +"\n")
        todo.close()
        print("Added todo "+user)

## to delete data from file       
    elif(user_input=='del'):
        user_del=int(input())
        try:
            
            todo= open("todo.txt", "r")
            lines = todo.readlines()
            todo.close() 
            del lines[user_del-1]
            new_file = open("todo.txt", "w+")
            for line in lines:
                new_file.write(line)
                new_file.close()
            print("deleted successfully")
        except IndexError:
            print("Error: todo #"+str(user_del)+ "does not exist. Nothing deleted.")
        
        
## to read data from file
    elif(user_input=='ls'):
        todo = open("todo.txt","r")
        read=todo.read()
        print(read)
        todo.close()



    
## complete task and add to done.txt file       
    elif(user_input=='done'):
        user_done=int(input())
        try:
            todo= open("todo.txt", "r")
            data=todo.readlines(user_done)                  
            todo.close()
            #conver list to str
            listToStr = ' '.join(map(str, data))
            #print(listToStr)
            #print( "Marked todo #"+str(user_done)+" as done.")
        
       
            #to add done task data to done.txt
            done = open("done.txt","a")
     
            done.write(str(today) + listToStr)
            done.close()

            #once todo added to done.txt now remove it from todo.txt
            todo= open("todo.txt", "r")
            lines = todo.readlines()
            todo.close() 
            del lines[user_done-1]
            new_file = open("todo.txt", "w+")
            for line in lines:
                new_file.write(line)
            new_file.close()
            print( "Marked todo #"+str(user_done)+" as done.")
        except IndexError:
            print("Error: todo #"+str(user_done)+ "does not exist.")
        

    elif(user_input=='help'):
        print(program_info)


    elif(user_input=='report'):
        print(str(today) + " Pending : "+ str(todo_task) +" Completed : "+ str(done_task))

    elif(user_input=='exit'):
        break

