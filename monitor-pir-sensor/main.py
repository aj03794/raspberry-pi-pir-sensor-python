# import pubsub.main
# from rx import Observable

# from RPi import GPIO
import time
import redis
import subject
from subject import create_subject

# create_subject = subject.create_subject
print('create_subject', create_subject)
(
    sensor_tripped,
    subscribe_to_sensor,
    filter
) = create_subject()

def pub_client(msg):
    print('foo msg', msg)

foo_subscription = subscribe_to_sensor(foo)
sensor_tripped('fake message')

# def setup_sensor():
#     publish = create_redis_client()
#     # GPIO.setwarnings(False)
#     # GPIO.setmode(GPIO.BOARD)
#     # Read output from PIR motion sensor
#     # GPIO.setup(11, GPIO.IN)
#     while True:
#         # i=GPIO.input(11)
#         i = 1
#         if i==0:                 #When output from motion sensor is LOW
#             print("No intruders", i)
#             publish('my-channel', 1)
#             time.sleep(1)
#         elif i==1:               #When output from motion sensor is HIGH
#             print("Intruder detected")
#             # Pubsub message out, set up Observable
#             time.sleep(1)


# setup_sensor()
