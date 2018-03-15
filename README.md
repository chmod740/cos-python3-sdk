# cos-python3-sdk
# 腾讯云对象存储服务（cos）Python3.5版本SDK
### *此版本非官方版本
##### 项目进展：开发完成(分片上传待测试)
##### 项目地址：https://github.com/imu-hupeng/cos-python3-sdk
##### 项目的来由：做基于Django个人网站时，采用了腾讯云的对象存储服务，发现他们并没有提供基于py3的sdk，然后就有了这个项目，另外此项目SDK已多次在我的其他项目中集成，使用较稳定。
## SDK用法简介
### 1.安装(下面两种方式任选其一即可)
#### 1.1 推荐使用pip安装，命令： pip install cos-lib3
#### 1.2 下载源码，使用setup.py安装
### 2.bucket操作
#### 2.1 得到一个bucket
调用格式：
```python
from cos_lib3.cos import Cos

cos = Cos(app_id=<appid>, secret_id='<secret_id>', secket_key='<secket_key>', region='<地域：sh（华东），gz（华南），tj（华北）>')
bucket = cos.get_bucket("<bucket名称>")
```
样例调用：
```python
from cos_lib3.cos import Cos
cos = Cos(app_id=123456789, secret_id='AKIDpTgPyrRUh6cS77PTGVtHZKklTBCurQq2', secket_key='2o5eXbkgNxJ2jWnZ67z1vlIVDxfAQ', region='tj')
bucket = cos.get_bucket("test")
```

### 3.目录操作
#### 3.1 创建目录
格式如下：
```python
bucket.create_folder('<目录名称>')
```
#### 3.2 查询目录属性
格式如下：
```python
bucket.query_folder('<目录名称>')
```
#### 3.3 列出目录
调用格式1：
```python
rst = bucket.list_folder(dir_name='<目录名称>')
print(rst)
```
调用格式2（查询某个目录下特定的特定前缀的文件）：
```python
rst = bucket.list_folder(dir_name='<目录名称>', prefix='<前缀>')
print(rst)
```
调用格式3（查询某个目录下的文件，并限定查询数量）：
```python
rst = bucket.list_folder(dir_name='<目录名称>',  num=<查询的数量>)
print(rst)
```
调用格式4（综合格式2，3）
```python
rst = bucket.list_folder(dir_name='<目录名称>', prefix='<前缀>',  num=<查询数量>)
```
#### 3.4 删除目录
调用格式
```python
rst = bucket.delete_folder('<目录名称>')
print(rst)
```
### 4 文件操作
#### 4.1 简单文件上传（适合上传的文件的大小小于20MB）
调用格式1（文件上传到bucket的根目录）：
```python
bucket.upload_file(real_file_path='<文件的在本地的路径>', file_name='<文件在bucket的名称>')
```
调用格式2（文件上传到bucket的特定的目录）
```python
bucket.upload_file(real_file_path='<文件的在本地的路径>', file_name='<文件在bucket的名称>', dir_name='<目录名称>')
```
#### 4.2 文件分片上传
暂未实现
#### 4.3 文件移动
调用格式
```python
bucket.move_file(source_fileid='<源文件的路径>', dest_fileid='目标文件的路径')
```
#### 4.4 文件复制
调用格式
```python
bucket.copy_file(source_fileid='<源文件路径>', dest_fileid='目标文件路径')
```
#### 4.5 文件删除
调用格式
```python
bucket.delete_file('<文件的绝对路径>')
```
#### 4.6 通过url上传文件
调用格式如下:
```python
bucket.upload_file_from_url("http://sucai.qqjay.com/qqjayxiaowo/201210/26/1.jpg", file_name="777.jpg", dir_name=None)
```
第一个参数为文件的url地址,<br>
第二个参数为放在云存储上的显示的文件的文件名,<br>
第三个参数为文件在云存储上的文件目录,可以为None,此时放在根目录上

### 5.附录
#### 5.1 上传文件后我该怎么获取用于访问的链接?
首先获取上传之后的返回值 如:data = bucket.upload_file(real_file_path='<文件的在本地的路径>', file_name='<文件在bucket的名称>') <br>
得到的data 的值形如:<br>
{'source_url': 'http://test-125255866665.costj.myqcloud.com/777.jpg', 'access_url': 'http://test-125255866665.file.myqcloud.com/777.jpg', 'url': 'http://tj.file.myqcloud.com/files/v2/125255866665/test/777.jpg', 'vid': '8fea559ee6578acf89698bef7ae5b6551494676054', 'resource_path': '/125255866665/test/777.jpg'}<br>
下面我们来解析这个data字符串,得到access_url字段的值并输出:
```python
access_url = eval(data).get("access_url")
print(access_url)
```
#### 5.2 如果我需要https形式的链接怎么办？
腾讯云的对象存储服务完全是支持https的，如果你获取到的链接并不是https形式的，尝试使用replace函数把‘http://’ 直接替换成 ‘https://’ 试试

#### 5.3 分片上传现在是无法使用吗？
感谢开源社区的热心成员，他们提供了分片上传的代码，现在已经集成进去了此sdk，由于本人忙于其他的项目,未能做详尽的测试,分片上传的方法名为 
```
upload_slice_file()
```
如果这个方法没办法满足您的需求，请尝试
https://github.com/a270443177/cos-python3-sdk-v4
这个类库的使用方法完全同于腾讯云对象存储的py2.7版本的SDK

#### 5.4 您发现了bug,或者有什么其他的需求和建议
请报告issue
