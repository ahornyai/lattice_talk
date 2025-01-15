def Babai_closest_vector(M, target):
    G = M.gram_schmidt()[0]
    diff = target
    
    for i in reversed(range(M.nrows())):
        c = (diff * G[i]) / (G[i] * G[i])
        diff -= M[i] * round(c)
    
    return target - diff