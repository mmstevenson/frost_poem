'''import various poems of Robert Frost and string them together'''

import requests

#download text poems of Robert Frost
frost = requests.get('https://archive.org/stream/poemsofrobertfro029898mbp/poemsofrobertfro029898mbp_djvu.txt')


#cut off the long legal footer in order to highlight the author's actual words, leaving "trunc" as a string with the full book text
from icemac.truncatetext import truncate
frost_trunc = truncate(frost.text, 350000)



#convert road not taken html to a string
road = requests.get('https://www.naic.edu/~gibson/poems/frost1.html')
road_text = road.text

#concatenate the two strings
seq = (frost_trunc, road_text);
full_text = ' '.join( seq )

#remove the html tags
import re
def striphtml(data):
    p = re.compile(r'<[^<]+?>')
    return p.sub('', data)

no_html = striphtml(full_text)

#remove everything other than letters
poems_header = re.sub("[^'a-zA-Z]"," ", no_html)

#remove the header
just_poems = poems_header[30000:]


#print just_poems
