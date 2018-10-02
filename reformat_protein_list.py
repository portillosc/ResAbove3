#This is just going to reformat the protein list I created in a file called raw_protein_id_list.txt
#I basically made a query on pdb and copied and pasted the output of the 10k+ ids so it looks pretty
#messy. I'm going to clean it up by reformatting it to another txt file with a single id per line, each
#will be seperated by a newline character

#read in the file
file = open('raw_protein_id_list.txt')

#create the output file
output = open('protein_id_list_10_2.txt','w')

#Theres only one line in the file so I can read it directly into a string
row = file.readline()

#strip and split row
row = row.strip().split(',')

#iterate through each index, check to make sure it's not only whitespace,
#then strip once again before writing each index to the output followed by a newline
for index in row:
   if(index):
      output.write(index.strip() + '\n')
