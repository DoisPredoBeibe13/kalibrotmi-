#!/bin/bash
# Configura DNS rápido sem quebrar o TryHackMe/VPN
if [ "$EUID" -ne 0 ]; then echo "Rode como root"; exit 1; fi

DHCP_CONF="/etc/dhcp/dhclient.conf"
if [ -f "$DHCP_CONF" ]; then
    sed -i '/prepend domain-name-servers/d' $DHCP_CONF
    echo 'prepend domain-name-servers 1.1.1.1, 8.8.8.8;' >> $DHCP_CONF
fi

cat << EOF > /etc/resolv.conf
search local
nameserver 1.1.1.1
nameserver 8.8.8.8
nameserver fe80::9a2a:aff:fe8d:dfcb%eth0
EOF

systemctl restart NetworkManager
echo -e "\033[0;32m[OK] DNS focado em VPN e TryHackMe configurado!\033[0m"
