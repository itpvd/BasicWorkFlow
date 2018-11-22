import app.configs.constant as const


class LoopEnd():
    #condition loop end of number even
    def loopEndEven(i):
        return i> const.LOOP_END_EVEN

    #condition loop end of number odd
    def loopEndOdd(i):
        return i < const.LOOP_END_ODD

