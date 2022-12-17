
def transpose(m):
    return list(map(list, zip(*m)))    

def minor(m, i, j):
    return [r[:j] + r[j+1:] for r in (m[:i]+ m[i+1:])]

def det(m):
    if len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]

    d = 0
    for x in range(0, len(m)):
        d = d + ((-1) ** x) * m[0][x] * det(minor(m, 0, x))
    return d

def inv(m):
    d = det(m)
    if len(m) == 2:
        return [[m[1][1]/d, -1 * m[0][1]/d], [-1 * m[1][0]/d, m[0][0]/d]]

    cf = []
    for r in range(0, len(m)):
        cfr = []
        for c in range(0, len(m)):
            mi = minor(m, r, c)
            cfr.append(((-1)**(r + c)) * det(mi))
        cf.append(cfr)
    cf = transpose(cf)

    for r in range(0, len(m)):
        for c in range(0, len(m)):
            cf[r][c] = cf[r][c]/d
    return cf

def matmul(a,b):
    zip_b = list(zip(*b))
    return [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b)) 
             for col_b in zip_b] for row_a in a]
