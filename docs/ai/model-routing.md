# Model Routing & API Cost Optimization

A escolha do modelo de Inteligência Artificial para cada tarefa não é arbitrária. Para manter o equilíbrio entre custo (OpenRouter), latência (RTX 3080) e qualidade de entrega, a tabela de roteamento abaixo deve ser rigorosamente seguida.

## Matriz de Decisão Operacional

| Perfil / Tarefa | Modelo Atribuído | Ambiente | Custo | Objetivo Principal |
| :--- | :--- | :--- | :--- | :--- |
| **Código Simples & CRUDs** | `Qwen3 14B` | Local (Ollama) | Zero | Desenvolvimento diário, testes unitários, formatação de dados, scripts rápidos. |
| **Raciocínio & Debugging** | `DeepSeek R1 14B` | Local (Ollama) | Zero | Lógica complexa, análise de falhas de segurança IAM, depuração de automações Playwright. |
| **Desenvolvimento Base (Feature)** | `DeepSeek V4 Flash` | Nuvem (OpenRouter)| Baixo | Criação de novas features abrangendo múltiplos arquivos. Custo-benefício padrão para nuvem. |
| **Auditoria & Arquitetura** | `Kimi K2.6` | Nuvem (OpenRouter)| Alto | Refatoração global, leitura de centenas de arquivos, análise de dependências de todo o projeto. |
| **Emergência / Backup** | `Nemotron Free` | Nuvem (OpenRouter)| Zero | Tarefas médias quando a GPU local estiver ocupada ou indisponível. |

## Regra de Ouro da Execução
O volume de processamento do projeto deve respeitar a proporção: **80% Local, 15% DeepSeek Flash, 5% Kimi K2.6.** Priorize sempre a execução local (Qwen3) em conjunto com as ferramentas MCP para minimizar o uso de tokens pagos.
