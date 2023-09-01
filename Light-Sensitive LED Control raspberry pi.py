import RPi.GPIO as GPIO
import time

# Define GPIO pins
LED_PIN = 17  # Use the actual GPIO pin number you've connected the LED to
LDR_PIN = 18  # Use the actual GPIO pin number you've connected the LDR to

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(LDR_PIN, GPIO.IN)

try:
    while True:
        # Read the LDR value (0 or 1)
        ldr_value = GPIO.input(LDR_PIN)

        if ldr_value == GPIO.HIGH:
            # If the LDR is exposed to light, turn on the LED
            GPIO.output(LED_PIN, GPIO.HIGH)
        else:
            # If the LDR is in the dark, turn off the LED
            GPIO.output(LED_PIN, GPIO.LOW)

        time.sleep(1)  # Check the LDR every 1 second

except KeyboardInterrupt:
    # Clean up GPIO settings when exiting
    GPIO.cleanup()
