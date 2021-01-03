#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from receive_mail import FetchEmail
from extract_content import extract_content
from send_mail import SendMail

# receivemail
# 下载对应邮箱的附件图片，下载到对应的文件夹 received
mail_server = ''
username = ''
password = ''  # 此处填写授权码
fetch_email = FetchEmail(mail_server, username, password)
emails = fetch_email.fetch_unread_messages()

# 调用相应的代码进行处理，识别内容，生成xlsx
save_dir_path = "to_send"
extract_content(save_dir_path)

# sendmail
from_mail = ''
tolist = ['']
username = ''
password = ''  # 此处填写授权码
send = SendMail(from_mail, tolist, username, password)
send.send_mail('./to_send')