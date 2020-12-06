import os
import sys

def help():
	print("HELP")

def goRename(walk_dir,renameExt,renameExtFilter,contains):
	print('walk_dir = ' + walk_dir)
	print('renameExt = ' + renameExt)
	print('renameExtFilter = ' + renameExtFilter)
	print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))

	for root, subdirs, files in os.walk(walk_dir):

		for filename in files:
			file_path = os.path.join(root, filename)
			base=os.path.basename(file_path)
			thefile=os.path.splitext(base)[0]
			if renameExtFilter != '':			
				if contains:
					if os.path.splitext(base)[1].count(renameExtFilter)>-1:
						os.rename(file_path, os.path.join(root, thefile+'.'+renameExt))
				else:

					if os.path.splitext(base)[1]=='.'+renameExtFilter:
						os.rename(file_path, os.path.join(root, thefile+'.'+renameExt))
			else:
					os.rename(file_path, os.path.join(root, thefile+'.'+renameExt))


if __name__ == "__main__":

	if len(sys.argv) <2:
		help()
		exit()


	walk_dir = sys.argv[1]
	renameExt= sys.argv[2]
	renameExtFilter= ''
	contains=0

	if len(sys.argv) >3:
		renameExtFilter=sys.argv[3]

	if len(sys.argv) >4:
		contains=sys.argv[4]

	goRename(walk_dir,renameExt,renameExtFilter,contains)