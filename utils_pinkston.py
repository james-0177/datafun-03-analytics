''' Final Iteration

Module: Pinkston Analytics - Reusable Module for My Data Analytics Projects

This module provides a simple, reusable foundation for my analytics projects.

Process:
In this fourth iteration, I introduce some basic statistics using Python.
    - min() is a built in function to find the smallest value passed in
    - max() is a built in function to find the largest value passed in
    - The statistics module offers methods to calculate mean and standard deviation.
'''

#####################################
# Import modules at the top.
#####################################

# In Python, we can import modules to add extra tools and functions.
# Below, we're importing:
# - `statistics`:  This gives us tools to calculate things like averages.
# Use CTRL F and type statistics to see where it is used in the code.
# Did you find statistics.mean()?
# Did you find statistics.stdev()?

import statistics

#####################################
# Declare global variables
#####################################

# Boolean variables to indicate if the company has international clients and is privately owned.
has_international_clients:  bool = True
is_privately_owned:  bool = True

# Integer variables for the number of years in operation and number of owners.
years_in_operation:  int = 10
number_of_owners:  int = 1

# List of strings representing the skills and tools offered and used by the company.
skills_offered:  list = ["Data Analysis", "Machine Learning", "Business Intelligence"]
tools_used:  list = ["Excel", "Git", "GitHub", "Python", "SQL"]

# List of floats representing individual client satisfaction scores and average monthly temperature in Jefferson City, MO.
client_satisfaction_scores:  list = [4.8, 4.6, 4.9, 5.0, 4.7]
avg_local_monthly_temp:  list = [31.7, 35.3, 45.5, 56.7, 66.1, 75.1, 79.6, 78.2, 70.5, 58.4, 46.6, 35.5]

#####################################
# Calculate Basic Statistics
#    Do this BEFORE we declare the byline
#    so the values have been calculated
#    and are ready for use in the byline.
#####################################

# Calculate basic stats using built-in functions min(), max(), and statistics module functions mean() and stdev().
min_score:  float = min(client_satisfaction_scores)
max_score:  float = max(client_satisfaction_scores)
mean_score:  float = statistics.mean(client_satisfaction_scores)
stdev_score:  float = statistics.stdev(client_satisfaction_scores)
min_temp:  float = min(avg_local_monthly_temp)
max_temp:  float = max(avg_local_monthly_temp)
mean_temp:  float = statistics.mean(avg_local_monthly_temp)
stdev_temp:  float = statistics.stdev(avg_local_monthly_temp)

#####################################
# Declare a global variable named byline.
# Make it a multiline f-string to show our information.
#####################################

byline: str = f"""
-------------------------------------------------------------
Pinkston Analytics: Professional Data Analysis On Demand
-------------------------------------------------------------
Has International Clients:  {has_international_clients}
Is Privately Owned:  {is_privately_owned}
Years in Operation:  {years_in_operation}
Number of Owners:  {number_of_owners}
Skills Offered:  {skills_offered}
Tools Used:  {tools_used}
Average Local Monthly Temperature (F):  {avg_local_monthly_temp}
Client Satisfaction Scores:  {client_satisfaction_scores}
Minimum Satisfacton Score:  {min_score}
Maximum Satisfaction Score:  {max_score}
Mean Satisfaction Score:  {mean_score}
Standard Deviation of Satisfaction Scores:  {stdev_score}
Minimum Average Local Monthly Temperature (F):  {min_temp}
Maximum Average Local Monthly Temperature (F):  {max_temp}
Mean Average Local Monthly Temperature (F):  {mean_temp}
Standard Deviation of the Average Local Monthly Temperature (F):  {stdev_temp}
"""

#####################################
# Define the get_byline() function.
#####################################

def get_byline() -> str:
    '''Return a byline for my analytics projects.'''
    return byline

#####################################
# Define a main() function for this module.
#####################################

# The main() function now calls the get_byline function to retrieve the byline.

def main() -> None:
    '''Print results of get_byline() when main() is called.'''
    print(get_byline())

#####################################
# Conditional Execution - Only call main() when executing this module as a script.
#####################################

if __name__ == '__main__':
    main()
