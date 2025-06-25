#!/bin/bash
# Script tự động cài đặt Termux và tải file tdm3.py, sn01.py

# Định nghĩa màu sắc
GREEN='\033[1;32m'
YELLOW='\033[1;33m'
BLUE='\033[1;34m'
CYAN='\033[1;36m'
BOLD='\033[1m'
NC='\033[0m' # No Color

# Hàm hiển thị thanh tiến trình (một dòng với hiệu ứng chạy dần)
show_progress() {
    local total=$1
    local message=$2
    local percent=$3
    local filled=$((percent / 3.333))  # 30 ký tự
    local empty=$((30 - filled))
    local bar=""
    for ((i=0; i<filled; i++)); do bar="${bar}■"; done
    for ((i=0; i<empty; i++)); do bar="${bar}─"; done
    echo -e "\r${CYAN}[⚡] ${message}: [${GREEN}${bar}${NC}] ${YELLOW}${percent}%${NC} "
    if [ $percent -eq 100 ]; then echo -e "${GREEN} →✅${NC}"; fi
    sleep 0.1  # Thêm độ trễ để thấy hiệu ứng
}

# Hàm hiển thị hiệu ứng loading
show_loading() {
    local message=$1
    echo -ne "${BLUE}[★] ${message} ${NC}"
    for i in {1..3}; do
        echo -ne "."
        sleep 0.1
    done
    echo -ne "\r\033[K"
}

# Hàm hiển thị tiến trình giả lập để tạo hiệu ứng
simulate_progress() {
    local message=$1
    for ((p=0; p<=100; p+=10)); do
        show_progress 100 "$message" $p
        sleep 0.2  # Tăng độ trễ để thấy rõ hơn
    done
    show_progress 100 "$message" 100
}

# Hiển thị tiêu đề trong khung đẹp với Developed by xuống dưới
echo -e "${BLUE}╒════════════════════════════════════════════╕${NC}"
echo -e "${CYAN}│ ${BOLD}★ TERMUX AUTO SETUP SCRIPT v2.1 ★${BOLD}     │${NC}"
echo -e "${CYAN}│ ${BOLD}Developed by Gia3010Q${BOLD}                │${NC}"
echo -e "${BLUE}╘════════════════════════════════════════════╛${NC}"
echo ""

# Cập nhật và nâng cấp Termux
show_loading "Khởi động cập nhật Termux"
simulate_progress "Cập nhật Termux" &
yes | pkg update > /dev/null 2>&1 && yes | pkg upgrade -y > /dev/null 2>&1
wait
echo -e "\n${GREEN}[✅] Cập nhật Termux hoàn tất!${NC}"
echo ""

# Cấp quyền truy cập bộ nhớ
show_loading "Khởi động cấp quyền lưu trữ"
simulate_progress "Cấp quyền lưu trữ" &
echo "y" | termux-setup-storage > /dev/null 2>&1
wait
echo -e "\n${GREEN}[✅] Cấp quyền lưu trữ hoàn tất!${NC}"
echo ""

# Cài đặt các gói cần thiết
show_loading "Khởi động cài đặt gói"
simulate_progress "Cài đặt gói" &
yes | pkg install python tsu libexpat openssl -y > /dev/null 2>&1
wait
echo -e "\n${GREEN}[✅] Cài đặt gói hoàn tất!${NC}"
echo ""

# Cài đặt các thư viện Python
show_loading "Khởi động cài đặt thư viện Python"
simulate_progress "Cài đặt thư viện Python" &
pip install requests Flask colorama aiohttp psutil crypto pycryptodome prettytable loguru rich pytz tqdm pyjwt pystyle cloudscraper > /dev/null 2>&1
wait
echo -e "\n${GREEN}[✅] Cài đặt thư viện Python hoàn tất!${NC}"
echo ""

# Tải file về /sdcard/Download
show_loading "Khởi động tải tdm3.py"
simulate_progress "Tải tdm3.py" &
curl -o /sdcard/Download/tdm3.py https://raw.githubusercontent.com/Gia3010Q/termux-setup/main/tdm3.py > /dev/null 2>&1
wait
echo -e "\n${GREEN}[✅] Đã tải tdm3.py!${NC}"
show_loading "Khởi động tải sn01.py"
simulate_progress "Tải sn01.py" &
curl -o /sdcard/Download/sn01.py https://raw.githubusercontent.com/Gia3010Q/termux-setup/main/sn01.py > /dev/null 2>&1
wait
echo -e "\n${GREEN}[✅] Đã tải sn01.py!${NC}"
echo ""

# Màn hình hoàn thành với banner
clear
echo -e "${BLUE}╒════════════════════════════════════════════╕${NC}"
echo -e "${CYAN}│ ${BOLD}★ TERMUX AUTO SETUP SCRIPT v2.1 ★${BOLD}     │${NC}"
echo -e "${CYAN}│ ${BOLD}Developed by Gia3010Q${BOLD}                │${NC}"
echo -e "${BLUE}╘════════════════════════════════════════════╛${NC}"
echo -e "${CYAN}╒════════════════════════════════════════════╕${NC}"
echo -e "${GREEN}│ ${BOLD}Setup Hoàn Tất Có Thể Sử Dụng Ngay${BOLD}    │${NC}"
echo -e "${CYAN}╘════════════════════════════════════════════╛${NC}"
echo -e "${BLUE}📦 Khởi động tool với lệnh sau:${NC}"
echo -e "${YELLOW}   ➜ cd /sdcard/Download && python sn01.py${NC}"
echo -e "${YELLOW}   ➜ cd /sdcard/Download && python tdm3.py${NC}"
