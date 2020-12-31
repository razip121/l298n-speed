# l298n-speed speed Module
This module is designed to be used with three GPIO pins on the Raspberry Pi.
the enable pin sets the speed and the other two the direction

## Usage
First, create an instance of l298n-speed using 3 GPIO pin numbers from the raspberry pi as
attributes. Use the GPIO number as opposed to the board number.

attributes are in following order: enable pin, pin 1, pin 2
most l298n board name them: ena, in1, in2

```python
from l298n-speed import l298n
motor = l298n(1, 2, 3)
```

Then, using methods from l298n, a motor can be activated in the desired direction.
```python
motor.forward(80)
motor.backward()
motor.stop()
```
if no speed is given it will be set to 100, else a pwm signal will be set to lower the speed


## Contributions
If you see areas for improvement in this module, please submit an issue or
feel free to email me. All contributions are welcome.
