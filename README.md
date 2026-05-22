# 🚀 Python Enterprise Boilerplate

Um template base de nível corporativo para projetos em Python, construído sobre a arquitetura do *Hypermodern Python*. Este boilerplate foi otimizado para automações, rotinas de governança de identidades (IAM) e pipelines de dados.

Fornece uma infraestrutura blindada de versionamento, garantindo que bancos de dados locais (SQLite) e credenciais permaneçam seguros, enquanto mantém a documentação altamente ágil e unificada através do Obsidian.

---

## 🎯 Principais Funcionalidades

* 🛡️ **Segurança por Padrão:** O `.gitignore` foi rigorosamente configurado para isolar ambientes Windows Server (IIS), bancos de dados locais (`.db`), pacotes *Air-Gapped* e variáveis de ambiente.
* 🗃️ **Isolamento de Dados (Instance Pattern):** Estrutura preparada para manter os dados operacionais, logs e credenciais na pasta `/instance`, separando a lógica de negócio dos arquivos gerados em tempo de execução.
* 🧪 **Ambiente Otimizado para PoCs (Sandbox):** Pasta isolada para experimentações rápidas, análises com Pandas ou scripts de rascunho com Playwright, impedindo que códigos experimentais poluam o diretório de produção.
* 🧠 **Documentação P.A.R.A (Obsidian Ready):** A pasta `/docs` abandonou geradores estáticos complexos (como o Sphinx). É agora um cofre nativo pronto para ser aberto no **Obsidian**, estruturado no método P.A.R.A (Projetos, Áreas, Recursos e Arquivos) para máxima velocidade operacional.
* ⚙️ **Qualidade de Código Automatizada:** Integração total com `pre-commit`, `nox` e `pytest` para garantir formatação, validação de tipos e testes consistentes antes de qualquer *commit*.

---

## 📂 Estrutura de Pastas e Governança

```text
meu-template-python/
 ┣ 📂 .github/           # Workflows de CI/CD para automação de testes na nuvem
 ┣ 📂 docs/              # 📚 Base de Conhecimento do Obsidian (Método P.A.R.A.)
 ┃  ┣ 📂 01_Projetos/    # Iniciativas ativas com prazo (Ex: sprint_integracao_ad/)
 ┃  ┣ 📂 02_Areas/       # Manutenções permanentes da operação (Ex: active_directory/)
 ┃  ┣ 📂 03_Recursos/    # Material de apoio, snippets e templates organizacionais
 ┃  ┗ 📂 04_Arquivo/     # Histórico técnico, projetos concluídos e POCs depreciadas
 ┣ 📂 instance/          # 🗄️ Dados locais e sensíveis (SQLite, logs, chaves) [IGNORADO PELO GIT]
 ┣ 📂 sandbox/           # 🧪 Caixa de Areia (POCs, testes de hipóteses, scripts isolados e notebooks)
 ┣ 📂 src/               # 💻 Código-fonte principal e homologado (Scripts, APIs, Módulos)
 ┣ 📂 tests/             # Suíte de testes automatizados de produção (Pytest)
 ┣ 📄 .pre-commit-config.yaml # Regras de formatação automática de código
 ┣ 📄 noxfile.py         # Maestro de testes multi-ambiente
 ┣ 📄 pyproject.toml     # Gestão moderna de dependências e definições do projeto
 ┗ 📄 README.md          # Este arquivo
```

> **Aviso de Documentação:** Não coloque manuais de arquitetura, guias de APIs ou fluxogramas neste `README`. Abra o Obsidian, aponte para a pasta `docs/` como o seu cofre e documente a arquitetura utilizando o padrão P.A.R.A.

---

## 🧠 Fluxo Ciclo de Vida: Da Ideia à Produção (POC-PARA-SMART-TDD-PDCA)

Este boilerplate implementa um pipeline rigoroso de desenvolvimento baseado no **Método Científico**, garantindo que apenas códigos validados e seguros cheguem ao ambiente de produção. O ciclo de vida segue o fluxo sequencial abaixo:

```text
 [ 🔬 1. POC (Sandbox) ] ──> Validação rápida de viabilidade na pasta sandbox/
         │
         ├─(Solução Trivial) ──> [ ⏩ FAST-TRACK ] ──> Arquivar em docs/03_Recursos/
         │
         ▼ (Integração Complexa)
 [ 📂 2. P.A.R.A. ]      ──> Classificação e abertura da nota em docs/01_Projetos/
         │
         ▼ (Métricas Definidas)
 [ 📐 3. S.M.A.R.T. ]    ──> Definição de alvos claros, restrições e prazo limite
         │
         ▼ (Desenvolvimento Inverso)
 [ 🔬 4. TDD ]           ──> Criação do Teste (Red) ➔ Código Mínimo (Green) ➔ Refatoração
         │
         ▼ (Diário de Bordo)
 [ 🔄 5. P.D.C.A. ]      ──> Ciclo Local ➔ Git Push ➔ Validação em Nuvem (GitHub Actions)
```

### Detalhamento das Etapas:
1. **🔬 POC (Sandbox):** Toda ideia começa como um experimento livre na pasta `sandbox/`. O objetivo é provar a viabilidade técnica. **Regra de Fast-Track:** Se a solução for trivial (snippet rápido), ela pula a burocracia e vai direto para a pasta `03_Recursos/`.
2. **📂 P.A.R.A. (Organização Física):** Se a POC for bem-sucedida e complexa, o projeto ganha uma casa física no cofre do Obsidian (`docs/01_Projetos/`), centralizando o conhecimento.
3. **📐 S.M.A.R.T. (Escopo Estratégico):** O projeto é formalizado estabelecendo critérios Específicos, Mensuráveis, Alcançáveis, Relevantes e Temporais. 
4. **🔬 TDD (Validação Científica):** O código definitivo na pasta `src/` nasce testado (`tests/`). Para pipelines de dados (ex: Pandas), aplicamos o **TDD Orientado a Dados**, focando em Validação de Esquemas (Schema Validation) para garantir a formatação correta de colunas e tipos antes do processamento.
5. **🔄 P.D.C.A. (Execução Contínua):** Incrementos técnicos seguem o ciclo *Planejar, Testar, Medir, Ajustar*. O ciclo (Act) só é considerado concluído quando o código sofre o `git push` e os robôs de CI/CD (GitHub Actions) testam e aprovam a integração em ambiente neutro.

> 💡 **Dica:** O documento base completo unificando este fluxo de ciclo de vida está disponível para uso em `docs/03_Recursos/template_poc_fluxo.md`.

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

## ⚙️ Configuração Técnico-Operacional

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

### 3. Configurar a Automação de Qualidade (Pre-commit)
O projeto possui robôs que formatam o código automaticamente antes de cada *commit*. Ative-os com:
```bash
pre-commit install
```

### 4. Executar os Testes (Opcional)
Para validar se a estrutura foi montada corretamente e se os testes base estão passando, execute o ciclo de validação científica local:
```bash
nox
```

---

## 🔐 Tratamento de Dados e Segurança Operacional
A segurança da infraestrutura é a nossa prioridade. Qualquer arquivo de banco de dados SQLite (`*.db`), arquivos de log rotativos ou arquivos com credenciais (`.env`, `secrets.json`) **devem obrigatoriamente** ser armazenados dentro da pasta `/instance/`. 

As regras do `.gitignore` bloqueiam proativamente o envio destes arquivos para o repositório remoto, mitigando riscos de vazamento de credenciais e garantindo compatibilidade segura com permissões restritas em servidores como o IIS (Windows Server).
