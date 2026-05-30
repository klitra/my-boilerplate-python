# Model Routing & AI Orchestration

## Objetivo
Este documento define a estratégia oficial de roteamento de IA para o projeto, equilibrando custo, velocidade, consumo de VRAM e capacidade de contexto. A escolha do modelo deve ser baseada na **natureza da tarefa**, e não na disponibilidade do provedor.

---

## Princípios Fundamentais

* **Local First:** Sempre priorizar a execução local quando a tarefa puder ser resolvida sem perda de qualidade. Benefícios: Custo zero, menor latência e total privacidade.
* **MCP Before Context:** Antes de aumentar o contexto ou trocar para modelos gigantes, utilize a recuperação seletiva. Acione ferramentas na seguinte ordem:
    1. MCP Filesystem
    2. MCP Git
    3. MCP SQLite
    4. MCP Playwright
* **Context Is Expensive:** Enviar centenas de arquivos para um modelo é exceção. Priorize busca seletiva, navegação por símbolos e leitura incremental.
* **Meta Operacional:** 80% Local | 15% OpenRouter Econômico | 5% OpenRouter Premium.

---

## Perfis de Capacidade

### 1. Local Coding (Prioridade: Alta)
* **Objetivo:** Implementação diária e tarefas operacionais.
* **Escopo:** CRUDs, APIs Flask, testes Pytest, automação Python, processamento com Pandas e documentação.
* **Ambiente / Atual:** Ollama / `Qwen3 14B`

### 2. Deep Reasoning (Prioridade: Média)
* **Objetivo:** Raciocínio lógico aprofundado e resolução de problemas.
* **Escopo:** Debugging complexo, modelagem de banco de dados, fluxos de segurança e governança de identidades (IAM).
* **Ambiente / Atual:** Ollama / `DeepSeek R1 14B`

### 3. Feature Development (Prioridade: Média)
* **Objetivo:** Implementação de funcionalidades envolvendo múltiplos módulos e integrações.
* **Escopo:** Novas features, refatorações médias e integrações de rotinas na nuvem.
* **Ambiente / Atual:** OpenRouter / `DeepSeek V4 Flash`

### 4. Global Architecture Review (Prioridade: Baixa)
* **Objetivo:** Análise de larga escala (usar apenas sob extrema necessidade).
* **Escopo:** Auditoria arquitetural, revisão global de dependências e refatoração estrutural massiva da pasta `/src`.
* **Ambiente / Atual:** OpenRouter / `Kimi K2.6`

### 5. Emergency Fallback
* **Objetivo:** Continuidade operacional.
* **Escopo:** Falha dos provedores principais, limites de API estourados ou testes rápidos de viabilidade.
* **Ambiente / Atual:** OpenRouter / `Nemotron Free`

---

## Processo de Escolha (Régua de Decisão)

| Situação | Capacidade Acionada |
| :--- | :--- |
| Testes, documentação e código isolado | **Local Coding** |
| Refatoração pontual e scripts simples | **Local Coding** |
| Debugging de falhas e regras IAM | **Deep Reasoning** |
| Nova funcionalidade complexa | **Feature Development** |
| Auditoria do projeto inteiro | **Global Architecture Review** |
| Queda de serviço / Emergência | **Emergency Fallback** |

## Context Thresholds

Até 5 arquivos:
→ Local Coding

Até 20 arquivos:
→ Deep Reasoning

Até 50 arquivos:
→ Feature Development

Acima de 50 arquivos:
→ Global Architecture Review

> **Regra Final:** Nunca utilize uma capacidade maior apenas porque ela está disponível. Escolha sempre o menor ambiente capaz de executar a tarefa com a qualidade exigida.
