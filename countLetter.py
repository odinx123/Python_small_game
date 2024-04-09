while True:
    inpt = input()
    if inpt[0] == '0': break                                     # if the key is not in English, discard it
    dic = {key:inpt.count(key) for key in inpt if key.isalpha()} # key is a input literal, value is count
    arr = sorted(dic) # sorted sort the dic(unchanged), and return a list to arr
    for i in arr:
        print(f"{i}:{dic[i]}", end=' ') # Use the key to find value
    else:                               # Here, Value is the count of Key in the sentence
        print()

# /*******************************************************/ #
# The second way of writing

# while True:
#     inpt = ''.join(s for s in input() if s.isalnum()) # put english in inpt, inpt is a str
#     if inpt[0] == '0': break                                 # and number
#     dic = {x:inpt.count(x) for x in inpt if x.isalpha()} # key is a input literal, value is count
#     arr = sorted(dic) # sorted sort the dic(unchanged), and return a list to arr
#     for i in arr:
#         print(f"{i}:{dic[i]}", end=' ')
#     else:
#         print()