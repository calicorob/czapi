
__all__ = []


class DifferentScoreLengthError(Exception):
    def __init__(self,score_1_len:int,score_2_len)->None:
        self.score_1_len = score_1_len
        self.score_2_len = score_2_len

        self.message = "Input scores have length %s and length %s and do not match."%(self.score_1_len,self.score_2_len)
        super().__init__(self.message)

class InvalidScoreError(Exception):
    def __init__(self,idx:int,val_1:int,val_2:int)->None:

        self.idx = idx
        self.val_1 = val_1
        self.val_2 = val_2
        self.message = "Input end scores of %s and %s for end %s are both greater than 0 and the end score is not valid."%(self.val_1,self.val_2,self.idx)
        super().__init__(self.message)

class InvalidEventError(Exception):
    def __init__(self,cz_event_id:int)->None:
        self.cz_event_id = cz_event_id

        self.message = "Inputted Event ID of %s is not valid, please check you have the right one."%self.cz_event_id
        super().__init__(self.message)