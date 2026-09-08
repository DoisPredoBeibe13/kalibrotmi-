# 🚀 Kali Linux Otimizado para Brasileiros (`kalibrotmi-`)

O **kalibrotmi-** é um ecossistema automatizado de otimização híbrida (Shell Script + Python) desenvolvido especificamente para a comunidade brasileira de segurança cibernética e Linux. Ele foi projetado para deixar o seu Kali Linux extremamente rápido, fluido e estável, eliminando gargalos crônicos de processamento sem alterar a estética visual nativa da distribuição.

Este utilitário foi totalmente projetado por **DoxxerX** (DoisPredoBeibe13).

---

## 🔒 Compatibilidade Avançada com TryHackMe / Hack The Box (VPN)

Muitos scripts de otimização genéricos que circulam na internet quebram as conexões de rede do Kali ao bloquear estaticamente o arquivo `/etc/resolv.conf`. Isso impede que você resolva os nomes de domínio ou acesse os IPs internos das salas e laboratórios virtuais (`.thm`) de plataformas como o TryHackMe.

**A Solução Injetada:** 
Nosso módulo injeta as diretrizes de velocidade através do recurso `prepend` diretamente no cliente DHCP do sistema. 
* **Navegação comum:** O sistema prioriza os servidores DNS mais rápidos do mundo integrados ao IX.br (**Cloudflare 1.1.1.1** e **Google 8.8.8.8**) para abrir abas e carregar páginas instantaneamente no navegador.
* **Uso de VPN (`openvpn` / `wireguard`):** Assim que você se conecta a uma sala de CTF, o túnel da VPN consegue injetar os servidores DNS internos dela normalmente. Você joga e estuda sem lag e sem queda de rota!

---

## 🛠️ O que o Orquestrador Híbrido faz?

Em vez de aplicar configurações cegas que podem sobrecarregar máquinas modestas ou limitar computadores potentes, o script principal (`otimizar.sh`) aciona um manipulador inteligente em **Python 3** (`otimizador.py`). O Python lê em tempo real os metadados do seu hardware e divide as tarefas de forma inteligente:

### 🐍 Controle de Baixo Nível & Limpeza Insana (Handler Python)
* **Análise de Hardware Dinâmica:** Detecta a quantidade exata de núcleos de processamento (vCPUs) e a memória RAM física instalada.
* **Perfil PC Fraco (Intel Celeron, Core i3, AMD Athlon ou até 4GB RAM):** Reduz o limite do cache de escrita em disco (`dirty_background_ratio` e `dirty_ratio`), impedindo que o navegador consuma toda a memória ativa do computador e cause congelamentos (*freezes*).
* **Perfil PC Forte (Intel i5, i7, i9, AMD Ryzen ou 8GB+ RAM):** Ativa o modo de energia **Performance** em todos os núcleos da CPU individualmente. Ele otimiza o cache de paginação para evitar que processadores intermediários (como o i5) apresentem engasgos ao abrir ferramentas pesadas de varredura ou múltiplas abas.
* **Detector Inteligente de Máquina Virtual:** Lê os dados do DMI do sistema operacional. Caso detecte ambiente virtualizado (**VirtualBox** ou **VMware**), altera parâmetros de pressão do cache de memória (`vfs_cache_pressure`) e desativa o modo laptop para acelerar o disco virtual compartilhado com o Windows.
* **O Melhor App de Faxina Interna:** Executa uma limpeza profunda forçando o Kernel a limpar memórias cache inativas (`drop_caches = 3`), trunca arquivos de logs antigos acumulados que roubam espaço em disco e elimina arquivos temporários e lixo acumulado dos principais navegadores.

### 🐚 Módulos de Interface e Sistema (Shell Script)
1. **`modulos/xfce_visuais.sh`:** Remove permanentemente as sombras das janelas, bordas e pop-ups do gerenciador XFCE. O visual nativo permanece idêntico, mas elimina o peso desnecessário sobre o chip gráfico.
2. **`modulos/dns_vpn.sh`:** Configura as regras híbridas de DNS focadas em CTFs.
3. **`modulos/sistema_ram.sh`:** Altera o parâmetro `swappiness` do sistema para `10`, forçando o Linux a utilizar a memória RAM física (que é infinitamente mais rápida) antes de recorrer ao disco rígido (Swap).

---

## 📂 Estrutura do Repositório

O projeto é modular. Se você não quiser aplicar todas as mudanças de uma vez através do script principal, pode entrar na pasta `modulos/` e rodar cada ferramenta separadamente:

```text
kalibrotmi-/
├── otimizar.sh              # Gatilho principal (Valida privilégios de root)
├── otimizador.py            # Orquestrador em Python (Mapeia hardware, limpa RAM e aplica regras)
├── README.md                # Documentação do repositório
└── modulos/                 # Pasta de scripts isolados
    ├── xfce_visuais.sh      # Desativa apenas efeitos gráficos e sombras
    ├── dns_vpn.sh           # Altera apenas as regras de DNS para VPN
    └── sistema_ram.sh       # Ajusta apenas uso de memória Swap e Wi-Fi
```

---

## ⚠️ Recomendação Importante (Snapshot)

Se você estiver utilizando o Kali Linux virtualizado dentro do **VirtualBox, VMware ou Hyper-V**, é altamente recomendável **tirar um Snapshot (Ponto de Restauração)** da sua máquina virtual antes de prosseguir. Embora o script seja seguro e utilize os padrões de repositório modernos (`deb822`), criar um snapshot garante a integridade do sistema operacional contra interrupções externas.

---

## 🚀 Como Executar no seu Kali Linux

Abra o terminal do seu Kali Linux e copie e cole a sequência de comandos abaixo para clonar a estrutura e iniciar o otimizador:

```bash
# 1. Clone o repositório para sua máquina local
git clone https://github.com/DoisPredoBeibe13/kalibrotmi-.git

# 2. Acesse o diretório do projeto
cd kalibrotmi-

# 3. Dê a permissão necessária de execução para o script
chmod +x otimizar.sh

# 4. Rode o utilitário como superusuário (root)
sudo ./otimizar.sh
```

Após a conclusão das etapas na tela do terminal, basta **reiniciar a sua máquina** para consolidar todas as melhorias permanentemente no sistema!
