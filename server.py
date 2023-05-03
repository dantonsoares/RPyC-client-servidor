import os
import threading
from rpyc.utils import server
import rpyc

class DoStuff(rpyc.Service):
    votes = {"city": 0, "real": 0}

    def exposed_vote(self, candidate):
        self.votes[candidate] += 1
        print(f"Voto recebido para {candidate} pelo processo com ID {os.getpid()}, na thread de ID {threading.get_ident()}")
    
    def exposed_get_votes(self):
        return self.votes

if __name__ == "__main__":
    server.ThreadPoolServer(
        DoStuff,
        hostname='localhost',
        port=8000
    ).start()
