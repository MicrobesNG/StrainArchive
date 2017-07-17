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



def get_strains_from_blast_output(output):

    parsed_output = NCBIXML.parse(output)

    for record in parsed_output:
        pass
        # process record to get tax data

        # for description in record.descriptions:
            
        # for alignment in record.alignments:

        #     for hit in alignment.hsps:
        #         pass
        #         # provess 