import os
from datetime import datetime

"""
create_directory: creates a directory if it does not exists
                        
arguments:
    directory_name: string
"""
def create_directory(directory_name):
    if not os.path.exists(directory_name):
        os.mkdir(directory_name)

"""
timer: calculates time spent

arguments:
    start_time: None or datetime object
"""
def timer(start_time = None):
    if start_time is None:
        start_time = datetime.now()
        return start_time
    else:
        hours, temp_seconds = divmod((datetime.now() - start_time).total_seconds(), 3600)
        minutes, seconds = divmod(temp_seconds, 60)
        print(f"Time spent: {int(hours)}:{int(minutes)}:{int(seconds)}")