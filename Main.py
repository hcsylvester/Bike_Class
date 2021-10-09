from bike import Bike

try:
    bianchi = Bike(19, 2, 9, "hand brakes")

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

    bianchi.increaseGear((input('Would you like to increase the gear, "Yes" or "No?" ')))
    print()
    bianchi.decreaseGear((input('Would you like to decrease the gear, "Yes" or "No?" ')))
    print()
    bianchi.resetGear((input('Would you like to reset the gear back to 1, "Yes" or "No?" ')))
    print()
    print("FINISHED")

except Exception as e:
    print(f"Got an error: {e}")