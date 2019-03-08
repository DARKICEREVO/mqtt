import socket
import sys

PORT = 50000


def main():
    # format: publish 'broker_ip_address' 'topic' 'value'
    user_input = input('>')
    if user_input == 'quit':
        print('Program exit')
        sys.exit(0)
    ip = user_input.split(' ')[1]
    sys.stdout.flush()
    # connect to broker
    addr = (ip, PORT)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect(addr)
    except:
        print('Cannot connect to {0}'.format(addr[0]))
        sys.exit(0)

    # successfully connect to broker
    while True:
        s.send(user_input.encode('utf-8'))
        if user_input == 'quit':
            print('Program exit')
            break
        user_input = input('>')
        sys.stdout.flush()


if __name__ == '__main__':
    main()
