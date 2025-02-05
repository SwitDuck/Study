import socket
import ssl
class server_back():
    def shipher():
        import kuzn as sh
        algor_shipher = sh.kuznechik
        ... 
    def authentication():
        ... 
    def logging():
        ...
    ... 
class server_main():
    def vpn_server(host='0.0.0.0', port=1194):
        # Создаем TCP сокет
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        server_socket.listen(5)

        print(f"VPN сервер запущен на {host}:{port}")

        while True:
            client_socket, addr = server_socket.accept()
            print(f"Подключение от {addr}")

            # Настраиваем шифрование с использованием SSL
            context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
            context.load_cert_chain(certfile="server.crt", keyfile="server.key")

            secure_socket = context.wrap_socket(client_socket, server_side=True)

            try:
                # Обработка клиентского трафика
                while True:
                    data = secure_socket.recv(4096)
                    if not data:
                        break
                    print(f"Получено от клиента: {data}")
                    # Отправляем обратно данные клиенту (эхо-сервер)
                    secure_socket.sendall(data)
            except Exception as e:
                print(f"Ошибка: {e}")
            finally:
                secure_socket.close()

    if __name__ == '__main__':
        vpn_server()