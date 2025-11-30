# Atomated Server Health Monitoring & Intrusion Detection System

![Linux](https://img.shields.io/badge/Linux-System_Admin-FCC624?style=for-the-badge&logo=linux)
![Bash](https://img.shields.io/badge/Bash-Scripting-4EAA25?style=for-the-badge&logo=gnu-bash)
![Python](https://img.shields.io/badge/Python-Log_Analysis-3776AB?style=for-the-badge&logo=python)
![Telegram](https://img.shields.io/badge/Telegram-Alerts-26A5E4?style=for-the-badge&logo=telegram)

## Overview
A comprehensive monitoring solution for Linux Servers developed on Ubuntu Server. This project combines **Bash scripting** for resource management and **Python** for security log analysis. It detects potential threats (like Brute-force SSH attacks) in real-time and sends alerts instantly via **Telegram Bot**.

## Features
1.  **Resource Monitoring (Bash):**
    - Checks Disk Usage % and Memory usage.
    - **Auto-Cleanup:** Automatically deletes temporary files in `/tmp` if disk usage exceeds 90%.
2.  **Security Monitoring (Python):**
    - Parses `/var/log/auth.log` using **Regex**.
    - Detects repeated `Failed password` attempts (Brute-force patterns).
    - Integrated with **Telegram API** for real-time alerting.

## Tech Stack
- **OS:** Ubuntu Server
- **Languages:** Bash Shell, Python 3
- **APIs:** Telegram Bot API
- **Tools:** Crontab (Scheduler), Regex

## Usage
### 1. Health Check Script
```bash
chmod +x src/health_check.sh
./src/health_check.sh
```
### 2. Security Monitoring Check Script
```bash
sudo pip3 install -r requirements.txt
sudo python3 src/log_monitor.py
```

## Video demo
https://github.com/user-attachments/assets/dc33467c-112b-404a-9728-6d5111bde6e2

