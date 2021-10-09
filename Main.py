# Hunter C. Sylvester
# Purpose: This tests my Bike class using different inputs and values

# Import our bike class
from bike import Bike


###############################################
# Instantiate a Bike object
###############################################
try:
    # Bianchi
    bianchi = Bike(19, 2, 9, "hand brakes")

    # Orbea
    # Now, instantiating a Bike object with no information initially.  You can change values below
    orbea = Bike()
    orbea.setNumberOfGears(10)
    orbea.setNumberOfWheels(4)
    orbea.setCurrentGear(9)
    orbea.setBrakeType("hand brakes")

    print(f"The number of gears my bike has is {bianchi.getNumberOfGears()}")
    print(f"The number of wheels my bike has is {bianchi.getNumberOfWheels()}")
    print(f"The current gear my bike is in is {bianchi.getCurrentGear()}")
    print(f"My bike has {bianchi.getBrakeType()}")
    input("Press [ENTER] to continue \n")
    
    # Increase Gear by 1
    bianchi.increaseGear((input('Would you like to increase the gear, "Yes" or "No?" ')))
    print()
    
    # Decrease Gear by 1
    bianchi.decreaseGear((input('Would you like to decrease the gear, "Yes" or "No?" ')))
    print()
    
    # Reset Gear to 1
    bianchi.resetGear((input('Would you like to reset the gear back to 1, "Yes" or "No?" ')))
    print()
    
    print(f"The number of gears my bike has is {orbea.getNumberOfGears()}")
    print(f"The number of wheels my bike has is {orbea.getNumberOfWheels()}")
    print(f"The current gear my bike is in is {orbea.getCurrentGear()}")
    print(f"My bike has {orbea.getBrakeType()}")
    input("Press [ENTER] to finish \n")
    
    print("FINISHED")

except Exception as e:
    print(f"Got an error: {e}")
