import math
class twig:

    def check(listvalue, chunks):
        if len(listvalue) == 0:
            return[]
        elif len(listvalue) > 0 and isinstance(chunks, int) and chunks > 0:
            return True
        return False


    def groupArrayElements(listValues, count):
        if twig.check(listValues ,count):
            numElemens = math.ceil(len(listValues) / count)
            list = [listValues[i:i + 1 * numElemens] for i in range(0, len(listValues), numElemens)]
            # case when the num of list is < of element
            if len(list) < count:
                for i in range(0, count-len(list)):
                    list.append([])
            return list
        else:
            return None


if __name__ == '__main__':
    tiwg=twig()
    print(twig.check([1, 2, 3, 4, 5], 3))
    print(twig.groupArrayElements([1, 2, 3, 4,5,6,7,8,9,10], 6))
    print(twig.groupArrayElements([1, 2, 3, 4,5,6,7,8,9,10,11,12,13], 6))
    print(twig.groupArrayElements([1,2,3,4,5,6,7], 6))







