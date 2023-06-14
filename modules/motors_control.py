import board
import busio
import adafruit_pca9685
import time

# You can also set the frequency of the PWM signals
signal_freq = 50 

# Define Motor GPIOs
ena = 0
in1 = 1 
in2 = 2
in3 = 3
in4 = 4
enb = 5

# Define value constants
low_value = 0x0000
high_value = 0xFFFF

half_value = high_value

# Define motor arrays
left_motor = [in1, in2]
right_motor = [in3, in4]

# Setup I2C and PCA9685
i2c = busio.I2C(board.SCL_1, board.SDA_1)
pca = adafruit_pca9685.PCA9685(i2c)
pca.frequency = signal_freq  

# Define motor control functions
def forward():
    pca.channels[ena].duty_cycle = half_value
    pca.channels[enb].duty_cycle = half_value
    pca.channels[left_motor[0]].duty_cycle = high_value
    pca.channels[left_motor[1]].duty_cycle = low_value
    pca.channels[right_motor[0]].duty_cycle = high_value
    pca.channels[right_motor[1]].duty_cycle = low_value

def backward():
    pca.channels[ena].duty_cycle = half_value
    pca.channels[enb].duty_cycle = half_value
    pca.channels[left_motor[0]].duty_cycle = low_value
    pca.channels[left_motor[1]].duty_cycle = high_value
    pca.channels[right_motor[0]].duty_cycle = low_value
    pca.channels[right_motor[1]].duty_cycle = high_value

def turn_left():
    pca.channels[ena].duty_cycle = half_value
    pca.channels[enb].duty_cycle = half_value
    pca.channels[left_motor[0]].duty_cycle = low_value
    pca.channels[left_motor[1]].duty_cycle = high_value
    pca.channels[right_motor[0]].duty_cycle = high_value
    pca.channels[right_motor[1]].duty_cycle = low_value

def turn_right():
    pca.channels[ena].duty_cycle = half_value
    pca.channels[enb].duty_cycle = half_value
    pca.channels[left_motor[0]].duty_cycle = high_value
    pca.channels[left_motor[1]].duty_cycle = low_value
    pca.channels[right_motor[0]].duty_cycle = low_value
    pca.channels[right_motor[1]].duty_cycle = high_value

def stop():
    pca.channels[ena].duty_cycle = low_value
    pca.channels[enb].duty_cycle = low_value
    pca.channels[left_motor[0]].duty_cycle = low_value
    pca.channels[left_motor[1]].duty_cycle = low_value
    pca.channels[right_motor[0]].duty_cycle = low_value
    pca.channels[right_motor[1]].duty_cycle = low_value

# Make sure to call deinit() when done
def cleanup():
    pca.deinit()

try:
    while True:
        forward()
        time.sleep(3)
        stop()
        time.sleep(3)
        backward()
        time.sleep(3)
        stop()
        time.sleep(3)
        turn_left()
        time.sleep(3)
        stop()
        time.sleep(3)
        turn_right()
        time.sleep(3)
        stop()
        time.sleep(3)
except KeyboardInterrupt:
    print("Interrupted by Keyboard")

except Exception as e:
    print("An error occurred:", str(e))

finally:
    # Clean up after using the PCA9685
    cleanup()
