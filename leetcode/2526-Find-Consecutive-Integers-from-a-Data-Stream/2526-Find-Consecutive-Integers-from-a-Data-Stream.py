class DataStream:

    def __init__(self, value: int, k: int):
        self.streak=0
        self.value= value
        self.size=k

    def consec(self, num: int) -> bool:
        if num== self.value:
            self.streak+=1
        else:
            self.streak=0
        return self.streak>= self.size