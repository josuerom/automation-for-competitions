# AUTOMATIZACIONES

Para que las automatizaciones enfocadas en concurso de `codeforces.com` funcionen, necesariamente debe instalar un paquete, con el comando: `pip install requests` nada más.


Y con `pip install pyinstaller` puedes convertir los programas en `.exe` y agregarlos al `Path` en las variables de entorno para que los puedas invocar desde cualquier parte de sistema Windows o Unix.


Comparto el comando:
```
pyinstaller --onefile --name=autocf gen_contest_cf_windows.py
```

En el directorio `dist` en contrará el archivo ejecutable para su añadidura.

Eso ha sido todo, hasta la próxima!