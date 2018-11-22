import app.configs.constant as const
from app.libs.check_even_odd import CheckEvenOdd
from app.libs.loop_end import LoopEnd
from app.libs.math_compute import MathCompute


class LoopStart():
    #start loop with n: number loop and array: array need handle
    def loopStart(n,array):
        dict = CheckEvenOdd.checkEvenOdd(array)
        for array in dict['even']:
            index = (dict['even'].index(array))
            for i in range(n):
                array=MathCompute.mathComputeEven(array)
                if LoopEnd.loopEndEven(array):
                    dict['even'][index]=array
                    break
            dict['even'][index]=array
        for array in dict['odd']:
            index = (dict['odd'].index(array))
            for i in range(n):
                array=array=MathCompute.mathComputeOdd(array)
                if LoopEnd.loopEndOdd(array):
                    dict['odd'][index]=array
                    break
            dict['odd'][index]=array
        return dict
