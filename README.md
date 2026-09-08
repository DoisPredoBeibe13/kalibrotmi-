# 🚀 Kali Linux Otimizado para Brasileiros (`kalibrotmi-`)

O **kalibrotmi-** é um ecossistema automatizado de otimização híbrida (Shell Script + Python) desenvolvido especificamente para a comunidade brasileira de segurança cibernética e Linux. Ele foi projetado para deixar o seu Kali Linux extremamente rápido, fluido e responsivo, eliminando gargalos crônicos do sistema sem destruir a estética visual padrão da distribuição.

Este projeto foi totalmente planejado por **DoxxerX** (DoisPredoBeibe13).

---

## 🔒 Compatibilidade Nativa com TryHackMe / Hack The Box (VPN)

Muitos scripts de otimização genéricos que circulam na internet quebram as conexões de rede do Kali ao travar o arquivo `/etc/resolv.conf`. Isso impede que você resolva os nomes de domínio ou acesse os IPs internos das salas e máquinas virtuais (`.thm`) de plataformas como o TryHackMe.

**Como resolvemos isso:** 
Nosso módulo injeta as diretrizes de velocidade através do recurso `prepend` diretamente no cliente DHCP do sistema. 
* **Navegação comum:** O sistema prioriza os servidores DNS mais rápidos do mundo integrados ao IX.br (**Cloudflare 1.1.1.1** e **Google 8.8.8.8**) para abrir abas e carregar páginas instantaneamente no navegador.
* **Uso de VPN (`openvpn` / `wireguard`):** Assim que você se conecta a uma sala de CTF, o túnel da VPN consegue injetar os servidores DNS internos dela normalmente. Você joga e estuda sem lag e sem queda de rota!

---

## 🛠️ O que o Orquestrador Híbrido faz?

Em vez de aplicar configurações cegas que podem sobrecarregar máquinas modestas ou limitar computadores potentes, o script principal (`otimizar.sh`) aciona um manipulador inteligente em **Python 3** (`otimizador.py`). O Python lê em tempo real os metadados do seu hardware e divide as tarefas:

### 🐍 Controle de Baixo Nível (Handler Python)
* **Análise de Hardware Dinâmica:** Detecta a quantidade exata de núcleos de processamento (vCPUs) e a memória RAM física instalada.
* **Perfil PC Fraco (Intel Celeron, Core i3, AMD Athlon ou até 4GB RAM):** Reduz o limite do cache de escrita em disco (`dirty_background_ratio` e `dirty_ratio`), impedindo que o navegador consuma toda a memória ativa do computador e cause congelamentos (*freezes*).
* **Perfil PC Forte (Intel i5, i7, i9, AMD Ryzen ou 8GB+ RAM):** Ativa o modo de energia **Performance** em todos os núcleos da CPU individualmente. Ele otimiza o cache de paginação para evitar que processadores intermediários (como o i5) apresentem engasgos ao abrir ferramentas pesadas de varredura ou múltiplas abas.
* **Otimização do Kernel (TCP BBR):** Injeta regras no Kernel do Linux para otimizar os buffers de envio e recebimento de rede, ativando o algoritmo de controle de congestionamento BBR da Google para downloads massivos.

### 🐚 Módulos de Interface e Sistema (Shell Script)
1. **`modulos/xfce_visuais.sh`:** Remove permanentemente as sombras das janelas, bordas e pop-ups do gerenciador XFCE. O visual nativo permanece idêntico, mas elimina o peso de renderização da placa de vídeo.
2. **`modulos/dns_vpn.sh`:** Configura as regras híbridas de DNS explicadas acima.
3. **`modulos/sistema_ram.sh`:** Altera o parâmetro `swappiness` do sistema para `10`, forçando o Linux a utilizar a memória RAM física (que é infinitamente mais rápida) antes de recorrer ao disco rígido (Swap).

---

## 📂 Estrutura do Repositório

O projeto é modular. Se você não quiser aplicar todas as mudanças de uma vez através do script principal, pode entrar na pasta `modulos/` e rodar cada ferramenta separadamente:

```text
kalibrotmi-/
├── otimizar.sh              # Gatilho principal (Valida privilégios de root)
├── otimizador.py            # Orquestrador em Python (Mapeia hardware e aplica regras)
├── README.md                # Documentação do repositório
└── modulos/                 # Pasta de scripts isolados
    ├── xfce_visuais.sh      # Desativa apenas efeitos gráficos e sombras
    ├── dns_vpn.sh           # Altera apenas as regras de DNS para VPN
    └── sistema_ram.sh       # Ajusta apenas uso de memória Swap e Wi-Fi
```

---

## ⚠️ Recomendação Importante (Snapshot)

Se você estiver utilizando o Kali Linux virtualizado dentro do **VirtualBox, VMware ou Hyper-V**, é altamente recomendável **tirar um Snapshot (Ponto de Restauração)** da sua máquina virtual antes de prosseguir. Embora o script seja seguro e utilize os padrões de repositório modernos (`deb822`), criar um snapshot garante que você possa reverter o estado do sistema caso ocorra alguma queda de energia durante o processo de atualização.

---

## 🚀 Como Executar no seu Kali Linux

Abra o terminal do seu Kali Linux e copie e cole a sequência de comandos abaixo para clonar a estrutura e iniciar o otimizador:

```bash
# 1. Clone o repositório para sua máquina local
git clone https://github.com

# 2. Acesse o diretório do projeto
cd kalibrotmi-

# 3. Dê a permissão necessária de execução para o script
chmod +x otimizar.sh

# 4. Rode o utilitário como superusuário (root)
sudo ./otimizar.sh
```

Após a conclusão das duas etapas na tela do terminal, basta **reiniciar a sua máquina** para consolidar todas as melhorias permanentemente no sistema!
