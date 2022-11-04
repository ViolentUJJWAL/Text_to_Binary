string = input("Enter String: ")
l=[]
for a in range(len(string)):
	l.append(str(bin(ord(string[a]))))
string=" ".join(l)
print(f"Binary String /// {string} \\\\\\")
with open("readToBINERY.txt", "w") as ap:
	ap.write(string)
with open("readToBINERY.txt", "r") as re:
	string=''
	for i in (re.read().split(" ")):
		string = string + chr(int(i,2))
print(f"String is <<< {string} >>>")