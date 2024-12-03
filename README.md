Ejercicio 1: Algoritmos de Sincronización
Implementar el algoritmo de Cristian para sincronizar el reloj de un cliente con un servidor en un sistema distribuido.

Escribir un programa en Python que:

Simule un cliente y un servidor con relojes inicializados a diferentes tiempos.

Calcule el retraso de red y sincronice el reloj del cliente utilizando el algoritmo.

Explique el funcionamiento del programa. Además, deben presentar el retraso o adelanto del reloj, cómo la latencia de red afecta la precisión del algoritmo. El programa debe indicar el procedimiento del algoritmo    

PARA QUE SIRVA EL PROYECTO SE DEBE CREAR UN ENTORNO VIRTUAL  -> activarlo -> instalar dependencias -> ejecutar el coomando de nameserver -> ejecutar los archivos con el entorno activo

python3 -m venv entorno_name
source entorno_name/bin/activate
pip install requirements.txt
python3 -m Pyro5.nameserver --host tuip 
python3 servidor.py
python3 cliente.py