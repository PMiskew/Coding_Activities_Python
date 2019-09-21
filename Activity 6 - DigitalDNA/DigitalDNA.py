''' 
Takes a valid codon represented as String s and returns the   
associated Amino Acid.

@param s must represent a valid codon sequence
@return a String representing amino acid associated with codon s
   
Precondition s must be a valid codon sequence
   
'''
def findAminoAcid(s):

	AA_CODE = [	"TTT","TTC","TTA","TTG","TCT","TCC","TCA","TCG","TAT","TAC",
				"TAA","TAG","TGT","TGC","TGA","TGG","CTT","CTC","CTA","CTG",
				"CCT","CCC","CCA","CCG","CAT","CAC","CAA","CAG","CGT","CGC",
				"CGA","CGG","ATT","ATC","ATA","ATG","ACT","ACC","ACA","ACG",
				"AAT","AAC","AAA","AAG","AGT","AGC","AGA","AGG","GTT","GTC",
				"GTA","GTG","GCT","GCC","GCA","GCG","GAT","GAC","GAA","GAG",
				"GGT","GGC","GGA","GGG"]

	AA_CODE_VALUE =	[	"F","F","L","L","S","S","S","S","Y","Y",
						"*","*","C","C","*","W","L","L","L","L",
						"P","P","P","P","H","H","Q","Q","R","R",
						"R","R","I","I","I","M","T","T","T","T",
						"N","N","K","K","S","S","R","R","V","V",
						"V","V","A","A","A","A","D","D","E","E",
						"G","G","G","G"]

	for i in range(0,len(AA_CODE),1):
		if AA_CODE[i] == s:
			return AA_CODE_VALUE[i]
	return "-1" #This program should never reach this point, but -1 is a nice way to indicate an error

''' 
 Takes one half of a DNA double helix represented as String s and
 returns the complement strand as a String.
 @param String s represents one half of a DNA double helix
 @return a string representing the complement of strands
 precondition s is a string consisting only of characters A,C,T and G 
'''
def findComplement(s):
	print("Find Complement")

'''
 Takes one half of a DNA double helix represented as string s and
 returns the RNA sequence derived from string s.
 @param  String s represents one half of a DNA double helix
 @return a string representing the RNA sequence derived from strands
  
 precondition s is a string consisting only of characters A,C,T and G    
'''
def findRNAStrand(s):
	print("find RNA Strand")



print(findAminoAcid("TTT"));
print(findAminoAcid("TAT"));
print(findAminoAcid("TAG"));
print(findAminoAcid("GGG"));