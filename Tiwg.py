import array as arr

class twig:

    def check(listvalue, chunks):
        if len(listvalue) == 0:
            return[]
        elif len(listvalue) > 0 and isinstance(chunks, int) and chunks > 0:
            return True
        return False


    def groupArrayElements(listValues, count):
        if twig.check(listValues ,count):
            numElemens = round(len(listValues) / count)
            return [listValues[i:i + 1 * numElemens] for i in range(0, len(listValues), numElemens)]
        else:
            return None

    def groupArrayElementsAlternative(data,chunk):
        if twig.check(data, chunk):
            numElemens = round(len(data) / chunk)
            list=[]
            while 0 < len(data):
                if len(data) < numElemens:
                    a = data[0:numElemens]
                    del data[0:numElemens]
                    list.append(a)
                    break
                else:
                    a = data[0:numElemens]
                    del data[0:numElemens]
                    list.append(a)
            return list


if __name__ == '__main__':
    tiwg=twig()
    print(twig.check([1, 2, 3, 4, 5], 3))
    print(twig.groupArrayElementsAlternative([1, 2, 3, 4, 5], 3))






