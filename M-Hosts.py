import os
import zipfile
import requests

aPath = os.path.abspath('.')
Path = aPath + "/M-hosts/system/etc/hosts"
zipPath = aPath + "/M-hosts"

default = '''#	127.0.0.1       localhost
#	::1             localhost\n\n\n'''

url = "https://raw.fastgit.org/521xueweihan/GitHub520/main/hosts"

response = requests.get(url)
hosts = response.text
hosts = default + hosts

with open(f"{Path}","w") as f:
	f.write(hosts)
	

def zipDir(dirpath,outFullName):
    """
    压缩指定文件夹
    :param dirpath: 目标文件夹路径
    :param outFullName: 压缩文件保存路径+xxxx.zip
    :return: 无
    """
    zip = zipfile.ZipFile(outFullName,"w",zipfile.ZIP_DEFLATED)
    for path,dirnames,filenames in os.walk(dirpath):
        # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
        fpath = path.replace(dirpath,'')

        for filename in filenames:
            zip.write(os.path.join(path,filename),os.path.join(fpath,filename))
    zip.close()

zipDir(f"{zipPath}",f"{aPath}/M-hosts.zip")