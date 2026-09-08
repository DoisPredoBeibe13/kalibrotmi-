import os
import sys
import subprocess
import multiprocessing
import time

# Cores para o terminal
VERDE = '\033[0;32m'
AZUL = '\033[0;34m'
VERMELHO = '\033[0;31m'
AMARELO = '\033[0;33m'
NC = '\033[0m'

def run_shell_script(script_path):
    """Executa os submódulos .sh com segurança"""
    if os.path.exists(script_path):
        print(f"{AZUL}[Módulo] Executando {script_path}...{NC}")
        subprocess.run(["bash", script_path], check=True)
    else:
        print(f"{VERMELHO}[Aviso] Módulo {script_path} não encontrado.{NC}")

def obter_ram_total():
    """Detecta a memória RAM em Gigabytes"""
    with open('/proc/meminfo', 'r') as f:
        for line in f:
            if "MemTotal" in line:
                mem_kb = int(line.split()[1])
                return round(mem_kb / (1024 * 1024))
    return 4

def otimizar_kernel_rede():
    """Otimizações avançadas de rede e latência direto no sysctl"""
    print(f"{AZUL}[Python] Injetando engenharia de rede de baixo nível (Kernel TCP BBR)...{NC}")
    configuracoes = [
        "\n# Otimizacoes Kali Fast BR - DoxxerX",
        "net.core.rmem_max=16777216",
        "net.core.wmem_max=16777216",
        "net.ipv4.tcp_rmem=4096 87380 16777216",
        "net.ipv4.tcp_wmem=4096 65536 16777216",
        "net.ipv4.tcp_congestion_control=bbr",
        "fs.file-max=2097152",
        "net.core.netdev_max_backlog=16384",
        "net.ipv4.tcp_fin_timeout=15"
    ]
    
    with open("/etc/sysctl.conf", "a") as f:
        for conf in configuracoes:
            f.write(conf + "\n")
            
    subprocess.run(["sysctl", "-p"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def aplicar_perfil_hardware(ram, cpus):
    print(f"\n{VERDE}[Hardware] {ram}GB RAM | {cpus} Núcleos de CPU{NC}")
    
    if ram <= 4 or cpus <= 2:
        print(f"{AMARELO}[Perfil] Aplicando otimizações para PC Fraco...{NC}")
        with open("/proc/sys/vm/dirty_background_ratio", "w") as f: f.write("5")
        with open("/proc/sys/vm/dirty_ratio", "w") as f: f.write("10")
    else:
        print(f"{VERDE}[Perfil] Aplicando otimizações para PC Forte...{NC}")
        if os.path.exists("/usr/bin/cpufreq-set"):
            for cpu in range(cpus):
                subprocess.run(["cpufreq-set", "-c", str(cpu), "-g", "performance"], stderr=subprocess.DEVNULL)
        
        with open("/proc/sys/vm/dirty_background_ratio", "w") as f: f.write("15")
        with open("/proc/sys/vm/dirty_ratio", "w") as f: f.write("30")

def detectar_e_otimizar_vm():
    """Procura strings do hipervisor no DMI do Linux"""
    print(f"\n{AZUL}[Etapa 3] Verificando ambiente de virtualização...{NC}")
    
    is_vm = False
    vendor_path = "/sys/class/dmi/id/sys_vendor"
    product_path = "/sys/class/dmi/id/product_name"
    hypervisor_name = "Bare Metal (PC Físico)"

    if os.path.exists(vendor_path):
        with open(vendor_path, "r") as f:
            vendor = f.read().lower()
            if "virtualbox" in vendor or "innotek" in vendor:
                is_vm = True
                hypervisor_name = "VirtualBox"
            elif "vmware" in vendor:
                is_vm = True
                hypervisor_name = "VMware"

    if not is_vm and os.path.exists(product_path):
        with open(product_path, "r") as f:
            product = f.read().lower()
            if "virtualbox" in product:
                is_vm = True
                hypervisor_name = "VirtualBox"
            elif "vmware" in product:
                is_vm = True
                hypervisor_name = "VMware"

    print(f"{VERDE}[Resultado] Ambiente detectado: {hypervisor_name}{NC}")

    if is_vm:
        print(f"{AZUL}[Python] Modificando parâmetros de I/O assíncrono para {hypervisor_name}...{NC}")
        with open("/proc/sys/vm/vfs_cache_pressure", "w") as f: f.write("50")
        with open("/proc/sys/vm/laptop_mode", "w") as f: f.write("0")
        print(f"{VERDE}[OK] Otimizações de latência de disco virtual aplicadas!{NC}")

def faxina_sistema_insana(usuario_real):
    """O melhor limpador: Varre logs, caches de navegadores e lixo do Kernel"""
    print(f"\n{AMARELO}[Etapa 4] Iniciando a Limpeza Insana do Sistema...{NC}")
    
    # 1. Forçar o Kernel a liberar PageCache, Dentries e Inodes acumulados (Limpeza de RAM real)
    print(f"{AZUL}[Limpeza] Forçando liberação de cache de RAM inativa no Kernel...{NC}")
    subprocess.run(["sync"])
    with open("/proc/sys/vm/drop_caches", "w") as f: f.write("3")
    
    # 2. Limpeza profunda de logs e lixo de relatórios antigos
    print(f"{AZUL}[Limpeza] Esvaziando arquivos de log acumulados (/var/log)...{NC}")
    log_dir = "/var/log"
    for root, dirs, files in os.walk(log_dir):
        for file in files:
            if file.endswith(".log") or ".log." in file or file.endswith(".gz"):
                try:
                    fp = os.path.join(root, file)
                    if os.path.isfile(fp):
                        with open(fp, "w") as f: f.truncate(0)
                except Exception:
                    pass

    # 3. Limpar Cache do Gerenciador de Pacotes
    print(f"{AZUL}[Limpeza] Expurgando instaladores antigos e resíduos do APT...{NC}")
    subprocess.run(["apt", "autoremove", "-y"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(["apt", "clean"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # 4. Limpar caches de navegadores se o usuário real for informado
    if usuario_real and usuario_real != "root":
        print(f"{AZUL}[Limpeza] Limpando arquivos temporários de navegadores do usuário {usuario_real}...{NC}")
        user_home = f"/home/{usuario_real}"
        cache_paths = [
            f"{user_home}/.cache/mozilla/firefox/",
            f"{user_home}/.cache/google-chrome/",
            f"{user_home}/.cache/chromium/"
        ]
        for path in cache_paths:
            if os.path.exists(path):
                subprocess.run(["rm", "-rf", path], stderr=subprocess.DEVNULL)
                
    print(f"{VERDE}[OK] Faxina concluída! Megabytes de lixo foram eliminados.{NC}")

def main():
    if len(sys.argv) < 2:
        sys.exit(1)
        
    usuario_real = sys.argv[1]
    
    print(f"\n{AZUL}[Etapa 1] Executando submódulos .sh sequenciais...{NC}")
    run_shell_script("modulos/xfce_visuais.sh")
    run_shell_script("modulos/dns_vpn.sh")
    run_shell_script("modulos/sistema_ram.sh")
    
    print(f"\n{AZUL}[Etapa 2] Aplicando controle de baixo nível via Python...{NC}")
    otimizar_kernel_rede()
    
    ram = obter_ram_total()
    cpus = multiprocessing.cpu_count()
    aplicar_perfil_hardware(ram, cpus)
    
    detectar_e_otimizar_vm()
    
    # Nova função super apelona de limpeza ativa
    faxina_sistema_insana(usuario_real)
    
    print(f"\n{VERDE}=================================================={NC}")
    print(f"{VERDE} OTIMIZAÇÃO EXECUTADA COM SUCESSO PELO SEU HANDLER!{NC}")
    print(f"{VERDE} Reinicie o sistema para consolidar as alterações. {NC}")
    print(f"{VERDE}=================================================={NC}")

if __name__ == "__main__":
    main()
