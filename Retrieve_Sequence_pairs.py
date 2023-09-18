# Retrive pairs of sequences to make dN/dS comparison
# Open Ectocarpus pep and put name and seq in a dictionary
ecto_dic = {}
e = open("EctsiV220171206110000.prot", "r")
ecto_prot = e.readlines()
e.close()
for line in ecto_prot:
    if line.startswith(">"):
        ecto_id = line.strip()
        ecto_id = line.split(" ")
        ecto_id = ecto_id[0]
    else:
        ecto_seq = line.strip()
        try:
            ecto_dic[ecto_id].append(ecto_seq)
        except KeyError:
            ecto_dic[ecto_id] = ecto_seq

# Open Kelp pep and put name and seq in a dictionary
kelp_dic = {}
k = open("longest_orfs.pep", "r")
kelp_prot = k.readlines()
k.close()
for line in kelp_prot:
    if line.startswith(">"):
        kelp_id = line.strip()
        kelp_id = line.split(" ")
        kelp_id = kelp_id[0]
    else:
        kelp_seq = line.strip()
        try:
            kelp_dic[kelp_id].append(kelp_seq)
        except KeyError:
            kelp_dic[kelp_id] = kelp_seq

# Get the annotations in a dictionary
# Read annotation file
f = open("Test_annot.txt", "r")
annotations = f.readlines()
f.close()
for line in annotations:
    line = line.strip()
    line = line.split("\t")
    # Make a new file containing the new alignment
    filename = line[0] + "_" + line[1] + ".pep"
    alg = open(filename, "w")
    line[0] = ">" + line[0]
    line[1] = ">" + line[1]
    name_kelp = line[1].split(".")
    name_kelp = name_kelp[0]
    if line[0] in ecto_dic and line[1] in kelp_dic:
        print(line[0], file = alg)
        print(ecto_dic[line[0]], file = alg)
        print(name_kelp, file = alg)
        print(kelp_dic[line[1]], file = alg)
    else:
        print("ERRORRR, can't find line")
    alg.close()
