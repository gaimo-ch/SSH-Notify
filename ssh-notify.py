#!/usr/bin/env python3
import socket
import netifaces
import requests
from datetime import datetime

webhook_url = 'ここにWebhookURLを入力'

def get_info():
    try:
        local_ip = netifaces.ifaddresses('ens18')[netifaces.AF_INET][0]['addr']
        global_ip = requests.get('https://api64.ipify.org?format=json').json()['ip']
        country = requests.get(f'https://ipinfo.io/{global_ip}/json').json().get('country', '不明')
        hostname = socket.gethostname()
        return local_ip, global_ip, country, hostname
    except Exception as e:
        return str(e), '不明'

def send_discord():
    local_ip, global_ip, country, hostname = get_info()
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    message = f'```🚨SSHログインが検知されたよ\n⌚{now}\n\n🟣サーバー\nホスト名: {hostname}\nローカルIP: {local_ip}\n\n🟡クライアント\nグローバルIP: {global_ip}\n国: {country}```'
    data = {'content': message}
    response = requests.post(webhook_url, json=data)

if __name__ == '__main__':
    send_discord()