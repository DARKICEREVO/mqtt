import socket
from threading import Thread
import os
import sys

PORT = 50000

# initialize list of topic and value
topic_client_list = {}


def handle_client(s):
    global topic_client_list
    while True:
        try:
            txtin = s.recv(1024)
            client_type, payload = txtin.decode('utf-8').split(' ', 1)
            
            if client_type == 'subscribe':
                try:#in case of fail split ( more than format )
                    ip, topic = payload.split(' ')
                except:
                    s.close()
                    return
                print(ip, ' subscribe topic: ', topic)

                # check if topic is exists ??
                if topic_client_list.get(topic, False) != False:
                    # append client sckt in topic_client_list
                    topic_client_list[topic].append(s)
                else:
                        # if there is no topic yet then create in the list
                    topic_client_list.update({topic: [s]})

            elif client_type == 'publish':
                    # split data into topic and value
                try:#in case of fail split ( more than format )
                    ip, topic, value = payload.split(' ')
                except:
                    s.close()
                    return
                print(ip, ' publish topic: ', topic, ' value: ', value)
                    # check if topic is exists ??
                if topic_client_list.get(topic, False) != False:
                    for client_socket in topic_client_list.get(topic):
                        client_socket.send(value.encode('utf-8'))
                else:
                    topic_client_list.update({topic: []})
                s.send(b'-')
            else:
                break
        except:
            if topic in topic_client_list.keys():
                    if s in topic_client_list[topic] :
                        topic_client_list[topic].remove(s)
                        break
            break
    s.close()
    return


def main():
    addr = ('127.0.0.1', PORT)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(addr)
    s.listen(1)
    print('TCP broker connected ..\n')

    while True:
        sckt, addr = s.accept()
        try:
            Thread(target=handle_client, args=(sckt,)).start()
        except:
            print('Cannot start thread..\n')


if __name__ == '__main__':
    main()
