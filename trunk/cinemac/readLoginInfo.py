
class LoginInfo:
	dbname = '';
	user = '';
	passwd = '';
	
	def readFile(fileName):	
		f = open(fileName, 'r')
		dbname = f.readLine()
		user = f.readLine()
		passwd = f.readLine()
		f.close();
		
		dbname.replace('\n', '')
		user.replace('\n', '')
		passwd.replace('\n', '')
