#!/bin/bash
# Script tự động cài đặt Termux - Scode Auto Setup

# Định nghĩa màu sắc tối giản
WHITE='\033[1;37m'
BLUE='\033[0;34m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BG_GREEN='\033[42m'
BG_RED='\033[41m'
NC='\033[0m' # No Color

# Hàm hiển thị banner Scode màu trắng
show_start_banner() {
    clear
    echo -e "${BLUE}╔══════════════════════════════════════════════════════════╗"
    echo -e "║${WHITE} ███████╗ ██████╗ ██████╗ ██████╗ ███████╗ ${BLUE}║"
    echo -e "║${WHITE} ██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝ ${BLUE}║"
    echo -e "║${WHITE} ███████╗██║     ██║   ██║██║  ██║█████╗   ${BLUE}║"
    echo -e "║${WHITE} ╚════██║██║     ██║   ██║██║  ██║██╔══╝   ${BLUE}║"
    echo -e "║${WHITE} ███████║╚██████╗╚██████╔╝██████╔╝███████╗ ${BLUE}║"
    echo -e "║${WHITE} ╚══════╝ ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝ ${BLUE}║"
    echo -e "╠══════════════════════════════════════════════════════════╣"
    echo -e "║ ${WHITE}🚀 Scode Auto Setup ${BLUE}                                  ║"
    echo -e "║ ${WHITE}🔧 Developed by Đặng Gia ${BLUE}                            ║"
    echo -e "║ ${WHITE}📌 Version 2.0 ${BLUE}                                       ║"
    echo -e "╚══════════════════════════════════════════════════════════╝${NC}"
    echo ""
}

# Hàm hiển thị banner hoàn thành
show_success_banner() {
    clear
    echo -e "${GREEN}╔══════════════════════════════════════════════════════════╗"
    echo -e "║${WHITE} ███████╗ ██████╗ ██████╗ ██████╗ ███████╗ ${GREEN}║"
    echo -e "║${WHITE} ██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝ ${GREEN}║"
    echo -e "║${WHITE} ███████╗██║     ██║   ██║██║  ██║█████╗   ${GREEN}║"
    echo -e "║${WHITE} ╚════██║██║     ██║   ██║██║  ██║██╔══╝   ${GREEN}║"
    echo -e "║${WHITE} ███████║╚██████╗╚██████╔╝██████╔╝███████╗ ${GREEN}║"
    echo -e "║${WHITE} ╚══════╝ ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝ ${GREEN}║"
    echo -e "╠══════════════════════════════════════════════════════════╣"
    echo -e "║ ${BG_GREEN}${WHITE}   🎉 CÀI ĐẶT THÀNH CÔNG - SẴN SÀNG SỬ DỤNG! 🚀   ${NC}${GREEN}   ║"
    echo -e "╠══════════════════════════════════════════════════════════╣"
    echo -e "║ ${WHITE}🚀 Scode Auto Setup ${GREEN}                                  ║"
    echo -e "║ ${WHITE}🔧 Developed by Đặng Gia ${GREEN}                            ║"
    echo -e "║ ${WHITE}📌 Version 2.0 ${GREEN}                                       ║"
    echo -e "╚══════════════════════════════════════════════════════════╝${NC}"
    echo ""
}

# Hàm hiển thị thanh tiến trình màu xanh lá cây
show_progress() {
    local duration=$1
    local message=$2
    local icon=$3
    
    echo -ne "${BLUE}[${icon}] ${WHITE}${message} ${NC}["
    # Tạo thanh tiến trình
    for i in {1..30}; do
        echo -ne "${GREEN}▓${NC}"
        sleep $duration
    done
    echo -e "]"
}

# Hàm hiển thị trạng thái đơn giản
show_status() {
    local message=$1
    local icon=$2
    
    echo -e "${BLUE}[${icon}] ${WHITE}${message}...${NC}"
    sleep 0.2
}

# Hàm xử lý lỗi
handle_error() {
    local message=$1
    echo -e "${RED}╔══════════════════════════════════════════════════════════╗"
    echo -e "║ ${WHITE}${BG_RED}                    LỖI CÀI ĐẶT!                     ${NC}${RED}║"
    echo -e "╠══════════════════════════════════════════════════════════╣"
    echo -e "║ ${YELLOW}✖ ${message} ${RED}                               ║"
    echo -e "║ ${WHITE}Nguyên nhân có thể do:${RED}                                 ║"
    echo -e "║ ${YELLOW}• Mất kết nối Internet${RED}                                 ║"
    echo -e "║ ${YELLOW}• Hết dung lượng lưu trữ${RED}                               ║"
    echo -e "║ ${YELLOW}• Xung đột gói cài đặt${RED}                                 ║"
    echo -e "║ ${WHITE}Vui lòng kiểm tra và thử lại!${RED}                           ║"
    echo -e "╚══════════════════════════════════════════════════════════╝${NC}"
    exit 1
}

# Hàm kiểm tra lỗi sau mỗi lệnh
check_error() {
    if [ $? -ne 0 ]; then
        handle_error "$1"
    fi
}

# Hiển thị banner đầu
show_start_banner

# Cập nhật và nâng cấp Termux
show_progress 0.03 "Khởi động cập nhật hệ thống" "🔄"
show_status "Cập nhật gói hệ thống" "⏳"
pkg update -y > /dev/null 2>&1
check_error "Không thể cập nhật danh sách gói"
pkg upgrade -y > /dev/null 2>&1
check_error "Không thể nâng cấp hệ thống"
echo -e "${GREEN}[✓] Cập nhật hệ thống hoàn tất!${NC}"
echo ""

# Cấp quyền truy cập bộ nhớ
show_progress 0.02 "Yêu cầu quyền lưu trữ" "🔑"
show_status "Cấp quyền lưu trữ" "💾"
termux-setup-storage <<< "y" > /dev/null 2>&1
check_error "Không thể cấp quyền truy cập bộ nhớ"
echo -e "${GREEN}[✓] Cấp quyền lưu trữ hoàn tất!${NC}"
echo ""

# Cài đặt các gói cần thiết
show_progress 0.02 "Chuẩn bị cài đặt gói" "📦"
show_status "Cài đặt gói hệ thống" "⚙️"
pkg install -y python tsu libexpat openssl > /dev/null 2>&1
check_error "Cài đặt gói hệ thống thất bại"
echo -e "${GREEN}[✓] Cài đặt gói hệ thống hoàn tất!${NC}"
echo ""

# Cài đặt các thư viện Python
show_progress 0.01 "Thiết lập môi trường Python" "🐍"
show_status "Cài đặt thư viện Python" "📚"
pip install requests Flask colorama aiohttp psutil crypto pycryptodome prettytable loguru rich pytz tqdm pyjwt pystyle cloudscraper > /dev/null 2>&1
check_error "Cài đặt thư viện Python thất bại"
echo -e "${GREEN}[✓] Cài đặt thư viện Python hoàn tất!${NC}"
echo ""

# Tải file về /sdcard/Download
show_progress 0.01 "Kết nối kho lưu trữ" "📡"
show_status "Tải tdm3.py" "⬇️"
curl -o /sdcard/Download/tdm3.py https://raw.githubusercontent.com/Gia3010Q/termux-setup/main/tdm3.py > /dev/null 2>&1
check_error "Tải tdm3.py thất bại"
echo -e "${GREEN}[✓] Tải tdm3.py hoàn tất!${NC}"

show_status "Tải sn01.py" "⬇️"
curl -o /sdcard/Download/sn01.py https://raw.githubusercontent.com/Gia3010Q/termux-setup/main/sn01.py > /dev/null 2>&1
check_error "Tải sn01.py thất bại"
echo -e "${GREEN}[✓] Tải sn01.py hoàn tất!${NC}"

show_status "Tải ld5.py" "⬇️"
curl -o /sdcard/Download/ld5.py https://raw.githubusercontent.com/Gia3010Q/termux-setup/refs/heads/main/ld5.py > /dev/null 2>&1
check_error "Tải ld5.py thất bại"
echo -e "${GREEN}[✓] Tải ld5.py hoàn tất!${NC}"
echo ""

# Hiển thị banner hoàn thành
show_success_banner

# Hiển thị hướng dẫn sử dụng
echo -e "${BLUE}╔══════════════════════════════════════════════════════════╗"
echo -e "║ ${WHITE}${BLUE}                    🚀 LỆNH KHỞI CHẠY                    ${NC}${BLUE}║"
echo -e "╠══════════════════════════════════════════════════════════╣"
echo -e "║ ${YELLOW}1. ${WHITE}cd /sdcard/Download ${BLUE}                               ║"
echo -e "║ ${YELLOW}2. ${WHITE}python sn01.py ${BLUE}                                   ║"
echo -e "║ ${YELLOW}3. ${WHITE}python tdm3.py ${BLUE}                                  ║"
echo -e "║ ${YELLOW}4. ${WHITE}python ld5.py ${BLUE}                                    ║"
echo -e "╚══════════════════════════════════════════════════════════╝${NC}"
echo ""
echo -e "${YELLOW}💡 Mẹo: ${WHITE}Bạn có thể chạy trực tiếp bằng cách nhập lệnh đầy đủ:"
echo -e "${WHITE}   python /sdcard/Download/sn01.py"
echo ""
echo -e "${GREEN}✅ Mọi quá trình đã hoàn tất thành công!"
echo -e "${BLUE}💖 Cảm ơn bạn đã sử dụng Scode Auto Setup!${NC}"
