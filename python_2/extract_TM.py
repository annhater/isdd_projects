#but: détermine les fragments transmembranaire (ou TM) de la protéine
# =  les zones où les carbones α sont au sein de la membrane
# vérifier si leur coordonnée z est située entre la couche de points du haut et du bas
# pour chaque chaîne de la protéine

#Le script ne devra pas s’éxécuter s’il est importé en tant que module.
# Le script lancé sans argument affichera l’usage et quittera
# => define how it will be working using sys module


#IMPORT LIBRARIES
import sys

#FUNCTIONS

# with open PBD as file:
# reads file turns the atom list
# => below the header of the PDB file => 
# if the line starts with ATOM yada yada
# turns into a dictionnary
# this format: [{'resname': 'SER', 'resnum': 23, 'z': 19.904},
# {'resname': 'ASP', 'resnum': 24, 'z': 16.911},
# {'resname': 'PRO', 'resnum': 25, 'z': 13.714},
# ...
# {'resname': 'GLY', 'resnum': 52, 'z': -25.077}]
# resname =  le nom de résidu,
# resnum = le numéro de résidu
# z = la position z du carbone α de de ce résidu

#points fictifs représentant les extrémités de la membrane sont récupérables avec le champ HETATM
# le nom de résidu DUM

# FIRST FUNCTION 
# reads the lines of the pbd and finds z_min and z_max of the mb
# returns the tuple (wo repeats) or list INCREASING ORDER
# pdbfilename (str)
def  extract_mb_pos(pdbfilename):
    dum_atm = []
    with open(pdbfilename, "r") as pdb_file:
        for line in pdb_file:
            if (line.startswith("HETATM")
                and line[17:20].strip() == "DUM"):
                #i need tuple here to remove repeats
                #find min and max with min() amd max()
                    z = float(line[46:54].strip())
                    dum_atm.append(z)
        #print(dum_atm)
                    mb_pos = (min(dum_atm), max(dum_atm))
        return mb_pos

#SECOND FUNCTION
# extraira tous les noms de chaîne (par exemple A, B, C et D)
#str triée par ordre alpabétique sera renvoyée par cette fonction

def extract_chains(pdbfilename):
    chains = []
    with open(pdbfilename, "r") as pdb_file:
        for line in pdb_file:
            if line.startswith("ATOM"):
                 if line[21:22].strip() not in chains:
                     chains.append(line[21:22].strip())
                 chains = sorted(chains)
        return chains

#return chain(str)

#THIRD FUNCTION
# chain (str) =  un nom de chaîne PDB (par exemple A, B, etc.)
#returns coors (list)
def extract_CA(pdbfilename, chain):
     coors = []
     with open(pdbfilename, "r") as pdb_file:
        for line in pdb_file:
            if (line.startswith("ATOM") 
                and line[12:16].strip() == "CA" 
                and line[21:22].strip() == chain):
                #x = float(line[30:38])
                #y = float(line[38:46])
                resname = line[17:20]
                resnum = line[22:26]
                z = float(line[46:54])
                coors.append({
                    'resname': resname,
                    'resnum': resnum,
                    'z': z
                })
     return coors


#FOURTH FUNCTION
#returns residues_in_mb (list)
def extract_residues_in_mb(coors, z_min, z_max):
    residues_in_mb = []
    for residue in range(len(coors)):
        if z_min <= coors[residue]["z"]<= z_max:
            residues_in_mb.append(coors[residue]["resname"] + coors[residue]["resnum"].strip())
    return residues_in_mb

 #FIFTH FUNCTION
#returns PRO25-LEU26-VAL27-[...]-THR42-ILE43-GLY44
def print_extract_TM(residues_in_mb):
    for residue in range(len(residues_in_mb)):
        residue_str = "-".join(residues_in_mb)
    print(f"{residue_str}\n")
     


# Main

## 0) Gestion des arguments. # Récupération du nom de fichier PDB ou affichage de l'usage.
if len(sys.argv) != 2:
    sys.exit("Usage: python extract_TM.py opm_file.pdb")

pdbfilename = sys.argv[1]
#pdbfilename = "2ljb.pdb"

## 1) Récupération des extrémités de la membrane. # Appel de la fonction extract_mb_pos() : récupération des vars "zmin" et "zmax" (floats). # Affichage de zmin et zmax et du nom de fichier PDB.
#z_min, z_max = 
z_min, z_max = extract_mb_pos(pdbfilename)
print(f"La membrane est située entre z_min = {z_min:.1f} et z_max = {z_max:.1f} pour le fichier {pdbfilename}")

# Create a dictionary to store coordinates for each chain
#chain_coordinates = {}

## 2) Récupération des chaînes. # Appel de la fonction extract_chains() : récupération de la var "chains" (liste de str).
## 3) Extraction des parties TMs. # Boucle sur chaque chaîne:
# Affichage du nom de chaîne 
# # Appel de la fonction extract_CA() : 
# # --> Récupération de tous les CA pour cette chaîne dans la var "coors" (liste de dicos).
# # Appel de la fonction extract_residues_in_mb() :
# --> Récupération des CA dans la membrane dans la var "coors_in_mb" (liste de dicos). # Appel de la fonction print_extract_TM() :
# --> Affichage de chaque fragment TM.
for chain in extract_chains(pdbfilename):
    print(f"chain {chain}")
    print_extract_TM(extract_residues_in_mb(extract_CA(pdbfilename, chain), z_min, z_max))

# Expected output: 
# La membrane est située entre z_min = -15.8 et z_max = 15.8 pour le fichier 2ljb.pdb
# chain A
#PRO25-LEU26-VAL27-[...]-THR42-ILE43-GLY44
# chain B
# PRO25-LEU26-VAL27-[...]-THR42-ILE43
# chain C
# PRO25-LEU26-VAL27-[...]-THR42-ILE43
# chain D 
# PRO25-LEU26-VAL27-[...]-THR42-ILE43-GLY44
