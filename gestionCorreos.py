emails = ["jon.smith@microsoft.com", "maria.fernandez@microsoft.com", "david@microsoft.com", "isabel@microsoft.es","alfonso@gmail.com"]
names = []
uniqueEmails = []

for i in emails:
    
    name,dominio = i.split("@")
    
    if len(i)>1 and dominio not in uniqueEmails:
        uniqueEmails.append(dominio)
        
    if "." in name:
        smallName, rest = name.split(".")
        names.append(smallName)
        
    else : names.append(name)

newEmails = []

for i in names:
    i = i+"@nazaret.eus"
    newEmails.append(i)
    
with open ("newEmails.csv", "w") as f: 
    for i in newEmails:
        f.write(i)
        f.write(",")