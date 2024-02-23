import os
import subprocess

for i in range(5):
    begin = 175
    step = 25
    start = begin + i * step
    end = start + step
    print(f"Processing files from {start} to {end}...")

    # Run your Python script here
    cmd = f"python runforGit.py --start {start} --end {end} --processNum {96} --output 'data/{start}_{end}'"
    subprocess.run(cmd, shell=True)

    # assert 1==2

    # Create a tar archive of the processed data
    tar_cmd = f"tar -czvf data/finished/{start}_{end}.tar -C data/{start}_{end} ."
    print(tar_cmd)

    subprocess.run(tar_cmd, shell=True)

    if i != 0:
        #delete data finished file
        delete_cmd = f"rm -r data/{start-step}_{end-step}"
        subprocess.run(delete_cmd, shell=True)

    # Optionally, create a log file to indicate completion
    log_file = f"{start}_{end}.log"
    with open(log_file, "w") as f:
        f.write("Processing completed successfully!")

    print(f"Files from {start} to {end} processed and archived.")
