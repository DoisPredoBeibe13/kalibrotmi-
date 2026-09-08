# Kali Linux Otimizado para Brasileiros 🇧🇷

Script automatizado para deixar o Kali Linux mais rápido, leve e totalmente compatível com laboratórios de **TryHackMe / Hack The Box (VPN)**. Desenvolvido por **DoxxerX**.

> ⚠️ **RECOMENDAÇÃO IMPORTANTE:** Se você estiver utilizando o Kali Linux dentro de uma Máquina Virtual (VirtualBox, VMware ou Hyper-V), **tire um Snapshot (ponto de restauração)** da sua VM antes de executar qualquer ferramenta de otimização profunda.

## 🚀 O que este projeto faz?
* **Otimização Geral (`otimizar.sh`):** Altera repositórios para o padrão moderno, limpa caches, desativa sombras do sistema e configura perfis inteligentes para PC Fraco (baixo consumo) e PC Forte (Alta performance estável em processadores i5, i7 e Ryzen).
* **Compatibilidade Dinâmica:** Injeta servidores DNS rápidos (Cloudflare/Google) no cliente DHCP. Isso garante navegação rápida na web e impede que os laboratórios de CTF e VPNs quebrem.

---

## 📁 Estrutura do Repositório

Se você prefere não rodar a otimização completa, o projeto está organizado em módulos separados na pasta `modulos/`:
1. `modulos/xfce_visuais.sh` -> Desativa apenas as sombras e composição de janelas do XFCE.
2. `modulos/dns_vpn.sh` -> Ajusta apenas o DNS rápido e regras de rotas para o TryHackMe.
3. `modulos/sistema_ram.sh` -> Modifica apenas o Swappiness e o foco no uso da memória RAM física.

---

## 🛠️ Como Executar na sua Máquina

Para aplicar todas as otimizações de uma vez só, abra o terminal do seu Kali Linux e rode a sequência abaixo:

```bash
# 1. Clone o repositório oficial
git clone https://github.com/DoisPredoBeibe13/kalibrotmi-

# 2. Acesse a pasta do projeto
cd kalibrotmi-

# 3. Dê permissão de execução para os scripts
chmod +x otimizar.sh
chmod +x modulos/*.sh

# 4. Execute o script principal como root
sudo ./otimizar.sh
```

Após o término da execução, reinicie o seu computador ou máquina virtual para aplicar todas as mudanças permanentemente.
