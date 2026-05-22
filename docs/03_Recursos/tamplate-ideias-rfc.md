# 💡 RFC (Request for Comments): [Nome Curto da Ideia]

**Autor:** [Seu Nome]
**Data da Proposta:** DD/MM/AAAA
**Status:** 🟡 Aguardando Consenso

---

## 🗂️ 1. Classificação da Ideia (O Caminho)
*Marque com um `x` o caminho que esta ideia deve seguir se aprovada:*

- [ ] **Automação de Dados:** (Envolverá manipulação via Pandas / ETL).
- [ ] **Governança/IAM:** (Envolverá Active Directory, IGA, PAM ou acessos).
- [ ] **Infraestrutura/RPA:** (Envolverá navegação web, Playwright ou APIs externas).
- [ ] **Fast-Track:** (Mudança trivial, menos de 2h de esforço. Pula o fluxo completo).

---

## 🚨 2. O Problema (Por que precisamos disso?)
*Descreva a dor atual da equipe, o gargalo operacional ou a falha de segurança que motivou esta ideia.*
> [Escreva aqui o contexto do problema]

## 🛠️ 3. A Proposta de Solução (Como vamos resolver?)
*Explique a sua ideia de forma direta. Se houver arquitetura envolvida, descreva qual será o fluxo.*
> [Escreva aqui a sua solução. Ex: "Criar um script em Python que cruze as tabelas X e Y usando Pandas e gere um alerta..."]

## 🛡️ 4. Análise de Impacto e Segurança
*Nenhuma ideia avança sem passar pelo crivo de segurança.*
* **Quais permissões a ideia exige?** (Ex: Acesso de leitura ao AD, conta de serviço no IIS).
* **Quais os riscos se der errado?** (Ex: Falso positivo bloqueando contas válidas).
* **Como mitigamos o risco?** (Ex: O script vai rodar apenas em base de homologação na primeira semana).

---

## ✅ 5. Votação e Consenso da Equipe
*A regra é clara: A ideia só vai para a fase de POC e desenvolvimento (TDD) quando TODOS os envolvidos marcarem `[x]`. Se você discordar, use o botão "Request Changes" do GitHub apontando a linha e sugerindo a alteração.*

- [ ] **Aprovação do Arquiteto/Sênior** (@UsuarioGitHub)
- [ ] **Aprovação de Segurança/Governança** (@UsuarioGitHub)
- [ ] **Aprovação da Operação/Gestão** (@UsuarioGitHub)

> **⚠️ Regra de Rejeição:** A reprovação sem proposta não é aceita. Se você reprovar, é obrigatório sugerir a arquitetura ou ferramenta que deve substituir a ideia original.
