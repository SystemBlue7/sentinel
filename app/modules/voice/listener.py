import speech_recognition as sr
from app.services.logger import log


def escuchar_palabra_clave(palabra_clave="sentinel"):
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)

    log("Modo escucha pasiva activado...")

    while True:
        try:
            with mic as source:
                audio = recognizer.listen(source)

            texto = recognizer.recognize_google(audio, language="es-ES").lower()

            if palabra_clave in texto:
                log("Palabra clave detectada.")
                return True

        except sr.UnknownValueError:
            continue
        except Exception as e:
            log(f"Error en escucha: {e}", level="error")