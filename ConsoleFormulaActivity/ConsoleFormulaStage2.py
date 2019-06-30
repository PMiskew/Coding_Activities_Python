SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
print("\n\n**************************************")
print("Introduction: ")
print("\n\tThis calculator will calculate the rpm of a")
print("\tdrive gear given the rpm of the motor gear.")

print("\nDefinition: Motor Gear")
print("\n\tThe motor gear is the gear directly connected\n\tto the motor.")
print("\nDefinition: Drive Gear")
print("\n\tThe drive gear is the gear directly connected\n\tto the part that is being moved.")
print("\nDefinition: Idler gears")
print("\n\tIdler gears are the gears that connect motor \n\tand the drive gear.")


print("\nFormula 1: Gear Rotation Ratio ")
print("\tThe number of teeth in the motor gear");
print("\tdivided by the number of teeth in the"); 
print("\tdrive gear will give the number of rotations");
print("\tof the drive gear for each single rotation of");
print("\tthe motor gear.")
print("\n\tFor example if the motor gear has 30 teeth"); 
print("\tand the drive gear has 20 teeth the drive gear");
print("\twill rotate 30/20 = 1.5 times for every single");
print("\trotation of the motor gear.");

teethm = input("Input motor gear teeth: ");
teethm = int(teethm);

teethd = input("Input drive gear teeth: ");
teethd = int(teethd);

rotationm = teethm/teethd;
print("The drive gear will turn "+str(rotationm)+" for every single rotation of the motor gear.");


print("\nFormula 2: ")
display = "rpmMotor/rpmDrive = teethMotor/teethDrive\n\trpmMotor = (rpm2*teeth1)/teeth2".translate(SUB)
print("\n\t"+display)
print("**************************************")

#INPUT
rpmd = input("Input drive gear rotation per minute (rpm2): ")
rpmd = int(rpmd)


#PROCESS
rpmm = rpmd*teethm/teethd

#OUTPUT
print(rpmm)