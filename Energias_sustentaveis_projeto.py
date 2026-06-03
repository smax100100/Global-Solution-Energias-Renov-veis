
import time
import random
from datetime import datetime

# --- Variáveis Globais para Armazenamento de Dados e Regras ---
# Armazena a última leitura de cada sensor
current_readings = {}

# Regras para alertas
alert_rules = {
    "temperatura_modulo_1": {"min": 20.0, "max": 80.0, "unit": "°C"},
    "nivel_energia_painel": {"min": 100.0, "max": 500.0, "unit": "W"},
    "status_comunicacao": {"min": 0.9, "max": 1.0, "unit": ""} # 0.9 = 90% de integridade
}

# --- Função Principal de Simulação ---

def simulate_mission(duration_seconds: int = 60):
    """Simula a operação da missão espacial, coletando dados e reagindo a eventos."""
    print("Iniciando simulação da missão espacial...")

    start_time = time.time()
    while time.time() - start_time < duration_seconds:
        # --- 1. Coleta de Dados Simulados ---
        timestamp = datetime.now()

        # Simula temperatura
        temp_value = random.uniform(10.0, 90.0)
        current_readings["temperatura_modulo_1"] = {"value": temp_value, "unit": "°C", "timestamp": timestamp}
        print(f"[MONITORAMENTO] Coletado: [{timestamp.strftime("%Y-%m-%d %H:%M:%S")}] temperatura_modulo_1: {temp_value:.2f} °C")

        # Simula nível de energia
        energy_value = random.uniform(50.0, 600.0)
        current_readings["nivel_energia_painel"] = {"value": energy_value, "unit": "W", "timestamp": timestamp}
        print(f"[MONITORAMENTO] Coletado: [{timestamp.strftime("%Y-%m-%d %H:%M:%S")}] nivel_energia_painel: {energy_value:.2f} W")

        # Simula status de comunicação
        comm_status = random.uniform(0.7, 1.0)
        current_readings["status_comunicacao"] = {"value": comm_status, "unit": "", "timestamp": timestamp}
        print(f"[MONITORAMENTO] Coletado: [{timestamp.strftime("%Y-%m-%d %H:%M:%S")}] status_comunicacao: {comm_status:.2f} ")

        # --- 2. Verificação de Alertas e Tomada de Decisão ---
        print("[DECISÃO] Verificando alertas e tomando decisões...")
        alert_triggered = False

        # Verifica temperatura
        sensor_id = "temperatura_modulo_1"
        data = current_readings[sensor_id]
        rule = alert_rules[sensor_id]
        if data["value"] < rule["min"]:
            alert_message = f"ALERTA: {sensor_id} abaixo do mínimo! Valor: {data["value"]:.2f} {data["unit"]} (Min: {rule["min"]:.2f} {rule["unit"]})"
            print(f"[DECISÃO] {alert_message}")
            print("[DECISÃO] Ação: Ativar aquecimento auxiliar.")
            alert_triggered = True
        elif data["value"] > rule["max"]:
            alert_message = f"ALERTA: {sensor_id} acima do máximo! Valor: {data["value"]:.2f} {data["unit"]} (Max: {rule["max"]:.2f} {rule["unit"]})"
            print(f"[DECISÃO] {alert_message}")
            print("[DECISÃO] Ação: Ativar sistema de resfriamento de emergência.")
            alert_triggered = True

        # Verifica nível de energia
        sensor_id = "nivel_energia_painel"
        data = current_readings[sensor_id]
        rule = alert_rules[sensor_id]
        if data["value"] < rule["min"]:
            alert_message = f"ALERTA: {sensor_id} abaixo do mínimo! Valor: {data["value"]:.2f} {data["unit"]} (Min: {rule["min"]:.2f} {rule["unit"]})"
            print(f"[DECISÃO] {alert_message}")
            print("[DECISÃO] Ação: Redirecionar energia de painéis auxiliares.")
            alert_triggered = True
        elif data["value"] > rule["max"]:
            alert_message = f"ALERTA: {sensor_id} acima do máximo! Valor: {data["value"]:.2f} {data["unit"]} (Max: {rule["max"]:.2f} {rule["unit"]})"
            print(f"[DECISÃO] {alert_message}")
            print("[DECISÃO] Ação: Desligar sistemas não essenciais.")
            alert_triggered = True

        # Verifica status de comunicação
        sensor_id = "status_comunicacao"
        data = current_readings[sensor_id]
        rule = alert_rules[sensor_id]
        if data["value"] < rule["min"]:
            alert_message = f"ALERTA: {sensor_id} abaixo do mínimo! Valor: {data["value"]:.2f} {data["unit"]} (Min: {rule["min"]:.2f} {rule["unit"]})"
            print(f"[DECISÃO] {alert_message}")
            print("[DECISÃO] Ação: Tentar restabelecer comunicação principal e ativar backup.")
            alert_triggered = True

        if not alert_triggered:
            print("[DECISÃO] Sistema operando normalmente. Nenhuma ação imediata necessária.")

        # --- 3. Exibição do Status Atual ---
        print("\n" + "-"*30)
        print("STATUS ATUAL DO SISTEMA ESPACIAL")
        print("-"*30)
        if not current_readings:
            print("Nenhum dado disponível ainda.")
        else:
            for sensor_id, data in current_readings.items():
                display_name = sensor_id.replace("_", " ").title()
                print(f"  {display_name}: {data["value"]:.2f} {data["unit"]}")
        print("-"*30)

        time.sleep(5) # Coleta a cada 5 segundos

    print("Simulação finalizada.")

# Chamada direta da função de simulação
simulate_mission(duration_seconds=30) # Executa a simulação por 30 segundos para demonstração
