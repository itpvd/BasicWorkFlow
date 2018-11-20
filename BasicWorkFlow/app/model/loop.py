
from app.model.check import Check
class Loop(Check):
    def __init__(self):
        pass
    def loop(n,dict):
        for array in dict['even']:
            index = (dict['even'].index(array))
            for i in range(n):
                array=array+2
                if array >100:
                    dict['even'][index]=array
                    break
            dict['even'][index]=array
        for array in dict['odd']:
            index = (dict['odd'].index(array))
            for i in range(n):
                array=array+2
                if array >100:
                    dict['odd'][index]=array
                    break
            dict['odd'][index]=array
        return dict
    def abc():
        array=[2,3,4,5,6,7,8]
        return self.check(array)
