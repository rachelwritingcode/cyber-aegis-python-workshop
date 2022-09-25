import os

#Run this file in the same location where you have downloaded the sherlock folder.
username = "username"
sherlock_location = "location of sherlock"
sherlock_results= "./sherlock_result.txt"

os.system('python3 '+sherlock_location+' '+username+' > '+sherlock_results)
 

