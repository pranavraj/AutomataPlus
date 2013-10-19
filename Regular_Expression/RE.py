"""created by Pranav Raj aka PRaj """

#An alternative for re python module

class RE ():

	def __init__( self , String ):

		self.String = String
		self.StringLength = len(String)	
		self.SPattern = "("
		self.FPattern = ")"
		self.OR = "|"
		self.KLEENSTAR = "*"
		self.KLEENCROSS = "+"
		self.Alphabets = map(chr, range(97, 123)) + map(chr, range(65, 91))

	def FindPattern( self ):

	    Stack = []
	    Reps = []
	    
	    for Index in range(self.StringLength) :

	        if self.String[Index] == self.SPattern : Stack.append(Index)

	        elif self.String[Index] == self.FPattern :

	            StartIndex = Stack.pop()
	            FinalIndex = Index + 1
	            SubString = self.String[StartIndex:FinalIndex]
	            Reps.append(SubString)
	    
	    return Reps

	def FindUnaryOperator( self, Operator = "*" ):

		Words = []

		for Index in range(self.StringLength-1):

			if self.String[Index + 1] == Operator and self.String[Index] in self.Alphabets: 
				Words.append(self.String[Index:Index+2])

		Stack = []

		for Index in range(self.StringLength):

			if self.String[Index] == self.SPattern : Stack.append(Index)

			elif self.String[Index] == self.FPattern:
				
				StartIndex = Stack.pop()
				FinalIndex = Index + 1

				if FinalIndex < self.StringLength and self.String[FinalIndex] == Operator :
					
					SubString = self.String[StartIndex:FinalIndex + 1]
					Words.append(SubString)

		return Words

	def FindSuccesiveClosingWord( self , String , Invert = False):

		Stack = []

		if Invert : self.SPattern,self.FPattern = self.FPattern,self.SPattern
		
		Length = len(String)

		for Index in range(Length):

			if String[Index] == self.SPattern : Stack.append(Index)

			elif String[Index] == self.FPattern :
				
				FinalIndex = Index + 1
				SubString = String[0:FinalIndex]
				Stack.pop()

				if Stack == []:	break

		if Invert : self.SPattern,self.FPattern = self.FPattern,self.SPattern

		return SubString

	def FindBinaryOperator( self , Operator):
		
		Occurances = [index for index in range(self.StringLength) if self.String[index] == Operator]
		Words = []

		for occurance in Occurances:

			occur = Operator

			#check right
			if self.String[occurance + 1] !=  self.SPattern: occur += self.String[occurance + 1]
			else: occur += self.FindSuccesiveClosingWord(self.String[occurance + 1:])

			#check left
			LString = self.String[occurance - 1 :  : -1]
	
			if LString[0] !=  self.FPattern: occur = LString[0] + occur
			else: occur = self.FindSuccesiveClosingWord(LString,Invert=True)[::-1] + occur

			Words.append(occur)

		return Words

	def Star( self ):
		return self.FindUnaryOperator(self.KLEENSTAR)

	def Plus( self ):
		return self.FindUnaryOperator(self.KLEENCROSS)

	def Or( self ):
		return self.FindBinaryOperator(self.OR)

if __name__ == "__main__":

	re = RE("as|de|(f(g|(fd)*))")
	print re.Star()
	print re.Plus()
	print re.Or()