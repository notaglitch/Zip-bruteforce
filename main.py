import zipfile

file_name = input("Enter the file name: ")
wordlist_name = input("Enter the wordlist name: ")

if file_name[-4:] == ".zip":
    pass
else:
    file_name = file_name + ".zip"

zip_file = zipfile.ZipFile(file_name)

with open(wordlist_name, "r") as file:
    for line in file:
        line = line.strip()

        try:
            zip_file.extractall(pwd=line)
            print("Password found: ", line)
            break
        except:
            print(line)
            continue
