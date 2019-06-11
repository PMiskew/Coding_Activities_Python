SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
print("\n\n**************************************")
print("Introduction: ")
print("\n\tThis calculator will calculate the rpm of a")
print("\tdrive gear given the rpm of the motor gear.")

print("\nDefinition: Motor Gear")
print("\n\tThe motor gear is the gear directly connected\n\tto the motor.")
print("\nDefinition: Drive Gear")
print("\n\tThe drive gear is the gear directly connected\n\tto the part that is being moved.")

print("Formula: ")
display = "rpm1/teeth1 = rpm2/teeth2\n\trpm2=(rpm1*teeth2)/teeth1".translate(SUB)
print("\n\t"+display)
print("**************************************")

#INPUT
rpm1 = input("Input motor gear rotation per minute (rpm): ")
rpm1 = int(rpm1)

teeth1 = input("Input motor gear teeth: ")
teeth1 = int(teeth1)

teeth2 = input("Input drive gear teeth: ")
teeth2 = int(teeth2)

#PROCESS
rpm2 = rpm1*teeth2/teeth1

#OUTPUT
print(rpm2)