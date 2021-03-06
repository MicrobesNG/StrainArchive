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
        
        print "----------------------"
        print record.alignments
        print record.matrix
        print "----------------------"

        for description in record.descriptions:
            print "D_title:", description.title
            print "-- -- -- -- -- --"

        for alignment in record.alignments:

            print ""
            print "A_title:", alignment.title

            for hit in alignment.hsps:

                print hit.score
                print hit.sbjct_start
                print hit.sbjct_end
                print "--------"

    print ""
    print ""    
    print "-- -- -- -- -- -- -- --"