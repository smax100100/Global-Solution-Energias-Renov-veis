# Global Solution: Monitoramento de Sistemas em Energias Renováveis e Sustentáveis

## Descrição do Projeto

Este projeto visa desenvolver um sistema inteligente de monitoramento para uma missão espacial experimental, com foco em energias renováveis e sustentabilidade. O sistema é capaz de simular a coleta de dados de sensores, monitorar esses dados em tempo real, gerar alertas para condições críticas e tomar decisões automatizadas para garantir a operação eficiente e segura dos módulos espaciais.

## Requisitos Técnicos Atendidos

Conforme as diretrizes da Global Solution, este projeto aborda os seguintes requisitos:

1.  **Monitoramento de Dados Simulados:** Recebe, interpreta e exibe dados simulados das condições operacionais da missão (temperatura, comunicação, energia e status dos módulos).
2.  **Geração de Alertas:** Implementa a geração automática de alertas diante de condições críticas simuladas.
3.  **Tomada de Decisão Básica:** Desenvolve estruturas lógicas para respostas automatizadas diante de situações críticas.
4.  **Visualização dos Dados:** Apresenta as informações monitoradas de forma clara e organizada (via console, neste protótipo).

## Estrutura do Código (Ultra-Simplificada e Linear)

O código foi reescrito para ser o mais linear e direto possível, ideal para iniciantes. Toda a lógica está contida na função `simulate_mission`, que é executada diretamente ao final do script. As principais partes são:

-   **`current_readings` e `alert_rules`**: Dicionários globais que armazenam as últimas leituras dos sensores e as regras para gerar alertas, respectivamente.
-   **Loop Principal (`while`):** Dentro deste loop, a cada 5 segundos, o programa realiza as seguintes ações:
    1.  **Coleta de Dados Simulados:** Gera valores aleatórios para temperatura, nível de energia e status de comunicação, e os armazena em `current_readings`.
    2.  **Verificação de Alertas e Tomada de Decisão:** Para cada sensor, verifica se o valor atual está fora dos limites definidos em `alert_rules`. Se um limite for excedido, uma mensagem de alerta é exibida e uma ação correspondente é sugerida.
    3.  **Exibição do Status Atual:** Imprime no console um resumo do estado atual de todos os sensores.
-   **Chamada Direta da Função:** A função `simulate_mission()` é chamada diretamente no final do script, sem a necessidade de um bloco `if __name__ == "__main__":`.

## Como Executar o Projeto

Para executar este projeto, siga os passos abaixo:

### Pré-requisitos

Certifique-se de ter o Python 3 instalado em sua máquina.

### Instalação

Não há dependências externas complexas para este protótipo. As bibliotecas `datetime`, `random` e `time` são nativas do Python.

### Execução

1.  Salve o código fornecido como `main.py`.
2.  Abra um terminal ou prompt de comando.
3.  Navegue até o diretório onde você salvou o arquivo `main.py`.
4.  Execute o script Python:

    ```bash
    python3 main.py
    ```

O programa simulará a coleta de dados por um período definido (padrão de 30 segundos para demonstração), exibindo o monitoramento, alertas e decisões no console.

## Exemplo de Saída (Console)

```
Iniciando simulação da missão espacial...
[MONITORAMENTO] Coletado: [2026-06-02 10:30:00] temperatura_modulo_1: 45.67 °C
[MONITORAMENTO] Coletado: [2026-06-02 10:30:00] nivel_energia_painel: 321.12 W
[MONITORAMENTO] Coletado: [2026-06-02 10:30:00] status_comunicacao: 0.95 
[DECISÃO] Verificando alertas e tomando decisões...
[DECISÃO] Sistema operando normalmente. Nenhuma ação imediata necessária.

------------------------------
STATUS ATUAL DO SISTEMA ESPACIAL
------------------------------
  Temperatura Modulo 1: 45.67 °C
  Nivel Energia Painel: 321.12 W
  Status Comunicacao: 0.95 
------------------------------
[MONITORAMENTO] Coletado: [2026-06-02 10:30:05] temperatura_modulo_1: 85.10 °C
[MONITORAMENTO] Coletado: [2026-06-02 10:30:05] nivel_energia_painel: 80.50 W
[MONITORAMENTO] Coletado: [2026-06-02 10:30:05] status_comunicacao: 0.75 
[DECISÃO] Verificando alertas e tomando decisões...
[DECISÃO] ALERTA: temperatura_modulo_1 acima do máximo! Valor: 85.10 °C (Max: 80.00 °C)
[DECISÃO] Ação: Ativar sistema de resfriamento de emergência.
[DECISÃO] ALERTA: nivel_energia_painel abaixo do mínimo! Valor: 80.50 W (Min: 100.00 W)
[DECISÃO] Ação: Redirecionar energia de painéis auxiliares.
[DECISÃO] ALERTA: status_comunicacao abaixo do mínimo! Valor: 0.75  (Min: 0.90 )
[DECISÃO] Ação: Tentar restabelecer comunicação principal e ativar backup.

------------------------------
STATUS ATUAL DO SISTEMA ESPACIAL
------------------------------
  Temperatura Modulo 1: 85.10 °C
  Nivel Energia Painel: 80.50 W
  Status Comunicacao: 0.75 
------------------------------
...
Simulação finalizada.
