''' This module provides functions for creating project folders. '''

#  Import standard library module and local module.


import pathlib
import utils_pinkston
import time


##################################
#  Declare global variables.
##################################

#  Create a path project
project_path = pathlib.Path.cwd()

#  Define the new sub folder path
data_path = project_path.joinpath('data')

#  Create new if it doesn't exist, otherwise do nothing
data_path.mkdir(exist_ok=True)


##################################
#  Define function 1 to create folders from a range
##################################

def create_folders_for_range(start_year: int, end_year: int) -> None:
    '''
    Create folders from a range.
    Arguments:
    start_year
    end_year
    '''
    start_year = 2020
    end_year = 2023
    print(f"FUNCTION CALLED: create_folders_for_range with start_year={start_year} and end_year={end_year}")

    for year in range(start_year, end_year + 1):
        folder_path = data_path.joinpath(str(year))
        folder_path.mkdir(parents=True, exist_ok=True)
        print(f"Created folder: {folder_path}")


##################################
# Define function 2 to create folders from a list of names
##################################

def create_folders_from_list(folder_list: list, to_lowercase: bool = False, remove_spaces: bool = False) -> None:
    '''
    Create folders from a list of names including options to force lowercase and remove spaces.
    Arguments:
    folder_list
    to_lowercase
    remove_spaces
    '''

    print(f"FUNCTION CALLED: create_folders_from_list with folder_list={folder_list}")

    for folder_name in folder_list:
        if to_lowercase:
            folder_name = folder_name.lower()
        if remove_spaces:
            folder_name = folder_name.replace(" ", "_")
        folder_path = data_path.joinpath(folder_name)
        folder_path.mkdir(parents=True, exist_ok=True)
        print(f"Created  folder: {folder_path}")


##################################
# Define function 3 to create prefixed folders from a list
##################################

def create_prefixed_folders(folder_list: list, prefix: str) -> None:
        '''
        Create folders from a list with a prefix
        Arguments:
        folder_list
        prefix
        '''

        print(f"FUNCTION CALLED: create_prefixed_folders with folder_list={folder_list} and prefix={prefix}")

        for folder_name in folder_list:
             prefixed_name = f"{prefix}{folder_name}"
             folder_path = data_path.joinpath(prefixed_name)
             folder_path.mkdir(parents=True, exist_ok=True)
             print(f"Created folder: {folder_path}")


##################################
# Define function 4 to create folders periodically
##################################

def create_folders_periodically(duration_seconds: int) -> None:
        '''
        Create folders periodically
        Arguments:
        duration_seconds
        '''

        print(f"FUNCTION CALLED: create_folders_periodically with duration_seconds={duration_seconds}")

        count = 0

        while count < 5:
             periodic_name = f"folder_{count}"
             folder_path = data_path.joinpath(periodic_name)
             folder_path.mkdir(parents=True, exist_ok=True)
             print(f"Created folder: {folder_path}")
             count += 1
             time.sleep(duration_seconds)


##################################
# Define a main() function for this module
##################################


def main() -> None:
    ''' Main function to demonstrate module capabilities. '''

    # Start of main execution
    print("#####################################")
    print("# Starting execution of main()")
    print("#####################################\n")

    # Print byline from imported module
    print(f"Byline: {utils_pinkston.get_byline()}")

    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start_year=2020, end_year=2023)

    # Call function 2 to create folders given a list
    folder_list = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_list)

    # Call function 3 to create folders using comprehension
    folder_list = ['csv', 'excel', 'json']
    prefix = 'data-'
    create_prefixed_folders(folder_list, prefix)

    # Call function 4 to create folders periodically using while
    duration_secs = 5  # duration in seconds
    create_folders_periodically(duration_secs)

    # Add options e.g., to force lowercase and remove spaces 
    # to one or more of your functions (e.g. function 2) 
    # Call your function and test these options
    regions = [
      "North America", 
      "South America", 
      "Europe", 
      "Asia", 
      "Africa", 
      "Oceania", 
      "Middle East"
    ]
    create_folders_from_list(regions, to_lowercase=True, remove_spaces=True)

    # End of main execution
    print("\n#####################################")
    print("# Completed execution of main()")
    print("#####################################")


##############################
# Conditional Execution
##############################


if __name__ == '__main__':
    main()
