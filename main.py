# Programming with For Loop
# Coder: Rory Lehtola
# Date: 05/14/25
# Class: STEM 103 Spring

# Notes:

# When executed, this program will print the total number of space missions, total 
# number of successful space missions, percentage of successful space missions and 
# all space missions pre year 2000.

# What I learned:

# Trial and error is messy and long. The list and for statement I created for missions 
# pre 2000 was a complete and total nightmare. I used Ai for help on that one after I 
# had enough head banging on my computer. Alot of the struggle was centered around 
# organization so everything ran properly. Variables were much more complicated on this
# assignment. I've discovered the importance of writing everything out step by step.

# Assignment:

mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

# Count the total number of space missions and mission success's
total_missions = len(mission_names)
total_success = sum(mission_success)

# Calculate the success rate of missions
success_rate = (total_success / total_missions) * 100

# Lists all the missions that were launched before the year 2000
missions_pre2000 = [mission_names[i] for i in range (total_missions) if mission_years[i] < 2000]

# Print the total number of missions and successful missions
print("Total number of space missions: ", total_missions)
print("Total number of successful space missions: ", total_success)

# Print success rate of missions
print(f"This is the value of {success_rate:.2f}%")

# Print the missions launched before 2000
print("Missions launched pre 2000: ")

for mission in missions_pre2000:
    print(mission)