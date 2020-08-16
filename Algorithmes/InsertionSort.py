import random, time
import matplotlib.pyplot as plt

def sort(values):
    sl = list()
    for i in values:
        index = 0
        # we reached the end, insert here
        while index < len(sl):
            if sl[index] < i:
                index += 1
            else:
                sl.insert(values.pop(index))
                #plot(sl)
                #time.sleep(2)
                break
    return sl

def plot(array):
    width = 3 / len(array)
    labels = [str(i) for i in array]

    plt.bar(labels, array, width)

    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('List Sorting')

    plt.show()
      
l = list(range(15))
random.shuffle(l)
print(sort(l))
