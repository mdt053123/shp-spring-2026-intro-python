def matmul(M1, M2):
    """
    Returns product matrix of M1, M2
    provided that product is well-defined
    """
    
    if not M1 and not M2: return None
    
    if len(M1[0]) != len(M2): return None
    
    result = [[0 for _ in range(len(M2[0]))] for _ in range(len(M1))]
    
    for i in range(len(M1)):
        for j in range(len(M2[0])):
            for k in range(len(M2)):
                result[i][j] += M1[i][k] * M2[k][j]
                
    return result

M1 = [[1, 2],
      [3, 4]]

M2 = [[5, 6],
      [7, 8]]

print(matmul(M1, M2))