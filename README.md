## 用来练手的在线手部关键点提取服务（已部署）

### 实现的功能

- [x] 图片关键点提取
- [ ] 在线关键点提取
- [ ] 提取结果图片下载

### 效果预览

自行部署后可以通过[公网或私网ip](http://xxx.xxx.xxx.xxx:5500)来访问部署页面



### 如何部署

conda的安装这里不过多赘述，首先创建新环境，python版本为3.5以上即可

>conda create -n xxx python==xxx

然后安装必要的包

>pip install -r requirements.txt

如果之后运行时出现错误

>ImportError: libGL.so.1: cannot open shared object file: No such file or directory

则运行以下命令

>pip uninstall opencv-python #这一步cv2的名称可能不同，只要卸载掉环境内的opencv即可
>
>pip install opencv-python-headless

安装环境之后运行server.py

>python server.py

之后通过服务器的公网ip即可访问网站，默认端口是5500，如果想要更改端口，可以在server.py中更改
