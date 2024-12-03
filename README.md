🕒 Ejercicio 1: Algoritmos de Sincronización
Implementar el algoritmo de Cristian para sincronizar el reloj de un cliente con un servidor en un sistema distribuido.

🎯 Objetivos del Ejercicio
Simular un cliente y un servidor con relojes inicializados a diferentes tiempos.
Calcular el retraso de red y sincronizar el reloj del cliente utilizando el algoritmo.
Explicar el funcionamiento del programa.
Mostrar el retraso o adelanto del reloj.
Describir cómo la latencia de red afecta la precisión del algoritmo.
Indicar claramente el procedimiento del algoritmo.
⚙️ Instrucciones para Usar el Proyecto
Crear un entorno virtual:
bash
Copiar código
python3 -m venv entorno_name
Activar el entorno virtual:
bash
Copiar código
source entorno_name/bin/activate
Instalar dependencias:
bash
Copiar código
pip install -r requirements.txt
Ejecutar el servidor de nombres:
bash
Copiar código
python3 -m Pyro5.nameserver --host tuip
Iniciar los archivos:
bash
Copiar código
python3 servidor.py
python3 cliente.py
🧠 Funcionamiento del Algoritmo
El algoritmo de Cristian sigue estos pasos:

El cliente registra la hora actual antes de enviar la solicitud al servidor.
El servidor responde con su hora actual.
El cliente calcula la diferencia teniendo en cuenta el retraso estimado de la red.
📊 Notas Importantes
Precisión del reloj: La latencia de red afecta directamente la sincronización.
Recomendación: Ejecutar en una red estable para minimizar errores de sincronización.
💡 Ejemplo de Salida
plaintext
Copiar código
Hora inicial del cliente: 10:30:45  
Hora inicial del servidor: 10:45:00  
Latencia de red estimada: 50 ms  
Hora ajustada del cliente: 10:45:00  
