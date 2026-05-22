# 🎯 Projeto: Automação de Auditoria de Acessos AD
**Status:** 🟡 Em Andamento
**Pasta:** `01_Projetos/`

---

## 📐 Escopo S.M.A.R.T.

* **S (Specific - Específico):** * *O que é:* Criar um script em Python que cruza a base de usuários ativos no RH com as contas habilitadas no Active Directory para encontrar contas órfãs.
* **M (Measurable - Mensurável):** * *Como medir sucesso:* O script deve rodar sem erros, exportar um CSV validado via Pandas e reduzir o tempo de auditoria manual de 4 horas para menos de 5 minutos.
* **A (Achievable - Alcançável):** * *É possível agora?* Sim. Tenho a biblioteca `ldap3` configurada no ambiente e a permissão de leitura via conta de serviço no IIS.
* **R (Relevant - Relevante):** * *Por que importa:* Elimina falhas de conformidade em auditorias de acessos e reforça a segurança contra contas inativas (IGA/IAM).
* **T (Time-bound - Temporal):** * *Prazo Final:* 15 de Junho de 2026. (Este é o prazo que valida o projeto no P.A.R.A.)

---
 

## ⚙️ 2. Execução (Planejar, Testar, Medir)

### 🔄 Sprint 1: Conexão com o Banco
* **📝 Planejar:** Configurar o SQLAlchemy para ler a base de dados em `/instance/` de forma segura.
* **🧪 Testar:** Rodar o script em ambiente local apontando para um `.db` de homologação.
* **📊 Medir:** O script conectou em 2 segundos, mas a query puxou dados duplicados.
* **🛠️ Ajustar:** Adicionar `.drop_duplicates()` no *dataframe* do Pandas para a próxima versão.

### 🔄 Sprint 2: Extração de Dados (Atual)
* **📝 Planejar:** [...]



## 📋 Lista de Tarefas (Checklist)
- [x] Configurar `pyproject.toml` e dependências locais.
- [x] Testar conexão de leitura na pasta `/instance/`.
- [ ] Criar lógica de *dataframe* no Pandas.
- [ ] Homologar regras de saída do CSV.
