import hashlib
import os 
import time
def hashing(path):
    with open(path, "rb") as f:
        bytes=f.read()
        readable_hash=hashlib.sha256(bytes).hexdigest()
        return readable_hash
def baseline(path):
	baseline={}
	for filename in os.listdir(path):
		path_x=os.path.join(path,filename)
		if os.path.isfile(path_x):
			hash = hashing(path_x)
			baseline[filename] = hash
	return baseline


def monitor_folder(folder_path):
    
    baseline_ = baseline(folder_path)
    print("Baseline created ")

    while True:
        time.sleep(5) 
        
        
        current_state = baseline(folder_path)
        
        
        for filename, current_hash in current_state.items():
           
            if filename not in baseline_:
                print(f"[!] ALERT: New File Created: {filename}")
            
            
            elif current_hash != baseline_[filename]:
                print(f"[!] ALERT: File Modified: {filename}")

        for filename in baseline_:
            if filename not in current_state:
                print(f"[!] ALERT: File Deleted: {filename}")

        baseline_ = current_state

monitor_folder("/home/kali/project/")	
	

