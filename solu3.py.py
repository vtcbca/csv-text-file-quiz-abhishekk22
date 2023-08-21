bcainfo=""" BCA course info:
it is 3 years undergraduate course."""

with open("BCA.txt", "w") as file:
     file.write(bcainfo)

rows={'A':0,'B':0, 'C':0}

with open('BCA.txt','r') as bca_intro:
    lines=bca_intro.readlines()
    for line in lines:
            f_char=line.strip()[0]
            if f_char in rows:
                rows[f_char]+=1

for char,cout in rows.items():
    print(f"Number of rows start with '{char}':{cout}")
                
