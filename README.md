<h1 align="center">
  🚨 SSH-Notify
</h1>

<p align="center">
  <b>
    Linuxサーバに対するSSH接続をPAMを用いて検知し、WebhookでDiscordに通知を行うよ。
  <br>
  Python 3.10.12 / Ubuntu 22.04.3
  </b>
</p>

<p align="center">
  <img src="https://github.com/gaimo-ch/SSH-Notify/assets/116097299/a54793b9-6b4c-44dd-8afd-72e356811a36">
</p>

---

# 🛠 準備をしよう

## Discord

適当なDiscordサーバを立て、Webhookを作成、URLをPythonコード内に貼り付けます。<br>
サーバー設定 → 連携サービス → ウェブフック

![2](https://github.com/gaimo-ch/SSH-Notify/assets/116097299/fbce3fc1-e9c9-4d55-a19b-3309c386f71f)

## Linux

PythonファイルをLinuxサーバ内の適当な場所に配置します。<br>
netifaces, requestsライブラリを使用するため、事前にインストールしておいてください。

PAMはLinuxで使用される認証システムのライブラリです。これを用いてSSH接続を検知し、Pythonスクリプトを実行します。<br>
管理者権限で`/etc/pam.d/sshd`に以下の記述を追記します。パスは各自変更してください。

```sh
session optional pam_exec.so type=open_session /path/to/dir/ssh-notify.py
```

# ✅ 試してみよう

SSH接続を行うと、Discordに通知が...‼️ やったね🎉