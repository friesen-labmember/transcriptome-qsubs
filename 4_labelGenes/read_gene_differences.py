id_dict = {}

for num in ['3', '5', '6', '7', '9', '10', '15', '17', '18']:
    print(num + " running")
    labelname = "/mnt/lustre_scratch_2012/keithzac/Tf_Analysis/GeneLabelOutput/Tf_" + num + "label"
    genefile = open(labelname, 'r')
    for line in genefile:
        linesplit = line.split(';')
        if len(linesplit) == 2:
            ID = linesplit[0]
            Note = linesplit[1]
            if ID not in id_dict:
                id_dict[ID] = (Note, [num])
            elif num not in id_dict[ID][1]:
                id_dict[ID][1].append(num)

outfile = open ("genedict", 'w')
for key in id_dict:
    outfile.write(str(key) + " ; " + str(id_dict[key][0]).rstrip() + " ; " + str(id_dict[key][1]) + "\n")

onlyOne = {}
onlyEight = {}
onlyGroupA = {}
onlyNotGroupA = {}
onlyGroupB = {}
onlyNotGroupB = {}
onlyGroupC = {}
onlyNotGroupC = {}

GroupA = ['3', '5', '6']
GroupB = ['7', '9', '10']
GroupC = ['15', '17', '18']

for key in id_dict:
    count = len(id_dict[key][1])
    if count == 1:
        onlyOne[key] = id_dict[key]
    elif count == 8:
        onlyEight[key] = id_dict[key]
    elif count == 3:
        if '3' in id_dict[key][1] and '5' in id_dict[key][1] and '6' in id_dict[key][1]:
            onlyGroupA[key] = id_dict[key]
        if '7' in id_dict[key][1] and '9' in id_dict[key][1] and '10' in id_dict[key][1]:
            onlyGroupB[key] = id_dict[key]
        if '15' in id_dict[key][1] and '17' in id_dict[key][1] and '18' in id_dict[key][1]:
            onlyGroupC[key] = id_dict[key]
    elif count == 6:
        if '3' not in id_dict[key][1] and '5' not in id_dict[key][1] and '6' not in id_dict[key][1]:
            onlyNotGroupA[key] = id_dict[key]
        if '7' not in id_dict[key][1] and '9' not in id_dict[key][1] and '10' not in id_dict[key][1]:
            onlyNotGroupB[key] = id_dict[key]
        if '15' not in id_dict[key][1] and '17' not in id_dict[key][1] and '18' not in id_dict[key][1]:
            onlyNotGroupC[key] = id_dict[key]

differencefile = open("gene_sample_differences.txt", 'w')

differencefile.write("Genes found only in group A (3, 5, 6):\n")
for key in onlyGroupA:
    differencefile.write(str(key) + " ; " + str(onlyGroupA[key][0]).rstrip() + " ; " + str(onlyGroupA[key][1]) + "\n")
differencefile.write("\n")
differencefile.write("Genes found only in group B (7, 9, 10):\n")
for key in onlyGroupB:
    differencefile.write(str(key) + " ; " + str(onlyGroupB[key][0]).rstrip() + " ; " + str(onlyGroupB[key][1]) + "\n")
differencefile.write("\n")
differencefile.write("Genes found only in group C (15, 17, 18):\n")
for key in onlyGroupC:
    differencefile.write(str(key) + " ; " + str(onlyGroupC[key][0]).rstrip() + " ; " + str(onlyGroupC[key][1]) + "\n")
differencefile.write("\n")

differencefile.write("Genes only missing from group A (3, 5, 6):\n")
for key in onlyNotGroupA:
    differencefile.write(str(key) + " ; " + str(onlyNotGroupA[key][0]).rstrip() + " ; " + str(onlyNotGroupA[key][1]) + "\n")
differencefile.write("\n")
differencefile.write("Genes only missing from group B (7, 9, 10):\n")
for key in onlyNotGroupB:
    differencefile.write(str(key) + " ; " + str(onlyNotGroupB[key][0]).rstrip() + " ; " + str(onlyNotGroupB[key][1]) + "\n")
differencefile.write("\n")
differencefile.write("Genes only missing from group C (15, 17, 18):\n")
for key in onlyNotGroupC:
    differencefile.write(str(key) + " ; " + str(onlyNotGroupC[key][0]).rstrip() + " ; " + str(onlyNotGroupC[key][1]) + "\n")
differencefile.write("\n")

differencefile.write("Genes found only in one sample:\n")
for key in onlyOne:
    differencefile.write(str(key) + " ; " + str(onlyOne[key][0]).rstrip() + " ; " + str(onlyOne[key][1]) + "\n")
differencefile.write("\n")
differencefile.write("Genes found in all but one one sample:\n")
for key in onlyEight:
    differencefile.write(str(key) + " ; " + str(onlyEight[key][0]).rstrip() + " ; " + str(onlyEight[key][1]) + "\n")
differencefile.write("\n")
