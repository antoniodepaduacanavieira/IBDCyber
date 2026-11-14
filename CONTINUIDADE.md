# Continuar em qualquer computador

## Modelo de trabalho

GitHub guarda o código e o histórico compartilhado. Codex Cloud executa o trabalho em um computador remoto. O aplicativo Desktop é a interface de acesso. A pasta C:\IBDCiber é uma cópia de trabalho deste PC e não se sincroniza sozinha.

Não é necessário manter este computador ligado para uma tarefa que tenha sido iniciada no modo Cloud. Esta conversa começou em modo local. Instalar o Desktop em outro PC não transporta automaticamente os arquivos locais.

## Pelo Desktop, com execução em nuvem

1. Entrar na mesma conta e conectar o GitHub autorizado.
2. Escolher Work in > Cloud ao iniciar o trabalho.
3. Selecionar o repositório antoniodepaduacanavieira/IBDCyber, branch master.
4. Solicitar a leitura de AGENTS.md e gestao/STATUS.md.
5. Ao concluir cada alteração, pedir validação, commit e envio ao GitHub.

Prompt de retomada:

> Continue o projeto de presença digital do IBDCyber a partir do repositório antoniodepaduacanavieira/IBDCyber, branch master. Leia AGENTS.md, README.md e gestao/STATUS.md. O portal é a primeira entrega. Verifique o estado do Git antes de alterar arquivos, preserve os links relativos e mantenha português e inglês atualizados.

## Ambiente reutilizável

Em Settings > Codex Cloud > Environments, selecionar ou preparar um ambiente com o repositório atual e a branch master. A execução do portal necessita apenas de Python. Usar como verificação de preparação:

```sh
python3 ferramentas/portal.py build
python3 ferramentas/portal.py check
```

Para prévia dentro do ambiente, iniciar `python3 ferramentas/portal.py serve --host 0.0.0.0` e usar o mecanismo de prévia privada do ambiente. Publicar a configuração do ambiente após a preparação; isso é diferente de publicar o site.

Em 14/11/2026, foi encontrado um ambiente chamado IBDCyber ainda não executável, ligado a outro identificador de repositório e à branch main. Não presumir que esse ambiente já usa o projeto atual. O ambiente padrão apareceu disponível, mas nenhuma tarefa deste projeto foi executada nele nesta organização.

## Alternativa local em outro PC

Com Git e Python disponíveis:

```sh
git clone https://github.com/antoniodepaduacanavieira/IBDCyber.git
cd IBDCyber
python ferramentas/portal.py check
```

Abrir essa pasta no Desktop. Antes de começar em uma cópia sem alterações locais, usar `git pull --ff-only`. Se houver alterações, revisar e registrá-las antes de integrar o trabalho remoto. Ao terminar, usar commit e push. OneDrive não substitui esse fluxo de versionamento.

## Documentos de trabalho

O dossiê e o acervo completo foram reunidos localmente. Como o GitHub permanece público, esses arquivos não entram automaticamente nos novos envios. Para editá-los em outro PC, usar um armazenamento privado conectado, como o Drive já indicado no projeto, ou outro repositório privado específico. Não há sincronização desses documentos configurada por este arquivo.

Referências oficiais consultadas em 14/11/2026:

- https://learn.chatgpt.com/docs/environments/cloud-environments
- https://help.openai.com/en/articles/20001545-using-codex-cloud
