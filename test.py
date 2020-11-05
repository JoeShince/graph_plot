'''

python script to plot the pattern in the list from the list of given integers
'''

import matplotlib.pyplot as plt

test_list = [3, 1, 2, 3, 6, 2, 3, 6, 2, 3, 6, 3, 2, 3, 6, 2, 3, 4, 3, 2, 5, 4, 2, 1, 2, 1, 2, 3, 1, 2, 6, 2, 3, 6, 2, 3,
             6, 3, 2, 3, 1, 5, 3, 2, 1, 2, 4, 2, 1, 8, 1, 2]
test_list_length = len(test_list)

result_list = []
for i in range(test_list_length):
    if i == 0:
        result_list.append(test_list[i])
    else:
        if i % 2 == 0:
            result_list.append(result_list[i - 1] + test_list[i])
        else:
            result_list.append(result_list[i - 1] - test_list[i])
print(result_list)
plt.plot(result_list)
plt.show()
