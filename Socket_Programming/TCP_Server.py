import socket

# Create a TCP/IP socket
server_socket = socket.socket ( socket.AF_INET , socket.SOCK_STREAM )

# Bind the socket to the port
server_address = ('localhost' , 65432)  # Use localhost and port 65432
server_socket.bind ( server_address )

# Listen for incoming connections
server_socket.listen ( 1 )
print ( "Server is listening on port 65432..." )

while True :
    # Wait for a connection
    connection , client_address = server_socket.accept ( )
    try :
        print ( f"Connection from {client_address}" )

        # Receive the data in small chunks and print it
        while True :
            data = connection.recv ( 1024 )
            if data :
                print ( f"Received: {data.decode ( 'utf-8' )}" )
                # Send a response back
                connection.sendall ( b"Message received" )
            else :
                break
    finally :
        # Clean up the connection
        connection.close ( )
