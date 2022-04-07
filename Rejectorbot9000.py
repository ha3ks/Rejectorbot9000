#Password Generator Project
import random
import itertools
import threading
import time
import sys

employer = ['Agio', 'MBA', 'ZeroDayLab', 'Card Factory', 'NCC Group', 'Nationwide Building Society', 'The IASME Consortium', 'Titan Labs Ltd', 'Quaero Group Limited', 'Ignite Digital Talent', 'Wipro Ltd',]

print(f"")
print(f"       _       _                         _ _           ___   ___   ___   ___   ")
print(f"      | |     | |      /\               | (_)         / _ \ / _ \ / _ \ / _ \  ")
print(f"      | | ___ | |__   /  \   _ __  _ __ | |_  ___ _ _| (_) | | | | | | | | | | ")
print(f"  _   | |/ _ \| '_ \ / /\ \ | '_ \| '_ \| | |/ _ \ '__\__, | | | | | | | | | | ")
print(f" | |__| | (_) | |_) / ____ \| |_) | |_) | | |  __/ |    / /| |_| | |_| | |_| | ")
print(f"  \____/ \___/|_.__/_/    \_\ .__/| .__/|_|_|\___|_|   /_/  \___/ \___/ \___/  ")
print(f"                            | |   | |                                          ")
print(f"                            |_|   |_|                                          powered by Linkedin")
print(f"")
print("Welcome to the job application bot")
print(f"")
userinput = (input("Type '1' and hit 'enter' to apply for a Penetration Tester job\n")) 
print(f"")

done = False
def animate():
  for c in itertools.cycle(['|', '/', '-', '\\']):
      if done:
        break
      sys.stdout.write('\rApplying for job ' + c)
      sys.stdout.flush()
      time.sleep(0.1)
  sys.stdout.write('\n\n')

t = threading.Thread(target=animate)
t.start()

  #long process here
time.sleep(10)
done = True

employer_list = []
for char in (userinput):
  employer_list.append(random.choice(employer))

random.shuffle(employer_list)
employer = ""
for char in employer_list:
  employer += char

print(f"")
print(f"")
print(f"")
print(f"")
print(f"")
print(f"")
print(f"")
print(f"")
print(f"")
print(f"")
print(f"")
print(f"")
print(f"")
print(f"")
print(f"")
print(f"email from: unmonitored.mailbox.dont.even.try.it.suxor@linkedin.linked")
print(f"")
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
print(f"I would happily take something in a 'constructive feedback' option from a recruiter or potential employer")
print(f"")
print(f"We really need to look at that bar that we have for 'what is entry level cyber' and give talent a chance, we are hard working and learn quickly, I mean look at this sh*t I put together in like an hour!")
print(f"")
print(f"Go follow @ha3ks, hes a cool guy!")