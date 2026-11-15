const lang=document.documentElement.lang.startsWith('pt')?'pt':'en';
const normalize=s=>s.normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase();
const menu=document.querySelector('.menu-toggle');
if(menu){const nav=document.querySelector('.nav');menu.addEventListener('click',()=>{const open=menu.getAttribute('aria-expanded')!=='true';menu.setAttribute('aria-expanded',String(open));nav.classList.toggle('open',open)});document.addEventListener('keydown',e=>{if(e.key==='Escape'&&menu.getAttribute('aria-expanded')==='true'){menu.setAttribute('aria-expanded','false');nav.classList.remove('open');menu.focus()}})}
const filterForm=document.querySelector('[data-filters]');
if(filterForm){const input=filterForm.querySelector('input');const select=filterForm.querySelector('select');const cards=[...document.querySelectorAll('[data-filter-item]')];const count=document.querySelector('.filter-count');const empty=document.querySelector('.empty');function update(){const query=normalize(input.value.trim());let found=0;cards.forEach(c=>{const show=(!query||normalize(c.textContent).includes(query))&&(!select.value||c.dataset.category===select.value);c.hidden=!show;if(show)found++});count.textContent=lang==='pt'?`${found} resultado${found===1?'':'s'}`:`${found} result${found===1?'':'s'}`;empty.hidden=found>0}input.addEventListener('input',update);select.addEventListener('change',update);filterForm.addEventListener('submit',e=>{e.preventDefault();update()});filterForm.addEventListener('reset',()=>queueMicrotask(update));update()}
const searchForm=document.querySelector('.search-form');
if(searchForm){const index=JSON.parse(document.getElementById('search-index').textContent);const input=searchForm.querySelector('input');const results=document.querySelector('.search-results');const status=document.querySelector('[data-search-status]');function render(){const q=normalize(input.value.trim());results.replaceChildren();if(!q){status.textContent=lang==='pt'?'Digite um assunto, uma atividade ou o nome de uma página.':'Enter a topic, activity or page name.';return}const tokens=q.split(/\s+/);const found=index.filter(p=>tokens.every(t=>normalize(p.title+' '+p.text).includes(t)));status.textContent=found.length?(lang==='pt'?`${found.length} resultados para “${input.value.trim()}”`:`${found.length} results for “${input.value.trim()}”`):(lang==='pt'?'Nenhum resultado. Experimente termos como formação, Parlamento ou estudos.':'No results. Try terms such as education, Parliament or research.');found.forEach(p=>{const li=document.createElement('li');const h=document.createElement('h2');const a=document.createElement('a');a.href=p.url;a.textContent=p.title;h.append(a);const desc=document.createElement('p');desc.textContent=p.description;li.append(h,desc);results.append(li)})}searchForm.addEventListener('submit',e=>{e.preventDefault();render();if(location.protocol!=='file:'){history.replaceState(null,'','?q='+encodeURIComponent(input.value.trim()))}});const initial=new URLSearchParams(location.search).get('q');if(initial){input.value=initial;render()}}

document.querySelectorAll('[data-carousel]').forEach(carousel=>{
  const slides=[...carousel.querySelectorAll('[data-slide]')];
  const dots=[...carousel.querySelectorAll('[data-slide-to]')];
  const toggle=carousel.querySelector('[data-carousel-toggle]');
  const label=carousel.querySelector('[data-rotation-label]');
  const icon=carousel.querySelector('[data-rotation-icon]');
  const timing=carousel.querySelector('[data-timing-label]');
  const progress=carousel.querySelector('.carousel-progress span');
  const viewport=carousel.querySelector('.carousel-viewport');
  const reduced=window.matchMedia('(prefers-reduced-motion: reduce)');
  const interval=Math.max(3000,Number(carousel.dataset.interval)||6000);
  let active=0,elapsed=0,last=performance.now(),paused=reduced.matches,hovered=false,inView=true;
  const text=(pt,en)=>lang==='pt'?pt:en;
  const canRotate=()=>!paused&&!hovered&&!document.hidden&&inView;
  const status=()=>{
    carousel.dataset.playback=paused?'paused':(canRotate()?'playing':'waiting');
    label.textContent=paused?text('Reproduzir','Play'):text('Pausar','Pause');
    icon.textContent=paused?'▷':'Ⅱ';
    toggle.setAttribute('aria-label',paused?text('Reproduzir carrossel','Play carousel'):text('Pausar carrossel','Pause carousel'));
    timing.textContent=paused?text('Troca automática pausada','Automatic rotation paused'):(hovered?text('Em pausa durante a leitura','Paused while reading'):text('Troca automática a cada 6 segundos','Automatic change every 6 seconds'));
    viewport.setAttribute('aria-live',paused?'polite':'off');
  };
  const show=(index,manual=false)=>{
    active=(index+slides.length)%slides.length;
    if(manual)paused=true;
    status();
    slides.forEach((slide,i)=>{slide.hidden=i!==active});
    dots.forEach((dot,i)=>dot.setAttribute('aria-pressed',String(i===active)));
    const strip=carousel.querySelector('.carousel-dots');
    const selected=dots[active];
    if(selected){
      const left=selected.offsetLeft-strip.offsetLeft;
      if(left<strip.scrollLeft)strip.scrollLeft=Math.max(0,left-8);
      else if(left+selected.offsetWidth>strip.scrollLeft+strip.clientWidth)strip.scrollLeft=left+selected.offsetWidth-strip.clientWidth+8;
    }
    carousel.querySelector('.carousel-counter').textContent=String(active+1).padStart(2,'0')+' / '+String(slides.length).padStart(2,'0');
    carousel.dataset.activeSlide=String(active+1);
    elapsed=0;last=performance.now();progress.style.transform='scaleX(0)';
  };
  toggle.addEventListener('click',()=>{paused=!paused;last=performance.now();status()});
  carousel.querySelector('[data-carousel-prev]').addEventListener('click',()=>show(active-1,true));
  carousel.querySelector('[data-carousel-next]').addEventListener('click',()=>show(active+1,true));
  dots.forEach((dot,i)=>dot.addEventListener('click',()=>show(i,true)));
  let touchStart=null;
  viewport.addEventListener('pointerdown',e=>{if(e.pointerType==='touch')touchStart={x:e.clientX,y:e.clientY}});
  viewport.addEventListener('pointerup',e=>{
    if(!touchStart)return;
    const dx=e.clientX-touchStart.x,dy=e.clientY-touchStart.y;touchStart=null;
    if(Math.abs(dx)>60&&Math.abs(dx)>Math.abs(dy)*1.5)show(active+(dx<0?1:-1),true);
  });
  viewport.addEventListener('pointercancel',()=>{touchStart=null});
  carousel.addEventListener('pointerenter',e=>{if(e.pointerType==='mouse'){hovered=true;status()}});
  carousel.addEventListener('pointerleave',()=>{hovered=false;last=performance.now();status()});
  carousel.addEventListener('focusin',e=>{if(e.target!==toggle){paused=true;status()}});
  carousel.addEventListener('keydown',e=>{
    if(e.key==='ArrowLeft'||e.key==='ArrowRight'){
      e.preventDefault();show(active+(e.key==='ArrowRight'?1:-1),true);
    }
  });
  document.addEventListener('visibilitychange',()=>{last=performance.now();status()});
  reduced.addEventListener('change',e=>{if(e.matches)paused=true;last=performance.now();status()});
  if('IntersectionObserver' in window){
    new IntersectionObserver(entries=>{inView=entries[0].isIntersecting;last=performance.now();status()},{threshold:.2}).observe(carousel);
  }
  carousel.querySelector('.carousel-controls').hidden=false;
  carousel.querySelector('.carousel-timing').hidden=false;
  show(0);
  setInterval(()=>{
    const now=performance.now(),delta=now-last;last=now;
    if(!canRotate())return;
    elapsed+=delta;
    if(elapsed>=interval)show(active+1);
    else progress.style.transform='scaleX('+elapsed/interval+')';
  },100);
});

