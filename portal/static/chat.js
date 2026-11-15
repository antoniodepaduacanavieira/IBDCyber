(() => {
  const pt = document.documentElement.lang.startsWith('pt');
  const panel = document.createElement('aside');
  panel.className = 'chat-access';
  const button = document.createElement('button');
  button.type = 'button';
  button.textContent = pt ? 'Abrir atendimento' : 'Open support chat';
  const status = document.createElement('p');
  status.setAttribute('role', 'status');
  status.textContent = pt ? 'Serviço externo HostGator. Carregado somente ao abrir.' : 'External HostGator service. Loaded only when opened.';
  const email = document.createElement('a');
  email.href = 'mailto:administrativo@ibdcyber.org.br';
  email.textContent = pt ? 'Prefiro enviar e-mail' : 'Contact by email';
  panel.append(button, status, email);
  document.querySelector('.site-footer')?.prepend(panel);
  let chat;
  button.addEventListener('click', async () => {
    button.disabled = true;
    status.textContent = pt ? 'Carregando atendimento…' : 'Loading support…';
    try {
      if (!chat) {
        const {default: BubbleChat} = await import('https://agent-factory-chat.hostgator.io/scripts/start-chat.js');
        chat = new BubbleChat('90521b22-a546-4a0b-bc18-68b1fd8d50ff', 'prod');
      }
      chat.open();
      status.textContent = pt ? 'Atendimento solicitado. Se não abrir, use o e-mail abaixo.' : 'Chat requested. If it does not open, use the email below.';
    } catch {
      status.textContent = pt ? 'Atendimento indisponível. Entre em contato por e-mail.' : 'Chat unavailable. Please contact us by email.';
    } finally { button.disabled = false; }
  });
})();
