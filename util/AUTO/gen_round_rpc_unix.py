"""
Generador automático de archivos para rondas de la Red de programación Colombiana (RPC) para sistemas Unix
Autor: josuerom
Fecha: 16/06/25
"""

import os
import re
import glob
import shutil
import subprocess
from datetime import datetime


def buscarDocumentoPDF(dir_descargas):
   archivos_pdf = glob.glob(os.path.join(dir_descargas, "*.pdf"))
   for archivo in archivos_pdf:
      nombre_archivo = os.path.basename(archivo)
      if re.search(r"(problem|set|rpc|rnd)", nombre_archivo, re.IGNORECASE):
         return archivo
   return None


def generadorRondaRPCUnix():
   ronda = input("\033[93mRonda del año ->\033[0m ")
   ruta_base_rpc = r"/home/josuerom/Workspace/contests/RPC"
   fecha_hora = datetime.now()
   anio = fecha_hora.strftime("%Y")
   ruta_base_anio = os.path.join(ruta_base_rpc, anio)
   ruta_ronda = os.path.join(ruta_base_anio, f"Rnd{ronda}")

   if not os.path.exists(ruta_base_anio):
      os.makedirs(ruta_base_anio)

   if os.path.exists(ruta_ronda):
      print("\033[91mMijito/a ese round ya existe 😞.\033[0m")
      return

   ruta_descargas = r"/home/josuerom/Descargas"
   archivo_pdf = buscarDocumentoPDF(ruta_descargas)
   obtener_pdf, encontro_pdf = None, False

   if archivo_pdf:
      capturar_pdf = os.path.basename(archivo_pdf)
      obtener_pdf = os.path.join(ruta_descargas, capturar_pdf)
      encontro_pdf = True
   else:
      print("\033[91mMijito/a no se encontró el problemset.pdf 😞\033[0m")

   os.makedirs(ruta_ronda)

   if encontro_pdf:
      shutil.move(obtener_pdf, ruta_ronda)

   tem_cpp = r"/home/josuerom/Workspace/util/TEMPLATES/tem_rpc.cpp"
   tem_java = r"/home/josuerom/Workspace/util/TEMPLATES/tem.java"
   tem_py = r"/home/josuerom/Workspace/util/TEMPLATES/tem.py"

   nombre_equipo = "2 BITS"
   dia = fecha_hora.strftime("%d")
   mes = fecha_hora.strftime("%m")
   anio = fecha_hora.strftime("%Y")

   lista_id = (
      input("\033[93mQué problemas intentará resolver. Ej: [A B] ->\033[0m ")
      .upper()
      .split()
   )

   while True:
      template = int(
         input(
               "\033[93mSeleccione el lenguaje:\n1. cpp\n2. java\n3. python\n->\033[0m "
         )
      )
      ext = None
      if template == 1:
         template, ext = tem_cpp, "cpp"
      elif template == 2:
         template, ext = tem_java, "java"
      elif template == 3:
         template, ext = tem_py, "py"
      else:
         print("\033[91mMijito/a opción inválida. Intente de nuevo.\033[0m")
         continue
      break

   for problemID in lista_id:
      ruta_rpc = os.path.join(ruta_ronda, problemID)
      os.makedirs(ruta_rpc, exist_ok=True)
      archivo_base = os.path.join(ruta_rpc, f"{problemID}.{ext}")
      shutil.copyfile(template, archivo_base)

      with open(archivo_base, "r", encoding="utf-8") as plantilla:
         lineas = plantilla.readlines()

      lineas_del_archivo_ajustadas = []
      for linea in lineas:
         linea = (
               linea.replace("$%U%$", nombre_equipo)
               .replace("$%D%$", dia)
               .replace("$%M%$", mes)
               .replace("$%Y%$", anio)
               .replace("$%R%$", ronda)
               .replace("$%file%$", problemID)
         )

         lineas_del_archivo_ajustadas.append(linea)

      with open(archivo_base, "w", encoding="utf-8") as plantilla:
         plantilla.writelines(lineas_del_archivo_ajustadas)

      archivo_in = os.path.join(ruta_rpc, "in1")
      with open(archivo_in, "x"):
         pass

   print("\033[94mIniciando la ronda con VSCode...\033[0m")
   subprocess.run(f"code {ruta_ronda}", shell=True)
   # subprocess.run("pkill -f bash", shell=True)


if __name__ == "__main__":
   generadorRondaRPCUnix()
