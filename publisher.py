import socket
import sys
import time


PORT = 50000


def main():
    # format: publish 'broker_ip_address' 'topic' 'value'
    while True:
        user_input = input('>')
        if user_input == 'quit':
            print('Program exit')
            sys.exit(0)
        ip = user_input.split(' ')[1]
        sys.stdout.flush()
        # connect to broker
        addr = (ip, PORT)
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(addr)
        except:
            print('Cannot connect to {0}'.format(addr[0]))
            sys.exit(0)
        finally:
            s.send(user_input.encode('utf-8'))
            s.close()


if __name__ == '__main__':
    main()
