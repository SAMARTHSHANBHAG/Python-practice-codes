distance = 5

if distance < 3:
    transport = "Walk"
elif distance <= 15:
    transport = "Bike"
else:
    transport ="Car"

print("I recommend you the transport of:", transport)         