#!/usr/bin/env bash

# System Info Script - Sprint 1

kv() { printf "%s: %s\n" "$1" "$2"; }


echo "=== OS & Kernel === "


#Host

HOSTNAME_VAL="$(hostname)"
kv "Host" "$HOSTNAME_VAL"

#Kernel

KERNEL_VAL="$(uname -r)"
kv "Kernel" "$KERNEL_VAL"

#Arch

ARCH_VAL="$(uname -m)"
kv "Arch" "$ARCH_VAL"

if command -v lsb_release >/dev/null 2>&1; then
   DISTRO_VAL="$(lsb_release -ds 2>/dev/null)"
else
  if [-r /etc/os-release ]; then
    ./etc/os-release
    DISTRO_VAL ="$NAME $VERSION"
  else
    DISTRO_VAL="OS info not found"
  fi
fi
kv "Distro" "$DISTRO_VAL"

#Date and Time

DATE_VAL="$(date '+%Y-%m-%d %H:%M:%S')"
kv "Date/Time" "$DATE_VAL"


#CPU Model

CPU_VAL="$(lscpu | grep -m 1 'Model name:' | sed 's/Model name:\s* //')"
kv "CPU" "$CPU_VAL"

#RAM Total
RAM_VAL="$(free -h | awk '/^Mem:/ {print $2}')"
kv "RAM Total" "$RAM_VAL"

#Disk Size
DISK_VAL="$(df -h / | awk 'NR==2 {print $2}')"
kv "Disk Size" "$DISK_VAL"

echo "====Network Info==="

#IPv4 διεύθυνση

IP4="$(ip -4 addr show scope global | awk '/inet / {print $2}' | cut -d/ -f1 | head -n1)"
GATEWAY="$(ip route | awk '/^default/ {print $3; exit}')"

#DNS servers

if command -v resolvectl >/dev/null 2>&1; then
  DNS="$(resolvectl status \
      | awk '/DNS Servers:/ {for(i=3;i<=NF;i++) print $i}' \
      | sort -u \
      | paste -sd ' ' -)"
else
  DNS="$(awk '/^nameserver/ {print $2}' /etc/resolv.conf \
      | grep -v '^127\.0\.0\.53$' \
      | paste -sd ' ' -)"
fi

IP4="${IP4:-N/A}"
GATEWAY="${GATEWAY:-N/A}"
DNS="${DNS:-N/A}"

kv "IP (v4)" "$IP4"
kv "Gateway" "$GATEWAY"
kv "DNS" "$DNS"


echo "=== System Status ==="

# Uptime
UP_VAL="$(uptime -p 2>/dev/null || true)"
# fallback αν για κάποιο λόγο δεν υπάρχει -p
[ -z "$UP_VAL" ] && UP_VAL="$(uptime | awk -F'up ' '{print $2}' | cut -d, -f1)"
kv "Uptime" "$UP_VAL"

# Logged-in users (μοναδικά ονόματα)
USERS_VAL="$(who | awk '{print $1}' | sort -u | paste -sd ' ' -)"
USERS_VAL="${USERS_VAL:-None}"
kv "Users" "$USERS_VAL"

echo "=== Top Processes ==="

# Top 5 σε χρήση CPU
TOP_CPU="$(ps aux --sort=-%cpu | awk 'NR==1 || NR<=6 {printf "%-8s %-20s %5s%% %s\n", $1,$11,$3,$2}' )"
# Top 5 σε χρήση RAM
TOP_MEM="$(ps aux --sort=-%mem | awk 'NR==1 || NR<=6 {printf "%-8s %-20s %5s%% %s\n", $1,$11,$4,$2}' )"

echo "--- by CPU ---"
printf "%s\n" "$TOP_CPU"
echo "--- by MEM ---"
printf "%s\n" "$TOP_MEM"




