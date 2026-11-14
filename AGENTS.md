# Instruções para continuidade

## Objetivo

Organizar e desenvolver a presença digital do Instituto Brasileiro de Defesa Cibernética. O portal institucional é a primeira entrega e a prioridade atual. Ler README.md, CONTINUIDADE.md e gestao/STATUS.md ao retomar.

## Regras do portal

- Manter português e inglês coerentes e atualizar as páginas equivalentes.
- Não usar o caractere U+2014 nos novos textos.
- Preservar a marca, o menu azul, os fundos claros e o carrossel compacto com fotografias institucionais.
- Preservar os links internos relativos e os arquivos index.html explícitos. O site deve funcionar em qualquer domínio ou subpasta e por file://.
- Não inventar serviços, parceiros, resultados ou vínculos com a FPCIBERSEG. Registrar fontes e pendências.
- Manter o e-mail administrativo@ibdcyber.org.br destacado nas páginas de contato.
- Não inserir senhas, tokens, arquivos .env ou transcrições de conversas no repositório.
- GitHub público não significa que a publicação no Sites deva mudar de audiência.

## Implementação

Conteúdo em portal/source/content.json. Geradores em portal/build.py, redesign.py e portable.py. Recursos estáticos e estilos em portal/dist. Essa pasta contém também recursos não gerados; não apagá-la.

Usar caminhos relativos ao repositório, sem dependência de nomes de usuário ou unidades Windows. Não instalar dependências para tarefas que a biblioteca padrão do Python resolve.

Após alterações, executar python ferramentas/portal.py build e python ferramentas/portal.py check. Para gerar a entrega, executar python ferramentas/portal.py package. Verificar visualmente mudanças de interface em desktop e celular quando houver ferramenta de navegador.

## Publicação

O repositório central usa a branch master. Registrar e enviar alterações para que estejam disponíveis no próximo computador. Não sobrescrever alterações remotas nem usar push --force.

Publicação do portal e sincronização de código são operações distintas. A hospedagem externa recebe somente o conteúdo de portal/dist. Sites possui identidade própria em portal/.openai/hosting.json; preservar essa identidade e usar a skill Sites ao publicar. Não enviar a raiz do projeto como conteúdo público do site.

Ao terminar, atualizar gestao/STATUS.md com resultado, verificações realizadas e pendências reais. Não afirmar que um ambiente de nuvem está funcionando sem uma execução confirmada.
