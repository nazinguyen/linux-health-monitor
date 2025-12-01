#  Linux Server Observability Stack (V3.0)

![Prometheus](https://img.shields.io/badge/Prometheus-Monitoring-E6522C?style=for-the-badge&logo=prometheus)
![Grafana](https://img.shields.io/badge/Grafana-Dashboard-F46800?style=for-the-badge&logo=grafana)
![Docker](https://img.shields.io/badge/Docker-Container-2496ED?style=for-the-badge&logo=docker)
![Python](https://img.shields.io/badge/Python-Custom_Exporter-3776AB?style=for-the-badge&logo=python)

##  Overview
This project upgrades the traditional monitoring scripts to a full **Observability Stack**. It uses **Prometheus** for metrics collection, **Grafana** for visualization, and **Node Exporter** for hardware monitoring. Additionally, a **Custom Python Exporter** was developed to expose security logs (SSH Brute-force attempts) as Prometheus metrics.

## ️ Architecture
1.  **Node Exporter:** Collects CPU, RAM, Disk metrics.
2.  **Custom Python Exporter:** Parses `/var/log/auth.log` and exposes `ssh_failed_login_attempts_total` metric on port `8000`.
3.  **Prometheus:** Scrapes data from both exporters.
4.  **Grafana:** Visualizes data on a unified Dashboard.

## ️ Tech Stack
- **Infrastructure:** Docker Compose
- **Monitoring:** Prometheus, Grafana, Node Exporter
- **Custom Logic:** Python (prometheus-client library)
- **OS:** Ubuntu Server

##  Deployment

### 1. Prerequisites
- Docker & Docker Compose installed.

### 2. Start the Stack
```bash
docker compose up -d --build
```

### 3. Access Dashboards
Grafana: http://localhost:3000 (Default user/pass: admin/admin)

Prometheus: http://localhost:9090

Metric Endpoint: http://localhost:8000

### Screenshots
Unified Dashboard (System + Security)
<img width="1920" height="1097" alt="image" src="https://github.com/user-attachments/assets/c399f0c6-87e3-451c-8f5a-7c1b8bd6fdb4" />

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
Link youtube: https://youtu.be/A_skscelId0


