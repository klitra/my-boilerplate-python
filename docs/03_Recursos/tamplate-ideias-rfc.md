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

## ✅ 5. Votação e Consenso (Quórum e Veto Democrático)
*A regra é o Veto Democrático: A ideia só avança para a fase de POC e desenvolvimento quando atingir o quórum de aprovação abaixo, **desde que não haja nenhum veto ativo** de qualquer outro membro da equipe.*

- [ ] **Aprovação de Arquitetura/Engenharia** (@UsuarioGitHub)
- [ ] **Aprovação de Segurança/Governança** (@UsuarioGitHub)
- [ ] **Aprovação da Operação/Gestão** (@UsuarioGitHub)

> **⚠️ Regra do Veto e Rejeição:** 100% da equipe possui poder de veto. Se você discordar da abordagem, use o botão "Request Changes" do GitHub. **A reprovação sem proposta não é aceita.** É obrigatório selecionar a linha no código/texto e sugerir a alteração arquitetural ou de ferramenta para desbloquear a ideia.
