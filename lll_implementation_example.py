def LLL(B, delta):
    Q = gram_schmidt(B)

    def mu(i,j):
        v = B[i]
        u = Q[j]
        return (v*u) / (u*u)

    n, k = B.nrows(), 1

    while k < n:
        # Length reduction step
        for j in reversed(range(k)):
            if abs(mu(k,j)) > .5:
                B[k] = B[k] - round(mu(k,j))*B[j]
                Q = gram_schmidt(B)
        
        # Lovász-condition
        if Q[k]*Q[k] >= (delta - mu(k,k-1)**2)*(Q[k-1]*Q[k-1]):
            k = k + 1
        else:
            B[k], B[k-1] = B[k-1], B[k]
            Q = gram_schmidt(B)
            k = max(k-1, 1)
    
    return B