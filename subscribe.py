import socket
import sys

PORT = 50000


def main():
    # format: subscribe 'broker_ip_address' 'topic'
    user_input = input('>')
    try:
        client_type, ip, topic = user_input.split(' ')
    except:
        print('Invalid input')
        sys.exit(0)
    # connect to broker
    addr = (ip, PORT)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect(addr)
    except:
        print('Cannot connect to {0}'.format(addr[0]))
        sys.exit(0)

    # successfully connect to broker then send a subsribed topic
    s.send(user_input.encode('utf-8'))
    print('Start listening to topic: ', topic)

    # stay receive subscribed data until keyboard interrupt is raise.
    while True:
        subscribed_data = s.recv(1024)
        if subscribed_data == b'':
            print("END")
            break
        print('{data}'.format(data=subscribed_data.decode('utf-8')))


if __name__ == '__main__':
    main()
