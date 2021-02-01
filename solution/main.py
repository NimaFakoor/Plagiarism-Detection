
__author__ = "NimaFakoor & SaraZamani"
__version__ = '1.0'

#####################################
#imports
#####################################
import os
import sys
#from argparse import ArgumentParser
#from plagiarism import PlagiarismDetector

#####################################
'''
Takes in the file of synonyms and constructs a dictionary assoicating them to
a singular common word.
'''
def construct_syn_dict(synfile):
	syndict = {}
	with open(synfile) as synsfile:
		for syns in synsfile:
			words = syns.split(" ")
			value = words[0].lower()
			for word in words:
				syndict[word.lower()] = value
	return syndict
#####################################
'''
Uses our synonym dictionary, input file, and n number of tuples to construct
individual tuples from our input text to cross reference.
'''
def construct_tuples(syndict, inputfile, n):
	tuples = []
	with open(inputfile) as inputfile:
		for line in inputfile:
			words = line.split(" ")
			for idx in range(len(words)):
				words[idx] = words[idx].lower()
				if words[idx] in syndict:
					words[idx] = syndict[words[idx]]
			for idx in range(len(words) - n + 1):
				n_tuple = ""
				for x in range(n):
					n_tuple += words[idx + x] + " "
				tuples.append(n_tuple)
	return tuples
#####################################
'''
Constructs a dictionary of tuples given our list of tuples for easy cross-referencing
to check if we have a previous occurance.
'''
def construct_tuples_dict(tuples):
	tuples_dict = {}
	for each in tuples:
		if each not in tuples_dict:
			tuples_dict[each] = 0
		tuples_dict[each] += 1
	return tuples_dict
#####################################
'''
Using two tuple lists, we construct a dictionary of tuples and then check occurances
of the second tuple list on the first tuple list using the dictionary.
'''
def plagiarism_detect(tules1, tuples2):
	tuple1_dict = construct_tuples_dict(tules1)
	plagiarism_count = 0
	for each in tuples2:
		if each in tuple1_dict:
			plagiarism_count += 1
	return plagiarism_count
#####################################

##########################################################################

##########################################################################

def main():

	#####################################
	#		defined and variables
	#####################################
	WELCOME = "|: welcome :|"

	#THIS_FOLDER = os.path.dirname(os.path.abspath('Plagiarism-Detection/problem/')) 

	#file1 = 'file1.txt'
	#file2 = 'file2.txt'
	#synfile = 'syms.txt'

	#tuple_size = 3		
	N = 3

	try:
			
		# assigning our supplied arguement files to variables
		file1 = sys.argv[1]
		file2 = sys.argv[2]
		synfile = sys.argv[3]

		print(os.listdir())

		print("\n"+ WELCOME +"\n")

		# if an optional arguement is supplied for N, we assign it to a variable
		if len(sys.argv) == 5:
			N = int(sys.argv[4])
		# construct our synonym dictionary from our synonym 
		
		print("File Path 1: {}\nFile Path 2: {}\nSynonyms Path: {}\n".format(file1, file2, synfile))

		#####################################
		#     class PlagiarismDetector 
		#####################################
		#print("\n Percentage Plagiarized: {} \n".format(PlagiarismDetector(file1, file2, synfile,tuple_size).get_plagiarized_percentage()))
		#####################################
		#     class PlagiarismDetector 
		#####################################

		syndict = construct_syn_dict(synfile)
		# construct a list of tuples from our input files
		input1tuples = construct_tuples(syndict, file1, N)
		input2tuples = construct_tuples(syndict, file2, N)
		# perform the plagiarism detection algorithm using our list of tuples from each input file
		plagiarism_count = plagiarism_detect(input1tuples, input2tuples)
		print (str(float(plagiarism_count)/len(input2tuples) * 100) + "")
	except: #if we have an exception thrown, the supplied arguements are incorrect
		print ("The inputs for the file were incorrect! \n For help and usage, please refer to readme.md!")
		sys.exit()

#####################################

if __name__ == '__main__':
	main()

####################################################################################################################################################