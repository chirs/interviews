


def partition(lst, pivot):
    lte = []
    gt = []
    for e in lst:
        if e <= pivot:
            lte.append(e)
        else:
            gt.append(e)

    lte.extend(gt)
    return lte


