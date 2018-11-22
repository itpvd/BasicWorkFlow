class CheckEvenOdd():
    #function check number even and number odd from array
    def checkEvenOdd(arrays):
        dict={}
        dict['even']=[]
        dict['odd']=[]
        for array in arrays:
            if array%2==0:
                dict['even'].append(array)
            else:
                dict['odd'].append(array)
        return dict
