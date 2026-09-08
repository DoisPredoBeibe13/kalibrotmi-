#!/bin/bash
# Remove efeitos visuais e sombras do XFCE
if [ -n "$SUDO_USER" ]; then
    sudo -u $SUDO_USER xfconf-query -c xfwm4 -p /general/use_compositing -s false 2>/dev/null
    sudo -u $SUDO_USER xfconf-query -c xfwm4 -p /general/show_popup_shadow -s false 2>/dev/null
    sudo -u $SUDO_USER xfconf-query -c xfwm4 -p /general/show_frame_shadow -s false 2>/dev/null
    echo -e "\033[0;32m[OK] Sombras e efeitos visuais desativados permanentemente!\033[0m"
else
    echo -e "\033[0;31m[ERRO] Rode o script usando sudo para mapear a interface gráfica.\033[0m"
fi
