import socket 


 # A estrutura funciona em 4 etaps, pelo mesno o que entendi até agora 
 # cliente envia um get, request, requisição
 # Servidor recebe esse get
 # servidor devolve 
 # Cliente recebe uma response

 # De forma grosseira, nesse primeiro codigo estamos simulando um cliente, um browser 

# Importamos socket como qualquer outra biblioteca 
# socket, files that we can send and receive, it's a two phases 


mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # says make a phone
mysock.connect(('data.pr4e.org', 80))                        # Dial the phone, to a domain name and woth the port domain = data.pr4e.org, port = 80, dail to this endpoint

# now the command that is th GET
# \r\n\r\n is just enter
# .encode is to say that is UTF-8, inside python is unicode. To convert, since python is unicode,we send in UTF-8
cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)  # we send the request

while True:

    data = mysock.recv(512)
    if len(data)<1:
        break
    print(data.decode(),end='')

mysock.close()

# At the first loop the connection is closed, so at the second one len(data) is <1 then the code break