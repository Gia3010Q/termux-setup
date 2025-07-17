#!/bin/bash
# Script tự động cài đặt Termux - Scode Premium Edition

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

# Hàm hiển thị banner Scode nhiều màu sắc
show_banner() {
    clear
    echo -e "${BRIGHT_MAGENTA}╔══════════════════════════════════════════════════════════╗"
    echo -e "║${BRIGHT_CYAN} ███████╗${BRIGHT_GREEN} ██████╗${BRIGHT_YELLOW} ██████╗${BRIGHT_BLUE} ██████╗${BRIGHT_MAGENTA} ███████╗${BRIGHT_MAGENTA} ║"
    echo -e "║${BRIGHT_CYAN} ██╔════╝${BRIGHT_GREEN}██╔════╝${BRIGHT_YELLOW}██╔═══██╗${BRIGHT_BLUE}██╔══██╗${BRIGHT_MAGENTA}██╔════╝${BRIGHT_MAGENTA} ║"
    echo -e "║${BRIGHT_CYAN} ███████╗${BRIGHT_GREEN}██║     ${BRIGHT_YELLOW}██║   ██║${BRIGHT_BLUE}██║  ██║${BRIGHT_MAGENTA}█████╗  ${BRIGHT_MAGENTA} ║"
    echo -e "║${BRIGHT_CYAN} ╚════██║${BRIGHT_GREEN}██║     ${BRIGHT_YELLOW}██║   ██║${BRIGHT_BLUE}██║  ██║${BRIGHT_MAGENTA}██╔══╝  ${BRIGHT_MAGENTA} ║"
    echo -e "║${BRIGHT_CYAN} ███████║${BRIGHT_GREEN}╚██████╗${BRIGHT_YELLOW}╚██████╔╝${BRIGHT_BLUE}██████╔╝${BRIGHT_MAGENTA}███████╗${BRIGHT_MAGENTA} ║"
    echo -e "║${BRIGHT_CYAN} ╚══════╝${BRIGHT_GREEN} ╚═════╝ ${BRIGHT_YELLOW}╚═════╝ ${BRIGHT_BLUE}╚═════╝ ${BRIGHT_MAGENTA}╚══════╝${BRIGHT_MAGENTA} ║"
    echo -e "╠══════════════════════════════════════════════════════════╣"
    echo -e "║ ${BRIGHT_CYAN}🚀 TERMUX AUTO SETUP - ${BRIGHT_GREEN}SCODE PREMIUM ${BRIGHT_YELLOW}EDITION ${BRIGHT_MAGENTA}  ║"
    echo -e "║ ${BRIGHT_BLUE}🔧 Developed by Đặng Gia - ${BRIGHT_YELLOW}Version 2.0 ${BRIGHT_MAGENTA}       ║"
    echo -e "╚══════════════════════════════════════════════════════════╝${NC}"
    echo ""
}

# Hàm hiển thị thanh tiến trình màu xanh lá cây
show_progress() {
    local duration=$1
    local message=$2
    local icon=$3
    
    echo -ne "${BRIGHT_CYAN}[${icon}] ${BRIGHT_WHITE}${message} ${NC}["
    # Tạo thanh tiến trình với gradient màu xanh lá cây
    for i in {1..30}; do
        if [ $i -le 10 ]; then
            color="${BRIGHT_BLACK}"
        elif [ $i -le 20 ]; then
            color="${GREEN}"
        else
            color="${BRIGHT_GREEN}"
        fi
        
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
    sleep 0.2
}

# Hàm xử lý lỗi
handle_error() {
    local message=$1
    echo -e "${BRIGHT_RED}╔══════════════════════════════════════════════════════════╗"
    echo -e "║ ${BRIGHT_WHITE}${BG_RED}                    LỖI CÀI ĐẶT!                     ${NC}${BRIGHT_RED}║"
    echo -e "╠══════════════════════════════════════════════════════════╣"
    echo -e "║ ${BRIGHT_YELLOW}✖ ${message} ${BRIGHT_RED}                               ║"
    echo -e "║ ${BRIGHT_WHITE}Nguyên nhân có thể do:${BRIGHT_RED}                                 ║"
    echo -e "║ ${BRIGHT_YELLOW}• Mất kết nối Internet${BRIGHT_RED}                                 ║"
    echo -e "║ ${BRIGHT_YELLOW}• Hết dung lượng lưu trữ${BRIGHT_RED}                               ║"
    echo -e "║ ${BRIGHT_YELLOW}• Xung đột gói cài đặt${BRIGHT_RED}                                 ║"
    echo -e "║ ${BRIGHT_WHITE}Vui lòng kiểm tra và thử lại!${BRIGHT_RED}                           ║"
    echo -e "╚══════════════════════════════════════════════════════════╝${NC}"
    exit 1
}

# Hàm kiểm tra lỗi sau mỗi lệnh
check_error() {
    if [ $? -ne 0 ]; then
        handle_error "$1"
    fi
}

# Hiển thị banner
show_banner

# Cập nhật và nâng cấp Termux
show_progress 0.03 "Khởi động cập nhật hệ thống" "🔄"
show_status "Cập nhật gói hệ thống" "⏳" $BRIGHT_CYAN
pkg update -y > /dev/null 2>&1
check_error "Không thể cập nhật danh sách gói"
pkg upgrade -y > /dev/null 2>&1
check_error "Không thể nâng cấp hệ thống"
echo -e "${BRIGHT_GREEN}[✓] Cập nhật hệ thống hoàn tất!${NC}"
echo ""

# Cấp quyền truy cập bộ nhớ
show_progress 0.02 "Yêu cầu quyền lưu trữ" "🔑"
show_status "Cấp quyền lưu trữ" "💾" $BRIGHT_YELLOW
termux-setup-storage <<< "y" > /dev/null 2>&1
check_error "Không thể cấp quyền truy cập bộ nhớ"
echo -e "${BRIGHT_GREEN}[✓] Cấp quyền lưu trữ hoàn tất!${NC}"
echo ""

# Cài đặt các gói cần thiết
show_progress 0.02 "Chuẩn bị cài đặt gói" "📦"
show_status "Cài đặt gói hệ thống" "⚙️" $BRIGHT_BLUE
pkg install -y python tsu libexpat openssl > /dev/null 2>&1
check_error "Cài đặt gói hệ thống thất bại"
echo -e "${BRIGHT_GREEN}[✓] Cài đặt gói hệ thống hoàn tất!${NC}"
echo ""

# Cài đặt các thư viện Python
show_progress 0.01 "Thiết lập môi trường Python" "🐍"
show_status "Cài đặt thư viện Python" "📚" $BRIGHT_MAGENTA
pip install requests Flask colorama aiohttp psutil crypto pycryptodome prettytable loguru rich pytz tqdm pyjwt pystyle cloudscraper > /dev/null 2>&1
check_error "Cài đặt thư viện Python thất bại"
echo -e "${BRIGHT_GREEN}[✓] Cài đặt thư viện Python hoàn tất!${NC}"
echo ""

# Tải file về /sdcard/Download
show_progress 0.01 "Kết nối kho lưu trữ" "📡"
show_status "Tải tdm3.py" "⬇️" $BRIGHT_CYAN
curl -o /sdcard/Download/tdm3.py https://raw.githubusercontent.com/Gia3010Q/termux-setup/main/tdm3.py > /dev/null 2>&1
check_error "Tải tdm3.py thất bại"
echo -e "${BRIGHT_GREEN}[✓] Tải tdm3.py hoàn tất!${NC}"

show_status "Tải sn01.py" "⬇️" $BRIGHT_MAGENTA
curl -o /sdcard/Download/sn01.py https://raw.githubusercontent.com/Gia3010Q/termux-setup/main/sn01.py > /dev/null 2>&1
check_error "Tải sn01.py thất bại"
echo -e "${BRIGHT_GREEN}[✓] Tải sn01.py hoàn tất!${NC}"

show_status "Tải ld5.py" "⬇️" $BRIGHT_YELLOW
curl -o /sdcard/Download/ld5.py https://raw.githubusercontent.com/Gia3010Q/termux-setup/refs/heads/main/ld5.py > /dev/null 2>&1
check_error "Tải ld5.py thất bại"
echo -e "${BRIGHT_GREEN}[✓] Tải ld5.py hoàn tất!${NC}"
echo ""

# Màn hình hoàn thành
show_banner
echo -e "${BRIGHT_GREEN}╔══════════════════════════════════════════════════════════╗"
echo -e "║ ${BRIGHT_WHITE}${BG_GREEN}         🎉 CÀI ĐẶT THÀNH CÔNG - SẴN SÀNG SỬ DỤNG! ${NC}${BRIGHT_GREEN}       ║"
echo -e "╠══════════════════════════════════════════════════════════╣"
echo -e "║ ${BRIGHT_YELLOW}███████╗${BRIGHT_GREEN} ██████╗${BRIGHT_CYAN} ██████╗${BRIGHT_BLUE} ██████╗${BRIGHT_MAGENTA} ███████╗${BRIGHT_GREEN} ║"
echo -e "║ ${BRIGHT_YELLOW}██╔════╝${BRIGHT_GREEN}██╔════╝${BRIGHT_CYAN}██╔═══██╗${BRIGHT_BLUE}██╔══██╗${BRIGHT_MAGENTA}██╔════╝${BRIGHT_GREEN} ║"
echo -e "║ ${BRIGHT_YELLOW}███████╗${BRIGHT_GREEN}██║     ${BRIGHT_CYAN}██║   ██║${BRIGHT_BLUE}██║  ██║${BRIGHT_MAGENTA}█████╗  ${BRIGHT_GREEN} ║"
echo -e "║ ${BRIGHT_YELLOW}╚════██║${BRIGHT_GREEN}██║     ${BRIGHT_CYAN}██║   ██║${BRIGHT_BLUE}██║  ██║${BRIGHT_MAGENTA}██╔══╝  ${BRIGHT_GREEN} ║"
echo -e "║ ${BRIGHT_YELLOW}███████║${BRIGHT_GREEN}╚██████╗${BRIGHT_CYAN}╚██████╔╝${BRIGHT_BLUE}██████╔╝${BRIGHT_MAGENTA}███████╗${BRIGHT_GREEN} ║"
echo -e "║ ${BRIGHT_YELLOW}╚══════╝${BRIGHT_GREEN} ╚═════╝ ${BRIGHT_CYAN}╚═════╝ ${BRIGHT_BLUE}╚═════╝ ${BRIGHT_MAGENTA}╚══════╝${BRIGHT_GREEN} ║"
echo -e "╠══════════════════════════════════════════════════════════╣"
echo -e "║ ${BRIGHT_CYAN}🚀 Scode Auto Setup - ${BRIGHT_YELLOW}Premium Edition ${BRIGHT_GREEN}${BRIGHT_GREEN}          ║"
echo -e "║ ${BRIGHT_MAGENTA}🔧 Phiên bản 2.0 - ${BRIGHT_BLUE}© 2023 Đặng Gia ${BRIGHT_GREEN}              ║"
echo -e "╚══════════════════════════════════════════════════════════╝${NC}"
echo ""
echo -e "${BRIGHT_BLUE}╔══════════════════════════════════════════════════════════╗"
echo -e "║ ${BRIGHT_WHITE}${BG_BLUE}                    🚀 LỆNH KHỞI CHẠY                    ${NC}${BRIGHT_BLUE}║"
echo -e "╠══════════════════════════════════════════════════════════╣"
echo -e "║ ${BRIGHT_YELLOW}1. ${BRIGHT_CYAN}cd /sdcard/Download ${BRIGHT_BLUE}                               ║"
echo -e "║ ${BRIGHT_YELLOW}2. ${BRIGHT_GREEN}python sn01.py ${BRIGHT_BLUE}                                   ║"
echo -e "║ ${BRIGHT_YELLOW}3. ${BRIGHT_MAGENTA}python tdm3.py ${BRIGHT_BLUE}                                  ║"
echo -e "║ ${BRIGHT_YELLOW}4. ${BRIGHT_CYAN}python ld5.py ${BRIGHT_BLUE}                                    ║"
echo -e "╚══════════════════════════════════════════════════════════╝${NC}"
echo ""
echo -e "${BRIGHT_MAGENTA}💡 Mẹo: ${BRIGHT_WHITE}Bạn có thể chạy trực tiếp bằng cách nhập lệnh đầy đủ:"
echo -e "${BRIGHT_YELLOW}   python /sdcard/Download/sn01.py"
echo ""
echo -e "${BRIGHT_GREEN}✅ Mọi quá trình đã hoàn tất thành công!"
echo -e "${BRIGHT_CYAN}💖 Cảm ơn bạn đã sử dụng Scode Premium Auto Setup!${NC}"
