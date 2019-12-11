import socket
from _thread import *
from player import Player
from car import Car
import pickle

server = "172.18.5.225"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)


s.listen(2)
print("Esperando conexões")

currentPlayer = 0


players = [Player(150,750,50,50,(255,0,0)), Player(650,750,50,50, (0,0,255))]



def threaded_client(conn, player):

    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(4096))
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]

                print("Received: ", data)
                print("Sending : ", reply)

                if ((players[0].pontuation == 3)or(players[1].pontuation == 3)) :
                    if players[0].pontuation == 3:
                        print("Player 1 Ganhou")
                        break
                    else:
                        print("Player 2 Ganhou")
                        break

            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    conn.close()

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
