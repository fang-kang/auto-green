import subprocess
import datetime
import requests

# 设置 Git 用户信息
subprocess.call(['git', 'config', '--global', 'user.email', '1793980864@qq.com'])
subprocess.call(['git', 'config', '--global', 'user.name', 'fang-kang'])

# 生成日期列表
start_date = datetime.date(2022, 1, 1)
end_date = datetime.date(2122, 12, 31)
date_diff = end_date - start_date
dates = [start_date + datetime.timedelta(days=i) for i in range(date_diff.days + 1)]

# 循环提交代码
for date in dates:
    # 跳过周末和不需要提交的日期
    if date.weekday() >= 5 or date in [datetime.date(2022, 1, 1), datetime.date(2122, 12, 25)]:
        continue

    # 创建一个空白文件
    with open('contribution.txt', 'w') as f:
        f.write(f'Contribution on {date.strftime("%Y-%m-%d")}')

    # 添加并提交文件
    subprocess.call(['git', 'add', 'contribution.txt'])
    subprocess.call(['git', 'commit', '-m', 'Contribution'])
    subprocess.call(['git', 'push'])

    # 获取提交的日期
    commit_date = date.strftime("%Y-%m-%d")

    # 使用 GitHub API 更新提交日期
    username = 'fang-kang'
    repository = 'auto-green'
    url = f'https://api.github.com/repos/{username}/{repository}/commits'

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/vnd.github.v3+json'
    }

    payload = {
        'message': 'Contribution',
        'author': {
            'name': 'fang-kang',
            'email': '1793980864@qq.com',
            'date': f'{commit_date}T12:00:00Z'
        }
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 201:
        print(f'Contribution on {commit_date} created successfully')
    else:
        print(f'Failed to create contribution on {commit_date}')

# 删除临时文件
subprocess.call(['git', 'rm', 'contribution.txt'])
subprocess.call(['git', 'commit', '-m', 'Remove temporary file'])
subprocess.call(['git', 'push'])
