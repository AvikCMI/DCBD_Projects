#Spazer tool for processing web pages
#

from bs4 import BeautifulSoup
import pathlib
import re

#Variables to track the input, output and gained space
space_gained = 0
space_input = 0
space_output = 0

print("Welcome to Spazer\n")

#Compiling regular expressions

Add = re.compile(r".*(address|Address).*")
All = re.compile(r".*") 
address = re.compile(r"address|Address|Contact(s)|CONTACT|ADDRESS|contact") 
pincode1 = re.compile(r"\b\d\d\d(\s)*\d\d\d\b")
pincode2 = re.compile(r"\b\d\d\d(\s)*\d\d\d\b|\b\d\d(\d?)\b")

for x in range(10):
    filename = str(x) + ".html"
    file = pathlib.Path('input/' + filename)
    if (file.exists()):

        #Read each file
        print("Reading " + filename)
        f = open('input/' + filename, 'r', errors="ignore")
        contents = f.read()   
        
        #Remove html tags
        soup = BeautifulSoup(contents,'html.parser') 
        
        #Your code begins  ###############################
        newoutput=''
        txt = ''
        
        
        
        if len(newoutput) < 20:
            soup = BeautifulSoup(contents,'html.parser')        
            output = soup.get_text()
            output = output.replace("\n",'')
        
            newoutput=''
            for i in re.finditer(address,output):
                j=(output[(i.start()):(i.start()+200)]).strip()
                if j not in newoutput:
                    newoutput=newoutput+(output[(i.start()):(i.start()+250)]).strip()
            for i in re.finditer(pincode1,output):
                j=(output[(i.start()-150):(i.start()+50)]).strip()
                if j not in newoutput:
                    newoutput=newoutput+(output[(i.start()-250):(i.start()+70)]).strip()
                    print(i)
            
        if len(newoutput) < 20:
            soup = BeautifulSoup(contents,'html.parser')        
            output = soup.get_text()
            output = output.replace("\n",'')
        
            newoutput=''
            for i in re.finditer(address,output):
                newoutput=newoutput+(output[(i.start()):(i.start()+250)]).strip()
            for i in re.finditer(pincode2,output):
                newoutput=newoutput+(output[(i.start()-250):(i.start()+70)]).strip()
        
        #Your code ends  #################################
             
        #Write the output variable contents to output/ folder.
        print ("Writing reduced " + filename)
        fw = open('output/' + filename, "w")
        fw.write(newoutput)
        fw.close()
        f.close()
        
        #Calculate space savings
        space_input = space_input + len(contents)     
        space_output = space_output + len(newoutput)
        
space_gained = round((space_input - space_output) * 100 / space_input, 2)

print("\nTotal Space used by input files = " + str(space_input) + " characters.") 
print("Total Space used by output files = " + str(space_output) + " characters.")
print("Total Space Gained = " + str(space_gained) + "%")
