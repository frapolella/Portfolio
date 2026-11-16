import os
print("n-Butane Bond Analysis")
print()
filename = "../data/raw/bond_distances.csv"
print("Input file:", os.path.basename(filename))
with open(filename, "r") as file:
    
        header = file.readline()
        print("Header:")
        print(header)
        bonds = []
        for line in file:
            #line = "C-C,1,9,1,1,520,"
            values = line.strip().split(",")
            #print(values)
            bond_type = values[0]
            initial_atom = int(values[1])
            terminal_atom = int(values[2])
            bond_order = int(values[3])
            
            bond_length = values[4] + "." + values[5] 
            bond_length = float(bond_length)
            
            bond = {
                    "type": bond_type,
                    "initial_atom": initial_atom,
                    "terminal_atom": terminal_atom,
                    "order": bond_order,
                    "length": bond_length 
                    }
            #print(bond)
            bonds.append(bond)
        
        print()
        print("Number of bonds:", len(bonds))

reference_length = 1.5
tolerance = 0.1
equal_bonds = 0
different_bonds = 0

for bond in bonds:
    if abs(bond["length"] - reference_length) <= tolerance:
        equal_bonds += 1
    else:
        different_bonds += 1
    
print()
print("Loose bonds (1.5 Å) :", equal_bonds, " Å")
print("Tight bonds (under 1.5 Å)", different_bonds, " Å")
