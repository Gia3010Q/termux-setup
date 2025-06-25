#!/bin/bash
# Script tự động cài đặt Termux và tải file tdm3.py, sn01.py

# Định nghĩa màu sắc
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m' # No Color

# Hàm hiển thị thanh tiến trình (một dòng)
show_progress() {
    local total=$1
    local message=$2
    local percent=$3
    local filled=$((percent / 4))
    local empty=$((25 - filled))
    local bar=""
    for ((i=0; i<filled; i++)); do bar="${bar}█"; done
    for ((i=0; i<empty; i++)); do bar="${bar} "; done
    echo -e "\r${YELLOW}[📥] ${message}: [${GREEN}${bar}${NC}] ${CYAN}${percent}%${NC}"
}

# Hàm hiển thị hiệu ứng loading
show_loading() {
    local message=$1
    echo -ne "${YELLOW}[🌟] ${message} ${NC}"
    for i in {1..3}; do
        echo -ne "."
        sleep 0.3
    done
    echo -ne "\r"
}

# Hiển thị banner
echo -e "${BLUE}┌────────────────────────────────────────────┐${NC}"
echo -e "${BLUE}│ 🌟 TERMUX AUTO SETUP SCRIPT v2.0 🌟        │${NC}"
echo -e "${BLUE}│     Created by Đặng Gia                    │${NC}"
echo -e "${BLUE}└────────────────────────────────────────────┘${NC}"
echo ""

# Cập nhật và nâng cấp Termux
show_loading "Khởi động cập nhật Termux"
yes | pkg update && yes | pkg upgrade -y
show_progress 20 "Cập nhật Termux" 100
echo -e "\n${GREEN}[✅] Cập nhật Termux hoàn tất!${NC}"
echo ""

# Cấp quyền truy cập bộ nhớ
show_loading "Khởi động cấp quyền lưu trữ"
echo "y" | termux-setup-storage
show_progress 10 "Cấp quyền lưu trữ" 100
echo -e "\n${GREEN}[✅] Cấp quyền lưu trữ hoàn tất!${NC}"
echo ""

# Cài đặt các gói cần thiết
show_loading "Khởi động cài đặt gói"
yes | pkg install python tsu libexpat openssl -y
show_progress 30 "Cài đặt gói" 100
echo -e "\n${GREEN}[✅] Cài đặt gói hoàn tất!${NC}"
echo ""

# Cài đặt các thư viện Python
show_loading "Khởi động cài đặt thư viện Python"
pip install requests Flask colorama aiohttp psutil crypto pycryptodome prettytable loguru rich pytz tqdm pyjwt pystyle cloudscraper
show_progress 40 "Cài đặt thư viện Python" 100
echo -e "\n${GREEN}[✅] Cài đặt thư viện Python hoàn tất!${NC}"
echo ""

# Tải file về /sdcard/Download
show_loading "Khởi động tải tdm3.py"
curl -o /sdcard/Download/tdm3.py https://raw.githubusercontent.com/Gia3010Q/termux-setup/main/tdm3.py
show_progress 10 "Tải tdm3.py" 100
echo -e "\n${GREEN}[✅] Đã tải tdm3.py!${NC}"
show_loading "Khởi động tải sn01.py"
curl -o /sdcard/Download/sn01.py https://raw.githubusercontent.com/Gia3010Q/termux-setup/main/sn01.py
show_progress 10 "Tải sn01.py" 100
echo -e "\n${GREEN}[✅] Đã tải sn01.py!${NC}"
echo ""

# Thông báo hoàn thành
echo -e "${GREEN}┌────────────────────────────────────────────┐${NC}"
echo -e "${GREEN}│ 🎉 HOÀN TẤT CÀI ĐẶT VÀ TẢI FILE! 🎉        │${NC}"
echo -e "${GREEN}│ ${BOLD}File lưu tại: /sdcard/Download${NC}        │${NC}"
echo -e "${GREEN}└────────────────────────────────────────────┘${NC}"
echo ""

# Hiển thị lệnh chạy tool
echo -e "${BLUE}${BOLD}📦 Lệnh chạy tool:${NC}"
echo -e "${YELLOW}   ➜ cd /sdcard/Download && python sn01.py${NC}"
echo -e "${YELLOW}   ➜ cd /sdcard/Download && python tdm3.py${NC}"
