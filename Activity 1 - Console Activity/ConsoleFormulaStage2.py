
import time
import random

print("\n\n**************************************")
print("Introduction: ")
print("\n\tThis calculator will perform two calculations\n")
print("\tCalculation 1: Calcate the number of rotations")
print("\tof the drive gear for each rotation of the")
print("\tmotor gear, given the tooth count of each.\n")
print("\tCalculation 2: Calculate the rotations per minute")
print("\t(rpm) of the motor gear given the tooth count")
print("\tof each gear and the rpm of the drive gear\n")
print("\tAssumption: This assumes a two gear system where")
print("\tthe motor gear is directly attached to the drive")
print("\tgear.")

input("\t\t\tPRESS ENTER TO CONTINUE")

print("\nDefinition: Motor Gear:")
print("\n\tThe motor gear is the gear directly connected\n\tto the motor.")

print("\nDefinition: Drive Gear:")
print("\n\tThe drive gear is the gear directly connected\n\tto the part that is being moved.")

print("\nDefinition: Idler gears:")
print("\n\tIdler gears are the gears that connect the motor \n\tgear and the drive gear. We will assume no idler\n\tgears in the calculations.\n")

input("\t\t\tPRESS ENTER TO CONTINUE")

print("\n*********************************************************")
print("Formula 1: Gear Rotation Ratio\n")
print("\tThe number of teeth in the motor gear");
print("\tdivided by the number of teeth in the"); 
print("\tdrive gear will give the number of rotations");
print("\tof the drive gear for each single rotation of");
print("\tthe motor gear.")
print("\n\tFor example if the motor gear has 30 teeth"); 
print("\tand the drive gear has 20 teeth the drive gear");
print("\twill rotate 30/20 = 1.5 times for every single");
print("\trotation of the motor gear.\n");

print("\tINPUT")
teethm = input("\tInput motor gear teeth: ");
teethm = int(teethm);

teethd = input("\tInput drive gear teeth: ");
teethd = int(teethd);




rotationm = teethm/teethd;
rotationm = round(rotationm,2)

rand = random.randint(1,10)

print("\n\tPROCESSS")
for i in range (0,rand,1):
	print("\tProcessing. . . ")
	time.sleep(0.5)

print("\n\tOUTPUT")
print("\tThe drive gear will turn "+str(rotationm)+" times")
print("\tfor 1 rotation of the motor gear.");


input("\t\t\tPRESS ENTER TO CONTINUE")
print("\n*********************************************************")
print("\nFormula 2: Rotations per Minute (rpm)")
display = "rpmMotor/rpmDrive = teethMotor/teethDrive\n\trpmMotor = (rpmDrive*teethMotor)/teethDrive\n\trpmDrive = (rpmMotor*teethDrive)/teethMotor";
print("\n\t"+display+"\n");

#INPUT
rpmd = input("Input drive gear rotation per minute (rpm2): ")
rpmd = int(rpmd)


#PROCESS
rpmm = rpmd*teethm/teethd

#OUTPUT
print(rpmm)