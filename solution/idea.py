file1=open("doc1.txt","r")
text1=file1.readlines()
file2=open("doc2.txt","r")
text2=file2.readlines()
str1=''.join(text1)
str2=''.join(text2)
sent_text1=str1.split('.')
sent_text2=str2.split('.')
final_list=[]
for z in sent_text1:
    for y in sent_text2:
        if z == y:
            final_list.append(z)
final_list            