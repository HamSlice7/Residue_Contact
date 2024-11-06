import numpy as np
import biotite.structure as structure
import biotite.structure.io.pdb as pdb

#The farthest distance in Angstroms between the atoms in the peptidase and the inhibitor to be considered 'in contact'.
Threshold_Distance = 5.0
