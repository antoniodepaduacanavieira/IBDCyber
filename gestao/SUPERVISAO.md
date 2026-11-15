# Supervisão do portal

## Supervisor ativo dentro do projeto

Em 15/11/2026 foi criado e confirmado no projeto local IBDCyber o chat **Supervisão institucional e SEO do IBDCyber**, identificador `01a1e0aa-10d7-7372-94da-0a57fbedb84e`, host local. Este é o supervisor ativo. A troca de mensagens com o construtor foi testada e já resultou em correções de acessibilidade e descrições SEO. O chat da nuvem abaixo permanece como histórico da primeira auditoria. Os novos relatórios ficam em gestao/auditorias/supervisao-local.

Por orientação expressa do responsável, notas de produção, aprovação administrativa e instruções dirigidas ao proprietário foram removidas das páginas públicas PT/EN. Pendências internas ficam em gestao/NOTAS-EDITORIAIS-INTERNAS.md. Propostas de serviços para validação estão em gestao/PROPOSTAS-SERVICOS.md e não constituem ofertas confirmadas.

## Histórico da supervisão na nuvem

Chat: Supervisionar qualidade do portal IBDCyber.
Identificador: 6af9bf2e-ceb0-8191-928a-257b59fe4024, host durable.
Chat de construção: 01a14bf1-6c81-7531-9c69-a3f2e5536713, host local.

O responsável autorizou a comunicação entre os dois chats e o ciclo de melhoria até 95/100. A rubrica fixa e a primeira avaliação estão na branch auditoria/avaliacao-01, commit 1acdc79032e72ae0be2f44d684dff3e33ae92e63. A nota inicial é 40/100 pontos comprovados, incluindo zeros por falta de teste. Não é uma certificação nem uma nota do Google.

## Rodada de implementação, 15/11/2026

- Comunicado de 05/11 identificado como histórico, sem afirmar realização ou resultados.
- Aviso de futura audiência pública incluído PT/EN por instrução do Instituto. Data, comissão e participantes permanecem a confirmar.
- Resultado oficial do Senado ligado diretamente nas páginas da Frente e da direção, com distinção entre designação pessoal e parceria institucional.
- Política editorial proposta e canal de correção publicados, com periodicidade pendente de validação administrativa.
- Canonical, hreflang e sitemap gerados a partir de domínio configurável; navegação relativa preservada.
- Variantes WebP de fotografias com fallback PNG. Primeira imagem móvel: 31.734 bytes, contra 749.432 bytes da origem PNG.
- Legenda do carrossel e números dos cartões com contraste reforçado.
- Chat externo carregado somente por ação do visitante, com alternativa por e-mail.
- Curadoria ampliada com CAIS/RNP e fascículos CERT.br. Instruções de hospedagem e reversão documentadas.

## Evidências locais

Build e reprodução limpa aprovados. 62 HTMLs e links internos conferidos. Sitemap com 61 endereços únicos, canonicals e destinos de alternates verificados. ZIP íntegro com somente dist.

Chrome local: início a 360 e 1440 px sem overflow, WebP selecionado, ausência de requisição do chat antes de interação. Abertura da página inicial via file funcionou. Foto RSA carregou após rolagem; a captura de página inteira sem rolagem não força o carregamento de imagens lazy. Essas verificações não equivalem a auditoria integral WCAG ou a medição de dados reais de usuários.

## Limites e próxima ação

O supervisor recebeu o commit 8ce9695a27caf9ca4ddf336aad11860a7ee439fe, mas a reavaliação foi interrompida pelo limite de uso da conta. Não há nota nova aprovada e não se deve declarar 95/100. Ao retomar, avaliar o HEAD atual, que inclui a correção adicional de contraste, e repetir a mesma rubrica.

A ferramenta de movimentação recusou a associação do chat da nuvem ao projeto local IBDCyber. O menu do chat não ofereceu a opção de mover para projeto. O chat original foi preservado na nuvem; este registro mantém a referência no repositório. Não criar um substituto nem declarar que o movimento foi concluído.

Hospedagem HostGator, certificado, cabeçalhos, Search Console, leitor de tela e métricas de campo ainda exigem validação específica. SEO técnico não garante posição no Google. A publicação deve usar o ZIP da entrega, e não a raiz do repositório.
