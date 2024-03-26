class User:

    def __init__(self, name, email, phoneNum, numPeople):
        
        self._name = name
        self._email = email
        self._phoneNum = phoneNum
        self._numPeople = numPeople

    def getName(self):
        return self._name
    def setName(self, name):
        self._name = name
    def getEmail(self):
        return self._email
    def setEmail(self, email):
        self._email = email
    def getPhoneNum(self):
        return self._phoneNum
    def setPhoneNum(self, phoneNum):
        self._phoneNum = phoneNum
    def setNumPeople(self, numPeople):
        self._numPeople = numPeople
    def getNumPeople(self):
        return self._numPeople
