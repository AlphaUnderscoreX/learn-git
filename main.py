# This is the main script which invokes other script

if __name__ == '__main__':
	print 'On the master'
	print 'Advancing master branch'

	has_branch_created()

def has_branch_created():
	print "Branch 'first' has been created"
