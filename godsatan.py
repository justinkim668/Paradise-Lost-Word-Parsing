import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

def wordfreq(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

text1 = []
filename1 = "pl.txt"
with open(filename1) as paradise:
    for line in paradise:
        replace = line.replace("\r", "").replace("\n", "").replace('"', '').replace(".", "").replace(",","").replace("?", "").replace(":", "").replace(";", "").replace("!", "").replace("(","").replace(")","").replace("--", "")
        text1.append(replace.lower())

bigassbook = " ".join(text1)
print(bigassbook)

print(wordfreq(bigassbook))

god = wordfreq(bigassbook).get("god")
satan = wordfreq(bigassbook).get("satan")
objects = ("God","Satan")
y_pos = np.arange(len(objects))
performance = [god, satan]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.title("God vs. Satan in Paradise Lost")
plt.xlabel('Word')
plt.ylabel('Frequency in Text')

plt.show()

exit()
