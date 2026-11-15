# IBDCyber: presença digital e projeto de IA

O portal institucional é a primeira entrega deste projeto. Este repositório reúne o código editável, as instruções de continuidade e o planejamento das próximas etapas.

## Onde trabalhar

- Repositório: https://github.com/antoniodepaduacanavieira/IBDCyber
- Pasta neste computador: `C:\IBDCiber\presenca-digital`.
- Código do portal: `portal/`.
- Site pronto para hospedagem: `portal/dist/`.
- Instruções para outro computador: [CONTINUIDADE.md](CONTINUIDADE.md).
- Situação e próximos passos: [gestao/STATUS.md](gestao/STATUS.md).
- Dossiê e acervo no Drive privado: [documentacao/ACERVO.md](documentacao/ACERVO.md).

## Estrutura

| Pasta | Conteúdo |
| --- | --- |
| `portal/source` | Conteúdo estruturado em português e inglês |
| `portal/static` | CSS, JavaScript, fotografias e marca de origem |
| `portal/dist` | Saída gerada para hospedagem |
| `.codex` | Preparação e instruções de inicialização na nuvem |
| `portal/*.py` | Geradores das páginas e conversão dos links relativos |
| `gestao` | Escopo, decisões e prioridades |
| `ferramentas` | Validação, prévia e empacotamento |
| `documentacao/historico` | Estudos e dossiê anteriores, com cópia no Drive privado |
| `acervo` | Apresentação e arquivos de marca, com cópia no Drive privado |
| `entregas` | ZIPs para hospedagem, gerados localmente ou na nuvem |

O repositório é público por decisão do responsável. Documentos de trabalho, acervo completo e credenciais ficam fora dos novos envios. As imagens e marcas necessárias ao portal permanecem em `portal/dist/assets`. Arquivos já publicados no histórico do GitHub continuam no histórico.

## Comandos

Requisito para edição e geração: Python 3.10 ou superior, apenas biblioteca padrão. O site gerado não exige Python, banco de dados ou servidor de aplicação.

```sh
python ferramentas/portal.py build
python ferramentas/portal.py verify-clean
python ferramentas/portal.py serve
python ferramentas/portal.py package
```

A prévia usa `http://127.0.0.1:4173`. No Linux, use `python3` se necessário. O comando de empacotamento inclui somente `portal/dist`, nunca a documentação interna.

Para hospedar, extraia o ZIP e envie seu conteúdo para a pasta pública do provedor. Não envie este repositório inteiro. Os links internos continuam relativos, com `index.html`, para funcionar também em subpastas e por abertura local.

## Continuidade editorial

Editar `portal/source/content.json` e executar a geração. Alterações de estrutura ficam em `portal/build.py` e `portal/redesign.py`. Os estilos, o JavaScript e os recursos visuais de origem são mantidos em `portal/static`. A pasta `portal/dist` pode ser reconstruída a partir do checkout. Não editar os arquivos gerados diretamente.

O dossiê histórico não é atualizado automaticamente quando o site muda. Para o conteúdo atual, consultar o JSON e as páginas geradas.
