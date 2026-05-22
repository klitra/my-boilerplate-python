# 🚀 Python Enterprise Boilerplate

Um template base de nível corporativo para projetos em Python, construído sobre a arquitetura do *Hypermodern Python*. Este boilerplate foi otimizado para automações, rotinas de governança de identidades (IAM) e pipelines de dados.

Fornece uma infraestrutura blindada de versionamento, garantindo que bancos de dados locais (SQLite) e credenciais permaneçam seguros, enquanto mantém a documentação altamente ágil e unificada através do Obsidian.

---

## 🎯 Principais Funcionalidades

* 🛡️ **Segurança por Padrão:** O `.gitignore` foi rigorosamente configurado para isolar ambientes Windows Server (IIS), bancos de dados locais (`.db`), pacotes *Air-Gapped* e variáveis de ambiente.
* 🗃️ **Isolamento de Dados (Instance Pattern):** Estrutura preparada para manter os dados operacionais, logs e credenciais na pasta `/instance`, separando a lógica de negócio dos arquivos gerados em tempo de execução.
* 🧠 **Documentação P.A.R.A (Obsidian Ready):** A pasta `/docs` abandonou geradores estáticos complexos (como o Sphinx). É agora um cofre nativo pronto para ser aberto no **Obsidian**, estruturado no método P.A.R.A (Projetos, Áreas, Recursos e Arquivos) para máxima velocidade operacional.
* ⚙️ **Qualidade de Código Automatizada:** Integração total com `pre-commit`, `nox` e `pytest` para garantir formatação, validação de tipos e testes consistentes antes de qualquer *commit*.

---

## 📂 Estrutura de Pastas e Governança

```text
meu-template-python/
 ┣ 📂 .github/           # Workflows de CI/CD para automação de testes
 ┣ 📂 docs/              # 📚 Base de Conhecimento do Obsidian (Método P.A.R.A.)
 ┃  ┣ 📂 01_Projetos/    # Iniciativas ativas com prazo (Ex: sprint_integracao_ad/)
 ┃  ┣ 📂 02_Areas/       # Manutenções permanentes da operação (Ex: active_directory/)
 ┃  ┣ 📂 03_Recursos/    # Material de apoio e scripts isolados (Ex: snippets_python/)
 ┃  ┗ 📂 04_Arquivo/     # Histórico técnico e projetos concluídos
 ┣ 📂 instance/          # 🗄️ Dados locais e sensíveis (SQLite, logs, chaves) [IGNORADO PELO GIT]
 ┣ 📂 src/               # 💻 Código-fonte principal do sistema (Scripts, APIs, Módulos)
 ┣ 📂 tests/             # Suíte de testes automatizados (Pytest)
 ┣ 📄 .pre-commit-config.yaml # Regras de formatação automática de código
 ┣ 📄 noxfile.py         # Maestro de testes multi-ambiente
 ┣ 📄 pyproject.toml     # Gestão moderna de dependências e definições do projeto
 ┗ 📄 README.md          # Este arquivo
```

---

## 🧠 Filosofia de Engenharia e Metodologia

Este boilerplate não dita apenas onde os arquivos ficam, mas **como o código deve ser construído**. Todo projeto iniciado a partir desta base deve seguir os 4 pilares da nossa engenharia:

1. **P.A.R.A. (Organização Física):** Manuais, guias de APIs e documentações de arquitetura não ficam soltos. Eles vivem no cofre do Obsidian (`/docs`).
2. **S.M.A.R.T. (Escopo Estratégico):** Nenhuma linha de código é escrita sem um objetivo claro. Todo projeto começa com um escopo Específico, Mensurável, Alcançável, Relevante e Temporal na pasta `01_Projetos/`. Se não tem prazo e métrica, não é projeto, é ideia.
3. **TDD / Método Científico (Testes):** O código deve se autoafirmar. Escrevemos a hipótese (Teste na pasta `tests/`) antes do experimento (Código na pasta `src/`). O teste falha (Red), o código prova a hipótese (Green), e a arquitetura é limpa (Refactor).
4. **P.D.C.A. (Execução Contínua):** O diário de bordo do desenvolvedor segue os ciclos de *Planejar, Testar, Medir e Ajustar*, criando um histórico imutável do **porquê** as decisões arquiteturais foram tomadas.

> 💡 **Dica:** Um template Markdown combinando S.M.A.R.T. e P.D.C.A. já está disponível para uso dentro de `docs/03_Recursos/template_projeto.md`.

---

## 🛠️ Como Utilizar Este Template (Para Novos Projetos)

1. No canto superior direito deste repositório no GitHub, clique no botão verde **"Use this template"** e selecione **"Create a new repository"**.
2. Defina o nome do seu novo projeto e clique em **Create repository**.
3. Clone o seu novo repositório para a máquina local:
   ```bash
   git clone [https://github.com/SeuUsuario/novo-projeto.git](https://github.com/SeuUsuario/novo-projeto.git)
   cd novo-projeto
   ```

---

## ⚙️ Configuração Técnica e Instalação

Siga os passos abaixo para inicializar a arquitetura rigorosa de desenvolvimento:

### 1. Criar e Ativar o Ambiente Virtual (`venv`)
Garante o isolamento das bibliotecas do projeto. Na raiz do projeto, execute:
```bash
python -m venv .venv
```

**Ativação:**
* **Windows (PowerShell):** `.venv\Scripts\Activate.ps1`
* **Windows (CMD):** `.venv\Scripts\activate.bat`
* **Linux / macOS / Git Bash:** `source .venv/bin/activate`

### 2. Instalar as Dependências (Via `pyproject.toml`)
Com o ambiente ativado, atualize as ferramentas base e instale o projeto em modo editável, juntamente com as ferramentas de desenvolvimento (como testes e *linters*):
```bash
pip install --upgrade pip setuptools wheel
pip install -e .[dev]
```
*(Nota: Dependendo do gerenciador de pacotes que escolheu ao gerar o Hypermodern, pode ser necessário utilizar o `poetry install` em vez de `pip`).*

### 3. Configurar a Automação de Qualidade (Pre-commit)
O projeto possui robôs que formatam o código automaticamente antes de cada *commit*. Ative-os com:
```bash
pre-commit install
```

### 4. Executar os Testes (Opcional)
Para validar se a estrutura foi montada corretamente e se os testes base estão passando, execute o ciclo de validação científica:
```bash
nox
```
*(O Nox irá criar ambientes temporários isolados para testar o seu código).*

---

## 🔐 Tratamento de Dados e Segurança Operacional
A segurança da infraestrutura é a nossa prioridade. Qualquer arquivo de banco de dados SQLite (`*.db`), arquivos de log rotativos ou arquivos com credenciais (`.env`, `secrets.json`) **devem obrigatoriamente** ser armazenados dentro da pasta `/instance/`. 

As regras do `.gitignore` bloqueiam proativamente o envio destes arquivos para o repositório remoto, mitigando riscos de vazamento de credenciais e garantindo compatibilidade segura com permissões restritas em servidores como o IIS (Windows Server).
