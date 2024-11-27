import datetime
import time
import Pyro5.api
HOST = "10.20.137.91"
PORT = 9091
def main():
    # Conectar con el servidor 
    timeserver = Pyro5.api.Proxy(f"PYRONAME:timeserver@{HOST}:{PORT}")

    print("Obteniendo hora del servidor...")

    # Paso 1: Captura el tiempo T1 antes de enviar la solicitud
    t1 = datetime.datetime.now()

    # Paso 2: Solicita la hora al servidor
    server_time = timeserver.get_server_time()

    # Paso 3: Captura el tiempo T2 después de recibir la respuesta
    t2 = datetime.datetime.now()

    # Paso 4: Calcular la latencia de ida y vuelta
    round_trip_delay = (t2 - t1).total_seconds() / 2

    # Paso 5: Ajustar el reloj del cliente
    corrected_time = server_time + datetime.timedelta(seconds=round_trip_delay)

    # Mostrar resultados
    print(f"Tiempo del cliente antes de sincronizar: {t1}")
    print(f"Tiempo del servidor: {server_time}")
    print(f"Tiempo del cliente después de sincronizar: {corrected_time}")
    print(f"Retraso de ida y vuelta (latencia): {round_trip_delay:.6f} segundos")

if __name__ == "__main__":
    main()
