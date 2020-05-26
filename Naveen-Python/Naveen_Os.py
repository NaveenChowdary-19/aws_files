import os 

from datetime import datetime


print(os.getcwd())
#o/p  --  #/home/ec2-user/environment/

#getcwd()  --  means Get Current working Directory
#chdir()  --  Means Change Directory


os.chdir('/home/ec2-user')
print(os.getcwd())
#o/p  --  /home/ec2-user

print(os.listdir())
#  o/p  --  ['package-lock.json', '.cache', '.mkshrc', '.bash_history', 'environment', '.ssh', '.python_history', '.codeintel', '.profile', '.aws', '.npm', '.npmrc', '.subversion', '.zlogin', '.config', '.zshrc', '.gnupg', '.gitconfig', 'node_modules', '.bash_logout', '.bashrc', '.bash_profile', '.gem', '.c9', '.nvm', '.rvm']


os.mkdir('Avengerss')
# makes A Folder
os.rename('Wakanda Forever','Hulk')
#Rename The Given Folder


os.makedirs('Avenger/Thor/Cap/Ant-Man')
# Makes a Folder That Contains Sub-Folders



os.removedirs('Cap')

os.rename('Avenger','Avengers')
os.rename('Avengerss','Olala Cops')

#Rename the File or Folder


print(os.stat('Avengers'))
#os.stat_result(st_mode=16893, st_ino=23805, st_dev=66305, st_nlink=3, st_uid=501, st_gid=501, st_size=4096, st_atime=1583745823, st_mtime=1583745823, st_ctime=1583746054)
print(os.stat('Olala Cops'))
#os.stat_result(st_mode=16893, st_ino=23565, st_dev=66305, st_nlink=2, st_uid=501, st_gid=501, st_size=4096, st_atime=1583744978, st_mtime=1583744978, st_ctime=1583746134)
print(os.stat('Avengers').st_size)
#4096 bytes
print(os.stat('Olala Cops').st_size)
#4096 bytes



#To See The Last Modification Time 
print(os.stat('Avengers').st_mtime)
#1583745823.8546562



#To See The Last Modification Time in date and Time
Modification_Time=os.stat('Avengers').st_mtime
print(datetime.fromtimestamp(Modification_Time))
#2020-03-09 09:23:43.854656





