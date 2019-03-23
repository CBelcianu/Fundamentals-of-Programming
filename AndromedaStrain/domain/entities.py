class person:
    def __init__(self,ID,imm,status):
        self.__ID=ID
        self.__imm=imm
        self.__status=status
    def getID(self):
        return self.__ID
    def getImm(self):
        return self.__imm
    def getStatus(self):
        return self.__status
    def __str__(self):
        s=''
        s+=str(self.__ID)
        s+=' '
        s+=str(self.__imm)
        s+=' '
        s+=str(self.__status)
        return s