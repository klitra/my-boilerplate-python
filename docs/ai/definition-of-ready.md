# Definition of Ready (DoR)

## Propósito
Nenhuma tarefa de desenvolvimento, refatoração ou correção de bug deve ser iniciada pelo Agente (modos Coder ou Developer) sem que os critérios abaixo estejam rigorosamente definidos e aprovados pelo modo Planner ou pelo usuário.

## Critérios de Aceitação Obrigatórios
Uma tarefa só pode ser movida para a fase de implementação quando atender a todos os itens:

- [ ] **Objetivo Claro:** O problema a ser resolvido ou o valor de negócio está inequivocamente definido.
- [ ] **Escopo Delimitado:** Sabe-se exatamente onde a tarefa começa e onde termina.
- [ ] **Arquivos Afetados:** Os módulos, rotas ou bancos de dados que sofrerão impacto foram identificados via MCP.
- [ ] **Dependências Conhecidas:** Bibliotecas, variáveis de ambiente ou credenciais IAM necessárias estão mapeadas.
- [ ] **Critérios de Aceite:** O que define que a tarefa funcionou (ex: "A rota retorna HTTP 200 com JSON validado").
- [ ] **Plano Aprovado:** O roadmap tático foi validado.

Se o Agente de IA for acionado sem um DoR claro, ele DEVE interromper a operação e solicitar a definição destes pontos.
