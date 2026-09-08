import os
import sys
import subprocess
import multiprocessing

# Cores para o terminal
VERDE = '\033[0;32m'
AZUL = '\033[0;34m'
VERMELHO = '\033[0;31m'
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
    print(f"{AZUL}[Python] Ajustando parâmetros de buffer de rede e Kernel...{NC}")
    configuracoes = [
        "\n# Otimizacoes Kali Fast BR",
        "net.core.rmem_max=16777216",
        "net.core.wmem_max=16777216",
        "net.ipv4.tcp_rmem=4096 87380 16777216",
        "net.ipv4.tcp_wmem=4096 65536 16777216",
        "net.ipv4.tcp_congestion_control=bbr",
        "fs.file-max=2097152"
    ]
    
    with open("/etc/sysctl.conf", "a") as f:
        for conf in configuracoes:
            f.write(conf + "\n")
            
    subprocess.run(["sysctl", "-p"], stdout=subprocess.DEVNULL)

def aplicar_perfil_hardware(ram, cpus):
    print(f"\n{VERDE}[Hardware Detectado] {ram}GB RAM | {cpus} Núcleos de CPU{NC}")
    
    # Decisão de perfil baseada em hardware real
    if ram <= 4 or cpus <= 2:
        print(f"{AZUL}[Perfil] Aplicando otimizações para PC Fraco...{NC}")
        # Reduz cache de escrita para poupar memória RAM ativa
        with open("/proc/sys/vm/dirty_background_ratio", "w") as f: f.write("5")
        with open("/proc/sys/vm/dirty_ratio", "w") as f: f.write("10")
    else:
        print(f"{AZUL}[Perfil] Aplicando otimizações para PC Forte...{NC}")
        # Melhora processamento paralelo e gerencia tarefas de navegador no i5/Ryzen
        if os.path.exists("/usr/bin/cpufreq-set"):
            for cpu in range(cpus):
                subprocess.run(["cpufreq-set", "-c", str(cpu), "-g", "performance"], stderr=subprocess.DEVNULL)
        
        # Otimiza o cache de disco para sistemas com mais RAM (evita gargalo no navegador)
        with open("/proc/sys/vm/dirty_background_ratio", "w") as f: f.write("15")
        with open("/proc/sys/vm/dirty_ratio", "w") as f: f.write("30")

def main():
    if len(sys.argv) < 2:
        sys.exit(1)
        
    usuario_real = sys.argv[1]
    
    # 1. Executa a junção dos 3 módulos existentes
    print(f"\n{AZUL}[Etapa 1] Executando submódulos .sh sequenciais...{NC}")
    run_shell_script("modulos/xfce_visuais.sh")
    run_shell_script("modulos/dns_vpn.sh")
    run_shell_script("modulos/sistema_ram.sh")
    
    # 2. Executa otimizações avançadas controladas por Python
    print(f"\n{AZUL}[Etapa 2] Aplicando controle de baixo nível via Python...{NC}")
    otimizar_kernel_rede()
    
    ram = obter_ram_total()
    cpus = multiprocessing.cpu_count()
    aplicar_perfil_hardware(ram, cpus)
    
    # 3. Limpeza profunda
    subprocess.run(["apt", "autoremove", "-y"], stdout=subprocess.DEVNULL)
    subprocess.run(["apt", "clean"], stdout=subprocess.DEVNULL)
    
    print(f"\n{VERDE}=================================================={NC}")
    print(f"{VERDE} OTIMIZAÇÃO EXECUTADA COM SUCESSO PELO SEU HANDLER!{NC}")
    print(f"{VERDE} Reinicie o sistema para consolidar as alterações. {NC}")
    print(f"{VERDE}=================================================={NC}")

if __name__ == "__main__":
    main()
