import speech_recognition as sr
import serial
import time

ser = serial.Serial('COM4', 9600)

def speech_recognition():
    sr.Microphone(device_index = 0)
    r = sr.Recognizer()
    r.energy_threshold=55
    r.dynamic_energy_threshold = False

    while True:
        with sr.Microphone(device_index=0) as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            try:
                frase = r.recognize_google(audio, language="es-ES")
                print(frase)

                if "minina" in frase:
                    ser.write(b'1')
                    time.sleep(3)
                    ser.write(b'0')
                    time.sleep(1)
            except sr.UnknownValueError:
                print("No se pudo entender el mensaje")
            time.sleep(1)
speech_recognition()    