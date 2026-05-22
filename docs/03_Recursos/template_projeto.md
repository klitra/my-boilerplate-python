# 🎯 Projeto: [Nome do Projeto]
**Status:** 🔴 Planejado | 🟡 Em Andamento | 🟢 Concluído
**Data de Criação:** [Data]
**Prazo Final:** [Data]

---

## 📐 1. Escopo S.M.A.R.T. (Alinhamento Estratégico)

* **S (Specific - Específico):**
  * *O que será construído:* [Descreva o script, pipeline ou portal de forma clara e direta]
* **M (Measurable - Mensurável):**
  * *Como medir o sucesso/performance:* [Ex: Rodar em menos de X minutos, mitigar X falhas, gerar CSV validado]
* **A (Achievable - Alcançável):**
  * *Viabilidade técnica atual:* [Ex: Bibliotecas disponíveis no ambiente virtual, acessos liberados via conta de serviço]
* **R (Relevant - Relevante):**
  * *Impacto na operação/segurança:* [Ex: Eliminar falhas de conformidade em auditorias de acessos, automação de IGA/IAM]
* **T (Time-bound - Temporal):**
  * *Prazo limite de execução:* [Data final que valida a permanência deste arquivo na pasta 01_Projetos]

---

## 🔬 2. Ciclo de Execução Científica (Planejar, Testar, Medir, Ajustar)

Este bloco funciona como o diário de bordo do desenvolvimento, utilizando o princípio de hipótese e validação (TDD/Método Científico).

### 🔄 Sprint 1: [Nome da Etapa - Ex: Conexão com o Banco]
* **📝 Planejar (Hipótese):** Configurar o SQLAlchemy para ler a base de dados de homologação dentro da pasta `/instance` de forma segura.
* **🧪 Testar (Experimento):** Rodar o script de validação de conexão isolado na pasta `tests/` para verificar o retorno da query.
* **📊 Medir (Resultado):** A conexão foi estabelecida em 2 segundos, porém a consulta retornou registros duplicados.
* **🛠️ Ajustar (Refatoração):** Implementar o método `.drop_duplicates()` no *dataframe* do Pandas para limpar os dados antes da exportação definitiva.

### 🔄 Sprint 2: [Próxima Etapa]
* **📝 Planejar (Hipótese):** * **🧪 Testar (Experimento):** * **📊 Medir (Resultado):** * **🛠️ Ajustar (Refatoração):** ---

## 📋 Lista de Tarefas (Checklist de Engenharia)
- [ ] Configurar ambiente virtual e travar dependências no `pyproject.toml`
- [ ] Escrever testes de validação inicial na pasta `tests/`
- [ ] Implementar lógica de negócio na pasta `src/`
- [ ] Homologar execução e permissões de escrita em ambiente seguro
- [ ] Mover arquivo de documentação para `04_Arquivo` após a conclusão
