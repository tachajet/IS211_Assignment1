def listDivide(numbers,divide=2):
	"""function to determine how many numbers are divisable in list of numbers
Args:
	numbers (list): a list of numbers
	divide (int): a number by which the list of numbers are to be divided, default is 2
Returns:
	divisables: number of numbers in numbers that can be divided by divide without a remainder
"""
	divisables=0
	for n in numbers:
		if (n%divide)==0:
			divisables+=1			
	return divisables
class ListDivideException(Exception):
	"""defining a custom error
"""
	pass 

def testListDivide():
	"""function to test listDivide function and invoke custom error if it fails
"""
	if (listDivide([1,2,3,4,5])==2 and
	listDivide([2,4,6,8,10])==5 and
	listDivide([30, 54, 63,98,100],10)==2 and
	listDivide([])==0 and
	listDivide([1,2,3,4,5], 1)==5):
		pass
	else:
		raise ListDivideException("Something got messed up!")
testListDivide()	


print(listDivide([1,6,7,8,10,3]))
