# Avaliação independente 01

Data: 15/11/2026, horário de Brasília. Base auditada: 8be7cc75a79971975ec1a4ee1ae56f7e2bdebbb5. Rubrica fixa v1 registrada ANTES da nota no commit 6368b66. Branch de relatórios: auditoria/avaliacao-01. Não houve alteração do código do portal nem de master.

## Resultado e limites

**40/100 pontos comprovados. Meta 95 não atingida.** É uma nota conservadora de evidência sob a rubrica fixa, não certificação de acessibilidade nem comparação estatística com o mercado. Os zeros por falta de teste não demonstram defeito. Não usar esta nota isolada para declarar que o produto tem apenas 40% de qualidade.

| Critério | Pontos | Estado e evidência |
| --- | ---: | --- |
| A1 | 5/5 | C: instituto, direção e contato identificam missão, origem institucional da biografia e e-mail |
| A2 | 0/5 | F: distinção pessoal/institucional correta; falta ligação direta ao documento de resultado que comprova a designação, disponível via página de reunião |
| A3 | 0/5 | F: governança informa limites documentais, mas não explicita responsável editorial e ciclo de revisão/correção |
| A4 | 0/5 | F: comunicado de 05/11 ainda em destaque sem estado histórico; não se pode afirmar que reunião ocorreu |
| B1 | 5/5 | C: 54 rotas PT/EN com alternates existentes e recíprocos, 27 pares |
| B2 | 5/5 | C: leitura comparada das áreas distingue finalidade de cursos, serviços, certificações e parcerias operacionais |
| B3 | 5/5 | C: registros e biblioteca têm resumos, origem e data de conferência; documentos externos são identificados como tais. Melhorar data própria e revisão por item é demanda editorial |
| N1 | 5/5 | C: verificador de 56 HTMLs, links internos e fragmentos sem destinos ausentes; navegação consistente |
| N2 | 5/5 | C: busca PT formação 8 resultados, EN education 6; termo inexistente gera orientação em ambos; mapa e breadcrumbs com destinos válidos |
| D1 | 5/5 | C: 32 combinações de 8 rotas e 320/360/768/1440 px sem overflow; menu móvel abre com Enter e fecha com Escape devolvendo foco; carrossel avança e pausa. Amostra não substitui teste de todo conteúdo |
| D2 | 5/5 | C: inspeção visual home PT desktop/mobile, home EN mobile, contatos PT/EN mobile; marca, azul, fundos claros, carrossel compacto e e-mail preservados |
| W1 | 0/5 | NT: menu por teclado comprovado, mas falta tarefa completa de teclado, skip link e ordem de foco |
| W2 | 0/5 | NT: não foi executado scanner automático e medição completa de contraste. Legenda clara e glifos quadrados nas capturas exigem revisão, sem generalizar efeito de fontes do ambiente |
| W3 | 0/5 | NT: reflow 320 sem overflow comprovado, mas zoom 200%, alvos e foco não oculto ainda não verificados |
| W4 | 0/5 | NT: pausa e reduced-motion comprovados, role=status da busca presente; falta leitor de tela manual |
| P1 | 0/5 | NT: faltam 3 medições móveis com throttling, LCP/CLS/TBT. Não há evidência de INP real |
| P2 | 0/5 | F: zero canonical e ausência de sitemap.xml; robots permite rastreamento; alternates relativos existem, mas falta configuração canônica para produção |
| P3 | 0/5 | F/DE: mesma imagem inicial de 749432 bytes de conteúdo em celular e desktop, sem variantes responsivas. Terceiro HostGator falhou no túnel deste ambiente, sem prova de indisponibilidade global |
| O1 | 0/5 | NT/DE: reprodução limpa e ZIP íntegro passaram; ausência real de U+2014 nos HTML/JSON/JS/CSS confirmada. Chromium bloqueou file por política administrativa; raiz testada, falta subpasta e file funcional |
| O2 | 0/5 | DE: há orientação de upload, mas rollback e configuração efetiva de HTTPS, cache, 404 e redirecionamento HostGator não testados |

Total: 40 C, 25 F, 35 NT/DE. Falhas de ambiente e testes incompletos não podem ser convertidos em pontos por conveniência. W1-W4, P1 e O1 devem primeiro ser testados pelo supervisor; não exigem alterações indiscriminadas do construtor.

## Medições e testes

Python check: 56 HTMLs aprovados. verify-clean: saída reproduzida byte a byte em diretório temporário sem dist prévia. package: integridade ZIP aprovada. Apenas dist empacotado; este ZIP é evidência da base, NÃO entrega final de versão aprovada.

Chromium instalado /usr/bin/chromium via Playwright, headless, sem throttling, viewport 900 px de altura. Capturas e JSON em avaliacao-01/. Teste de layout usou sessão com cache; seus zeros de transferência nas páginas seguintes NÃO significam carga zero. Teste de rede repetiu contextos novos em 360 e 1440 px e aguardou 1,5 segundo: 894253 bytes de recursos reportados em cada largura, 8 entradas, excluindo HTML principal e qualquer mídia carregada depois de scroll/rotação. Não é medição completa de sessão nem Core Web Vitals.

Dos recursos iniciais, gallery-p14-3.png transferiu 749732 bytes incluindo overhead local; os JP2 não apareceram nessa janela inicial. Portanto, não se deve atribuir 14 MB de carregamento inicial ao portal. Os cerca de 14 MB são tamanho em disco de assets; gallery-p14-1.png chega a cerca de 2,5 MiB e pode pesar em navegação/rotação futura. Remover JP2 sem uso reduz pacote, sem presumir ganho de primeira dobra.

HostGator start-chat.js: net::ERR_TUNNEL_CONNECTION_FAILED. O teste demonstra falha de acesso daqui, não falha do serviço para usuários da hospedagem. O código abre o chat automaticamente; testar em ambiente onde ele carregue para verificar obstrução, foco e privacidade. Não enviamos mensagens ao atendimento.

Abertura file: net::ERR_BLOCKED_BY_ADMINISTRATOR. Não houve tentativa de contornar a política. Subpasta não foi testada nesta rodada. Não declarar portabilidade completa com base somente em links válidos.

## Demandas ao construtor

Todas as correções devem ser feitas na origem, geradas e verificadas em PT/EN, preservando as regras de AGENTS.md. Não editar dist manualmente.

| Prioridade / ID | Arquivo ou página | Problema | Solução concreta | Aceite |
| --- | --- | --- | --- | --- |
| P1 / E01 | portal/source/content.json; portal/redesign.py; home e atividade de 05/11 PT/EN | destaque temporal ambíguo | Marcar comunicado como histórico: data prevista já encerrada, realização/resultados ainda não confirmados. Remover convite vigente; preservar pauta como documento histórico | Em 15/11, nenhum convite futuro para 05/11; PT/EN equivalentes; sem inventar ata ou resultados |
| P1 / E02 | portal/build.py; direção e FPCIBERSEG PT/EN | evidência da designação exige navegação extra | Acrescentar link direto ao resultado de 25/03/2025, página 2, mantendo link da reunião e explicação de designação pessoal | Nome completo e função fiéis ao PDF; não chamar parlamentares de parceiros do IBDCyber sem instrumento/fonte própria |
| P1 / E03 | portal/source/content.json; governança PT/EN | falta política editorial operável | Informar responsabilidade institucional pela publicação e canal de correção via e-mail; propor periodicidade de revisão e declarar o que aguarda validação institucional. Não inventar responsável nominal ou estatuto | Página pública com responsável institucional, revisão e canal; datas reais por registro; pendências separadas de fatos |
| P1 / T01 | portal/build.py, portable.py e configuração de produção | canonical/sitemap ausentes | Gerar sitemap XML e canonical/hreflang para domínio de produção configurável; manter links de navegação relativos e index.html; distinguir distribuição portátil e produção | URLs absolutas de metadados no domínio correto, pares recíprocos, sitemap com todas as rotas indexáveis; nenhuma URL de prévia indevida |
| P1 / T02 | portal/static/assets, redesign.py, build.py | PNG inicial grande e sem srcset | Criar variantes compatíveis WebP/AVIF com fallback, srcset/sizes, dimensões, prioridade só da primeira imagem; lazy nas demais; excluir JP2 sem referência da distribuição | HAR antes/depois em contexto sem cache: celular seleciona variante menor; imagem inicial ideal <=200 KB como orçamento de projeto, não norma universal; sem perda visual e fotos completas |
| P1 / Q01 | CSS/JS e home PT/EN | capturas exibem setas como quadrados, área RSA vazia e legenda do carrossel pálida | Reproduzir em navegadores/fontes usuais, medir contraste e testar clique/foco. Preferir SVG acessível para ícones; verificar por que fotografia RSA não aparece | Sem glifos ausentes em Chromium/Firefox, foto ou composição intencional legível, contraste AA medido; não trocar paleta ou ampliar carrossel |
| P1 / Q02 | testes de validação e página acessibilidade | evidência WCAG incompleta | Entregar mapa de tarefas teclado/zoom/contraste/leitor de tela e relatório automático sem alegar certificação; supervisor reexecuta os testes pertinentes | Menu, busca, filtro, carrossel e contato utilizáveis por teclado/leitor; resultados anunciados; foco visível e não oculto; falhas com critério WCAG e reprodução |
| P2 / O01 | ferramentas/portal.py; instruções HostGator | funcionamento subpasta/file e operação não comprovados | Registrar teste raiz/subpasta/file em ambiente permitido, instruções de backup/rollback, 404 e headers reais; chat deve carregar sob ação do usuário ou ter fallback claro | Artefato estático íntegro, sem fontes/documentos internos; rollback ensaiado em cópia; disponibilidade de terceiros testada no destino |
| P2 / C01 | biblioteca e páginas de áreas PT/EN | curadoria ainda reduzida a 4 entradas | Acrescentar seleção enxuta de fontes verificadas abaixo, por público/tema, com autor, idioma, data e utilidade; eventual atuação parlamentar deve linkar registros de contribuições reais | Cada referência útil e acessível, sem chamar curadoria de pesquisa própria, nem copiar serviços de CSIRT para o portfólio do Instituto |

## Pesquisa de fontes primárias e implicações

Consultas em 15/11/2026. Leitura direta quando possível; falhas explicitadas. São referências de desenho editorial e serviço, não parceiros do IBDCyber.

1. IBDCyber: https://www.ibdcyber.org.br/ devolveu seletor de idiomas no extrator. A rota interna /pt/index.html não abriu no serviço web; não presumir que a versão online seja igual ao commit. A autoridade institucional deve vir de identificação, governança e documentos publicáveis, não de aparência.
2. Senado, resultado de 25/03/2025: https://legis.senado.gov.br/sdleg-getter/documento/download/b0c46488-a5c9-4af2-acc7-cc2272e97218, página 2. Designação de Carlos Diego de Araújo Pinto e Lima como Secretário Executivo. Documento comprova função pessoal na ocasião, não vínculo jurídico permanente IBDCyber/FPCIBERSEG. Reunião: https://legis.senado.leg.br/atividade/comissoes/comissao/2716/reuniao/13380. Comissão eleita e participantes devem ser descritos como fatos daquela data, sem converter presença em parceria institucional.
3. PL 4752/2025: https://www25.senado.leg.br/web/atividade/materias/-/materia/170613 consultado diretamente. Página indica em tramitação, com relatoria de Jorge Seif e estado de 03/09/2026. Não é lei vigente. Registrar data da consulta; resumos institucionais não devem se apropriar da autoria parlamentar.
4. CERT.br: https://cartilha.cert.br/fasciculos/ lida diretamente. Recursos por problema concreto, PDFs e orientações de uso em https://cartilha.cert.br/orientacoes-materiais/. Aplicação: leitura prática por assunto e respeito à autoria/licença.
5. RNP/CAIS: https://www.rnp.br/servicos/cais/ lida diretamente. Separa operação, conscientização, estatísticas e alertas para a comunidade de ensino e pesquisa. Aplicação: público e escopo explícitos; IBDCyber não deve anunciar resposta a incidentes sem capacidade e autorização comprovadas.
6. ITS Rio: https://itsrio.org/pt/projetos/ e https://itsrio.org/pt/projetos/dialogos-digitais/ lidas. Projeto tem contexto e finalidade, busca permite filtrar áreas. Aplicação: fichas de projetos com evidência e contribuições identificadas, versões PT/EN coerentes.
7. Igarapé: https://ciberseguranca.igarape.org.br/sobre/ e https://igarape.org.br/temas/seguranca-digital/. Portal separa estratégia, ecossistema, cronologia e riscos. Aplicação: organizar política pública por instrumentos, atores e datas sem inferir compromissos de terceiros.
8. CCDCOE: https://ccdcoe.org/library/publications/ lida diretamente. Biblioteca separa ano, área e acesso à publicação; https://ccdcoe.org/research/ descreve escopo. Aplicação: biblioteca temática com autores e filtros, sem substituir conteúdo próprio por alegação de produção do Instituto.
9. GFCE/Cybil: https://cybilportal.org/about-cybil/ e https://cybilportal.org/content-policy/ encontrados no índice oficial, mas leitura direta retornou 502. Fonte primária complementar do parceiro: https://gcscc.ox.ac.uk/cybil-knowledge-portal. Aplicação proposta: mapa de capacidades e fichas de iniciativa; política de curadoria e não endosso. Revisar detalhes diretamente antes de publicar conteúdo derivado.
10. ENISA: https://www.enisa.europa.eu/publications consultada via índice primário, com filtros por assunto e público; leitura direta bloqueada nesta sessão. Aplicação: filtros e metadados consistentes; confirmar cada documento final antes de incluir.
11. NCSC: https://www.ncsc.gov.uk/collection/small-business-guidance--response-and-recovery/resources lida diretamente depois de 403 em outra rota. Expõe público, publicação, revisão, versão e formatos de recurso. Aplicação: páginas orientadas a tarefas com data de revisão própria; guias estrangeiros contextualizados para Brasil.
12. INCIBE: https://www.incibe.es/ciudadania lida diretamente; guia interno /ciudadania/formacion/guias retornou timeout. Arquitetura diferencia cidadania, empresas e INCIBE-CERT, incluindo transparência e canais. Aplicação: separar quem procura conhecimento, cooperação e eventual atendimento; não prometer o equivalente ao 017 espanhol.
13. Global Cyber Alliance: https://globalcyberalliance.org/work/gca-cybersecurity-toolkit/ lida diretamente. Recursos por pequenos negócios, indivíduos, jornalistas e organizações. Aplicação: trilhas de leitura por público e chamadas para ações verificáveis, sem afirmar vínculo com GCA.

## Referenciais técnicos e continuidade

WCAG 2.2: https://www.w3.org/TR/WCAG22/. Core Web Vitals: https://web.dev/articles/vitals. SEO Google: https://developers.google.com/search/docs/fundamentals/seo-starter-guide. Limiares de LCP <=2,5s, CLS <=0,1 e INP <=200ms orientam qualidade de experiência em dados de campo; TBT <=200ms é orçamento de laboratório desta rubrica e não substitui INP. A nota composta não é uma métrica publicada por essas entidades.

Autorização de coordenação confirmada por leitura do pedido original no chat local 01a14bf1-6c81-7531-9c69-a3f2e5536713, título Planejar novo portal IBDCyber. Não se copiou a conversa para o repositório.

Bloqueio factual do loop: as ferramentas disponíveis permitem read_thread e wait_threads, mas não send_message_to_thread, handoff_thread ou equivalente de envio. A descoberta por nome foi repetida e não encontrou ferramenta de envio. Portanto, este relatório não foi entregue diretamente como mensagem ao construtor. Torná-lo disponível em branch remota e fornecer o commit nesta resposta é o canal alternativo revisável. Não afirmar envio realizado ou seguir atribuindo notas a versões não recebidas. Próxima avaliação exige novo hash completo, leitura do diff e repetição dos testes afetados, com a mesma rubrica. O usuário não precisa reautorizar a supervisão.
