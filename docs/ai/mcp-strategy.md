# MCP Strategy: Eficiência de Contexto e Recuperação

## Propósito
O Model Context Protocol (MCP) é a principal engrenagem de economia de hardware e tokens deste projeto. O Agente de IA é OBRIGADO a seguir a técnica de "Recuperação Lenta e Cirúrgica".

## Ordem Obrigatória de Recuperação
Antes de ler o conteúdo de um arquivo para o prompt, execute os passos nesta ordem estrita:

1. **Procurar Símbolo:** Use ferramentas de busca no repositório.
2. **Procurar Função/Método:** Identifique a assinatura exata.
3. **Procurar Classe:** Entenda o isolamento do objeto.
4. **Ler Trecho Específico:** Extraia apenas o bloco delimitado por linhas.
5. **Expandir Contexto:** Leia o arquivo inteiro APENAS se a dependência contextual for inegociável para compreender a falha.

## Proibições Absolutas
Para evitar a explosão do KV Cache e falhas de memória (OOM):
- 🚫 É PROIBIDO ler o diretório `/src` inteiro.
- 🚫 É PROIBIDO ler o diretório `/docs` inteiro.
- 🚫 É PROIBIDO ler o repositório raiz inteiro.
- 🚫 É PROIBIDO utilizar consultas de banco de dados genéricas (ex: `SELECT * FROM table`). Consulte sempre o Schema.

Qualquer exceção a estas regras exige justificativa explícita e documentada no chat antes da execução.
