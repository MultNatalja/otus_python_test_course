import socket
import http


def parse_request(data):
    method, headers = data.split("\r\n", 1)
    headers_dict = dict(header.split(": ", 1) for header in headers.split("\r\n")[1:])
    return method.split(" ")[0], headers_dict


def extract_status(data):
    try:
        status = data.split()[1].split("/?status=")
        if len(status) == 2:
            status_code = int(status[1].split()[0])
            return http.HTTPStatus(status_code)
    except (ValueError, IndexError) as e:
        print(f"Error: {e}")
    return None


def generate_response(connection, status, address, headers):
    status_line = f"HTTP/1.1 {status.value} {status.phrase}"
    response_headers = "\r\n".join([f"{key}: {value}" for key, value in headers.items()])

    response_body = (
            'Request-response headers:\r\n'
            f"Request Method: {headers.get('Method', 'Unknown')}\r\n"
            f'Request Source: {connection.getpeername()}\r\n'
            f'Response Status: {status}\r\n'
            'Request headers:\r\n'
            f"{response_headers}\r\n")

    return f"{status_line}\r\n" \
           f"Request Method: {headers.get('Method', 'Unknown')}\r\n" \
           f"Request Source: {address}\r\n" \
           f"Response Status: {status.value} {status.phrase}\r\n" \
           f"{response_headers}\r\n" \
           f"\r\n" \
           f"{response_body}".encode()


def run_server():
    host = "127.0.0.1"
    port = 8080

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serv_socket:
        print(f"Connecting to {host}:{port}")
        serv_socket.bind((host, port))
        serv_socket.listen()

        while True:
            print("Waiting request...")
            connection, address = serv_socket.accept()
            print("Connection from", address)

            data = connection.recv(1024)
            print(f"Received data: \n{data}\n")
            data = data.decode().strip()

            method, headers = parse_request(data)
            status = extract_status(data)

            if status is None:
                status = http.HTTPStatus(500)
                headers['Host'] = host

            response_data = generate_response(connection, status, address, {"Method": method, **headers})
            connection.sendall(response_data)
            connection.close()


if __name__ == "__main__":
    run_server()
