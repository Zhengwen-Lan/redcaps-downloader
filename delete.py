import os
import subprocess

# 获取所有.json文件的路径
annotation_dir = 'data/annotations'
json_files = [f for f in os.listdir(annotation_dir) if f.endswith('.json')]
print(json_files)
print(len(json_files))

def custom_sort(json_filename):
    parts = json_filename.split('_')
    word = parts[0]
    year = int(parts[1].split('.')[0])  # 提取年份并去除扩展名
    return (word, year)

sorted_json_list = sorted(json_files, key=custom_sort)
json_files = sorted_json_list[410:] 
print(json_files)
print(len(json_files))
# # 设置图像保存路径
# image_save_path = '/content/drive/MyDrive/redcaps_260'

# # 如果目录不存在，则创建
# if not os.path.exists(image_save_path):
#     os.makedirs(image_save_path)
num = 0
# 遍历每个.json文件并执行下载命令
for json_file in json_files:
    file_path = os.path.join(annotation_dir, json_file)
    print(f'Deleting: {file_path}')
    # assert 1==2
#     print("cur file",json_file)
    print("number ",num)
    num = num+1
    try:
        os.remove(file_path)
        print(f'{json_file} deleted successfully.')
    except Exception as e:
        print(f'Error deleting {json_file}: {e}')
#     cmd = f"redcaps download-imgs -a {os.path.join(annotation_dir, json_file)} --save-to {image_save_path} --resize 256 -j 280"
#     subprocess.run(cmd, shell=True)

# # 如果你不想调整图像大小，可以将--resize 512更改为--resize -1
