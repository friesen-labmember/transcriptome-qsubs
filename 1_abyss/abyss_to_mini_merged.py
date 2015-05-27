for s in ["3", "5", "6", "7", "9", "10", "15", "17", "18"]:
	for k in ["70", "75", "80", "85"]:
	
		path = "/mnt/scratch/keithzac/new_TF/" + s + "/" + k +"/"
		infilename = path + "Tf_" + s + "_k" + k + "-contigs.fa"
	
		try:
			infile = open(infilename, 'r')
			outfilename = path + "Tf_" + s + "_k" + k + "-contigs-mini.fa"
			outfile = open(outfilename, 'w')
	
			for line in infile:
				
				#Check if line has spaces (lines with spaces are summary lines)
				if len(line.split()) > 1:
					
					#The second item in a summary line is the length of a contig - remove contigs with length < 200
					if int(line.split()[1]) < 200:
						good = False
	
					#Only write summary lines that belong to 200+bp contigs
					else:
						outfile.write(line)
						good = True
				
				#No spaces means the line is the raw base pairs
				else:
					#If you wrote the summary line, write the base pairs too
					if good:
						outfile.write(line)
	
			infile.close()
			outfile.close()
	
		except IOError:
			print("Could not open " + infilename)
			
	#Merge the mini files	
	mergefilename = "/mnt/scratch/keithzac/new_TF/" + s + "/Tf_" + s + "-merged.fa"
	mergefile = open(mergefilename, 'w')
	for k in ["70", "75", "80", "85"]:
		path = "/mnt/scratch/keithzac/new_TF/" + s + "/" + k +"/"
		infilename = path + "Tf_" + s + "_k" + k + "-contigs-mini.fa"
		infile = open(infilename)
		for line in infile:
			mergefile.write(line)
		infile.close()
	mergefile.close()