import os

def rename_files():
	file_list = os.listdir(r"c:")
	trans_table = str.maketrans("","", "0123456789")
	for file_name in file_list:
		print (file_name)
		print (file_name.translate(trans_table))
		os.rename(file_name, file_name.translate(trans_table))
		
rename_files()

