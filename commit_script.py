import datetime
import os
import random

# 生成一个包含当前日期的文件
current_date = datetime.datetime.now().date().isoformat()
file_name = f"{current_date}.txt"
file_path = os.path.join(os.getcwd(), file_name)

# 根据条件来决定生成深绿或浅绿的提交
if datetime.datetime.now().weekday() < 5:  # 星期一到星期五
    with open(file_path, "w") as file:
        file.write("This is a deep green commit!")
else:
    if random.random() < 0.5:
        with open(file_path, "w") as file:
            file.write("This is a light green commit!")

# 只有当文件不为空时才添加、提交和推送文件
if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
    os.system(f"git add {file_path}")
    os.system(f"git commit -m 'Add commit for {file_name}'")
    os.system("git push")
