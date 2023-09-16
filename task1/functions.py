
def prod_non_zero_diag(x):
    ans = 1
    for i in range(len(x)):
        if len(x[i]) == i:
            break
        if x[i][i] != 0:
            ans *= x[i][i]
    return ans


def are_multisets_equal(x, y):
    x.sort()
    y.sort()
    return x.all() == y.all()

def max_after_zero(x):
    ans = 0
    for i in range(1, len(x)):
        if x[i - 1] == 0:
            ans = max(ans, x[i])
        
    return ans


def convert_image(img, coefs):
    for i in range(len(img)):
        for j in range(len(img[i])):
            img[i][j] = float(img[i][j][0]) * coefs[0] + float(img[i][j][1]) * coefs[1] + float(img[i][j][2]) * coefs[2]
    return img


def run_length_encoding(x):
    num = [x[0]]
    cnt = [1]
    for i in range(1, len(x)):
        if x[i] == x[i - 1]:
            cnt[-1] += 1
        else: 
            num.append(x[i])
            cnt.append(1)
    return [num, cnt]


def pairwise_distance(x, y):
    ans = []
    for i in x:
        ans.append([])
        for j in y:
            ans[-1].append(((i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2) ** 0.5)
    return ans
