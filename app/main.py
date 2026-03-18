from config.settings import ENV, APP_NAME
from app.modules.temperature.monitor import run as run_temperature
from app.services.logger import log
from app.utils.helpers import separator
from app.services.database import db


def main():
    print(separator("SENTINEL"))
    log(f"{APP_NAME} INICIANDO...")
    log(f"ENTORNO: {ENV}")

    with db.connect() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        log(f"DB OK: {cursor.fetchone()[0]}")

    print(separator("MODULOS"))
    run_temperature()


if __name__ == "__main__":
    main()