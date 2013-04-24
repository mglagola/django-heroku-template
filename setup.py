import os, subprocess, fileinput

CURRENT_DIR = os.getcwd()

def log(message):
	print '===> ' + message + '...'

def find_replace_all(find, replace, file_paths):
	# with fileinput.FileInput(file_paths) as f: <--Python 3.x
	for line in fileinput.FileInput(file_paths, inplace=1):
		line = line.replace(find, replace)
		print line,

def main():
	print '\nMake sure you enter "appropriate" responses to each question, DO NOT enter shell commands. Anything that happens is not my fault.\n'
	project_name = raw_input('What would you like to name your project? ')

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

	database_name = raw_input('What should your database name be? ')
	log('Creating postgres database %s using cmd "createdb"' % database_name)
	subprocess.call('createdb ' + database_name, shell=True)
	file_paths = [os.path.join(CURRENT_DIR, project_name, project_name, 'settings.py')]
	find_replace_all('POSTGRES_DATABASE_NAME', database_name, file_paths)
	log('Settings postgres database name to %s in settings.py' % database_name)

	user_name = raw_input('What is your current computer username (i.e. Mark)? ')
	log('Settings postgres username to ' + user_name)
	find_replace_all('POSTGRES_USER_NAME', user_name, file_paths)

main()