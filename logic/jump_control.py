# generator of available labels for jumps

import copy

label_counter = 1

class label_controller():
    labels = 1

    def __init__(self):
        self.labels = copy.deepcopy(label_counter)

    def reserve(self):
        current_label = "label_" + str(self.labels)
        self.labels += 1
        return current_label

# test
# controller = label_controller()

# a = controller.reserve()
# b = controller.reserve()

# print(a)
# print (b)

