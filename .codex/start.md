# Iniciar trabalho no IBDCyber

Localize a raiz do checkout do repositório antoniodepaduacanavieira/IBDCyber. Leia AGENTS.md e gestao/STATUS.md. Use a branch master como referência e confira git status antes de editar.

Para preparar o portal, execute bash .codex/setup.sh na raiz. O projeto usa Python 3.10 ou superior e somente a biblioteca padrão; não exige pip, npm, banco de dados ou chave de API.

Para uma prévia, execute python3 ferramentas/portal.py serve --host 0.0.0.0 --port 4173 na raiz e use a prévia privada do ambiente. Não anuncie localhost como endereço público. Encerre o servidor quando não for mais necessário.

O código está em portal/source, portal/static e nos geradores Python. portal/dist é a saída gerada. Execute a geração e a validação antes de empacotar ou publicar.

Ao concluir uma alteração, atualize gestao/STATUS.md, registre os arquivos no Git e envie o commit ao repositório autorizado. Não use push --force. Manter GitHub público não autoriza tornar públicas credenciais ou documentos internos.
