import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LIBS_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "libs"))

if LIBS_DIR not in sys.path:
    sys.path.insert(0, LIBS_DIR)

from app.services.logger import log
from app.services.voice import hablar
from app.modules.voice.listener import escuchar_palabra_clave


def main():
    log("Sentinel en modo pasivo...")

    while True:
        activado = escuchar_palabra_clave("sentinel")

        if activado:
            log("Activación detectada.")
            hablar("Sentinel en línea")


if __name__ == "__main__":
    main()