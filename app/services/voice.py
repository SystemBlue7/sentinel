import asyncio
import os
import tempfile
import time
import edge_tts
import pygame

VOZ = "es-ES-AlvaroNeural"


async def _generar_audio(texto: str, ruta_audio: str):
    communicate = edge_tts.Communicate(
        text=texto,
        voice=VOZ,
        rate="-18%",
        pitch="-18Hz"
    )
    await communicate.save(ruta_audio)


def hablar(texto: str):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        ruta_audio = tmp.name

    asyncio.run(_generar_audio(texto, ruta_audio))

    if not pygame.mixer.get_init():
        pygame.mixer.init()

    pygame.mixer.music.load(ruta_audio)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    time.sleep(1.0)

    pygame.mixer.music.stop()
    pygame.mixer.quit()

    if os.path.exists(ruta_audio):
        os.remove(ruta_audio)