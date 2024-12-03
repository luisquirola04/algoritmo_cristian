import datetime
import time  # Importar para manejar la espera
import Pyro5.api

HOST = "192.168.1.60"

def main():
    # Conectar con el servidor 
    timeserver = Pyro5.api.Proxy(f"PYRONAME:timeserver@{HOST}")

    print("Obteniendo hora del servidor...")

    # 1: Captura el tiempo T1 antes de enviar la solicitud
    t1 = datetime.datetime.now()

    # 2: Solicita la hora al servidor
    server_time = timeserver.get_server_time()

    # CONVERSION DE LO QUE DEVUELVE EL SERVIDOR A UN FORMATO QUE SE PUEDA MANIPULAR
    if isinstance(server_time, str):
        server_time = datetime.datetime.strptime(server_time, "%Y-%m-%dT%H:%M:%S.%f")

    # 3: Captura el tiempo T2 después de recibir la respuesta
    t2 = datetime.datetime.now()

    # 4: Calcular la latencia de ida y vuelta
    calculo_latencia = (t2 - t1).total_seconds() / 2

    # 5: Ajustar el reloj del cliente
    corrected_time = server_time + datetime.timedelta(seconds=calculo_latencia)

    # 6: Verificar si hay que detenerse
    if t2 < corrected_time:
        tiempo_espera = (corrected_time - t2).total_seconds()
        print(f"El tiempo actual del cliente es menor al tiempo corregido. Esperando {tiempo_espera:.6f} segundos...")
        time.sleep(tiempo_espera)
    else:
        print("El tiempo del cliente ya está sincronizado con el servidor. No es necesario esperar.")

    # Resultados
    print(f"Tiempo del cliente antes de sincronizar: {t1}")
    print(f"Tiempo del servidor: {server_time}")
    print(f"Tiempo del cliente después de sincronizar: {datetime.datetime.now()}")
    print(f"Retraso de ida y vuelta (latencia): {calculo_latencia:.6f} segundos")

if __name__ == "__main__":
    main()
