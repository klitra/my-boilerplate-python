# 🚀 Python Enterprise Boilerplate

Um template base de nível corporativo para projetos em Python, construído sobre a arquitetura do *Hypermodern Python*. Este boilerplate foi otimizado para automações, rotinas de governança de identidades (IAM) e pipelines de dados.

Fornece uma infraestrutura blindada de versionamento, garantindo que bancos de dados locais (SQLite) e credenciais permaneçam seguros, enquanto mantém a documentação altamente ágil e unificada através do Obsidian.

---

## 🎯 Principais Funcionalidades

* 🛡️ **Segurança por Defeito:** O `.gitignore` foi rigorosamente configurado para isolar ambientes Windows Server (IIS), bancos de dados locais (`.db`), pacotes *Air-Gapped* e variáveis de ambiente.
* 🗃️ **Isolamento de Dados (Instance Pattern):** Estrutura preparada para manter os dados operacionais, logs e credenciais na pasta `/instance`, separando a lógica de negócio dos ficheiros gerados em tempo de execução.
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
 ┗ 📄 README.md          # Este ficheiro
Aviso de Documentação: Não coloque manuais de arquitetura, guias de APIs ou fluxogramas neste README. Abra o Obsidian, aponte para a pasta docs/ como o seu cofre e documente a arquitetura utilizando o padrão P.A.R.A.
```
🛠️ Como Utilizar Este Template (Para Novos Projetos)
No canto superior direito deste repositório no GitHub, clique no botão verde "Use this template" e selecione "Create a new repository".
Defina o nome do seu novo projeto e clique em Create repository.
Clone o seu novo repositório para a máquina local:
git clone [https://github.com/SeuUsuario/novo-projeto.git](https://github.com/SeuUsuario/novo-projeto.git)
cd novo-projeto
⚙️ Configuração Técnica e Instalação
Siga os passos abaixo para inicializar a arquitetura rigorosa de desenvolvimento:

1. Criar e Ativar o Ambiente Virtual (venv)
Garante o isolamento das bibliotecas do projeto. Na raiz do projeto, execute:

python -m venv .venv
Ativação:

Windows (PowerShell): .venv\Scripts\Activate.ps1
Windows (CMD): .venv\Scripts\activate.bat
Linux / macOS / Git Bash: source .venv/bin/activate
2. Instalar as Dependências (Via pyproject.toml)
Com o ambiente ativado, atualize as ferramentas base e instale o projeto em modo editável, juntamente com as ferramentas de desenvolvimento (como testes e linters):

pip install --upgrade pip setuptools wheel
pip install -e .[dev]
(Nota: Dependendo do gestor de pacotes que escolheu ao gerar o Hypermodern, pode ser necessário utilizar o poetry install em vez de pip).

3. Configurar a Automação de Qualidade (Pre-commit)
O projeto possui robôs que formatam o código automaticamente antes de cada commit. Ative-os com:

pre-commit install
4. Executar os Testes (Opcional)
Para validar se a estrutura foi montada corretamente e se os testes base estão a passar, execute:

nox
(O Nox irá criar ambientes temporários isolados para testar o seu código).

🔐 Tratamento de Dados e Segurança Operacional
A segurança do servidor é a nossa prioridade. Qualquer ficheiro de base de dados SQLite (*.db), ficheiros de log rotativos ou ficheiros com credenciais (.env, secrets.json) devem obrigatoriamente ser armazenados dentro da pasta /instance/.

As regras do .gitignore bloqueiam proativamente o envio destes ficheiros para o repositório remoto, mitigando riscos de fugas de credenciais e garantindo compatibilidade segura com permissões restritas em servidores como o IIS (Windows Server).
