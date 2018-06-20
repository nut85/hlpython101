from gpiozero import LED
from time import sleep

red_led = LED(23)
yellow_led = LED(24)
green_led = LED(25)
blue_led = LED(8)

# print welcome message
print("Hello welcome to Elliette's BMI calculator.")
 
# get weight from user
pounds = int(input("What is your weight in pounds: "))
# print(pounds)

# get height from user 
inches = int(input("What is your height in inches: "))
# print(inches)

# convert pounds to kilograms
kilograms = pounds * 0.4535
# print(kilograms)

# convert inches to meters
meters = inches * 0.0254
# print(meters) 

# calculate BMI
# BMI = kg/m2 
BMI = kilograms/(meters * meters)
print(BMI)

# determine the range (under weight, normal, over weight, obese)
# underweight under 18.5
if BMI < 18.5:
    print("Underweight.")
    blue_led.on()    
# normal 18.5 - 25
if BMI >= 18.5 and BMI <= 25:
    print("Normal.")
    green_led.on()    
# overweight 25 - 30
if BMI > 25 and BMI <= 30: 
    print("Overweight.")
    yellow_led.on()    
# obese over 30
if BMI > 30:
    print("Obese.")
    red_led.on()    

sleep(10)    

