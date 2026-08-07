'''
Problem 6: The Autonomous Vehicle Speed Flag Filter
Problem Statement: Write a function named check_speed_violation that takes speed (integer) and zone (string: "school", "highway", or "residential"). 
It should return True if the vehicle is violating the speed limit for that zone, and False if it is traveling safely.
Limits: school: 30 km/h, residential: 50 km/h, highway: 100 km/h.
Expected Test Code: print(check_speed_violation(35, "school")) should output True.
Small Hint: Handle unmatched or unknown zones gracefully by returning a string or False based on your filtering architecture.
'''
def check_speed_violation(speed: float, zone: str) ->bool:
    if zone == 'school':
        return speed > 30       #return false if speed is less than or equal to 30, else return true
    elif zone == 'residential':
        return speed > 50
    elif zone == 'highway':
        return speed > 100
    else :
        return 'Invalid Zone Entry; Enter Valid Zone'
        
print(check_speed_violation(125,"school"))
        
    

