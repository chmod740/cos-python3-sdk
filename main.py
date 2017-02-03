from qcloud_cos.cos import Cos
""""
appid = 1252558465
secret_id = u'AKIDzTgPxrRHu6sC47PTGVtGZKklTBCurQK1'
secret_key = u'2O5eXGkgNxJ2jWnbZ67z1vlIVDxlufAQ'
region_info = "tj"
"""
cos = Cos(app_id=1252558465, secret_id='AKIDzTgPxrRHu6sC47PTGVtGZKklTBCurQK1', secket_key='2O5eXGkgNxJ2jWnbZ67z1vlIVDxlufAQ', region='tj')
# result = cos.get_bucket('test').create_folder('aaa')
bucket = cos.get_bucket("test")
bucket.query_folder('aaa')