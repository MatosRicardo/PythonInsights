# Python Insights - Análise de Cancelamento de Clientes - Jornada Python

Este projeto foi desenvolvido para analisar e validar uma base de dados de clientes que cancelaram seus planos, identificando padrões e propondo medidas para reduzir os cancelamentos. Utilizamos **Python**, as bibliotecas **Pandas** para manipulação de dados e **Plotly** para visualização interativa.

---

## 📊 Objetivo

O principal objetivo deste projeto é entender os motivos por trás dos cancelamentos de clientes e propor ações estratégicas baseadas nos dados analisados, como:

- **Identificar clientes com maior probabilidade de cancelamento.**
- **Propor estratégias para retenção de clientes.**
- **Criar alertas preventivos baseados em padrões de comportamento.**

---

## 🛠 Tecnologias Utilizadas

- **Python** - Linguagem principal para análise e manipulação de dados.
- **Pandas** - Biblioteca para tratamento e análise da base de dados.
- **Plotly** - Para criação de gráficos interativos.

---

## 📂 Estrutura do Projeto

- **`cancelamentos_sample.csv`**: Arquivo com a base de dados de cancelamentos.
- **`main.ipynb`**: Código principal para análise, validação e criação de gráficos.
- **Gráficos interativos**: Visualizações criadas para identificar padrões e tendências.

---

## 📋 Estratégias Implementadas

1. **Validação da Base de Dados**:
   - Remoção de dados inconsistentes e valores ausentes.
   - Limpeza e preparação para análise.

2. **Identificação de Padrões**:
   - Clientes com contrato mensal apresentam maior taxa de cancelamento.
   - Clientes que atrasam pagamentos por mais de 20 dias têm maior chance de cancelar.

3. **Medidas Propostas**:
   - **Incentivo para contratos anuais ou trimestrais**, oferecendo descontos.
   - **Alertas automáticos** para clientes com 15 dias de atraso no pagamento.
   - **Monitoramento preventivo** de clientes com alto número de chamadas ao suporte.

---

## 📈 Exemplos de Gráficos

Visualizamos os padrões de cancelamento com gráficos interativos para uma melhor compreensão:

- **Taxa de Cancelamento por Tipo de Contrato**
- **Impacto do Atraso de Pagamentos**
- **Relação entre Chamadas ao Call Center e Cancelamento**

---

## 🚀 Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/python-insights.git
