# Atualização na HostGator

1. Baixar uma cópia completa da pasta pública atual, incluindo arquivos ocultos e regras existentes. Guardar o backup fora da pasta pública, com data e versão.
2. Extrair o ZIP em uma pasta de teste. O index.html deve estar na raiz, junto de pt, en e assets. Não enviar a raiz do repositório.
3. Conferir portal/source/production.json antes de gerar para outro domínio ou subpasta. canonicalBase define somente os metadados para buscadores. A navegação permanece relativa.
4. Enviar o conteúdo do ZIP à pasta pública do domínio pelo canal de hospedagem autorizado. Preservar configurações do provedor; não sobrescrever .htaccess sem revisão.
5. Testar início PT/EN, contato, busca, agenda, imagens e um endereço inexistente. Conferir HTTPS e o domínio canônico. A resposta de página inexistente deve ser HTTP 404, não 200.
6. No cPanel, verificar compressão e cache. Sugestão de operação: HTML com revalidação; imagens e CSS/JS com cache curto enquanto não houver nomes versionados. Não ativar cache anual em arquivos de mesmo nome.
7. Enviar sitemap.xml ao Google Search Console da propriedade autorizada e acompanhar indexação e Core Web Vitals. Isso não garante posição na busca.

## Reversão

Se a validação falhar, restaurar os arquivos e as configurações do backup completo, incluindo a remoção apenas dos arquivos novos identificados no inventário da entrega. Repetir os testes das páginas principais. Não apagar a pasta pública inteira sem verificar a presença de outros sistemas.

## Limites desta entrega

O ZIP é estático. Não modifica certificado, regras do servidor nem Search Console. Esses itens exigem verificação na hospedagem após o envio. O chat externo carrega somente por ação do visitante e oferece alternativa por e-mail. Não há envio simulado de formulário.
