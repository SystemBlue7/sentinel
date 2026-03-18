from config.settings import ENV, APP_NAME
from app.modules.temperature.monitor import run as run_temperature
from app.services.logger import log
from app.utils.helpers import separator


def main():
    print(separator("SENTINEL"))
    log(f"{APP_NAME} INICIANDO...")
    log(f"ENTORNO: {ENV}")

    print(separator("MODULOS"))
    run_temperature()


if __name__ == "__main__":
    main()