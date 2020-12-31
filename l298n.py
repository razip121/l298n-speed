import RPi.GPIO as GPIO

class L298N:
    """A class to control one side of an L298N dual H bridge motor driver with speed control."""
    def __init__(self, ena, in1, in2):
        self.in1 = in1
        self.in2 = in2
        self.ena = ena
        all_pins = [self.ena, self.in1, self.in2]
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(all_pins, GPIO.OUT)
        GPIO.setwarnings(False)

    def forward(self, speed=100):
        pwm = GPIO.PWM(self.ena, 800)
        pwm.start(speed)
        GPIO.output(self.in1, 1)
        GPIO.output(self.in2, 0)

    def backward(self, speed=100):
        pwm = GPIO.PWM(self.ena, 800)
        pwm.start(speed)
        GPIO.output(self.in1, 0)
        GPIO.output(self.in2, 1)

    def stop(self):
        pwm = GPIO.PWM(self.ena, 800)
        pwm.stop()
        GPIO.output(self.ena, 0)
        GPIO.output(self.in1, 0)
        GPIO.output(self.in2, 0)

    def cleanup(self):
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
