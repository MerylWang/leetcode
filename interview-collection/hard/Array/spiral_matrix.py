
def spiralOrder(matrix):
    output = []

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    min_r = 0
    max_r = num_rows
    min_c = 0
    max_c = num_cols

    r = min_r
    c = min_c

    r_inc = 1 # 1, -1
    c_inc = 1

    current_dir = "hori" # hori, vert


    next_elt = matrix[r][c]

    # TODO: check pos instead of value
    while next_elt not in output:
        current_elt = next_elt
        output.append(current_elt)
        
        # find direction of next element
        if current_dir == "hori":
            next_c = c + c_inc
            if next_c < min_c or next_c >= max_c:
                current_dir = "vert"
                c_inc = -1 if c_inc == 1 else 1
                if next_c < min_c: min_c += 1
                if next_c >= max_c: max_c -= 1
        else:
            next_r = r + r_inc
            if next_r < min_r or next_r >= max_r:
                current_dir = 'hori'
                r_inc = -1 if r_inc == 1 else 1
                if next_r < min_r: min_r += 1
                if next_r >= max_r : max_r -= 1

        # get next_elt
        if current_dir == "hori":
            c += c_inc
        else:
            r += r_inc





        next_elt = matrix[r][c]

    return output


# input = [[1,2,3],[4,5,6],[7,8,9]]
# result = spiralOrder(input)
# expected = [1,2,3,6,9,8,7,4,5]

input = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
result = spiralOrder(input)
expected = [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]

print(result == expected)
print("result: ", result)
print("expected: ", expected)








        # if current_dir == "hori":
        #     next_c = c + c_inc
        #     if next_c >= min_c and next_c < max_c:
        #         c = next_c
        #     else:
        #         current_dir = 'vert'
        #         c_inc = -1 if c_inc == 1 else 1
        #
        #         r += r_inc
        #
        #         if next_c < min_c: min_c += 1
        #         if next_c >= max_c: max_c -= 1
        #
        # else:
        #     next_r = r + r_inc
        #     if next_r >= min_r and next_r < max_r:
        #         r = next_r
        #     else:
        #         current_dir = 'hori'
        #         r_inc = -1 if r_inc == 1 else 1
        #
        #         c += c_inc
        #
        #         if next_r < min_r: min_r += 1
        #         if next_r >= max_r : max_r -= 1
