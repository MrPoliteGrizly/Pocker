f = open("file.txt")
l = f.read().split("\n")

pri_1 = dict(A=14, K=13, Q=12, J=11, T=10)
pri_2 = {a: a for a in range(2, 10)}
pri_3 = dict(S=1, C=2, H=3, D=4)
pri_1_ = dict(A="A", K="K", Q="Q", J="J", T="T")
pri_3_ = dict(S="S", C="C", H="H", D="D")

s_1 = 0
s_2 = 0

print(pri_1)  # Check
print(pri_2)
print(pri_3)
print("\n")


for line in l: # Стриты и пары
    line = line.split()
    a = line[:5]
    b = line[5:]

        
    p = 0 # 1
    while p < len(a):
        if a[p][0] == pri_1_["A"]:
            s_1 += pri_1["A"]
        elif b[p][0] == pri_1_["K"]:
            s_1 += pri_1["K"]
        elif b[p][0] == pri_1_["Q"]:
            s_1 += pri_1["Q"]
        elif b[p][0] == pri_1_["J"]:
            s_1 += pri_1["J"]
        elif b[p][0] == pri_1_["T"]:
            s_1 += pri_1["T"]
        elif b[p][0] == pri_2[9]:
            s_1 += pri_2[9]
        elif b[p][0] == pri_2[8]:
            s_1 += pri_2[8]
        elif b[p][0] == pri_2[7]:
            s_1 += pri_2[7]
        elif b[p][0] == pri_2[6]:
            s_1 += pri_2[6]
        elif b[p][0] == pri_2[5]:
            s_1 += pri_2[5]
        elif b[p][0] == pri_2[4]:
            s_1 += pri_2[4]
        elif b[p][0] == pri_2[3]:
            s_1 += pri_2[3]
        elif b[p][0] == pri_2[2]:
            s_1 += pri_2[2]
        p += 1
    p = 0
    while p < len(b):
        if b[p][0] == pri_1_["A"]:
            s_2 += pri_1["A"]
        elif b[p][0] == pri_1_["K"]:
            s_2 += pri_1["K"]
        elif b[p][0] == pri_1_["Q"]:
            s_2 += pri_1["Q"]
        elif b[p][0] == pri_1_["J"]:
            s_2 += pri_1["J"]
        elif b[p][0] == pri_1_["T"]:
            s_2 += pri_1["T"]
        elif b[p][0] == pri_2[9]:
            s_2 += pri_2[9]
        elif b[p][0] == pri_2[8]:
            s_2 += pri_2[8]
        elif b[p][0] == pri_2[7]:
            s_2 += pri_2[7]
        elif b[p][0] == pri_2[6]:
            s_2 += pri_2[6]
        elif b[p][0] == pri_2[5]:
            s_2 += pri_2[5]
        elif b[p][0] == pri_2[4]:
            s_2 += pri_2[4]
        elif b[p][0] == pri_2[3]:
            s_2 += pri_2[3]
        elif b[p][0] == pri_2[2]:
            s_2 += pri_2[2]
        p += 1

print(s_1)
print(s_2)




