Network Programming
-------------------

Using Sockets:  Client Server Echo  Program
-------------------------------------------

**_Make sure that you have read and understood_**

*   **_module Unit 8_**
*   **_Helpful Python3 tutorial links:_**
    *   [**_Socket Programming: HOWTO_** (Links to an external site.)Links to an external site.](https://docs.python.org/3/howto/sockets.html)
    *   [**_Python3 NetworkProgramming_** (Links to an external site.)Links to an external site.](https://www.tutorialspoint.com/python3/python_networking.htm)

In this lab you will be using Python's socket module to create a simple working client server network program.  

**Understand the Application**

For this lab you will create a connection-oriented client-server program.  

At a low level, you will access the basic socket support in the underlying operating system, which allows you to implement clients and servers for connection-oriented network protocols.

**The Program Spec**

Write a program that establishes a network connection between a server and client on the same HOST and PORT.  

Establish a network connection between server and client.  Conduct a simple message transfer initiated by the client to the server.  Have the server echo the message back to the client. 

**Implementation Details**

Write a program that creates a simple echo server program that runs on a host and port available at your development disposal.  Then write a simple echo client program that runs on the same host and port as the server you are using.  Use Python's socket module to establish socket objects for both the client and server.  The server will first bind to the HOST and PORT used for your solution then listen for a connection request from the client. Have the server accept the client request.  The client will then send a message to the server.  The server will receive the message and send an echo back to the client mirroring the message received.  Close the network connection when either one of the parties closes its connection or sends an empty string.  

**Test Run Requirements:**

Here are some other _tips_ and requirements:

1\. Set the message buffer size to 1K.

2\. Run your server program before the client program in order to get channel connection established.

3\. Validate if there is an error creating the socket or binding to the host and port.

4\. Have the server print a statement to verify connection to the client.  

5\. Have the client print a statement echoing back the message received from the server. 

6\. Close the socket connections before your programs exit. 

**Deliverables: Submit 2 files:**

*   **yournameLab7server.py **Your source code solution for the server network program.
*   **yournameLab7client.py**  Your source code solution for the client network program.

Example run:
``` python
'''  
Connected by ('127.0.0.1', 57854)  #annFoothillLab7server.py output   
'''  
  
'''  
Received b'Demo Message - client: Ann Foothill'#annFoothillLab7client.py output  
'''
```