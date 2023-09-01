# Light-Sensitive-LED-Control-raspberry-pi
Controlling an LED with a Raspberry Pi based on light sensitivity involves using a light-dependent resistor (LDR) or a similar light sensor. You can read the sensor's values and use them to determine when to turn the LED on or off. Here's a step-by-step guide on how to set up light-sensitive LED control with a Raspberry Pi:

Materials Needed:

Raspberry Pi (any model with GPIO pins will work)
LED (any color)
220-330Ω resistor (for current limiting)
Light-dependent resistor (LDR)
Breadboard and jumper wires
Power supply for the Raspberry Pi
Internet connection (for software setup)
Steps:

Hardware Setup:

a. Connect the LED:

Connect the anode (longer leg) of the LED to one end of the current-limiting resistor.
Connect the other end of the resistor to one of the GPIO pins on the Raspberry Pi (e.g., GPIO17).
Connect the cathode (shorter leg) of the LED directly to a GND (ground) pin on the Raspberry Pi.
b. Connect the LDR:

Connect one leg of the LDR to a 3.3V pin on the Raspberry Pi.
Connect the other leg of the LDR to a different GPIO pin (e.g., GPIO18).
Connect a resistor (10kΩ is a typical value) from the LDR's second leg to the ground (GND) pin on the Raspberry Pi.
c. Ensure your Raspberry Pi is powered on and connected to the internet.

![image](https://github.com/AhMedMubarak20/Light-Sensitive-LED-Control-raspberry-pi/assets/76844219/6786d7c1-1503-48e0-a440-ab0c27651e6e)


Software Setup:

a. Make sure your Raspberry Pi is running a compatible operating system (e.g., Raspbian).

b. Update your system's package list and upgrade any existing packages by running these commands:

shell:
sudo apt update
sudo apt upgrade
c. Install Python libraries for GPIO control and any necessary sensor libraries:

shell:
sudo apt install python3-gpiozero
d. Create a Python script to read the LDR's values and control the LED. You can use any text editor or integrated development environment (IDE) you prefer. Here's an example Python script (save it as light_led.py):

python Code.

e. Run the script with the following command:

shell:
python3 light_led.py
Testing:

Observe the LED's behavior. It should turn on when the light level drops below the specified threshold (0.5 in the example) and turn off when it rises above the threshold.

You can adjust the threshold value in the script to make the LED respond to different light levels. This basic setup can be expanded upon for various light-sensitive applications, such as creating a simple light-activated switch or a nightlight.
