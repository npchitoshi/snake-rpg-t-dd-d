1. Criação e Ativação do Ambiente Virtual

python -m venv venv

Windows
.venv\Scripts\activate

Linux / Mac
source .venv/bin/activate
source .venv/Scripts/activate

2. Instalação das Dependências

pip install -e ".[dev]"