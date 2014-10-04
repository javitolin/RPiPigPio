import pigpio
from time import sleep

Motor1A = 23 #PIN 16
Motor1B = 24 #PIN 18
Motor1E = 25 #PIN 22

Motor2A = 10 #PIN 19
Motor2B = 9  #PIN 21
Motor2E = 11 #PIN 23
pi = pigpio.pi()

pi.set_mode(Motor1A, pigpio.OUTPUT)
pi.set_mode(Motor1B, pigpio.OUTPUT)
pi.set_mode(Motor1E, pigpio.OUTPUT)
pi.set_mode(Motor2A, pigpio.OUTPUT)
pi.set_mode(Motor2B, pigpio.OUTPUT)
pi.set_mode(Motor2E, pigpio.OUTPUT)
pi.set_PWM_range(Motor1E,100)
pi.set_PWM_range(Motor2E,100)

pi.write(Motor1A, 0)
pi.write(Motor1B, 1)
pi.write(Motor1E, 1)
pi.write(Motor2A, 0)
pi.write(Motor2B, 1)
pi.write(Motor2E, 1)

pi.set_PWM_dutycycle(Motor1E, 0)
pi.set_PWM_dutycycle(Motor2E, 0)
sleep(2)
print("Duty cycle 25")
pi.set_PWM_dutycycle(Motor1E, 25)
pi.set_PWM_dutycycle(Motor2E, 25)
sleep(2)
print("Duty cycle 40")
pi.set_PWM_dutycycle(Motor1E, 40)
pi.set_PWM_dutycycle(Motor2E, 40)
sleep(2)
print("Duty cycle 80")
pi.set_PWM_dutycycle(Motor1E, 80)
pi.set_PWM_dutycycle(Motor2E, 80)
sleep(2)
print("Duty cycle 100")
pi.set_PWM_dutycycle(Motor1E, 100)
pi.set_PWM_dutycycle(Motor2E, 100)
sleep(2)
pi.set_PWM_dutycycle(Motor1E,0)
pi.set_PWM_dutycycle(Motor2E,0)
pi.stop()