# Rubrica fixa v1

Fixada em 15/11/2026 antes da pontuação. Base inicial: 8be7cc75a79971975ec1a4ee1ae56f7e2bdebbb5. Avaliação independente de qualidade do portal, sem certificação WCAG ou endosso das organizações citadas.

Cada subcritério é binário: integral apenas se todos os testes descritos passarem; zero se falhar ou não for testado. Usar C (comprovado), F (falhou), NT (não testado), DE (dependência externa). NT e DE sem evidência não recebem pontos. Não mudar pesos durante o loop. Meta 95 exige 95 pontos efetivamente comprovados. Correções somente em relatórios nesta branch.

| ID | Peso | Critério objetivo, evidência e teste |
| --- | ---: | --- |
| A1 | 5 | Identidade, missão, direção e contato identificados com origem declarada, conferir páginas instituto/direção/contato PT/EN |
| A2 | 5 | Relação parlamentar pessoal separada da institucional, ligação direta a documento primário que sustenta a designação e data |
| A3 | 5 | Governança com responsável editorial, política de atualização e canal de correção públicos; sem parceiros ou resultados sem prova |
| A4 | 5 | Agenda e proposições com data, fonte primária e estado temporal correto; passado não apresentado como convite vigente |
| B1 | 5 | Todas as rotas editoriais têm equivalente PT/EN e seletor leva à mesma página |
| B2 | 5 | Conteúdo de serviços, pesquisas e cooperação distingue oferta atual, intenção e referência externa; leitura comparada PT/EN |
| B3 | 5 | Biblioteca e agenda com fonte, data, resumo útil e distinção entre publicação própria e curadoria em todos os itens |
| N1 | 5 | Todos os links e fragmentos internos válidos; home, contato e idioma alcançáveis por navegação consistente |
| N2 | 5 | Busca entrega resultado relevante e vazio compreensível; mapa e breadcrumbs funcionam; testes PT/EN |
| D1 | 5 | Sem overflow ou colisão nas páginas home, conteúdo longo, busca e contato a 360/768/1440 px; menu e carrossel operáveis |
| D2 | 5 | Marca, fundos claros, menu azul, carrossel compacto e e-mail destacado preservados por inspeção visual PT/EN |
| W1 | 5 | Teclado: menu, busca e carrossel, ordem de foco, skip link e foco visível sem aprisionamento; WCAG 2.1.1, 2.4.3, 2.4.7 |
| W2 | 5 | Contraste texto 4,5:1 normal/3:1 grande, controles 3:1; nomes acessíveis, idioma, títulos, alt e landmarks; análise automática e amostra manual |
| W3 | 5 | Reflow 320 CSS px, zoom 200%, alvos 24 CSS px ou exceção, foco não oculto; WCAG 1.4.10, 1.4.4, 2.5.8, 2.4.11 |
| W4 | 5 | Carrossel pausa/redução de movimento, mensagens de busca anunciadas e leitura de tela manual das tarefas essenciais; WCAG 2.2.2, 4.1.3 |
| P1 | 5 | Três execuções móveis de laboratório documentadas: mediana LCP <=2,5s, CLS <=0,1, TBT <=200ms; bytes/requisições e configuração registrados. INP de campo separado e não inferido de TBT |
| P2 | 5 | Titles/descriptions únicos e úteis, lang, headings, canonical/hreflang/sitemap consistentes com domínio de produção confirmado; sem bloquear indexação indevidamente |
| P3 | 5 | Carga real de imagens adequada ao viewport, formatos compatíveis, dimensões e lazy load fora da dobra; sem erros de rede/JS próprios nem chat aberto intrusivo |
| O1 | 5 | Build limpo reproduz saída; links relativos explícitos funcionam em raiz, subpasta e file; ausência real de U+2014; teste de ZIP íntegro só com dist |
| O2 | 5 | Instrução HostGator, rollback, 404, HTTPS/cache/redirecionamentos e dependências de terceiros verificadas no ambiente aplicável; chat indisponível não vendido como operacional |

Referenciais: WCAG 2.2 (https://www.w3.org/TR/WCAG22/), métricas Core Web Vitals (https://web.dev/articles/vitals), SEO Google (https://developers.google.com/search/docs/fundamentals/seo-starter-guide). TBT é proxy de laboratório, não INP. Referências institucionais orientam arquitetura e evidência editorial, não conferem certificação à nota composta. Headers e disponibilidade do domínio são DE até teste na hospedagem efetiva.
