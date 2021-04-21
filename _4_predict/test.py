def LevenshteinInstance(SourceString, TargetString):
    m, n = len(SourceString) + 1, len(TargetString) + 1
    matrix = [[0] * n for i in range(m)]
    matrix[0][0] = 0
    for i in range(1, m):
        matrix[i][0] = matrix[i - 1][0] + 1
    for j in range(1, n):
        matrix[0][j] = matrix[0][j - 1] + 1
    for i in range(1, m):
        for j in range(1, n):
            if SourceString[i - 1] == TargetString[j - 1]:
                cost = 0
            else:
                cost = 1
            matrix[i][j] = min(matrix[i - 1][j] + 1, matrix[i][j - 1] + 1, matrix[i - 1][j - 1] + cost)
    return matrix[m - 1][n - 1]


print(LevenshteinInstance('a', 'b'))
