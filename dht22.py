import RPi.GPIO as GPIO
import time
import Adafruit_DHT as dht

# DHT22 센서를 GPIO 핀 4에 연결합니다.
DHT_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(DHT_PIN, GPIO.IN)

while True:
    try:
        print("성공")
        humidity, temperature_c = dht.read_retry(dht.DHT22, DHT_PIN)
        if temperature_c is not None:
            temperature_f = temperature_c * (9 / 5) + 32  #화씨온도f= 섭씨온도 c+32
            print(
                "온도: {:.1f} F / {:.1f} C  습도: {:.1f}% ".format(temperature_f, temperature_c, humidity)
            )   
        else:
            print("온도 데이터 실패")
    
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        raise error
    
    time.sleep(2.0)
