# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.
import requests
from bs4 import BeautifulSoup

base_url = 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")

html_str = soup.prettify(formatter=None)

html_str = html_str.replace('student', 'AMAZING student')
html_str = html_str.replace('https://testbed.files.wordpress.com/2012/09/bsi_exposition_041316_192.jpg', 'media/IMG_6197.JPG')

#for menu in soup.find_all(class_='menu'):
	# for item in menu:
	# 	try:
	# 		text = item.get_text()
	# 	except:
	# 		continue
	# 	if 'student' in text:
	# 		text = text.replace_with('AMAZING student')
			#print(text)

# for elem in soup.find_all(class_='field-item even'):
# 	text2 = elem.get_text()
# 	text2 = text2.replace_with('student', 'AMAZING student')
# 	print(text2)

# for image in soup.find_all('img'):
# 	if image.get('src') == 'https://testbed.files.wordpress.com/2012/09/bsi_exposition_041316_192.jpg':
# 		image.get('src') == 'IMG_6197.JPG'

fout = open('index.html','w')
fout.write(html_str)



#prettify converts to string
#fout.write(results

