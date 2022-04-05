#Password Generator Project
import random
employer = ['Agio', 'MBA', 'ZeroDayLab', 'Card Factory', 'NCC Group', 'Nationwide Building Society', 'The IASME Consortium', 'Titan Labs Ltd', 'Quaero Group Limited', 'Ignite Digital Talent', 'kWipro Ltd',]

print("Welcome to the job application bot")
nr_letters= int(input("Type '1' and hit 'enter' to apply for a Penetration Tester job\n")) 

employer_list = []
for char in range(1, nr_letters + 1):
  employer_list.append(random.choice(employer))

random.shuffle(employer_list)
employer = ""
for char in employer_list:
  employer += char
print(f"")
print(f"  _     _       _            _ ___       ")
print(f" | |   (_)_ __ | | _____  __| |_ _|_ __  ")
print(f" | |   | | '_ \| |/ / _ \/ _` || || '_ \ ")
print(f" | |___| | | | |   <  __/ (_| || || | | |")
print(f" |_____|_|_| |_|_|\_\___|\__,_|___|_| |_|")
print(f"")                                        
print(f"Thank you for your interest in the Penetration Tester position. Unfortunately, we will not be moving forward with your application, but we appreciate your time and interest in {employer}.")
print(f"")
print(f"If you find this email completely useless as a job seeker, you are not alone.")
print(f"")
print(f"Go follow @ha3ks, hes a cool guy!")
print(f"")