

from Bio.Blast.Applications import NcbiblastxCommandline
from Bio.Blast.Applications import NcbiblastnCommandline
from Bio.Blast.Applications import NcbiblastpCommandline
from Bio.Blast.Applications import NcbitblastxCommandline
from Bio.Blast.Applications import NcbitblastnCommandline
import searchUtils
from Bio.Blast import NCBIWWW


BLAST_N_PATH = "path"
BLAST_P_PATH = "path"
BLAST_DATABASE_PATH = "path"



def ncbi_blast_n(target_database, fasta_query_string):

    results = NCBIWWW.qblast("blastn", target_database, fasta_query_string)

    return results
    
def ncbi_blast_p(target_database, fasta_query_string):

    results = NCBIWWW.qblast("blastp", target_database, fasta_query_string)

    return results
    





# nucleotide - nucleotide blast
def local_blast_n(query, e_value, output_filepath):

    # get unique number for temp file name
    # avoids overwriting currently in use temp files if more than one person searching
    new_temp_file_index = searchUtils.generate_temp_output_filepath("tmp")
    new_filename = "tmp_%d.xml" % new_temp_file_index

    # generate blast search
    blast_command_line = NcbiblastnCommandline(
        BLAST_N_PATH,
        BLAST_DATABASE_PATH,
        evalue = e_value,
        "tmp/%s" % new_filename
    )

    # run the blast search
    stdout, stderr = blast_command_line()

    return new_filename
    # return stdout, stderr


# protein - protein blast
def local_blast_p(query, e_value, output_filepath):

    # get unique number for temp file name
    # avoids overwriting currently in use temp files if more than one person searching
    new_temp_file_index = searchUtils.generate_temp_output_filepath("tmp")
    new_filename = "tmp_%d.xml" % new_temp_file_index

    # generate blast search
    blast_command_line = NcbiblastpCommandline(
        BLAST_P_PATH,
        BLAST_DATABASE_PATH,
        evalue = e_value,
        ("tmp/%s" % new_filename)
    )

    # run the blast
    stdout, stderr = blast_command_line()

    # return stdout, stderr
    return new_filename