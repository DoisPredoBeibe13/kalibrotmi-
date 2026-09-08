#!/bin/bash

# Cores para o terminal
VERDE='\033[0;32m'
VERMELHO='\033[0;31m'
AZUL='\033[0;34m'
NC='\033[0m' # Sem cor

clear
echo -e "${AZUL}==================================================${NC}"
echo -e "${VERDE}    SCRIPT DE OTIMIZAÇÃO KALI LINUX (BRASIL)      ${NC}"
echo -e "${AZUL}==================================================${NC}"

# Verificar se está rodando como root
if [ "$EUID" -ne 0 ]; then
  echo -e "${VERMELHO}[ERRO] Por favor, execute este script como root (sudo ./otimizar.sh).${NC}"
  exit 1
fi

echo -e "\n${AZUL}[1/5] Ajustando Repositórios no Padrão Moderno (deb822)...${NC}"
# Limpa o arquivo antigo para evitar erros 404 de caminhos brutos
echo "# Gerenciado via kali.sources" > /etc/apt/sources.list

# Configura o redirecionador oficial inteligente
cat << EOF > /etc/apt/sources.list.d/kali.sources
X-Type-Deb822: yes
URIs: http://kali.org
Suites: kali-rolling
Components: main contrib non-free non-free-firmware
EOF
echo -e "${VERDE}[OK] Repositórios configurados de forma estável!${NC}"

echo -e "\n${AZUL}[2/5] Otimizando DNS + Compatibilidade com VPN (TryHackMe)...${NC}"
DHCP_CONF="/etc/dhcp/dhclient.conf"
if [ -f "$DHCP_CONF" ]; then
    sed -i '/prepend domain-name-servers/d' $DHCP_CONF
    echo 'prepend domain-name-servers 1.1.1.1, 8.8.8.8;' >> $DHCP_CONF
    echo -e "${VERDE}[OK] Prioridade de DNS rápido configurada no DHCP.${NC}"
fi

# Aplica imediatamente o resolv.conf misto estável para uso local
cat << EOF > /etc/resolv.conf
search local
nameserver 1.1.1.1
nameserver 8.8.8.8
nameserver fe80::9a2a:aff:fe8d:dfcb%eth0
EOF
systemctl restart NetworkManager
echo -e "${VERDE}[OK] Rede e DNS de alta velocidade aplicados!${NC}"

echo -e "\n${AZUL}[3/5] Desativando Sombras e Efeitos Visuais (XFCE)...${NC}"
if [ -n "$SUDO_USER" ]; then
    sudo -u $SUDO_USER xfconf-query -c xfwm4 -p /general/use_compositing -s false 2>/dev/null
    sudo -u $SUDO_USER xfconf-query -c xfwm4 -p /general/show_popup_shadow -s false 2>/dev/null
    sudo -u $SUDO_USER xfconf-query -c xfwm4 -p /general/show_frame_shadow -s false 2>/dev/null
    echo -e "${VERDE}[OK] Sombras e efeitos desativados permanentemente!${NC}"
fi

echo -e "\n${AZUL}[4/5] Otimizando Sistema e Uso de Memória (Permanente)...${NC}"
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
echo -e "${VERDE}[OK] Swappiness e gerenciamento de Wi-Fi ajustados!${NC}"

echo -e "\n${AZUL}[5/5] Seleção de Perfil de Hardware...${NC}"
echo "Escolha o perfil do seu computador:"
echo "1) PC Fraco (Celeron, Intel i3, AMD Athlon, 4GB RAM ou menos)"
echo "2) PC Forte (Intel i5, i7, Ryzen, 8GB RAM ou mais)"
read -p "Digite a opção (1 ou 2): " OPCAO

if [ "$OPCAO" -eq 1 ]; then
    echo -e "\n${AZUL}Aplicando ajustes para PC Fraco...${NC}"
    systemctl disable NetworkManager-wait-online.service 2>/dev/null
    echo -e "${VERDE}[OK] Modificações de baixo consumo concluídas.${NC}"
elif [ "$OPCAO" -eq 2 ]; then
    echo -e "\n${AZUL}Aplicando ajustes para PC Forte...${NC}"
    if apt install cpufrequtils -y &>/dev/null; then
        cpufreq-set -g performance 2>/dev/null
        echo -e "${VERDE}[OK] Processador configurado no modo Performance (sem travamentos no navegador).${NC}"
    fi
fi

apt autoremove -y &>/dev/null
apt clean &>/dev/null

echo -e "\n${VERDE}==================================================${NC}"
echo -e "${VERDE} OTIMIZAÇÃO CONCLUÍDA! PRONTO PARA O TRYHACKME!   ${NC}"
echo -e "${VERDE} Reinicie o seu Kali Linux para aplicar tudo.      ${NC}"
echo -e "${VERDE}==================================================${NC}"
