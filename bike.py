# Hunter C. Sylvester
# Purpose: Creating a Bike Class that allows a user to increase,decrease, or reset gears while defining their
#          number of gears, number of wheels, current gear, and brake type
# The Bike class
#
# Properties
#  Number of Gears: getNumberOfGears(), setNumberOfGears()
#  Number of Wheels: getNumberOfWheels(), setNumberOfWheels()
#  Current Gear: getCurrentGear(), setCurrentGear()
#  Type of Brakes: getBrakeType(), setBrakeType()
#
#
# Methods
#   increaseGear(answer)
#   decreaseGear(answer)
#   resetGear(answer)
#



class Bike:
    # Private Properties
    __numberOfGears: int = 1
    __currentGear: int = 1

    __numberOfWheels: int = 1
    __brakeType: str = ""

    ########################
    # Instantiate a copy of this class
    def __init__(self,
                numberOfGears = 1,
                numberOfWheels = 1,
                currentGear = 1,
                brakeType = "hand brakes" or "foot brakes"):

        # Set all our properties
        self.setNumberOfGears(numberOfGears)
        self.setNumberOfWheels(numberOfWheels)
        self.setBrakeType(brakeType)
        self.setCurrentGear(currentGear)

    ####################################################
    # Getter and Setter for the number of gears property
    def getNumberOfGears(self) -> int:
        return self.__numberOfGears

    def setNumberOfGears(self, numberOfGears: int) -> None:
        try:
            if 16 > numberOfGears > 0:
                self.__numberOfGears = int(numberOfGears)

            else:
                print("That is the incorrect amount of gears.  The value can be 1-15 inclusive. "
                            f"Your number of gears will be set back to the default amount of {self.__numberOfGears}")
                self.__numberOfGears = 1

        except Exception as e:
            raise e

    ####################################################
    # Getter and Setter for the number of wheels property
    def getNumberOfWheels(self) -> int:
        return self.__numberOfWheels

    def setNumberOfWheels(self, numberOfWheels: int) -> None:
        try:
            if 4 >= numberOfWheels >= 1:
                self.__numberOfWheels = int(numberOfWheels)

            else:
                return print("That is the incorrect amount of wheels.  The bike can have 1-4 wheels inclusive.  "
                             f"Your number of wheels will be set back to the default amount of {self.__numberOfWheels}")

        except Exception as e:
            raise e

    ####################################################
    # Getter and Setter for the type of brakes property
    def getBrakeType(self) -> str:
        return self.__brakeType

    def setBrakeType(self, brakeType: str) -> None:
        try:
            if brakeType == "hand brakes" or brakeType == "foot brakes":
                self.__brakeType = brakeType

            else:
                print('That is the incorrect type of brakes.  These bikes can only have "hand brakes" or "foot brakes."'
                      f"Your type of breaks will be left blank until you correct the input. {self.__brakeType}")

        except Exception as e:
            raise e

    ####################################################
    # Getter and Setter for the current gear property
    #   The current gear must fall between 1 and 15 inclusive, otherwise not possible
    #       Also, if the numberOfGears is defaulted back to 1 due to input then the output is based off the default of 1
    #           For example, you can't have 16 gears so default to 1, but your original input of gear set to is 9 which
    #           is impossible for a number of gears of 1
    def getCurrentGear(self) -> int:
        return self.__currentGear

    def setCurrentGear(self, currentGear: int) -> None:
        try:
            if 15 >= currentGear >= 1:
                if currentGear <= self.__numberOfGears:
                    self.__currentGear = int(currentGear)
                else:
                    print("The set gear is higher than the amount of gears the bike has.  "
                          "Your set gear is defaulted to 1")

            else:
                print("The current gear can only be between 1-15 inclusive.  "
                      f"The current gear will be set back to default of {self.__currentGear}")

        except Exception as e:
            raise e

    ####################################################
    # Increase Gear property
    # In case of a default set of 1 for number of Gears, I cannot shift past that either
    def increaseGear(self, answer: str) -> None:
        try:
            answer = str(answer)
            if answer == "Yes":
                if self.__currentGear < 15 and self.__currentGear < self.__numberOfGears:
                    self.__currentGear = self.__currentGear + 1
                    print(f"We have shifted up and my current gear is now set to {self.__currentGear}")
                else:
                    print(f"We cannot shift past 15th gear or current gear of {self.__currentGear}, sorry!")

            elif answer == "No":
                self.__currentGear = self.__currentGear
                print(f"We decided not to shift up so my current gear is still {self.__currentGear}")

            else:
                print(f'{answer} is not a valid answer.  You must type in "Yes" or "No"')

        except Exception as e:
            raise e

    ####################################################
    # Decrease Gear property
    def decreaseGear(self, answer: str) -> None:
        try:
            answer = str(answer)
            if answer == "Yes":
                if self.__currentGear > 1:
                    self.__currentGear = self.__currentGear - 1
                    print(f"We have shifted down and my current gear is now set to {self.__currentGear}")
                else:
                    print("We cannot shift down past 1st gear, sorry!")

            elif answer == "No":
                self.__currentGear = self.__currentGear
                print(f"We decided not to shift down so my current gear is still {self.__currentGear}")

            else:
                print(f'{answer} is not a valid answer.  You must type in "Yes" or "No"')

        except Exception as e:
            raise e

    ####################################################
    # Reset back to gear 1 property
    def resetGear(self, answer: str) -> None:
        try:
            answer = str(answer)
            if answer == "Yes":
                self.__currentGear = 1
                print(f"We have reset the gears back to {self.__currentGear}")

            elif answer == "No":
                print(f"We did not reset the gears, so your gear remains set at {self.__currentGear}")

            else:
                print(f'{answer} is not a valid answer.  You must type in "Yes" or "No"')

        except Exception as e:
            raise e




