import os

#lazy ai code :)
def ask_yes_no(question):
    while True:
        response = input(f"{question} (y/n): ").lower()
        if response in ['y', 'n']:
            return response == 'y'
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

pwd = os.getcwd()
projectName = input("Enter name of your project (p much just the folder name rn tbh)\n")
#idk how to automatically find game info yet so we doing this now
print("Couldn't find game info (coming later i swear)")
gameName = input("Enter name of your game (this can be changed later.)\n")
devName = input("Enter the Developer's name (this can be changed later.)\n")
#ask mod and author name 
modName = input("Enter name of your mod (this can be changed later.)\n")
authorName = input("Enter your author name (this can be changed later.)\n")

if ask_yes_no("Sanity check, is this correct?\nMod Name:", modName, "\nMod Author", authorName, "\nGame Name:", gameName, "\nGame Author", devName, "\nDirectory:", pwd):
    projFolderDir = f"{pwd}/{projectName}"
    projdata = [projectName, gameName, devName, modName, authorName, projFolderDir]
    
    print(f"MT: OK, Making project folder at {projFolderDir}...")
    os.mkdir(projFolderDir, mode=0o777)
    print ("MT: Created! changing to new directory...")
    os.chdir(projFolderDir)
    print("MT: Done! creating project...")
    os.system(f'dotnet new classlib -f net6.0 -o {projectName}')
    os.system('dotnet new sln')
    print("MT: creating AssembleyInfo...")
    assemble = f'using MelonLoader;\nusing MyProject; // The namespace of your mod class\n// ...\n[assembly: MelonInfo(typeof(MyMod), "{modName}", "version", "{authorName}")]\n[assembly: MelonGame("{devName}", "{gameName}")]'

    with open("AssemblyInfo.cs", "a") as assfile:
        assfile.write(assemble)
    
    os.system(f'dotnet sln add {projectName}/{projectName}.csproj')
    
    print("MT: successfuly created project! exiting...")
    exit()
else:
    print("MT: Cancelling project creation and exiting...")
    exit()

#------------------------------------------------------------------------------------------------
#setup game refs

#read game name and version from logs
#parse first 24 lines or until the "Preferences Loaded" msg

#create AssemblyInfo.cs and put following data

