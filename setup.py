import os, subprocess, fileinput

CURRENT_DIR = os.getcwd()

def log(message):
	print '===> ' + message + '...'

def ask(message):
	response = raw_input(message + ' (y/n) ')
	if response == 'y':
		return True
	return False

def find_replace_all(find, replace, file_paths):
	# with fileinput.FileInput(file_paths) as f: <--Python 3.x
	for line in fileinput.FileInput(file_paths, inplace=1):
		line = line.replace(find, replace)
		print line,

def append_file(file_path, lines):
	with open(file_path, 'a') as f:
		for line in lines:
			f.write(line+'\n')

def rename_project(project_name):
	settings = os.path.join(CURRENT_DIR, 'project_name', 'project_name', 'settings.py')
	wsgi = os.path.join(CURRENT_DIR, 'project_name', 'project_name', 'wsgi.py')
	manage = os.path.join(CURRENT_DIR, 'project_name', 'manage.py')
	procfile = os.path.join(CURRENT_DIR, 'Procfile')

	log('Changing "project_name" to %s in .py files' % project_name)
	file_paths = [settings, wsgi, manage, procfile]
	find_replace_all('project_name', project_name, file_paths)

	log('Renaming "project_name" folders to %s' % project_name)
	os.rename(CURRENT_DIR + '/project_name/project_name', CURRENT_DIR + '/project_name/%s' % project_name)
	os.rename(CURRENT_DIR + '/project_name', CURRENT_DIR + '/%s' % project_name)

def create_local_database(project_name):
	database_name = raw_input('What should your database name be for local testing? ')
	log('Creating postgres database %s using cmd "createdb"' % database_name)
	subprocess.call('createdb ' + database_name, shell=True)
	file_paths = [os.path.join(CURRENT_DIR, project_name, project_name, 'settings.py')]
	find_replace_all('POSTGRES_DATABASE_NAME', database_name, file_paths)
	log('Settings postgres database name to %s in settings.py' % database_name)

	user_name = raw_input('What is your current computer username (i.e. Mark)? ')
	log('Settings postgres username to ' + user_name)
	find_replace_all('POSTGRES_USER_NAME', user_name, file_paths)

def create_herokuapp():
	#builds heroku cedar app - https://devcenter.heroku.com/articles/cedar
	herokuapp_name = ''
	while len(herokuapp_name) <= 0:
		print '\nWhat would you like to name your heroku app? This will create a cedar stack (heroku\'s default and recommended stack) and make sure your app name is unique!'
		herokuapp_name = raw_input('==> ')
		if len(herokuapp_name) == 0:
			print '\nNot a valid name!'

	log('Creating heroku app')
	subprocess.call('heroku create --stack cedar ' + herokuapp_name, shell=True)

def s3_setup(project_name):
	AWS_ACCESS_KEY_ID = raw_input('AWS ACCESS KEY ID: ')
	AWS_SECRET_ACCESS_KEY = raw_input('AWS SECRET ACCESS KEY: ')
	S3_BUCKET_NAME = raw_input('S3 BUCKET NAME: ')
	log('Setting Heroku Config')
	subprocess.call(
		'heroku config:set AWS_ACCESS_KEY_ID=%s AWS_SECRET_ACCESS_KEY=%s S3_BUCKET_NAME=%s' 
		% (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, S3_BUCKET_NAME), shell=True
	)
	log('Updating virtualenv')
	lines = [
		'export AWS_ACCESS_KEY_ID=%s' % AWS_ACCESS_KEY_ID, 
		'export AWS_SECRET_ACCESS_KEY=%s' % AWS_SECRET_ACCESS_KEY, 
		'export S3_BUCKET_NAME=%s' % S3_BUCKET_NAME,
	]
	append_file(os.path.join(CURRENT_DIR, '.env', 'bin', 'activate'), lines)
	log('Updating settings.py')
	find_replace_all('USING_S3 = False', 'USING_S3 = True', [os.path.join(CURRENT_DIR, project_name, project_name, 'settings.py')])

def main():
	print '\nMake sure you enter "appropriate" responses to each question, DO NOT enter shell commands. Anything that happens is not my fault.\n'

	project_name = raw_input('What would you like to name your project? ')
	rename_project(project_name)

	if ask('Would you like to create a local postgres database?'):
		create_local_database(project_name)

	if ask('Would you like to create your heroku app now?'):
		create_herokuapp()

		if ask('Would you like to setup S3 for your heroku app?'):
			s3_setup(project_name)

	else:
		log('Skipping heroku app creation')

main()