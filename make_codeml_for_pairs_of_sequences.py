# This code is used in conjuction to bash script to produce a codeml script for each gene analyzed.
# The codemml file is then processed to produce dN/dS for each gene sequence

f = open("names.txt", "r")
names = f.readlines()
f.close()

for name in names:
    file = name.strip() + ".ctl"
    j = open(file, "w")
    print("seqfile = ", name.strip() + ".pal2nal", " * sequence data filename", file=j)
    print("outfile = codeml.txt   * main result file name", file=j)
    print("*treefile = cluster_1_tree2.nw", file=j)
    print("noisy = 0      * 0,1,2,3,9: how much rubbish on the screen", file=j)
    print("verbose = 0      * 1:detailed output", file=j)
    print("runmode = -2     * -2:pairwise", file=j)
    print("seqtype = 1      * 1:codons", file=j)
    print("CodonFreq = 2      * 0:equal, 1:F1X4, 2:F3X4, 3:F61", file=j)
    print("model = 1      *", file=j)
    print("NSsites = 0      *", file=j)
    print("icode = 0      * 0:universal code", file=j)
    print("fix_kappa = 1      * 1:kappa fixed, 0:kappa to be estimated", file=j)
    print("kappa = 1      * initial or fixed kappa", file=j)
    print("fix_omega = 0      * 1:omega fixed, 0:omega to be estimated", file=j)
    print("omega = 0.5    * initial omega value", file=j)
    print("*ndata = 1", file=j)
    j.close()
