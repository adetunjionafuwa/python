# Task
# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

#=======Solution=======
def split_and_join(line):
    # write your code here
    
    return '-'.join(line.split(' '))