import json
from typing import DefaultDict
import sys

# shitf alt f to format json output


def main(file1, file2):
    method1_dependencies = extractDependencies(file1)
    with open(file1.split(' ')[0] + '.json', 'w') as file:
        file.write(json.dumps(method1_dependencies))

    method2_dependencies = extractDependencies(file2)
    with open(file2.split(' ')[0] + '.json', 'w') as file:
        file.write(json.dumps(method2_dependencies))

    common = compareDependencies(method2_dependencies, method1_dependencies)

    print('Comparing method 1 and method 2 dependencies:')
    print(' Total number of common dependencies: {:d}'.format(len(common)))
    print(' Total number of method 1 dependencies: {:d}'.format(
        totalDependencies(method1_dependencies)))
    print(' Total number of method 2 dependencies: {:d}'.format(
        totalDependencies(method2_dependencies)))
    print(' Percentage of method 1 dependencies found in common dependencies: {:.2%}'.format(
        len(common)/totalDependencies(method1_dependencies)))
    print(' Percentage of method 2 dependencies found in common dependencies: {:.2%}'.format(
        len(common)/totalDependencies(method2_dependencies)))


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


def compareDependencies(dict1, dict2):
    compare = []

    for dependent in dict1.keys():
        for dependency in dict1[dependent]:
            if dependency in dict2[dependent]:
                compare.append(dependent + ":" + dependency)

    return compare


def totalDependencies(dependencies):
    count = 0

    for dependent in dependencies.keys():
        count += len(dependencies[dependent])

    return count


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
