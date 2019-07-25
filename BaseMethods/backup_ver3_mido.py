import os
import time

# 1. 需要备份的文件与目录将被
# 指定在一个列表中。
# 例如在 Windows 下：
# 在这里要注意到我们必须在字符串中使用双引号
# 用以括起其中包含空格的名称。
# source = ['"C:\\My Documents"', 'C:\\Code']
source = ['D:\Work\Project\TestFiles\SourceDir']
# 又例如在 Mac OS X 与 Linux 下：
# source = ['/Users/swa/notes']
# 2. 备份文件必须存储在一个
# 主备份目录中
# 例如在 Windows 下：
target_dir = 'D:\Work\Project\TestFiles\TargetDir'
# 又例如在 Mac OS X 和 Linux 下：
# target_dir = '/Users/swa/backup'
# 要记得将这里的目录地址修改至你将使用的路径
# 3. 备份文件将打包压缩成 zip 文件。
# 4. zip 压缩文件的文件名由当前日期与时间构成。
# 子目录名称
today = target_dir + os.sep + time.strftime('%Y%m%d')
# 如果子目录尚不存在则创建一个
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)
# 将当前时间作为 zip 文件的文件名
now = time.strftime('%H%M%S')
# 添加一条来自用户的注释以创建
# zip 文件的文件名
comment = input('Enter a comment --> ')
# 检查是否有评论键入
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'
# 5. 我们使用 7-zip 软件的命令将文件打包成 zip 格式
zip_command = '7z a -r {0} {1}'.format(target, ' '.join(source))
# 运行备份
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')