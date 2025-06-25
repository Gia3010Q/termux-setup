#!/bin/bash
# Script tự động cài đặt Termux và tải file tdm3.py, sn01.py

echo "Đang cập nhật Termux..."
pkg update && pkg upgrade -y

echo "Đang cấp quyền lưu trữ..."
echo "y" | termux-setup-storage

echo "Đang cài đặt python, tsu, libexpat, openssl..."
pkg install python tsu libexpat openssl -y

echo "Đang cài đặt các thư viện Python..."
pip install requests Flask colorama aiohttp psutil crypto pycryptodome prettytable loguru rich pytz tqdm pyjwt pystyle cloudscraper

echo "Đang tải tdm3.py và sn01.py..."
curl -o /sdcard/Download/tdm3.py https://raw.githubusercontent.com/Gia3010Q/termux-setup/main/tdm3.py
curl -o /sdcard/Download/sn01.py https://raw.githubusercontent.com/Gia3010Q/termux-setup/main/sn01.py

echo "Hoàn tất! File tdm3.py và sn01.py đã được tải về /sdcard/Download"
