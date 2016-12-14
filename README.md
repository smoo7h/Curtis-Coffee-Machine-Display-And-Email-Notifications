# Curtis-Coffee-Machine-Display-And-Email-Notifications

Using a Raspberry PI and LCD Display, 

Displays the last time a coffee was brewed and sends an email notification for a Curtis Coffee Machine 

Parts : 

1 x Raspberry Pi 2

1 x Acrylic Stand for 16x2 Character LCD

1 x USB + Serial Backpack Kit with 16x2  RGB backlight positive LCD

1 x Fast Vibration Sensor Switch (Easy to trigger)

1 x Pibow Coupé - Enclosure for Raspberry Pi 2 / B+ / Pi 


Attach the vibration sensor to the inbound water tube attached to the coffee machnine. Connect this to GPIO #23 and the 3.3vPin on the Raspberry Pi 

Attach the LCD Display to the Raspberry Pi via USB

Modify the sendEmail() function with your own credentials

Run the application with 

sudo python CoffeeAlert.py &


Images of my setup:

http://imgur.com/a/w8ZXO
https://youtu.be/wBn5ZSc2Rgc
