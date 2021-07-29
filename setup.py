from setuptools import setup, find_packages
import phylib
from os import walk, listdir
from os.path import join,normpath,isfile

param = {
    'name': phylib.PROGRAM_NAME,
    'version': phylib.PROGRAM_VERSION,
    'description': phylib.PROGRAM_DESCRIPTION,
    'author': phylib.PROGRAM_AUTHOR,
    'license': phylib.PROGRAM_LICENSE,
    'packages': find_packages(),
    'include_package_data': True,
    'scripts' : ['labelTrees.py','prune_tree.py','sample_sequences.py','select_sequences.py'],
    'zip_safe': True,
    'install_requires': ['dendropy>=4.3.0','treeswift'],
    'keywords': 'Phylogenetics Evolution Biology',
    'long_description': """A Python implementation of the wLogDate algorithm""",
    'classifiers': ["Environment :: Console",
                    "Intended Audience :: Developers",
                    "Intended Audience :: Science/Research",
                    "License :: OSI Approved :: GNU General Public License (GPL)",
                    "Natural Language :: English",
                    "Operating System :: OS Independent",
                    "Programming Language :: Python",
                    "Topic :: Scientific/Engineering :: Bio-Informatics",
                    ],
    }
    
setup(**param)
