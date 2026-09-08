#!/bin/bash
# Otimiza o uso de memória RAM e processamento
if [ "$EUID" -ne 0 ]; then echo "Rode como root"; exit 1; fi

if ! grep -q "vm.swappiness" /etc/sysctl.conf; then
    echo "vm.swappiness=10" >> /etc/sysctl.conf
else
    sed -i 's/vm.swappiness=.*/vm.swappiness=10/g' /etc/sysctl.conf
fi
sysctl -p > /dev/null

WIFI_CONF="/etc/NetworkManager/conf.d/default-wifi-powersave-on.conf"
if [ -f "$WIFI_CONF" ]; then
    sed -i 's/power_save=3/power_save=2/g' $WIFI_CONF
    systemctl restart NetworkManager
fi
echo -e "\033[0;32m[OK] Swappiness e economia de Wi-Fi ajustados!\033[0m"
