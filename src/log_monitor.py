import subprocess
import requests # Thư viện để gọi API
import os
import time

# --- CẤU HÌNH ---
TELEGRAM_TOKEN = "8484131804:AAFeqg-Cq6a_lO47xWfvvBSnLNMJBhU7lHk"
CHAT_ID = "8174852342"

LOG_FILE = "/var/log/auth.log"
KEYWORD = "Failed password"
THRESHOLD = 5  # Ngưỡng cảnh báo (số lần sai)

def send_telegram_alert(message):
    """Hàm gửi tin nhắn đến Telegram"""
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": f" SECURITY ALERT:\n{message}"
    }
    
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print(" Đã gửi cảnh báo lên Telegram!")
        else:
            print(f" Lỗi gửi Telegram: {response.text}")
    except Exception as e:
        print(f" Lỗi kết nối: {e}")

def check_logs():
    # 1. Kiểm tra file log có tồn tại không
    if not os.path.exists(LOG_FILE):
        print(f"Lỗi: Không tìm thấy file {LOG_FILE}")
        return

    print(f"Dang quet file {LOG_FILE} tim tu khoa '{KEYWORD}'...")

    # 2. Dùng lệnh grep đếm số dòng
    try:
        # Lệnh chạy: grep -c "Failed password" /var/log/auth.log
        cmd = f'grep -c "{KEYWORD}" {LOG_FILE}'
        
        # subprocess.check_output chạy lệnh shell và lấy kết quả trả về
        output = subprocess.check_output(cmd, shell=True)
        count = int(output.strip()) # Chuyển kết quả từ text sang số

        print(f" Phat hien: {count} lan dang nhap that bai.")

        # 3. Logic cảnh báo
        if count > THRESHOLD:
            msg = f"Phát hiện {count} lần đăng nhập thất bại trên máy chủ Ubuntu!\nHãy kiểm tra ngay!"
            send_telegram_alert(msg)
        else:
            print(" Hệ thống an toàn (Số lần sai dưới ngưỡng).")

    except subprocess.CalledProcessError:
        # grep trả về lỗi nếu không tìm thấy dòng nào (count = 0)
        print(" Không có lần đăng nhập sai nào (Count = 0).")

if __name__ == "__main__":
    check_logs()
