import datetime
import Pyro5.api


HOST = "192.168.1.60"
PORT = 9090

@Pyro5.api.expose
class TimeServer:
    def get_server_time(self):
        # Devuelve la hora actual del servidor
        server_time = datetime.datetime.now() #- datetime.timedelta(minutes=1) # PROBAR, SE PUEDE ANADIR, RESTAR O DEJAR LA HORA ACTUAL
        return server_time

#INICIAR EL SERVIDOR
def iniciar():

    demon = Pyro5.server.Daemon(host = HOST)  
    ns = Pyro5.api.locate_ns(host = HOST)  
    objeto_remoto = demon.register(TimeServer)  
    ns.register("timeserver", objeto_remoto)
    print("Se inicializa servidor RMI")
    print("LISTO PARA OTORGAR SERVICIO DE TIEMPO")

    demon.requestLoop()  

iniciar()
'''
###
**ABRIR SERVER**
python3 -m Pyro5.nameserver --host 10.20.137.91 

###'
'''