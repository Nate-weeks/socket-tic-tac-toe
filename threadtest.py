import time
from threading import Thread
import socket

def handleSocket(clientsocket):
    clientsocket.send("hello from thread 1")
