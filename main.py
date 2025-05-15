# Programming with For Loop
# Coder: Rory Lehtola
# Date: 05/14/25
# Class: STEM 103 Spring

# Notes:

#

# What I learned:

#

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

# Use a for loop to iterate through the list of missions.
# Count the total number of missions.
# Count the number of successful missions.
# Identify and list all missions launched before the year 2000.

# Print the total number of missions.
# Print the number of successful missions.
# Print the success rate as a percentage.
# Print the names of the missions launched before the year 2000.

# Use a counter variable to keep track of the total number of missions and successful missions.
# Use an if statement to check the year of each mission and whether it was successful.
# Calculate the success rate using the formula: (number of successful missions / total number of missions) * 100.
# Use string formatting to display the success rate with two decimal places. 