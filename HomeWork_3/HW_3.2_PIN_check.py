##### PIN Check #####

### User date
SECRET_PIN = 9999
#### user interface ####
input_pin = 0000
num_of_attempts = 3
while input_pin != SECRET_PIN:
    print("Mai aveti", num_of_attempts, " incercari")
    input_pin = int(input("PIN: "))
    if num_of_attempts == 1:
        break
    num_of_attempts -= 1
