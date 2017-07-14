import os

def generate_temp_output_filepath(temp_directory):

    if os.path.isdir(temp_directory):

        number_of_temp_files = len(os.listdir(temp_directory))

        generated_number = number_of_temp_files + 1

        return generated_number
    
    else:

        raise OSError(
            "Directory %s does not exist or is not a valid directory." % temp_directory
        )

def remove_temp_output_filepath(temp_file)