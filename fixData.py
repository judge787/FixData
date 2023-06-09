#-----------------------------This section is for indivual years-----------------------------------------------------

# import os
# # Define the paths to the input and output files
# year = "1989"
# city = "London"

# input_file_path = "EPW Files/" + year + "/ERA5_" + city + "_Dec" + year +".epw"
# output_file_path = "Modified EPW Files/ERA5_" + city + "_Dec" + year + ".epw"
# output_original_path = "EPW Files/" + year + "/ERA5_" + city + "_Dec" + year +".epw"

# # Check if the output directory exists, and create it if it doesn't
# if not os.path.exists("Modified EPW Files/"):
#     os.makedirs("Modified EPW Files/")


# # Open the input EPW file for reading
# with open(input_file_path, 'r') as input_file:
#     # Read the lines of the file into a list
#     lines = input_file.readlines()

#     # Check if line 4 contains the character 'H'
#     if 'H' in lines[3]:
#         # Find the index of the character 'H' in line 4
#         index = lines[3].index('H')
#         # Insert a newline after the character 'H'
#         lines[3] = lines[3][:index] + '\n' + lines[3][index:]

# with open(output_original_path, 'w') as output_file:
#     # Write the modified lines back to the file
#     output_file.writelines(lines)

# with open(input_file_path, 'r') as input_file:
#     # Read the lines of the file into a list
#     lines = input_file.readlines()

# # Replace lines 747-752 with the contents of lines 723-728
# lines[746:752] = lines[722:728]
# lines[1418:1424] = lines[1394:1400]
# lines[2162:2168] = lines[2138:2144]
# lines[2882:2888] = lines[2858:2864]
# lines[3626:3632] = lines[3602:3608]
# lines[4346:4352] = lines[4322:4328]
# lines[5090:5096] = lines[5066:5072]
# lines[5834:5840] = lines[5810:5816]
# lines[6554:6560] = lines[6530:6536]
# lines[6554:6560] = lines[6530:6536]
# lines[7298:7304] = lines[7274:7280]
# lines[8018:8023] = lines[7994:7999]
# lines[8761:8788]= lines[8737:8744]
# # Open the output EPW file for writing
# with open(output_file_path, 'w') as output_file:
#     # Write the modified lines back to the file
#     output_file.writelines(lines)







#-------------------------------------------------This section is for a range of years----------------------------------------------
import os

# Set the city variable to "London"
city = "London"

# Iterate over the range of years from 1981 to 1999
for year in range(1981, 2000):
    # Define the paths to the input and output files for the current year
    input_file_path = f"EPW Files/{year}/ERA5_{city}_Dec{year}.epw"
    output_file_path = f"Modified EPW Files/ERA5_{city}_Dec{year}.epw"
    output_original_path = f"EPW Files/{year}/ERA5_{city}_Dec{year}.epw"

    # Check if the output directory exists, and create it if it doesn't
    if not os.path.exists(f"Modified EPW Files"):
        os.makedirs(f"Modified EPW Files")

    # Open the input EPW file for reading
    with open(input_file_path, 'r') as input_file:
        # Read the lines of the file into a list
        lines = input_file.readlines()

    if 'H' in lines[3]:
        # Find the index of the character 'H' in line 4
        index = lines[3].index('H')
        # Insert a newline after the character 'H'
        lines[3] = lines[3][:index] + '\n' + lines[3][index:]

    with open(output_original_path, 'w') as output_file:
        # Write the modified lines back to the file
        output_file.writelines(lines)

    with open(input_file_path, 'r') as input_file:
        # Read the lines of the file into a list
        lines = input_file.readlines()
    

    # Replace lines 747-752 with the contents of lines 723-728
    lines[746:752] = lines[722:728]
    lines[1418:1424] = lines[1394:1400]
    lines[2162:2168] = lines[2138:2144]
    lines[2882:2888] = lines[2858:2864]
    lines[3626:3632] = lines[3602:3608]
    lines[4346:4352] = lines[4322:4328]
    lines[5090:5096] = lines[5066:5072]
    lines[5834:5840] = lines[5810:5816]
    lines[6554:6560] = lines[6530:6536]
    lines[6554:6560] = lines[6530:6536]
    lines[7298:7304] = lines[7274:7280]
    lines[8018:8023] = lines[7994:7999]
    lines[8761:8788]= lines[8737:8744]

    # Open the output EPW file for writing
    with open(output_file_path, 'w') as output_file:
        # Write the modified lines back to the file
        output_file.writelines(lines)