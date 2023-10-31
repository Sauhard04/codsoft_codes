import random as r
print("\n\n\t\t\t\tPASSWORD GENERATOR\n\n")
inp=int(input("\t----PRESS 1 AND HIT ENTER KEY TO GENERATE PASSWORD----\n"))
if inp==1:
    l_alp=[chr(i) for i in range(97,123)]
    u_alp=[chr(j) for j in range(65,91)]
    num="0123456789"
    sp_ch="()*&^%$#@!?><:|"
    p=""
    for i in range(2):
        p+=r.choice(l_alp)
    for i in range(2):
        p+=r.choice(u_alp)
    for i in range(2):
        p+=r.choice(num)
    for i in range(2):
        p+=r.choice(sp_ch)
    pas=[i for i in p]
    r.shuffle(pas)
    password=""
    for ch in pas:
        password+=ch
    print(password)