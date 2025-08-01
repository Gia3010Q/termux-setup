#!/bin/bash
# Script tự động cài đặt Termux và tải file tdm3.py, sn01.py

# Định nghĩa màu sắc
GREEN='\033[1;32m'
YELLOW='\033[1;33m'
BLUE='\033[1;34m'
CYAN='\033[1;36m'
BOLD='\033[1m'
NC='\033[0m' # No Color

# Hàm hiển thị hiệu ứng loading
show_loading() {
    local message=$1
    echo -ne "${BLUE}[✨] ${message} ${NC}"
    for i in {1..3}; do
        echo -ne "."
        sleep 0.1
    done
    echo -ne "\r\033[K"
}

# Hàm hiển thị trạng thái đơn giản
show_status() {
    local message=$1
    echo -e "${CYAN}[⏳] ${message}...${NC}"
    sleep 0.5  # Thêm độ trễ tự nhiên
    echo -e "${GREEN}[✅] ${message} hoàn tất!${NC}"
}

# Xóa màn hình trước khi hiển thị
clear

# Hiển thị tiêu đề trong khung đẹp với Developed by xuống dưới
echo -e "${BLUE}╒════════════════════════════════════════════╕${NC}"
echo -e "${CYAN}│ ${BOLD}✨ TERMUX AUTO SETUP      ✨${BOLD}               │${NC}"
echo -e "${CYAN}│ ${BOLD}✨ Developed by Đặng Gia  ✨${BOLD}               │${NC}"
echo -e "${CYAN}│ ${BOLD}✨ Version 1.1 (Beta)     ✨${BOLD}               │${NC}"
echo -e "${BLUE}╘════════════════════════════════════════════╛${NC}"
echo ""

# Cập nhật và nâng cấp Termux
show_loading "Khởi động cập nhật Termux"
show_status "Cập nhật Termux"
yes | pkg update > /dev/null 2>&1 && yes | pkg upgrade -y > /dev/null 2>&1
echo ""

# Cấp quyền truy cập bộ nhớ
show_loading "Khởi động cấp quyền lưu trữ"
show_status "Cấp quyền lưu trữ"
echo "y" | termux-setup-storage > /dev/null 2>&1
echo ""

# Cài đặt các gói cần thiết
show_loading "Khởi động cài đặt gói"
show_status "Cài đặt gói"
yes | pkg install python tsu libexpat openssl -y > /dev/null 2>&1
echo ""

# Cài đặt các thư viện Python
show_loading "Khởi động cài đặt thư viện Python"
show_status "Cài đặt thư viện Python"
pip install requests Flask colorama aiohttp psutil crypto pycryptodome prettytable loguru rich pytz tqdm pyjwt pystyle cloudscraper > /dev/null 2>&1
echo ""

# Tải file về /sdcard/Download
show_loading "Khởi động tải tdm3.py"
show_status "Tải tdm3.py"
curl -o /sdcard/Download/tdm3.py https://raw.githubusercontent.com/Gia3010Q/termux-setup/main/tdm3.py > /dev/null 2>&1
echo -e "${GREEN}[✅] Đã tải tdm3.py!${NC}"
show_loading "Khởi động tải sn01.py"
show_status "Tải sn01.py"
curl -o /sdcard/Download/sn01.py https://raw.githubusercontent.com/Gia3010Q/termux-setup/main/sn01.py > /dev/null 2>&1
echo -e "${GREEN}[✅] Đã tải sn01.py!${NC}"
show_loading "Khởi động tải ld5.py"
show_status "Tải ld5.py"
curl -o /sdcard/Download/ld5.py https://raw.githubusercontent.com/Gia3010Q/termux-setup/refs/heads/main/ld5.py > /dev/null 2>&1
echo -e "${GREEN}[✅] Đã tải ld5.py!${NC}"
echo ""

# Màn hình hoàn thành với banner
clear
echo -e "${BLUE}╒════════════════════════════════════════════╕${NC}"
echo -e "${CYAN}│ ${BOLD}✨ TERMUX AUTO SETUP      ✨${BOLD}               │${NC}"
echo -e "${CYAN}│ ${BOLD}✨ Developed by Đặng Gia  ✨${BOLD}               │${NC}"
echo -e "${CYAN}│ ${BOLD}✨ Version 1.1 (Beta)     ✨${BOLD}               │${NC}"
echo -e "${BLUE}╘════════════════════════════════════════════╛${NC}"
echo -e "${CYAN} ╒════════════════════════════════════════════╕${NC}"
echo -e "${GREEN} │ ${BOLD}Setup Hoàn Tất Có Thể Sử Dụng Ngay${BOLD}          │${NC}"
echo -e "${CYAN} ╘════════════════════════════════════════════╛${NC}"
echo -e "${BLUE}📦 Khởi động tool với lệnh sau:${NC}"
echo -e "${YELLOW}   ➜ cd /sdcard/Download && python sn01.py${NC}"
echo -e "${YELLOW}   ➜ cd /sdcard/Download && python tdm3.py${NC}"
echo -e "${YELLOW}   ➜ cd /sdcard/Download && python ld5.py${NC}"
