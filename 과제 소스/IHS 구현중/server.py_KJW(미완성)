import socket, select
ef broadcast_chatroom (sock, message):
    #do not send the message to master socket and the client who has send us the message
    for socket in chatroom:
        if socket != server_socket and socket != sock :
             try :
                 socket.send(message)
             except:
                 # broken socket connection may be, chat client pressed ctrl+c for example
                 socket.close()
                 chatroom.remove(socket)

if __name__ == "__main__":

     #user_info = []
     user_info = [[]*4 for x in range(9)]

     user_info[0].append('qw')
     user_info[0].append('as')
     user_info[0].append('0')
     user_info[1].append('er')
     user_info[1].append('df')
     user_info[1].append('0')
     user_info[2].append('ty')
     user_info[2].append('gh')
     user_info[2].append('0')
     user_info[3].append('ui')
     user_info[3].append('jk')
     user_info[3].append('0')
     print (user_info)


     chatroom = []
     user_num = 0
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
         print 'g' #JW = to check how loop run
         # Get the list sockets which are ready to be read through select
         read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST,[],[])
         print "----------------read_socket----------------"
         print (read_sockets)
         print "----------------Connection----------------"
         print (CONNECTION_LIST)
         for sock in read_sockets:
             print "----------------sock-----------------"
             print (sock)
             #New connection
             if sock == server_socket:
                 # Handle the case in which there is a new connection recieved through server_socket
                 sockfd, addr = server_socket.accept()
                 CONNECTION_LIST.append(sockfd)
                 print "Client (%s, %s) connected" % addr

                 broadcast_data(sockfd, "[%s:%s] entered room\n" % addr)

             #Some incoming message from a client
             else:
                 # Data recieved from client, process it
                 try:
                     #In Windows, sometimes when a TCP program closes abruptly,
                     # a "Connection reset by peer" exception will be thrown
                     data = sock.recv(RECV_BUFFER)


                     #IHS = Recieved the data which the client send and i split it. then if there is the log message i send the ok message to the client.
                     print 'recieved data from client'
                     splitdata = data.split('\\')
                     print 'split the data'
                     if splitdata[0] == 'log':
                         print data
                         print splitdata
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
                         #JW = want to stop loop when client.socket suddenly disappear. but there is syntax error
                         
                         for x in CONNECTION_LIST:
                                if CONNECTION_LIST[] != sockfd:
                                sock.close()
                                CONNECTION_LIST.remove(sock)
                                continue

                      else:
                         if splitdata[0] == 'inv' :
                       #gotta change the client. if i chat by my own hands the client send this \\ to this \\. but if i send by s.send this \\ changes to \. so we must change this part with changing the client.py
                       #      splitdata[1] = (splitdata[1].split('\n'))[0]
                             splitdata[2] = (splitdata[2].split('\n'))[0]
                             print data
                             print splitdata
                             print splitdata[0]
                             print splitdata[1]
                             print splitdata[2]
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
                                         ChatRoom.append(User_Info[y][3])
                                         ChatRoom.append(User_Info[User_Num][3])
                                         #change the state of the user
                                         User_Info[y][2] = '2'
                                         User_Info[User_Num][2] = '2'
                                         sock.send('talknow')
                                         break
                                     else :
                                         sock.send('busy')
                                         break
                                 else :
                                     if y==3 :
                                         sock.send('unable')
                                         
                                         
                                         #IHS = the problem is i ain't made the User(Client) data. so I can't identify if the ID, PW is correct. must add the data and make it check
                     print 'aa' #JW = check where loop end
                     if data:
                         broadcast_chatroom(sock, "\r" + '<' + str(sock.getpeername()) + '> ' + data)
                
                 except:
                     broadcast_data(sock, "Client (%s, %s) is offline" % addr)
                     print "Client (%s, %s) is offline" % addr
                     sock.close()
                     CONNECTION_LIST.remove(sock)
                     continue 
     print 'd'  #JW = check where loop end
     server_socket.close()
