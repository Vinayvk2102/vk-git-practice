"""
Title: The Autonomous Vehicle Speed Governor
Problem Statement: Drawing inspiration from your work background, let's write a simplified diagnostic tool for an autonomous vehicle speed safety controller!
The program takes two inputs:

speed: The current vehicle speed (an integer in km/h).
zone: A string indicating the area type ("school", "highway", or "residential").

The vehicle is flagged as "VIO_SPEED" (Speeding Violation) if:
- In a "school" zone, its speed is strictly above 30 km/h.
- In a "residential" zone, its speed is strictly above 50 km/h.
- In a "highway" zone, its speed is strictly above 100 km/h.

If the speed is within the safe limit for that zone, print "STATUS_OK". 
If the user inputs an unknown zone type altogether, print "ERROR: Unknown Zone Diagnostics Code"
"""

usr_zone = str(input("Enter the vehicle traveling zone number (\"1 = school\", \"2 = highway\", or \"3 = residential\"): "))
if usr_zone == "1":
    zone = "school"
elif usr_zone == "2":
    zone = "highway"
elif usr_zone == "3":
    zone = "residential"
else:
    print("Invalid Zone: Please enter a valid zone number (\"1\", \"2\", or \"3\").")
    exit()

speed = float(input("Enter the vehicle's speed in km/h: "))
print(f"Vehicle Speed: {speed} km/h in {zone} zone.")
if zone == "school":
    if speed > 30:
        print("Alert!! VIO_SPEED - Speeding Violation: You are over the speed limit for a school zone.")
    else:
        print("Safe Driving: You are within the speed limit for a school zone.")
elif zone == "residential":
    if speed > 50:
        print("Alert!! VIO_SPEED - Speeding Violation: You are over the speed limit for a residential area.")
    else:
        print("Safe Driving: You are within the speed limit for a residential area.")
elif zone == "highway":
    if speed > 100:
        print("Alert!! VIO_SPEED - Speeding Violation: You are over the speed limit for a highway.")
    else:
        print("Safe Driving: You are within the speed limit for a highway.")
else:
    print("Invalid Zone: Please enter a valid zone (\"school\", \"highway\", \"residential\").")
