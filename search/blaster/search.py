

from Bio.Blast.Applications import NcbiblastxCommandline
from Bio.Blast.Applications import NcbiblastnCommandline
from Bio.Blast.Applications import NcbiblastpCommandline
from Bio.Blast.Applications import NcbitblastxCommandline
from Bio.Blast.Applications import NcbitblastnCommandline

BLAST_N_PATH = "path"
BLAST_P_PATH = "path"
BLAST_DATABASE_PATH = "path"

# nucleotide - nucleotide blast
def blast_n(query, e_value, output_filepath):

    blast_command_line = NcbiblastnCommandline(
        BLAST_N_PATH,
        BLAST_DATABASE_PATH,
        evalue = e_value, output_filepath
    )

    stdout, stderr = blast_command_line()

    return stdout, stderr


# protein - protein blast
def blast_p(query, e_value, output_filepath):

    blast_command_line = NcbiblastpCommandline(
        BLAST_P_PATH,
        BLAST_DATABASE_PATH,
        evalue = e_value, output_filepath
    )

    stdout, stderr = blast_command_line()

    return stdout, stderr

