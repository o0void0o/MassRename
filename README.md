# MassRename
Python scrippy to go rename all extensions of files/filtered files in a folder.

Usage: python3 MassRename.py m1 m2 o1 o2 o3

Mandatory parameters:

m1: The base directory: [String] The base directory the script will apply extension renaming on, all nested folders will be processed.

m2: The new file extension: [String] The new file extension. If no filter is specified then all file extension are renamed.

Optional parameters: 

o1: The file extension filter: [String] Only apply the extension rename to files matching this filter.

o2: Use Contains matching: [INT 1 or 0] When set to 1 the extension rename will be applied if the filter is contained in the rename candidate file. The default behavior is 0 and it relies on direct matching the filter criteria.
