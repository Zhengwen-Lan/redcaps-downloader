import tarfile
import os

def compress_folders_to_tar(base_folder, target_tar_gz):
    source_folders = [os.path.join(base_folder, folder) for folder in os.listdir(base_folder) if os.path.isdir(os.path.join(base_folder, folder))]
    print(len(source_folders))

    base0 = source_folders[0]
    base1 = base0[:5]+'__MACOSX'
    base2 = base0[:5]+'annotations'

    idx_list = []
    for idx in range(len(source_folders)-1, -1, -1):
        print('idx:',idx)
        direc = source_folders[idx]
        if direc == base1 or direc == base2:
            source_folders.pop(idx)
    print(source_folders)
    source_folders = source_folders[:1]

    with tarfile.open(target_tar_gz, 'w:gz') as tar:
        for source_folder in source_folders:
            for root, dirs, files in os.walk(source_folder):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, source_folder)
                    tar.add(file_path, arcname=arcname)

# 基础文件夹路径
base_folder = 'data'

# 目标 tar 文件路径
target_tar = '/workspaces/redcaps-downloader/data/compressed_folders.tar.gz'

# 执行压缩
compress_folders_to_tar(base_folder, target_tar)
