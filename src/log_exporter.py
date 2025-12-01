import time
import subprocess
import os
from prometheus_client import start_http_server, Gauge

# --- CẤU HÌNH ---
LOG_FILE = "/var/log/auth.log"
KEYWORD = "Failed password"
EXPORTER_PORT = 8000  # Cổng để Prometheus chọc vào

# --- ĐỊNH NGHĨA METRIC ---
# Gauge: Là loại biểu đồ đo lường con số có thể tăng giảm
# Tên metric: ssh_failed_login_attempts_total
ssh_failures = Gauge('ssh_failed_login_attempts_total', 'Number of failed SSH login attempts detected in auth.log')

def count_logs():
    if not os.path.exists(LOG_FILE):
        return 0
    try:
        # Đếm tổng số dòng chứa lỗi trong file log
        cmd = f'grep -c "{KEYWORD}" {LOG_FILE}'
        output = subprocess.check_output(cmd, shell=True)
        return int(output.strip())
    except subprocess.CalledProcessError:
        return 0

def main():
    # 1. Khởi động Web Server nhỏ để Prometheus scrape
    print(f" Custom Exporter đang chạy tại port {EXPORTER_PORT}...")
    start_http_server(EXPORTER_PORT)

    # 2. Vòng lặp cập nhật số liệu
    while True:
        count = count_logs()
        
        # Cập nhật giá trị vào Metric
        ssh_failures.set(count)
        
        print(f"Update Metric: {count} failures")
        
        # Nghỉ 15 giây quét 1 lần
        time.sleep(15)

if __name__ == "__main__":
    main()
