#!/usr/bin/env python3
import socket
import netifaces
import requests
import re
from datetime import datetime
import subprocess

webhook_url = 'ここにWebhookURLを入力'
log_path = '/var/log/auth.log' # 認証ログのパス
ssh_pattern = r'sshd.*Accepted .* for .* from (\d+\.\d+\.\d+\.\d+)' # 認証ログからIPを取得するための正規表現

def get_server(): # サーバの情報を取得
    try:
        hostname = socket.gethostname() # サーバのホスト名を取得
        server_ip = netifaces.ifaddresses('ens18')[netifaces.AF_INET][0]['addr'] # ens18をNIC名に指定していますが、環境に合わせて変更してください
        return hostname, server_ip
    except Exception as e:
        return str(e)

def get_client(): # クライアントの情報を取得
    try:
        # 最新のデータを取得するため、ログファイルから最後の10行を取得
        result = subprocess.check_output(['tail', '-n', '10', log_path], universal_newlines=True)
        log_lines = result.split('\n')
        client_ip = [re.findall(ssh_pattern, line)[0] for line in log_lines if re.search(ssh_pattern, line)]
        
        if client_ip:
            return client_ip[-1]
        else:
            return "IPを取得できないよ"
    except Exception as e:
        return 'アクセスログを取得する権限がないよ'

def send_discord(): # Discordに通知を送信
    hostname, server_ip = get_server()
    client_ip = get_client()
    
    if client_ip == 'ここに除外するIPを入力': 
        pass
        return

    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    message = f'```🚨SSHログインが検知されたよ\n⌚{now}\n\n🟣サーバー\nホスト名: {hostname}\nIP: {server_ip}\n\n🟡クライアント\nIP: {client_ip}```'
    data = {'content': message}
    requests.post(webhook_url, json=data)

if __name__ == '__main__':
    send_discord()
