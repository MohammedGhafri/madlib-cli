import re
arrayForInput=[]


# function for inputs
def fin(x):
    a=input()
    arrayForInput.append(a)
    
    return arrayForInput[x] 



a=6
# tp open the text.txt file
with open('assets/text.txt') as f:
    content=f.read()


content
# to change the changable words with %s to do the string format
x=re.sub("{\w*}","%s",content)

# to store the changable words into list
words=re.findall("{\w*}",content)
# print(x,words)



# for test purposes
def parse(txt):
    words=re.findall("{\w*}",txt)
    str1 = ''.join(words)
    return str1,words

# print(parse(content))


# for test purposes

def  read_template(txt):
    return txt.read().strip()




# an empty array to store input from user
emp_arr=[]   

# function to do the input from user and show the final result
def fun_input(statement):

    for i in words:
        remove_char=re.sub("{|}",'',i)
        
        emp_arr.append(input("\n\nPlease Enter a/an %s  : "%(remove_char)))
    with open('assets/user_text.txt','w') as f2:
        f2.write(x % tuple(emp_arr))
    return (x % tuple(emp_arr))

print(fun_input(words))

def fun_input_test(statement,entries):
    # input_arr=["mohammed","study","alone","computer","home","sleepy","table","mouse","laptop"]
    # test_word=re.findall("{\w*}",statement)
    x=re.sub("{\w*}","%s",statement)
    # print(x)
    return (x % entries)



# print(fun_input_test(open('assets/text.txt').read(),aaaa))


























# file=open('assets/text.txt')
# content=file.read()

# x = re.findall("{\w*}", content)
# # print(x)
# b=''
# # for i in x:
    
#     # b=re.sub(correction[0],"change",content)
#     # b=re.sub(i,fin(x.index(i)),content)


# # print(b)
# arr=['{noun}', '{verb}', '{adverb}', '{noun}', '{noun}', '{adjective}', '{noun}', '{noun}', '{noun}']
# # print(len(content))
# x_index=0
# emp_arr=''
# for i in arr:
#     x_index=content.index("{",x_index+2,)
#     print(x_index)
#     b=re.sub(arr[0],fin(x.index(i)),content[x_index:x_index+7])
#     emp_arr+=b
#     # x_index+=5
# print(emp_arr)
# # print(b)




welcome= """ 
♥♦♥Welcome ♥♦♥
This is madlib game, You need to enter different kinds of words such as nouns verbs adjectives adverbs.
lword case is not sensitve
"""

# if __name__=='__main__':
#     print(welcome)    









