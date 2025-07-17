#!/bin/bash
# Script tự động cài đặt Termux - Scode Edition

# Định nghĩa màu sắc nâng cao
BLACK='\033[0;30m'
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
MAGENTA='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[0;37m'
BRIGHT_BLACK='\033[1;30m'
BRIGHT_RED='\033[1;31m'
BRIGHT_GREEN='\033[1;32m'
BRIGHT_YELLOW='\033[1;33m'
BRIGHT_BLUE='\033[1;34m'
BRIGHT_MAGENTA='\033[1;35m'
BRIGHT_CYAN='\033[1;36m'
BRIGHT_WHITE='\033[1;37m'
BG_RED='\033[41m'
BG_GREEN='\033[42m'
BG_YELLOW='\033[43m'
BG_BLUE='\033[44m'
BG_MAGENTA='\033[45m'
BG_CYAN='\033[46m'
NC='\033[0m' # No Color

# Hàm hiển thị banner Scode
show_banner() {
    clear
    echo -e "${BRIGHT_BLUE}"
    echo -e "███████╗ ██████╗ ██████╗ ██████╗ ███████╗"
    echo -e "██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝"
    echo -e "███████╗██║     ██║   ██║██║  ██║█████╗  "
    echo -e "╚════██║██║     ██║   ██║██║  ██║██╔══╝  "
    echo -e "███████║╚██████╗╚██████╔╝██████╔╝███████╗"
    echo -e "╚══════╝ ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝"
    echo -e "${NC}"
    echo -e "${BRIGHT_MAGENTA}╔════════════════════════════════════════════╗"
    echo -e "║   ${BRIGHT_CYAN}🚀 TERMUX AUTO SETUP - SCODE EDITION ${BRIGHT_MAGENTA}   ║"
    echo -e "║   ${BRIGHT_YELLOW}🔧 Developed by Đặng Gia - Version 1.2 ${BRIGHT_MAGENTA}  ║"
    echo -e "╚════════════════════════════════════════════╝${NC}"
    echo ""
}

# Hàm hiển thị thanh tiến trình
show_progress() {
    local duration=$1
    local message=$2
    local color=$3
    local icon=$4
    
    echo -ne "${color}[${icon}] ${message} ${NC}["
    for i in {1..20}; do
        echo -ne "${color}▓${NC}"
        sleep $duration
    done
    echo -e "]"
}

# Hàm hiển thị trạng thái đơn giản
show_status() {
    local message=$1
    local icon=$2
    local color=$3
    
    echo -e "${color}[${icon}] ${message}...${NC}"
    sleep 0.3
    echo -e "${BRIGHT_GREEN}[✓] ${message} hoàn tất!${NC}"
}

# Hiển thị banner
show_banner

# Cập nhật và nâng cấp Termux
show_progress 0.05 "Khởi động cập nhật hệ thống" $BRIGHT_BLUE "🔄"
show_status "Cập nhật gói hệ thống" "⏳" $BRIGHT_CYAN
yes | pkg update > /dev/null 2>&1 && yes | pkg upgrade -y > /dev/null 2>&1
echo ""

# Cấp quyền truy cập bộ nhớ
show_progress 0.03 "Yêu cầu quyền lưu trữ" $BRIGHT_MAGENTA "🔑"
show_status "Cấp quyền lưu trữ" "💾" $BRIGHT_YELLOW
echo "y" | termux-setup-storage > /dev/null 2>&1
echo ""

# Cài đặt các gói cần thiết
show_progress 0.04 "Chuẩn bị cài đặt gói" $BRIGHT_YELLOW "📦"
show_status "Cài đặt gói hệ thống" "⚙️" $BRIGHT_BLUE
yes | pkg install python tsu libexpat openssl -y > /dev/null 2>&1
echo ""

# Cài đặt các thư viện Python
show_progress 0.02 "Thiết lập môi trường Python" $BRIGHT_CYAN "🐍"
show_status "Cài đặt thư viện Python" "📚" $BRIGHT_MAGENTA
pip install requests Flask colorama aiohttp psutil crypto pycryptodome prettytable loguru rich pytz tqdm pyjwt pystyle cloudscraper > /dev/null 2>&1
echo ""

# Tải file về /sdcard/Download
show_progress 0.01 "Kết nối kho lưu trữ" $BRIGHT_GREEN "📡"
show_status "Tải tdm3.py" "⬇️" $BRIGHT_CYAN
curl -o /sdcard/Download/tdm3.py https://raw.githubusercontent.com/Gia3010Q/termux-setup/main/tdm3.py > /dev/null 2>&1
show_status "Tải sn01.py" "⬇️" $BRIGHT_MAGENTA
curl -o /sdcard/Download/sn01.py https://raw.githubusercontent.com/Gia3010Q/termux-setup/main/sn01.py > /dev/null 2>&1
show_status "Tải ld5.py" "⬇️" $BRIGHT_YELLOW
curl -o /sdcard/Download/ld5.py https://raw.githubusercontent.com/Gia3010Q/termux-setup/refs/heads/main/ld5.py > /dev/null 2>&1
echo ""

# Màn hình hoàn thành với banner Scode
show_banner
echo -e "${BRIGHT_BLUE}"
echo -e "███████╗ ██████╗ ██████╗ ██████╗ ███████╗"
echo -e "██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝"
echo -e "███████╗██║     ██║   ██║██║  ██║█████╗  "
echo -e "╚════██║██║     ██║   ██║██║  ██║██╔══╝  "
echo -e "███████║╚██████╗╚██████╔╝██████╔╝███████╗"
echo -e "╚══════╝ ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝"
echo -e "${NC}"
echo -e "${BRIGHT_MAGENTA}╔════════════════════════════════════════════╗"
echo -e "║   ${BRIGHT_CYAN}🚀 CÀI ĐẶT THÀNH CÔNG - SẴN SÀNG SỬ DỤNG ${BRIGHT_MAGENTA}   ║"
echo -e "║   ${BRIGHT_YELLOW}🔧 Scode Auto Setup - Phiên bản 1.2 ${BRIGHT_MAGENTA}       ║"
echo -e "╚════════════════════════════════════════════╝${NC}"
echo ""
echo -e "${BRIGHT_GREEN}╔════════════════════════════════════════════╗"
echo -e "║ ${BRIGHT_WHITE}${BG_BLUE}              🚀 LỆNH KHỞI CHẠY ${NC}${BRIGHT_GREEN}             ║"
echo -e "╠════════════════════════════════════════════╣"
echo -e "║ ${BRIGHT_CYAN} cd /sdcard/Download ${BRIGHT_GREEN}                       ║"
echo -e "║ ${BRIGHT_YELLOW} python sn01.py ${BRIGHT_GREEN}                          ║"
echo -e "║ ${BRIGHT_MAGENTA} python tdm3.py ${BRIGHT_GREEN}                         ║"
echo -e "║ ${BRIGHT_CYAN} python ld5.py ${BRIGHT_GREEN}                            ║"
echo -e "╚════════════════════════════════════════════╝${NC}"
echo ""
echo -e "${BRIGHT_YELLOW}🔔 Lưu ý: ${BRIGHT_WHITE}Luôn cập nhật script để nhận tính năng mới nhất!"
echo -e "${BRIGHT_MAGENTA}💖 Cảm ơn đã sử dụng ${BRIGHT_CYAN}Scode ${BRIGHT_MAGENTA}Auto Setup!${NC}"
