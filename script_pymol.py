from pymol import cmd
from glob import glob

list_rmsd = []
cmd.load("/Users/francescapaoletti/Downloads/tetR.pdb")
filename = "/Users/francescapaoletti/Downloads/Struct3D/struct_*.pdb"


for file in glob(filename):
    print(file)
    index = int(file.split("_")[1].split(".")[0])
    cmd.load(file, "test")
    RMSD = cmd.cealign("test","tetR",d0=600,d1=600)
    list_rmsd.append((index, RMSD['RMSD']))
    cmd.delete("test")


print(list_rmsd)
