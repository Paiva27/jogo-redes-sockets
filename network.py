import socket
import pickle
from car import Car

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "172.18.5.225"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()
        self.cars = [Car(800,580,50,20,(80,80,80),5,1),Car(800,450,50,20,(80,80,80),5,1),Car(-20,300,50,20,(80,80,80),5,2),Car(-20,180,50,20,(80,80,80),5,2)]

    def getP(self):
        return self.p
    
    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(4096))
        except:
            pass

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(4096))
        except socket.error as e:
            print(e)