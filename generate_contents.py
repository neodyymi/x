#!/usr/bin/env python3

import os
import re
import itertools
import nbformat
import sys
NOTEBOOK_DIR = os.path.join(os.path.dirname(__file__), '..', 'notebooks')

CHAPTERS = {"00": "Preface",
            "01": "IPython: Beyond Normal Python",
            "02": "NumPy",
            "03": "Pandas",
            "04": "Matplotlib",
            "05": "Machine Learning"}

REG = re.compile(r'(\d\d)\.(\d\d)-(.*)\.ipynb')


def iter_notebooks():
    return sorted(nb for nb in os.listdir(NOTEBOOK_DIR) if REG.match(nb))


def get_notebook_titles(nb_file):
#    nb = nbformat.read(os.path.join(NOTEBOOK_DIR, nb_file), as_version=4)
    nb = nbformat.read(nb_file, as_version=4)
    for cell in nb.cells:
        if cell.source.startswith('#') and cell.cell_type != "code":
            yield cell.source.splitlines()[0].strip()


def print_contents(nb):
    print('\n'.join(get_notebook_titles(nb)))


if __name__ == '__main__':
    print_contents(sys.argv[1])
    #print('\n', 70 * '#', '\n')
    #print_contents('http://nbviewer.jupyter.org/github/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/')
