[app]

# Nama aplikasi dan metadata dasar
title = MyKivyApp
package.name = mykivyapp
package.domain = org.example
version = 1.0.0

# Konfigurasi Android/IOS
requirements = python3==3.11.5, kivy==2.3.0, numpy
android.permissions = INTERNET
android.api = 34
android.minapi = 21
android.ndk = 23b
android.sdk = 34
android.arch = arm64-v8a

# Konfigurasi build
source.dir = .
source.include_exts = py,png,jpg,kv,ttf,json
orientation = portrait
fullscreen = 0

# Icon dan presplash (sesuaikan path)
icon.filename = %(source.dir)s/data/icon.png
presplash.filename = %(source.dir)s/data/presplash.png

# Perilaku build
log_level = 2
warn_on_root = 1
android.accept_sdk_license = True

# Opsi tambahan untuk performa
android.enable_androidx = True
android.enable_multidex = True

# Hook khusus (opsional)
pre_build_command = 
post_build_command =
