
import sqlite3
connection = sqlite3.connect("my_database")

def friends_requests():
  
  your_username = input("Your username: ")
  
  print("You have a friend request from :")
  
  addRequest = " SELECT friendRequest from  pending_request WHERE user_name=?"
  
  result_table = connection.execute(addRequest, (your_username, ))
  
    #print(result_table.fetchall())
  
  a=result_table.fetchall()
  if a==None:
    print("no friend requests")
    #print(a[1]) 
    
  for i in range(len(a)):
    print(i+1, '. ', a[i])

  


  for i in range(len(a)):
    #print(i+1, '. ', a[i])
    print("who would you like to accept follow requests from? To exit type 0")
    answer=input("Their Username :")
    if answer=="0":
      return "home"
    if answer!="0":
      friend_name=answer
      addFriend = "INSERT INTO friends (user_name, friend_name) VALUES ('" + your_username + "','" + answer + "')"
      result_table=connection.execute(addFriend)
      connection.commit()
      print("Added to your friends list")
      a=result_table.fetchall()
      for i in range(len(a)):
         print(i+1, '. ', a[i])
      
      deleteRequest = " DELETE from pending_request WHERE user_name=? AND friendRequest=?"
      
      
      result_table = connection.execute(deleteRequest, (your_username,answer, ))
      
      connection.commit()
     
      result_table = connection.execute(addRequest, (your_username, ))
      a=result_table.fetchall()
      for i in range(len(a)):
         print(i+1, '. ', a[i])

      return ("home")

        
       


    