'''Running a Markov Chain to build Robert Frost's first "original" poem in 50 years. May need to rerun until you get a good one!'''


from markov_python.cc_markov import MarkovChain 
from fetch_data_f import just_poems 


mc = MarkovChain()
mc.add_string(just_poems)

#Goal: Make a three stanza poem of 4 lines, 9 words per line in the phrasing of Robert Frost

print '"Random thoughts" by Robert (Markov) Frost\n'

def poem():
	stanzas = 3
	while stanzas > 0:
		stanza()
		print ("\n")
		stanzas = stanzas - 1

def stanza():
	set = 4
	while set > 0:
		raw_list = mc.generate_text()
		#convert list to a string, make the first word uppercase and print
		string = ' '.join(raw_list)
		line = string.capitalize()
		print line
		set = set - 1
		
print poem()
	




