import os
import sys

walk_dir = sys.argv[1]

print('walk_dir = ' + walk_dir)

# If your current working directory may change during script execution, it's recommended to
# immediately convert program arguments to an absolute path. Then the variable root below will
# be an absolute path as well. Example:
# walk_dir = os.path.abspath(walk_dir)
print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))

for root, subdirs, files in os.walk(walk_dir):

	for filename in files:
		file_path = os.path.join(root, filename)
		base=os.path.basename(file_path)
		thefile=os.path.splitext(base)[0]
		if os.path.splitext(base)[1]=='.002':
			os.remove(file_path)
			continue
		if os.path.splitext(base)[1]=='.001':
			os.rename(file_path, os.path.join(root, thefile+'.jar'))
		#dst ="Hostel" + str(count) + ".jpg"
       # src ='xyz'+ filename 
       # dst ='xyz'+ dst 
          
        # rename() function will 
        # rename all the files 
         
		