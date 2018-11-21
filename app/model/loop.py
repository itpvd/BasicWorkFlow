class Loop():
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
