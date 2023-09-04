#!/usr/bin/env python3
import socket
import netifaces
import requests
import re
from datetime import datetime

webhook_url = 'ここにWebhookのURLを入力'
log_path = '/var/log/auth.log' #認証ログのパス
ssh_pattern = r'sshd\[\d+\]: Accepted .* for .* from (\d+\.\d+\.\d+\.\d+)'

def get_info():
    try:
        hostname = socket.gethostname() # サーバのホスト名を取得

        server_ip = netifaces.ifaddresses('ens18')[netifaces.AF_INET][0]['addr'] # サーバのIPを取得

        with open(log_path) as log_file: # ログからクライアントのIPを取得
            log_content = log_file.read()
            match = re.search(ssh_pattern, log_content)
            if match:
                client_ip = match.group(1)
            else:
                client_ip = 'IPを取得できないよ' 

        return hostname, server_ip, client_ip
    except Exception as e:
        return str(e), '不明'

def send_discord():
    hostname, server_ip, client_ip = get_info()
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    message = f'```🚨SSHログインが検知されたよ\n⌚{now}\n\n🟣サーバー\nホスト名: {hostname}\nIP: {server_ip}\n\n🟡クライアント\nIP: {client_ip}```'
    data = {'content': message}
    response = requests.post(webhook_url, json=data)

if __name__ == '__main__':
    send_discord()