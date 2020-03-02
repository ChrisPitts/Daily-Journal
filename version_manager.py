CURRENT_VERSION = 0

#   Integer values represent each of the sections
#   0   Version
#   1   Daily Summary
#   2   Emotional Summary
#   3   Personal Growth Summary

SECTIONS = ["Daily Summary", "Emotional Summary", "Personal Growth Summary"]

VERSIONS = [
    [0, 1, 2, 3]    # Version 0
]


def read_file(path):
    file_array = open(path, 'r').read().split('\0')
    if int(file_array[0]) == CURRENT_VERSION:
        return file_array

    return update_file(path, file_array)


def update_file(path, array):
    prev_version_array = VERSIONS[int(array[0])]
    current_version_array = VERSIONS[int(CURRENT_VERSION)]
    new_file_array = [''] * len(VERSIONS[int(CURRENT_VERSION)])
    new_file_array[0] = CURRENT_VERSION

    for i in range(1, len(prev_version_array)):
        if prev_version_array[i] in current_version_array:
            new_file_array[current_version_array.index(prev_version_array[i])] = array[i]
    save_file(path, new_file_array)
    return new_file_array


def save_file(path, array):
    file = open(path, 'w')
    for i in array:
        file.write("%s%s" % (i, '\0'))
    file.close()
