import os

from Bio.Blast import NCBIXML

def generate_temp_output_filepath(temp_directory):

    if os.path.isdir(temp_directory):

        number_of_temp_files = len(os.listdir(temp_directory))

        generated_number = number_of_temp_files + 1

        return generated_number
    
    else:

        raise OSError(
            "Directory %s does not exist or is not a valid directory." % temp_directory
        )



def get_strains_from_blast_results(results_filepath):

    if os.path.isfile(results_filepath):

        records = NCBIXML.read(results_filepath)

        for record in records:
            # get strain name? -> get pk -> get DB object
            pass
    
    else:

        raise OSError(
            "File does not exist."
        )