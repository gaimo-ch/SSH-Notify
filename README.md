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
  <img src="https://github.com/gaimo-ch/SSH-Notify/assets/116097299/c0852792-f22a-42d2-ab9a-274bd60a801a">
</p>

---

# 🛠 準備をしよう

## Discord

適当なDiscordサーバを立て、Webhookを作成、URLをコード内に貼り付けます。<br>
サーバー設定 → 連携サービス → ウェブフック

![2](https://github.com/gaimo-ch/SSH-Notify/assets/116097299/fbce3fc1-e9c9-4d55-a19b-3309c386f71f)

## Linux

ssh-notify.pyをLinuxサーバ内の適当な場所に配置します。<br>
netifaces, requestsライブラリを使用するため、事前に`pip install`しておいてください。

SSHのアクセスログからクライアントのIPアドレスを取得します。各ディストリビューションごとに認証ログのパスが違うため、編集する必要があるかもしれません。<br>
本コードでは`/var/log/auth.log`を指定しています。

PAMはLinuxで使用される認証システムのライブラリです。これを用いてSSH接続を検知し、Pythonスクリプトを実行します。<br>
root権限で`/etc/pam.d/sshd`に以下の記述を追記します。パスは各自変更してください。

```sh
session optional pam_exec.so type=open_session /path/to/dir/ssh-notify.py
```

# ✅ 試してみよう

SSH接続を行うと、Discordに通知が...‼️ やったね🎉