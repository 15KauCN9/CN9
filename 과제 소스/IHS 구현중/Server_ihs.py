# Tcp Chat server 
  
import socket, select 
  
#Function to broadcast chat messages to all connected clients 
def broadcast_data (sock, message): 
    #Do not send the message to master socket and the client who has send us the message 
    for socket in CONNECTION_LIST: 
        if socket != server_socket and socket != sock : 
             try : 
                 socket.send(message) 
             except: 
                 # broken socket connection may be, chat client pressed ctrl+c for example 
                 socket.close() 
                 CONNECTION_LIST.remove(socket) 
                  
def broadcast_chatroom (sock, message, RN): 
    #Do not send the message to master socket and the client who has send us the message 
    for socket in ChatRoom[RN]: 
        if socket != server_socket and socket != sock : 
             try : 
                 socket.send(message) 
             except: 
                 # broken socket connection may be, chat client pressed ctrl+c for example 
                 socket.close() 
                 ChatRoom[RN].remove(socket) 
                  
if __name__ == "__main__": 
       
     #User_Info = []
     User_Info = [[]*5 for x in range(9)]

     User_Info[0].append('qw')
     User_Info[0].append('as')
     User_Info[0].append('0')
     User_Info[1].append('er')
     User_Info[1].append('df')
     User_Info[1].append('0')
     User_Info[2].append('ty')
     User_Info[2].append('gh')
     User_Info[2].append('0')
     User_Info[3].append('ui')
     User_Info[3].append('jk')
     User_Info[3].append('0')
     print (User_Info)


     #ChatRoom = []
     ChatRoom = [[]*4 for x in range(8)]
     User_Num = 0
     Count_Room = 0

     # List to keep track of socket descriptors 
     CONNECTION_LIST = [] 
     RECV_BUFFER = 4096 # Advisable to keep it as an exponent of 2 
     PORT = 5000
       
     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
     # this has no effect, why ? 
     server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
     server_socket.bind(("0.0.0.0", PORT)) 
     server_socket.listen(10) 
   
     # Add server socket to the list of readable connections 
     CONNECTION_LIST.append(server_socket) 
     
    

     print "Chat server started on port " + str(PORT)
   
     while 1: 
         # Get the list sockets which are ready to be read through select 
         read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST,[],[]) 
      #   print "----------------read_socket----------------"
      #   print (read_sockets)
      #   print "----------------Connection----------------"
      #   print (CONNECTION_LIST)
         for sock in read_sockets: 
             #print "----------------sock-----------------"
             #print (sock)
             #New connection 
             if sock == server_socket: 
                 # Handle the case in which there is a new connection recieved through server_socket 
                 sockfd, addr = server_socket.accept() 
                 CONNECTION_LIST.append(sockfd) 
                 print "Client (%s, %s) connected" % addr
                   
                 broadcast_data(sockfd, "[%s:%s] has login !!\n" % addr) 
               
             #Some incoming message from a client 
             else: 
                 # Data recieved from client, process it 
                 try: 
                     #In Windows, sometimes when a TCP program closes abruptly, 
                     # a "Connection reset by peer" exception will be thrown 
                     data = sock.recv(RECV_BUFFER)


		     #IHS = Recieved the data which the client send and i split it. then if there is the log message i send the ok message to the client.
		     #print 'recieved data from client' 
		     splitdata = data.split('\\')
		     #print 'split the data' 
                     if splitdata[0] == 'exit':
                         print "Client (%s, %s) is offline" % addr
                         sock.close() 
                         ChatRoom[RN].remove(socket) 
                         CONNECTION_LIST.remove(sock) 

		     if splitdata[0] == 'log':
                         #print data
                         #print splitdata
                         #IHS = Need to split because when i get the info from client they have extra '\n' on there back
                         splitdata[1] = (splitdata[1].split('\n'))[0]
                         splitdata[2] = (splitdata[2].split('\n'))[0]
			 
                         #IHS = Checking the info is right by comparing wiTh the Server's User_Info 
                         for x in range(4) : 
                             if (splitdata[1] == User_Info[x][0]) & (splitdata[2] == User_Info[x][1]) : 
                                 #Change the user state
                                 User_Info[x][2] = '1'
                                 User_Info[x].append(sock)
                                 #Send to client that the login is approved
                                 sock.send('ok')
			         break
                             else : 
                                 if x==3 :
				     sock.send('log fail')
	                 print 'Login Process'
                     else:
                         if splitdata[0] == 'inv' :
                       #gotta change the client. if i chat by my own hands the client send this \\ to this \\. but if i send by s.send this \\ changes to \. so we must change this part with changing the client.py
                             splitdata[1] = (splitdata[1].split('\n'))[0]
                             splitdata[2] = (splitdata[2].split('\n'))[0]
                             for x in range(4) : 
                                 #finding the one who send the invite msg
                                 if (splitdata[1] == User_Info[x][0]) : 
                                     #save the number of the msg sender
                                     User_Num = x
                                     break                             
			     for y in range(4) :
                                 #find the one who will be invite 
                                 if (splitdata[2] == User_Info[y][0]) : 
                                     #Check the user state
                                     if (User_Info[y][2] == '1') :
                                         #bind them in the chatroom
                                         ChatRoom[Count_Room].append(User_Info[y][3])
                                         ChatRoom[Count_Room].append(User_Info[User_Num][3])
                                         
                                         #change the state of the user
                                         User_Info[y].append(Count_Room)
                                         User_Info[y][2] = '2'
                                         User_Info[User_Num].append(Count_Room)
                                         User_Info[User_Num][2] = '2'
                                         Count_Room = Count_Room + 1
                                         sock.send('ChatNow\n')
                                         break
                                     else :
                                         sock.send('busy')
                                         break
                                 else : 
				     if y==3 :   
				         sock.send('unable')



		     #IHS = the problem is i ain't made the User(Client) data. so I can't identify if the ID, PW is correct. must add the data and make it check



                     if data: 
                         try : 
                             for x in range(4) : 
                                 #the problem is when 1,3 user is in 2 is empty so 3 can't talk in the room. it goes to except, when x == 2
                                 if (sock == User_Info[x][3]) & (Count_Room > 0) : 
                                     RoomNum = User_Info[x][4]
                                     break
                             broadcast_chatroom(sock, "\r" + '<' + str(sock.getpeername()) + '> ' + data, RoomNum)
                         except : 
                             Count_Room = Count_Room                
                   
                 except: 
                     broadcast_data(sock, "Client (%s, %s) is offline\n" % addr) 
                     print "Client (%s, %s) is offline" % addr
                     sock.close() 
                     CONNECTION_LIST.remove(sock) 
                     continue 
       
     server_socket.close() 
