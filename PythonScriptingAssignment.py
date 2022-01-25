# Python Assignment
import json,urllib.request
import sys

subDomain = input("Enter the sub-domain: ")
#print("Subdomain: "+subDomain)

data = ""
try:
    data = urllib.request.urlopen("https://jsonplaceholder.typicode.com/"+subDomain).read()
except:
    sys.exit("Data is not found for domain type :/"+subDomain)
    
input = json.loads(data)
# print(data)

file1 = open(subDomain+".txt","w")

if subDomain == "user":
    file1.write("List of all Users\n\n")
    for row in input:
        file1.write("Name-"+row['name']+"\n")
        file1.write("Phone-"+row['phone']+"\n")
        file1.write("Address-"+row['address']+"\n")
        file1.write("\n")
elif subDomain == "comments":
    file1.write("List of all Comments\n\n")
    for row in input:
        file1.write("Name-"+row['name']+"\n")
        file1.write("Email-"+row['email']+"\n")
        file1.write("Body-"+row['body']+"\n")
        file1.write("\n")
elif subDomain == "album" or subDomain == "todos":
    if subDomain == "album":
        file1.write("List of all Albums\n\n")
    else:
        file1.write("List of all Todos\n\n")
    for row in input:
        file1.write("Title-"+row['title']+"\n")
        file1.write("\n")
elif subDomain == "photos":
    file1.write("List of all Photos\n\n")
    for row in input:
        file1.write("Title-"+row['title']+"\n")
        file1.write("URL-"+row['url']+"\n")
        file1.write("\n")

file1.close()

print(subDomain+".txt file created successfully !!!")