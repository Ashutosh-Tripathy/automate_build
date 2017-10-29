from os.path import relpath
import os
my_path = "C:/test/CodeJam/CodeJam"

path_map = {}
for root, directories, files in os.walk(my_path):
    for filename in files:
        # Join the two strings in order to form the full filepath.
        filepath = os.path.join(root, filename)
        # file_paths.append(filepath)  # Add it to the list.
        filepath = relpath(filepath,my_path).replace("\\","/")
        # filepath = filepath.replace("\\","/")
        path_map[filename] = filepath
output = []
with(open("input.txt","r")) as f:
    test = f.readline().split(":").pop(0).strip()
    output.append(path_map[test])
print(output)
with(open("output.txt", "w")) as f:
    f.writelines(output)
    f.close()
