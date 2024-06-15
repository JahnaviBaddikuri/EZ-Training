def count_vowel(s):
    l={'a':0,'e':0,'i':0,'o':0,'u':0}
    for i in s:
        for j in i:
            # print(j)
            if j=='a' or j=='A':
                l['a']+=1
            elif j=='e'or j=='E':
                l['e']+=1
            elif j=='i'or j=='I':
                l['i']+=1
            elif j=='o'or j=='O':
                l['o']+=1
            elif j=='u'or j=='U':
                l['u']+=1
    x=max(l.values())
    result=[]
    for i,j in l.items():
        if j==x:
            result.append(i)
    return result

i_p=[
    ["Alex","I enjoy hiking in the mountains."],
    ["Sam","A lovely sunny day at the beach"],
]
o_p={}
for i in i_p:
    o_p[i[0]]=count_vowel(i[1])
print(o_p)
