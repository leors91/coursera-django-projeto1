from socket import *

# Imagine o socket do servidor como uma recepção de um hotel:

# A recepção (socket do servidor) está sempre aberta para receber hóspedes (clientes).
# Quando um hóspede chega, ele é atendido e encaminhado para um quarto (socket do cliente) onde poderá interagir diretamente com os serviços do hotel.
# A recepção continua disponível para receber novos hóspedes enquanto outros estão acomodados.

# Continua na ideia de 4 pontas em dois fluxos 
# Fluxo 1: Evio da requisição, Ponta 1: Socket do client, Ponta 2 Socket do Servidor
# Fluxo 2: Response do servidor, Ponta 3: Socket do servidor, Ponta 4: Socket de recebimento do cliente

def createServer():
    serversocket = socket(AF_INET, SOCK_STREAM)  # Criando o socket do servidor
    # AF_INET indica que o socket usa o protocolo IPv4.
    # SOCK_STREAM define que o socket é do tipo TCP (orientado a conexão), o que significa que ele garante entrega confiável e ordenada dos dados.

    try:
        serversocket.bind(('localhost', 9000))  # Vinculando o socket à porta 9000
        serversocket.listen(5)  # Configurando para ouvir até 5 conexões pendentes
        print('Server running on http://localhost:9000')
        
        while True:
            (clientsocket, address) = serversocket.accept()  # Aceitando uma conexão

            # Recebendo dados do cliente
            rd = clientsocket.recv(5000).decode()
            pieces = rd.split("\n")
            if len(pieces) > 0:
                print(pieces[0])  # Exibindo a primeira linha da requisição HTTP

            # Criando a resposta HTTP
            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>Hello World</body></html>\r\n"

            # Enviando a resposta para o cliente
            clientsocket.sendall(data.encode())  # Codificando a string para bytes
            clientsocket.shutdown(SHUT_WR)  # Encerrando a comunicação para escrita
            clientsocket.close()  # Fechando o socket do cliente

    except KeyboardInterrupt:
        print("\nShutting down...\n")
    except Exception as exc:
        print("Error:")
        print(exc)
    finally:
        serversocket.close()  # Garantindo o fechamento do socket do servidor


createServer()
