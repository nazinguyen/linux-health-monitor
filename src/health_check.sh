#!/bin/bash
# Dòng trên gọi là Shebang, báo cho OS biết dùng trình biên dịch nào

echo "======= SERVER HEALTH CHECK ======="
date

# 1. Kiểm tra dung lượng đĩa (Disk Usage)
echo "[1] Checking Disk Space..."
# df -h: disk free human-readable | grep ra dòng root
DISK_USAGE=$(df -h / | grep / | awk '{print $5}' | sed 's/%//g')

if [ "$DISK_USAGE" -gt 80 ]; then
    echo " WARNING: Disk is full! Usage: $DISK_USAGE%"
else
    echo " Disk is OK. Usage: $DISK_USAGE%"
fi

# 2. Kiểm tra RAM (Memory Usage)
echo "[2] Checking RAM..."
# free -m: hiện RAM theo MB
TOTAL_RAM=$(free -m | grep Mem | awk '{print $2}')
USED_RAM=$(free -m | grep Mem | awk '{print $3}')
#Bash chỉ tính toán số nguyên
PERCENT_RAM=$(( 100 * USED_RAM / TOTAL_RAM ))

echo "  - Total: ${TOTAL_RAM}MB"
echo "  - Used: ${USED_RAM}MB ($PERCENT_RAM%)"

if [ "$PERCENT_RAM" -gt 90 ]; then
    echo " DANGER: RAM is critical!"
else
    echo " RAM is stable."
fi

echo "===================================="

