from typing import DefaultDict
import sys


def main(file1, file2, file3):
    method1_dependencies = extractDependencies(file1)

    method2_dependencies = extractDependencies(file2)

    method3_dependencies = extractDependencies(file3)

    common = compareDependencies(
        method1_dependencies, method2_dependencies, method3_dependencies)

    print('Comparing dependency extraction techniques:')
    print(' Total number of common dependencies: {:d}'.format(len(common)))
    print(' Percentage of method 1 dependencies in the total common dependencies: {:.2%}'.format(
        len(common)/totalDependencies(method1_dependencies)))
    print(' Percentage of method 2 dependencies in the total common dependencies: {:.2%}'.format(
        len(common)/totalDependencies(method2_dependencies)))
    print(' Percentage of method 3 dependencies in the total common dependencies: {:.2%}'.format(
        len(common)/totalDependencies(method3_dependencies)))


def extractDependencies(file):
    my_dict = DefaultDict(list)
    f = open(file, 'r')
    lines = f.read().splitlines()

    for line in lines:
        text = line.split(' ')

        if text[0] == 'cLinks':

            if text[1] not in my_dict.keys():
                my_dict[text[1]] = [text[2]]
            else:
                my_dict[text[1]].append(text[2])

    return my_dict


def compareDependencies(dict1, dict2, dict3):
    compare = []

    for dependent in dict1.keys():
        for dependency in dict1[dependent]:
            if dependency in dict2[dependent] and dependency in dict3[dependent]:
                compare.append(dependent + ":" + dependency)

    return compare


def totalDependencies(dependencies):
    count = 0

    for dependent in dependencies.keys():
        count += len(dependencies[dependent])

    return count


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
