import os
import uuid
import shutil

# 获取当前目录
current_dir = os.getcwd()

# 创建目标目录
target_dir = os.path.join(current_dir, "ok")
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

# 遍历当前目录及子目录中的文件
for root, dirs, files in os.walk(current_dir):
    for file in files:
        # 获取文件的完整路径
        file_path = os.path.join(root, file)
        
        # 检查文件是否为图片
        if file_path.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
            # 生成随机的UUID作为新文件名
            new_filename = str(uuid.uuid4())
            
            # 获取文件的扩展名
            extension = os.path.splitext(file_path)[1]
            
            # 构建新的文件路径
            new_file_path = os.path.join(target_dir, new_filename + extension)
            
            # 复制文件并重命名
            shutil.copy2(file_path, new_file_path)
            print(f"已复制并重命名文件：{file_path} -> {new_file_path}")
