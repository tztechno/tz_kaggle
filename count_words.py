
A = pd.DataFrame(0, index=range(len(data)), columns=words)

for i, text in enumerate(data):
    for word in words:
        #A.loc[i, word] = int(word in text) # exist or not 
        A.loc[i, word] = text.count(word) # count the word
