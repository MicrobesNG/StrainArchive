

from Bio.Blast.Applications import NcbiblastxCommandline
from Bio.Blast.Applications import NcbiblastnCommandline
from Bio.Blast.Applications import NcbiblastpCommandline
from Bio.Blast.Applications import NcbitblastxCommandline
from Bio.Blast.Applications import NcbitblastnCommandline
import searchUtils

BLAST_N_PATH = "path"
BLAST_P_PATH = "path"
BLAST_DATABASE_PATH = "path"

# nucleotide - nucleotide blast
def blast_n(query, e_value, output_filepath):

    # get unique number for temp file name
    # avoids overwriting currently in use temp files if more than one person searching
    new_temp_file_index = searchUtils.generate_temp_output_filepath("tmp")

    # generate blast search
    blast_command_line = NcbiblastnCommandline(
        BLAST_N_PATH,
        BLAST_DATABASE_PATH,
        evalue = e_value,
        "tmp/tmp_%d.xml" % new_temp_file_index
    )

    # run the blast search
    stdout, stderr = blast_command_line()

    return stdout, stderr


# protein - protein blast
def blast_p(query, e_value, output_filepath):

    # get unique number for temp file name
    # avoids overwriting currently in use temp files if more than one person searching
    new_temp_file_index = searchUtils.generate_temp_output_filepath("tmp")

    # generate blast search
    blast_command_line = NcbiblastpCommandline(
        BLAST_P_PATH,
        BLAST_DATABASE_PATH,
        evalue = e_value,
        "tmp/tmp_%d.xml" % new_temp_file_index
    )

    # run the blast
    stdout, stderr = blast_command_line()

    return stdout, stderr