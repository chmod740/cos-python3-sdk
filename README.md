# cos-python3-sdk
# 腾讯云对象存储服务（cos）Python3.5版本SDK
### *此版本非官方版本
##### 项目进展：部分开发完成
##### 项目地址：https://github.com/imu-hupeng/cos-python3-sdk
## SDK用法简介
### 1.安装
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

