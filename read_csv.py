import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("RFAM_512_viral_subset.csv")
print(df.head())

lines = []
lengths = {}

for seq, len, family in zip(df['1'].to_list(), df['len'].to_list(), df['label'].to_list()):
    line = ''
    for ch in seq:
        if ch.lower() not in ['c', 'a', 'g', 't', 'u', 'n', 'w', 'r', 'k', 'm', 'y', 's', 'v', 'h', 'd', 'b', '\n']:
            print(ch, "NOT IN VOCAB:", line)
        line = line + ch + ' '
    line = line + '\n'
    lines.append(line)
    if family not in lengths:
        lengths[family] = [len]
    else:
        lengths[family].append(len)

print(lengths.keys())
# plot
seq_lengths = []
for k in lengths.keys():
    seq_lengths.append(np.array(lengths[k]))

fig, ax = plt.subplots()
VP = ax.boxplot(seq_lengths)
plt.savefig("./boxplot_2.png")
plt.show()


f = open("RFAM_512_viral_subset_seq_only.txt", "w")
f.writelines(lines)
f.close()


