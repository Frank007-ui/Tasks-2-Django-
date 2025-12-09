import matplotlib.pyplot as plt
from collections import Counter
text="ANKITHA"
counter=Counter(text)
chars=list(dict.fromkeys(text))
counts=tuple(counter[ch] for ch in chars)
print("character:", chars)
print("count:",counts)
plt.bar(chars,counts)
plt.title("Character Frequency Count")
plt.xlabel("Characters")
plt.ylabel("Counts")
plt.show()