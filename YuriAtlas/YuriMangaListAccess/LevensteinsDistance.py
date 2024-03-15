def distance(str1, str2):
    if str1 == str2:
        return 0

    row_count = len(str1) + 1
    col_count = len(str2) + 1

    matrix = [[row + col if row == 0 or col == 0 else None for col in range(col_count)] for row in range(row_count)]

    for i in range(row_count):
        matrix[i][0] = i

    for j in range(1, col_count):
        matrix[0][j] = j

    for i in range(1, row_count):
        for j in range(1, col_count):

            insertion = matrix[i - 1][j] + 1
            deletion = matrix[i][j - 1] + 1

            substitution_cost = matrix[i - 1][j - 1]

            if str1[i - 1] != str2[j - 1]:
                substitution_cost += 1

            min_cost = min(insertion, deletion, substitution_cost)
            matrix[i][j] = min_cost

    return matrix[row_count - 1][col_count - 1]
