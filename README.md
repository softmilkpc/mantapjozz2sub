
### Features
- Sepenuhnya dapat dicustom.
- Dapat di-deploy di heroku & vps.
- Pesan sambutan & Forcesub yang dapat dicustom.
- Lebih dari satu Posting dalam Satu Link (batch).
- Fleksibel FSUB Button bisa 1 button atau 2 button menyesuaikan dengan var yang di isi.

### Setup

- Tambahkan bot ke Channel Database dengan semua izin admin
- Tambahkan bot ke Channel ForceSub tambahkan bot sebagai ADMIN
- Tambahkan bot ke Group ForceSub tambahkan bot sebagai ADMIN

##
### Installation
#### Deploy on Heroku
## <p align="center">DEPLOY TO WEB HEROKU</p>

<p align="center"><a href="https://heroku.com/deploy?template=https://github.com/softmilkpc/mantapjozz2sub">
  <img src="https://img.shields.io/badge/Deploy%20To%20Heroku-aqua?style=flat&logo=heroku" width="325" height="50.100" /></a></p>


#### Deploy in your VPS
````bash
git clone https://github.com/madloyer/mantapjozz2sub
cd File-Sharing-Man
pip3 install -r requirements.txt
cp sample_config.env config.env
# edit config.env Anda dan isi VARS menggunakan nano config.env CTRL + S untuk menyimpan VARS Anda, 
# gunakan CTRL + X untuk keluar dan kembali ke direktori File-Sharing-Man
bash start
````

### Admin Commands

```
/start - mulai bot atau dapatkan postingan

/batch - buat link untuk lebih dari satu posting

/genlink - buat link untuk satu posting

/users - lihat statistik pengguna bot

/broadcast - menyiarkan/broadcast pesan apa pun ke pengguna bot

/ping - untuk mengecek bot

/uptime - untuk melihat waktu aktif bot
```

### Variables

* `API_HASH` Dapatkan API HASH di web my.telegram.org.
* `API_ID` Dapatkan APP ID di web my.telegram.org
* `TG_BOT_TOKEN` Dapatkan dari t.me/BotFather
* `OWNER` Masukan Username Telegram untuk Owner BOT
* `OWNER_ID` Masukan User ID Telegram untuk Owner BOT
* `CHANNEL_ID` Masukan ID Channel Untuk [Channel Database] contoh:- -100xxxxxxxx
* `ADMINS` Masukan User ID untuk mendapatkan hak Admin BOT [Hanya dapat membuat link]
* `START_MESSAGE` Opsional: Pesan /start memulai awalan ke bot, Gunakan <a href='https://github.com/softmilk/mantapjozz2sub/blob/main/README.md#start_message'>format</a> parsemode HTML 
* `FORCE_SUB_MESSAGE` Opsional: Pesan Paksa Subscribe bot, Gunakan Format parsemode HTML
* `FORCE_SUB_CHANNEL` Masukan ID dari Channel Untuk Wajib Subscribenya
* `FORCE_SUB_GROUP` Masukan ID dari Group Untuk Wajib Subscribenya

### Extra Variables

* `CUSTOM_CAPTION` letakkan teks teks Kustom Anda jika Anda ingin Mengatur Teks Kustom, Anda dapat menggunakan HTML dan <a href='https://github.com/softmilk/mantapjozz2sub/blob/main/README.md#custom_caption'>fillings</a> untuk pemformatan (hanya untuk dokumen)
* `DISABLE_CHANNEL_BUTTON` Masukan True untuk Nonaktifkan Tombol Berbagi Saluran, Default jika False

### Fillings
#### START_MESSAGE | FORCE_SUB_MESSAGE

* `{first}` - User first name
* `{last}` - User last name
* `{id}` - User ID
* `{mention}` - Mention the user
* `{username}` - Username

#### CUSTOM_CAPTION

* `{filename}` - file name of the Document
* `{previouscaption}` - Original Caption


### Credits

- Thanks To Dan For His Awsome [Libary](https://github.com/pyrogram/pyrogram)
- Thanks To [CodeXBotz](https://github.com/CodeXBotz/File-Sharing-Bot)
- Our Support Group Members

### Licence
[![GNU GPLv3 Image](https://www.gnu.org/graphics/gplv3-127x51.png)](http://www.gnu.org/licenses/gpl-3.0.en.html)  

Free Software: You can use, study share and improve it at your
will. Specifically you can redistribute and/or modify it under the terms of the
[GNU General Public License](https://www.gnu.org/licenses/gpl.html) as
published by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version. 

##

   **Berikan Bintang Repo ini jika Anda menyukainya ⭐⭐⭐⭐⭐**

