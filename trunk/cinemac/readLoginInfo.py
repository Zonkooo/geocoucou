
class LoginInfo:
	dbname = '';
	user = '';
	passwd = '';
	
	def __init__(self, fileName):	
		f = open(fileName, 'r')
		dbname = f.readline()
		user = f.readline()
		passwd = f.readline()
		f.close();
		
		dbname.replace('\n', '')
		user.replace('\n', '')
		passwd.replace('\n', '')
