import datetime
import Pyro5.api


HOST = "10.20.137.91"
PORT = 9091

@Pyro5.api.expose
class TimeServer:
    def get_server_time(self):
        # Devuelve la hora actual del servidor
        server_time = datetime.datetime.now()
        return server_time

def main():
    # Configura el demonio de Pyro5 y registra el objeto del servidor
    daemon = Pyro5.server.Daemon(host = (HOST, PORT))  # Demonio Pyro5
    ns = Pyro5.api.locate_ns(host = HOST)      # Localiza el servidor de nombres
    uri = daemon.register(TimeServer)  # Registra el objeto
    ns.register("timeserver", uri)  # Registra el objeto en el servidor de nombres
    print("Servidor listo. Esperando clientes...")
    daemon.requestLoop()  # Mantiene al servidor en espera de solicitudes

if __name__ == "__main__":
    main()
'''
###
**ABRIR SERVER**
python3 -m Pyro5.nameserver --host 10.20.137.91 --port 9091
###'
'''