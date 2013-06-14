
class JSMrClone:
    def __init__(self):
        self.currentKey = None
        self.currentLine = None
        self.currentValue = None
        self.reducerData = None
        self.separator = '|'

    def Emit(self, *args):
        if len(args) == 1:
            print args[0]
        elif len(args) == 2:
            print '%s%s%s' % (args[0], self.separator, args[1])
        else:
            print args

    def Map(self, data, mapper):
        for line in data:
            mapper(self, line)

    def Reduce(self, data, reducer):
        self.reducerData = data.__iter__()
        while self.NextKey():
            reducer(self, self.currentKey)

    def NextKey(self):
        if self.currentLine is None:
            try:
                self.currentLine = self.reducerData.next()
            except StopIteration:
                return False
        tmp = self.currentLine.split(self.separator)
        self.currentKey = tmp[0]
        self.currentValue = tmp[1]
        return True

    def HaveMoreValues(self):
        if self.currentLine is None:
            try:
                self.currentLine = self.reducerData.next()
            except StopIteration:
                return False

        tmp = self.currentLine.split(self.separator)
        thisKey = tmp[0]
        thisValue = tmp[1]
        if (thisKey != self.currentKey):
            return False
        self.currentValue = thisValue
        self.currentLine = None
        return True

    def GetNextValue(self):
        return self.currentValue
        

