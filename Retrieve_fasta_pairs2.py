# Retrive sequence fasta in pairs

# Open Ectocarpus pep and put name and seq in a dictionary
ecto_dic = {}
e = open("EctsiV220171206110000.mRNA", "r")
ecto_prot = e.readlines()
e.close()
for line in ecto_prot:
    if line.startswith(">"):
        ecto_id = line.strip()
        ecto_id = line.split(" ")
        ecto_id = ecto_id[0]
    else:
        ecto_seq = line.strip()
        # try:
        #     ecto_dic[ecto_id].append(ecto_seq)
        # except KeyError:
        ecto_dic[ecto_id] = ecto_seq

# Open Kelp pep and put name and seq in a dictionary
kelp_dic = {}
k = open("1561073896_clean_99_500_collapsed_reads.fa", "r")
kelp_prot = k.readlines()
k.close()
for line in kelp_prot:
    if line.startswith(">"):
        kelp_id = line.strip()
        kelp_id = line.split("\t")
        kelp_id = kelp_id[0].strip()
    else:
        kelp_seq = line.strip()
        # try:
        #     kelp_dic[kelp_id].append(kelp_seq)
        # except KeyError:
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
    filename = line[0] + "_" + line[1] + ".fa"
    alg = open(filename, "w")
    ecto_name = ">" + line[0]
    kelp_name = ">" + line[1]
    kelp_name = kelp_name.split(".")
    kelp_name = kelp_name[0]
    if ecto_name in ecto_dic and kelp_name in kelp_dic:
        print(ecto_name, file = alg) #, file = alg
        print(ecto_dic[ecto_name], file = alg)
        print(kelp_name, file = alg)
        print(kelp_dic[kelp_name], file = alg)
    else:
        print("ERRORRR, can't find line")
    alg.close()
