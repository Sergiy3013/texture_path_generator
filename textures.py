import os
import glob

resFile = "result.txt"
folder = ""
if folder == "": folder = os.getcwd()

whiteListFormats = [".png", ".dds"]
blackListWords = ["preview", "Screenshot"]
resFile = "result.txt"

files = []
dir_path = folder + "\\**\\*.*"
for file in glob.glob(dir_path, recursive=True): 
    files.append(file)

result = []
for file in files:
    if any(a in file for a in whiteListFormats):
        if not any(b in file for b in blackListWords):
            result.append(file)

print("Files find:", len(files))
print("Files selecter:", len(result))

string = ""
for file in result: string = f'{string}{file}\n'

text_file = open(resFile, "wt")
n = text_file.write(string)
text_file.close()
