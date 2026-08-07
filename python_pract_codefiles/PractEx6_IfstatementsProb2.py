"""
Title: The Smart Product Delivery Classifier
Problem Statement: An e-commerce warehouse needs to sort items based on weight. 
Write a program that asks for an item's weight in kilograms.

If the weight is less than 2 kg, it goes to the "Drone Delivery" station.
If the weight is between 2 kg and 20 kg (inclusive), it goes to the "Standard Truck" station.
If the weight is greater than 20 kg, it goes to the "Heavy Freight" station.
"""


item_weight = float(input("Enter the weight of the item in kg: "))

if item_weight < 2:
    print("Assigned station: Drone Delivery")
elif item_weight > 2 and item_weight <= 5:
    print("Assigned station: Standard Truck")
elif item_weight > 5 and item_weight <= 20:
    print("Assigned station: Medium Freight")
elif item_weight > 20:
    print("Assigned station: Heavy Freight")