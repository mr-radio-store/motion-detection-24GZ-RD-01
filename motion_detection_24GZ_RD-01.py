from machine import Pin
import time

# --- PIN DEFINITIONS ---
# OT1 (Motion) connected to GP2
# We use PULL_DOWN to ensure the pin stays at 0V when no motion is detected
motion_pin = Pin(2, Pin.IN, Pin.PULL_DOWN)    

# Internal LED for visual feedback on the Pico board
led = Pin(25, Pin.OUT)

print("-" * 30)
print("RD-01: ACTIVE MOTION DETECTION ONLY")
print("Listening on GP2 (OT1)...")
print("-" * 30)

while True:
    # Read the digital value from OT1
    # 1 = Motion detected, 0 = No motion
    is_moving = motion_pin.value()

    if is_moving:
        # This triggers ONLY when there is active movement (walking/waving)
        print(">>> STATUS: MOTION DETECTED!")
        led.value(1) # Turn on Pico LED
    else:
        # This triggers when the room is empty OR someone is sitting perfectly still
        print("--- STATUS: NOTHING DETECTED ---")
        led.value(0) # Turn off Pico LED

    # Check the sensor state 5 times per second
    time.sleep(0.2)