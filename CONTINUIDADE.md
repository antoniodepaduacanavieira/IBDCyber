# Continuar em qualquer computador

## Pelo Codex Desktop, com execução em nuvem

1. Entrar na mesma conta usada para configurar este projeto.
2. Ao iniciar um trabalho, selecionar Cloud no seletor de local de execução.
3. Escolher o ambiente **IBDCyber - Presença digital**. Ele usa o repositório antoniodepaduacanavieira/IBDCyber, branch master.
4. Pedir a leitura de AGENTS.md, README.md e gestao/STATUS.md antes de alterar arquivos.
5. Ao concluir uma alteração, pedir validação, commit e envio ao GitHub. Alterações ainda não enviadas não devem ser consideradas disponíveis para outras sessões.

Prompt de retomada:

> Continue o projeto de presença digital do IBDCyber. Leia AGENTS.md, README.md e gestao/STATUS.md no repositório IBDCyber. Verifique o estado do Git e use a branch master como referência. O portal é a primeira entrega. Preserve os links relativos e mantenha português e inglês coerentes. Valide as alterações, registre o estado do projeto e envie o trabalho concluído ao GitHub.

O ambiente foi publicado e confirmado como executável em 15/11/2026. Seu identificador é `a91f01b4-a15b-4ef6-99a6-55e606bf1557~asenvcfg_ca46f17856308191b74015dc2c2162fb`. Não selecionar a configuração antiga chamada apenas IBDCyber, que continua não executável e aponta para uma referência anterior.

## O que fica na nuvem

- GitHub público: código, histórico, planejamento e instruções de continuidade.
- Codex Cloud: execução remota e configuração reutilizável de preparação.
- Google Drive privado: dossiê e acervo de trabalho. Links e recuperação em [documentacao/ACERVO.md](documentacao/ACERVO.md).
- GitHub Actions: geração, verificação e ZIP do portal a cada envio de código para master.

Não é necessário manter este PC ligado para uma tarefa iniciada na nuvem. A pasta C:\IBDCiber é uma cópia local e não se sincroniza sozinha. O login no Desktop não transporta arquivos locais nem concede acesso à conta Google; conectar o Drive autorizado quando precisar do acervo.

Esta conversa começou localmente. Para continuar a execução em nuvem, selecionar o ambiente acima. As instruções permanentes estão no repositório e não dependem de reler todo este chat.

## Preparação e prévia

O ambiente contém instruções de instalação e inicialização. O checkout é montado em `/workspace/IBDCyber`. Na raiz:

```sh
bash .codex/setup.sh
python3 ferramentas/portal.py serve --host 0.0.0.0 --port 4173
```

Usar a prévia privada do ambiente para consultar `/pt/index.html` e `/en/index.html`. Para uma entrega de hospedagem:

```sh
python3 ferramentas/portal.py package
```

O ZIP fica em entregas. Publicar a configuração do ambiente não publica o portal em ibdcyber.org.br. A hospedagem externa recebe somente o conteúdo de portal/dist pelo canal autorizado.

## Alternativa local

Neste PC, abrir `C:\IBDCiber\presenca-digital`. Em outro PC com Git e Python 3.10 ou superior:

```sh
git clone https://github.com/antoniodepaduacanavieira/IBDCyber.git
cd IBDCyber
python ferramentas/portal.py build
python ferramentas/portal.py verify-clean
```

Antes de começar em uma cópia sem alterações locais, usar `git pull --ff-only`. Se houver alterações, revisar e registrá-las antes de integrar o trabalho remoto. Não usar push forçado. OneDrive não substitui esse versionamento.

## Verificações realizadas

A preparação executou no Codex Cloud com Python 3.12: geração, 56 páginas HTML, links internos, e-mail bilíngue, reprodução limpa da saída e integridade do ZIP. As páginas iniciais responderam com HTTP 200. A publicação foi confirmada pela listagem de ambientes como pronta e executável. Uma nova tarefa independente após a publicação ainda não foi iniciada nesta entrega.

Referências oficiais consultadas em 14/11/2026:

- https://learn.chatgpt.com/docs/environments/cloud-environments
- https://help.openai.com/en/articles/20001545-using-codex-cloud
