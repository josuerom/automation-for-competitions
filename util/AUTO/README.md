# AUTOMATIZACIONES

Para que las automatizaciones enfocadas a codeforces funcionen, necesariamente debe instalar un paquete, con el comando: `pip install requests` nada más.


Y con `pip install pyinstaller` puedes convertir los programas en `.exe` y agregarlos a las variables de entorno para que los puedas invocar desde cualquier parte de sistema.


Le comparto el comando:
```
pyinstaller --onefile --name=autocf gen_contest_cf_windows.py
```