file = open("class-notes.txt", "r")
print(file.read(40))
file.close()
print()

file = open("class-notes.txt", "r")
lines = file.readlines()
file.close()
print("Total lines:", len(lines))
for i in range(len(lines)):
    print(i + 1, "->", lines[i].strip())
print()

file = open("class-notes.txt", "r")
for line in file:
    print("Reading:", line.strip())
file.close()
print()

file = open("class-notes.txt", "r")
for line in file:
    if line.startswith("SKIP"):
        print("skip ->", line.strip())
    else:
        print("keep ->", line.strip())
file.close()
print()

print("\nPART 5: Copy selected lines to a new file")
file = open("class-notes.txt", "r")
lines = file.readlines()
file.close()
out = open("organized-notes.txt", "w")
for i in range(0, len(lines), 2):
    out.write(lines[i])
out.close()
print("Odd lines saved to organized-notes.txt")

print("====== Organized notes ======")
file = open("organized-notes.txt", "r")
for line in file:
    print(line.strip())
file.close()