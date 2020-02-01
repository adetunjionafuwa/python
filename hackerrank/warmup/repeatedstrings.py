def repeatedString(s, n):
    submod = n % (len(s))
    subdiv = n // (len(s))
    acount = s.count('a')
    return acount * subdiv + s[:submod].count('a')

#====Alternative=====
return s.count('a') * (n // (len(s))) + s[:n % (len(s))].count('a')