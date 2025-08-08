# System Info Script (Bash) — v1.0

A small and practical **system info reporter** written in Bash.  
Displays OS, hardware, network, uptime, logged-in users, and top processes.  
Perfect for quick diagnostics or as a portfolio-friendly Linux scripting project.

---

## 📌 Features
- **OS & Kernel**: Hostname, Kernel, Architecture, Distro, Date/Time
- **Hardware**: CPU model, total RAM, root disk size
- **Network**: IPv4, default gateway, DNS (supports systemd-resolved)
- **Status**: Uptime (pretty format), logged-in users
- **Top processes**: by CPU and by MEM (top 5), clean formatting

---

## 📂 Requirements
- Bash (>= 4)
- `coreutils` (`df`, `free`, `uname`)
- `iproute2` (`ip`)
- `procps` (`ps`, `uptime`)
- (Optional) `lsb_release` for better distro detection

---

## 🚀 Usage
1. Clone the repo:
   ```bash
   git clone https://github.com/<your-username>/sysinfo-script.git
   cd sysinfo-script
