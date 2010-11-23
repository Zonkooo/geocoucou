
class LoginInfo:
	dbname = '';
	user = '';
	passwd = '';
	
	def __init__(self, fileName):	
		print 'reading file \'%s\'' %(fileName)
		with open(fileName, 'r') as f:
			dbname = f.readline().rstrip("\n")
			user = f.readline().rstrip("\n")
			passwd = f.readline().rstrip("\n")
			
