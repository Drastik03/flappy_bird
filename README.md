# FLAPPY BIRD GAME - PYGAME

Game created with python using OOP and pygame

## Instalación

1. Crea y activa un entorno virtual (asegúrate de tener `virtualenv` instalado):

   ```bash
   # Instala virtualenv si aún no lo tienes
   pip install virtualenv
   # Crea tu entorno virtual
   virtualenv venv
   # activa tu virtualenv
   source venv/bin/activate  # Para sistemas basados en Unix
   # o
   .\venv\Scripts\activate  # Para sistemas basados en Windows
   ```

2. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

## Uso

Ejecuta el juego en modo desarrollo

```bash

python flappy.py
```
## Conversion a .exe (archivo ejecutable)

Forma de distribucion del juego

```bash
pip install pyinstaller
# En sistemas basados en Windows
dist\flappy.exe
# En sistemas basados en Unix
./dist/flappy
