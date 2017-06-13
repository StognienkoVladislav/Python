from PIL import Image
SIZE = 10
COUNT_OF_EXAMPLES = 3
vector = []
flag = True

def signumFunc(a):
    if a >= 0:
        return 1
    return -1

def getValueOfPixels(imageName):
    vectorOfPixels = []
    im = Image.open(imageName)

    for i in range(SIZE):
        for j in range(SIZE):
            if im.getpixel((j, i)) == (255, 255, 255, 255):
                vectorOfPixels.append(-1)
            else:
                vectorOfPixels.append(1)
    return vectorOfPixels

for count in range(COUNT_OF_EXAMPLES):
    vector.append(getValueOfPixels("ex" + str(count + 1) + ".png"))

nMatrix = []
for i in range(SIZE ** 2):
    nMatrix.append([])
    for j in range(SIZE ** 2):
        nMatrix[i].append(0)

for count in range(COUNT_OF_EXAMPLES):
    for i in range(SIZE ** 2):
        for j in range(SIZE ** 2):
            nMatrix[i][j] += vector[count][i] * vector[count][j]

#--------------------------------------------------------------------------#

test_vector = []
test_vector = getValueOfPixels("test.png")

while flag:
    flag = False
    result_vector = []
    for i in range(SIZE ** 2):
        result_number = 0
        for j in range(SIZE ** 2):
            result_number += nMatrix[i][j] * test_vector[j]
        result_vector.append(result_number)

    for i in range(SIZE ** 2):
        result_vector[i] = signumFunc(result_vector[i])

    for i in range(SIZE ** 2):
        if test_vector[i] != result_vector[i]:
            flag = True
        test_vector[i] = result_vector[i]


mas_of_sums = []
for i in range(COUNT_OF_EXAMPLES):
    mas_of_sums.append(0)
    for j in range(SIZE ** 2):
        if vector[i][j] == test_vector[j]:
            mas_of_sums[i] += 1
            continue

max_sum = 0
page_index = -1
for i in range(COUNT_OF_EXAMPLES):
   if mas_of_sums[i] >= max_sum:
       page_index = i + 1
       max_sum = mas_of_sums[i]

print(mas_of_sums)
print("this picture like a picture number", page_index)
print("INDEX: ", page_index)
im = Image.open("ex" + str(page_index) + ".png").show()