import glob, os




OLDSTR = b"""lang_3_3_2 = {"""

NEWSTR = b"""lang_3_4_0 = {
    "Show calendar": "",
    "Disabled": "",
    "Open quick settings": "",
    "Show desktop": "",
    "Open run dialog": "",
    "Open task manager": "",
    "Open start menu": "",
    "Open search menu": "",
    "Change task": "",
    "Change the action done when the clock is clicked": "",
}

lang_3_3_2 = lang_3_4_0 | {"""

input(f"Path is \"{os.getcwd()}\" Press [INTRO] to contniue")
print()
print()
print("Lang files to update: ")

for file in glob.glob("lang_*.py"):
    print(" -", file)
print()
input("Press [INTRO] to contniue")

print()
print()
print("old string:", OLDSTR)
print("new string:", NEWSTR)
print()
input("Press [INTRO] to contniue")

for file in glob.glob("lang_*.py"):
    print("Processing", file, "...")
    try:
        with open(file, "rb") as f:
            contents = f.read()
        with open(file, "wb") as f:
            f.write(contents.replace(OLDSTR, NEWSTR))
            
        print(file, "has been updated successfully")
    except:
        print("🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥", file, "has been updated successfully")
        
input("Finished, press [INTRO] to close")
