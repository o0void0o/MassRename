import os
import sys

def help():
	print("Usage: python3 MassRename.py m1 m2 o1 o2 o3")
	print("Mandatory parameters:")

	print("m1: The base directory: [String] The base directory the script will apply extension renaming on, all nested folders will be processed.")
	print("m2: The new file extension: [String] The new file extension. If no filter is specified then all file extension are renamed.")
	print("Optional parameters: ")
	print("o1: The file extension filter: [String] Only apply the extension rename to files matching this filter.")
	print("o2: Use Contains matching: [INT 1 or 0] When set to 1 the extension rename will be applied if the filter is contained in the rename candidate file. The default behavior is 0 and it relies on direct matching the filter criteria.")

def goRename(baseDir,newExt,filter,matchingStrategy):
	print('baseDir = ' + baseDir)
	print('newExt = ' + newExt)
	print('filter = ' + filter)
	print('matchingStrategy = ' + str(matchingStrategy))
	print('baseDir (absolute) = ' + os.path.abspath(baseDir))

	for root, subdirs, files in os.walk(baseDir):

		for filename in files:
			file_path = os.path.join(root, filename)
			base =  os.path.basename(file_path)
			thefile = os.path.splitext(base)[0]
			if renameExtFilter != '':			
				if matchingStrategy:
					if os.path.splitext(base)[1].count(filter)>0:
						os.rename(file_path, os.path.join(root, thefile+'.'+newExt))
				else:

					if os.path.splitext(base)[1] == '.'+filter:
						os.rename(file_path, os.path.join(root, thefile+'.'+newExt))
			else:
					os.rename(file_path, os.path.join(root, thefile+'.'+newExt))


if __name__ == "__main__":

	if len(sys.argv) <=2:
		help()
		exit()

	base_dir = sys.argv[1]
	renameExt= sys.argv[2]
	renameExtFilter= ''
	contains=0

	if len(sys.argv) >3:
		renameExtFilter=sys.argv[3]

	if len(sys.argv) >4:
		contains=int(sys.argv[4])

	goRename(base_dir,renameExt,renameExtFilter,contains)