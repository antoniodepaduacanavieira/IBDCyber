import json,html,re,shutil
from portable import make_portable
from redesign import render_home
from pathlib import Path
ROOT=Path(__file__).resolve().parent; DIST=ROOT/'dist'
DIST.mkdir(parents=True, exist_ok=True)
shutil.copytree(ROOT/'static', DIST, dirs_exist_ok=True)
data=json.loads((ROOT/'source/content.json').read_text(encoding='utf-8-sig'))
pages={p['id']:p for p in data['pages']}
def esc(v):return html.escape(str(v),quote=True)
def tx(lang,pt,en):return pt if lang=='pt' else en
def href(id,lang):
 if id=='home':return '/'+lang+'/'
 if id=='search':return '/'+lang+'/'+tx(lang,'busca','search')+'/'
 if id=='sitemap':return '/'+lang+'/'+tx(lang,'mapa-do-site','sitemap')+'/'
 return '/'+lang+'/'+pages[id]['slug'][lang].strip('/')+'/'
def detail(kind,item,lang):return href('knowledge' if kind=='knowledge' else 'agenda',lang)+item['id']+'/'
def link(id,lang,label=None,cls='text-link'):return f'<a class="{cls}" href="{href(id,lang)}">{esc(label or pages[id][lang]["title"])} <span aria-hidden="true">↗</span></a>'
def button(id,lang,label,secondary=False):return f'<a class="button {"secondary" if secondary else ""}" href="{href(id,lang)}">{esc(label)}<span class="arrow" aria-hidden="true">↗</span></a>'
def header(id,lang,alternate=None):
 other='en' if lang=='pt' else 'pt'
 labels={'pt':['O Instituto','Atuação e serviços','Conhecimento','FPCIBERSEG','Agenda','Cooperação','Contato'],'en':['The Institute','Our work','Knowledge','FPCIBERSEG','Events','Cooperation','Contact']}
 ids=['institute','work','knowledge','front','agenda','cooperation','contact']
 nav=''.join(f'<a href="{href(k,lang)}" {"aria-current=page" if k==id else ""}>{label}</a>' for k,label in zip(ids,labels[lang]))
 return f'''<a class="skip" href="#main">{tx(lang,'Ir para o conteúdo','Skip to content')}</a><header class="site-header"><div class="wrap"><div class="utility"><span>{tx(lang,'Instituição técnica, apartidária e sem fins lucrativos','Technical, nonpartisan and nonprofit institution')}</span><div class="lang"><span class="location">Brasília, Brasil</span><a href="{href(id,lang) if id in pages or id in ['search','sitemap'] else '#'}" aria-current="page" lang="{lang}">{lang.upper()}</a><a href="{alternate or href(id,other)}" lang="{other}" aria-label="{tx(lang,'Read this page in English','Ler esta página em português')}">{other.upper()}</a></div></div><div class="header-main"><div class="brand-row"><a class="brand" href="{href('home',lang)}" aria-label="IBDCyber {tx(lang,'início','home')}"><img src="/assets/logo-white.svg" width="128" height="84" alt="IBDCyber"><span>Instituto Brasileiro<br>de Defesa Cibernética</span></a><div class="header-actions"><a class="search-link" href="{href('search',lang)}"><span class="search-icon" aria-hidden="true"></span>{tx(lang,'Buscar','Search')}</a><button type="button" class="menu-toggle" aria-controls="navigation" aria-expanded="false">Menu</button></div></div><nav class="nav" id="navigation" aria-label="{tx(lang,'Navegação principal','Main navigation')}">{nav}</nav></div></div></header>'''
def footer(lang):
 return f'''<section class="cta-band"><div class="wrap"><div><h2>{tx(lang,'O diálogo começa com uma questão concreta.','A useful conversation starts with a specific question.')}</h2><p>{tx(lang,'Conheça os caminhos para apresentar uma pauta de pesquisa, formação ou cooperação institucional.','Explore ways to discuss a research topic, an education need or institutional cooperation.')}</p></div>{button('contact',lang,tx(lang,'Fale com o Instituto','Contact the Institute'))}</div></section><footer class="site-footer"><div class="wrap"><div class="footer-top"><div><img class="footer-brand" src="/assets/logo-white.svg" width="150" height="99" alt="IBDCyber" loading="lazy"><p>Instituto Brasileiro de Defesa Cibernética<br>{tx(lang,'Estudos, formação e diálogo sobre políticas públicas de cibersegurança.','Research, education and dialogue on cybersecurity policy.')}</p></div><div><h2>{tx(lang,'Institucional','Institution')}</h2>{link('institute',lang)}{link('governance',lang)}{link('leadership',lang)}{link('front',lang)}</div><div><h2>{tx(lang,'Informações','Information')}</h2>{link('privacy',lang)}{link('accessibility',lang)}{link('sitemap',lang,tx(lang,'Mapa do site','Site map'))}<a href="https://www.instagram.com/institutociberbr/">Instagram ↗</a></div></div><div class="footer-bottom"><span>© 2026 IBDCyber · Brasília, Brasil</span><span>{tx(lang,'Base editorial revisada em 17 de outubro de 2026','Editorial sources reviewed on 17 October 2026')}</span></div></div></footer>'''
def section_html(s,index):
 return f'<section id="section-{index}"><h2>{esc(s["heading"])}</h2>'+''.join(f'<p>{esc(p)}</p>' for p in s.get('paragraphs',[]))+('<ul>'+''.join(f'<li>{esc(x)}</li>' for x in s['items'])+'</ul>' if s.get('items') else '')+'</section>'
def resource(item,lang):
 return f'<article class="resource" data-filter-item data-category="{esc(item["topic"][lang])}"><p class="tag">{esc(item["kind"][lang])} · {esc(item["topic"][lang])}</p><h3><a href="{detail("knowledge",item,lang)}">{esc(item["title"][lang])}</a></h3><p>{esc(item["summary"][lang])}</p><a class="text-link" href="{detail("knowledge",item,lang)}">{tx(lang,"Consultar referência","Explore resource")} ↗</a></article>'
def event(item,lang):
 return f'<a class="agenda-item" data-filter-item data-category="{esc(item["type"][lang])}" href="{detail("events",item,lang)}"><time datetime="{esc(item.get("startDate",item["date"]))}">{esc(item["displayDate"][lang])}</time><div><h3>{esc(item["title"][lang])}</h3><p>{esc(item["type"][lang])}</p></div><span aria-hidden="true">↗</span></a>'
def areas(lang):
 ids=['policy','research','education','cooperation']
 return '<div class="areas">'+''.join(f'<a class="area" href="{href(id,lang)}"><span class="num">0{i+1}</span><div><h3>{esc(pages[id][lang]["title"])}</h3><p>{esc(pages[id][lang]["description"])}</p></div><span aria-hidden="true">↗</span></a>' for i,id in enumerate(ids))+'</div>'
def filters(items,key,lang):
 cats=sorted(set(x[key][lang] for x in items))
 return f'''<form class="filters" data-filters><label>{tx(lang,'Buscar nesta seção','Search this section')}<input type="search" name="q" placeholder="{tx(lang,'Palavra ou assunto','Keyword or topic')}"></label><label>{tx(lang,'Filtrar por tema','Filter by topic')}<select name="topic"><option value="">{tx(lang,'Todos os temas','All topics')}</option>{''.join('<option>'+esc(c)+'</option>' for c in cats)}</select></label><button class="button light" type="reset">{tx(lang,'Limpar','Reset')}</button></form><p class="filter-count" role="status" aria-live="polite"></p><p class="empty" hidden>{tx(lang,'Nenhum resultado nesta seleção. Limpe os filtros ou tente outro termo.','No results for this selection. Reset the filters or try another term.')}</p>'''
def heading(lang,title,eyebrow,intro,parent=None):
 return f'<section class="page-heading"><div class="wrap"><div class="breadcrumb"><a href="{href("home",lang)}">{tx(lang,"Início","Home")}</a> / '+(f'<a href="{href(parent,lang)}">{esc(pages[parent][lang]["title"])}</a> / ' if parent else '')+f'{esc(title)}</div><p class="eyebrow">{esc(eyebrow)}</p><h1>{esc(title)}</h1><p class="lead">{esc(intro)}</p></div></section>'
def standard(id,lang):
 p=pages[id][lang];sections=p['sections'];side=''.join(f'<a href="#section-{i}">{esc(s["heading"])}</a>' for i,s in enumerate(sections))
 extra=''
 if id in ['institute','governance','leadership']:extra='<div class="buttons">'+link('governance',lang)+link('leadership',lang)+'</div>'
 elif id=='work':extra=areas(lang)
 elif id=='contact':extra='<div class="buttons"><a class="button" href="https://www.instagram.com/institutociberbr/">Instagram @institutociberbr ↗</a></div>'
 elif id=='front':extra='<div class="source-box">'+tx(lang,'Registro oficial da Frente no Senado Federal','Official Senate record for the parliamentary front')+': <a href="https://www25.senado.leg.br/web/atividade/conselhos/-/conselho/FPCIBERSEG">FPCIBERSEG ↗</a><br>'+tx(lang,'Secretaria Executiva: registro de 25/03/2025','Executive Secretary: record of 25 March 2025')+': <a href="https://legis.senado.leg.br/atividade/comissoes/comissao/2716/reuniao/13380">'+tx(lang,'Consultar registro','View record')+' ↗</a></div>'
 if id in ['front','leadership']:
  extra+='<div class="source-box"><strong>'+tx(lang,'Designação pessoal documentada','Documented personal appointment')+'</strong><p>'+tx(lang,'O resultado da reunião de 25/03/2025 registra a designação de Carlos Diego de Araújo Pinto e Lima como Secretário Executivo da FPCIBERSEG. O registro comprova a função pessoal naquela data; não constitui instrumento de parceria entre o Instituto e a Frente.','The record of the meeting on 25 March 2025 names Carlos Diego de Araújo Pinto e Lima as Executive Secretary of FPCIBERSEG. It documents a personal appointment on that date; it is not a partnership agreement between the Institute and the Front.')+'</p><a href="https://legis.senado.gov.br/sdleg-getter/documento/download/b0c46488-a5c9-4af2-acc7-cc2272e97218">'+tx(lang,'Resultado oficial, página 2 (PDF)','Official meeting outcome, page 2 (PDF)')+'</a></div>'
 pic=''
 if id=='leadership':pic=f'<figure><img class="portrait" src="/assets/director.png" alt="Carlos Diego de Araújo" width="880" height="1280"><figcaption>{tx(lang,"Acervo da apresentação institucional do IBDCyber.","From the IBDCyber institutional presentation.")}</figcaption></figure>'
 listing=''
 if id=='knowledge':listing=filters(data['knowledge'],'topic',lang)+'<div class="small-grid">'+''.join(resource(x,lang) for x in data['knowledge'])+'</div>'
 if id=='agenda':listing=filters(data['events'],'type',lang)+'<div class="agenda-list">'+''.join(event(x,lang) for x in sorted(data['events'],key=lambda x:x['date'],reverse=True))+'</div>'
 if id=='front':listing='<div class="agenda-list">'+''.join(event(x,lang) for x in data['events'] if x['id'].startswith('front-'))+'</div>'
 contact_card=''
 if id=='contact':
  email=esc(pages[id]['email'])
  contact_card=f'<section class="wrap contact-primary" aria-labelledby="contact-email-heading"><div><h2 id="contact-email-heading">{tx(lang,"E-mail administrativo","Administrative email")}</h2><a class="contact-email" href="mailto:{email}">{email}<span aria-hidden="true"> ↗</span></a><p>{tx(lang,"Clique no endereço para escrever ao Instituto.","Select the address to email the Institute.")}</p></div></section>'
 return '<main id="main">'+heading(lang,p['title'],p['eyebrow'],p['intro'])+contact_card+f'<div class="wrap article-layout"><aside class="side-nav" aria-label="{tx(lang,"Nesta página","On this page")}"><h2>{tx(lang,"Nesta página","On this page")}</h2>{side}</aside><article class="body-content">{pic}{"".join(section_html(s,i) for i,s in enumerate(sections))}{listing}{extra}</article></div></main>'
home=lambda lang:render_home(lang,pages,data,tx,link,button,event,resource,areas)
index={'pt':[],'en':[]}
def save(path,title,description,body,id,lang,alternate=None):
 alt=alternate or href(id,'en' if lang=='pt' else 'pt')
 doc=f'''<!doctype html><html lang="{'pt-BR' if lang=='pt' else 'en'}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{esc(title)} | IBDCyber</title><meta name="description" content="{esc(description)}"><meta name="robots" content="index,follow"><meta name="theme-color" content="#06192b"><link rel="alternate" hreflang="{'en' if lang=='pt' else 'pt-BR'}" href="{alt}"><link rel="icon" href="/assets/logo-white.png"><link rel="stylesheet" href="/site.css"><link rel="stylesheet" href="/theme.css"><link rel="stylesheet" href="/light.css?v=contact-20261103"><script src="/site.js" defer></script></head><body>{header(id,lang,alt)}<noscript><p class="no-js">{tx(lang,'As páginas e os links funcionam sem JavaScript. Busca e filtros precisam dele para atualizar os resultados.','Pages and links work without JavaScript. Search and filters require it to update results.')}</p><style>.nav{{display:flex!important}}.menu-toggle{{display:none}}</style></noscript>{body}{footer(lang)}</body></html>'''
 out=DIST/path.strip('/')/'index.html';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(doc,encoding='utf-8')
 return doc
for lang in ['pt','en']:
 for id,p in pages.items():
  text=' '.join([p[lang]['intro']]+[str(s) for s in p[lang]['sections']]);index[lang].append({'title':p[lang]['title'],'description':p[lang]['description'],'text':text,'url':href(id,lang)})
  save(href(id,lang),p[lang]['title'],p[lang]['description'],home(lang) if id=='home' else standard(id,lang),id,lang)
 for kind in ['knowledge','events']:
  for item in data[kind]:
   parent='knowledge' if kind=='knowledge' else 'agenda';title=item['title'][lang];summary=item['summary'][lang]
   paras=item.get('body',{}).get(lang,[]) or [tx(lang,'Este material é uma referência externa selecionada para consulta. A autoria, a atualização e o conteúdo integral pertencem à instituição indicada na fonte.','This is a selected external resource. Authorship, updates and the complete content belong to the institution named as its source.')]
   label=item['topic'][lang] if kind=='knowledge' else item['type'][lang]
   body='<main id="main">'+heading(lang,title,label,summary,parent)+'<div class="wrap article-layout"><aside class="side-nav">'+link(parent,lang,tx(lang,'Voltar à listagem','Back to listing'))+'</aside><article class="body-content">'
   img='rsa' if 'rsa' in item['id'].lower() else 'mission' if 'miss' in item['id'].lower() else None
   if img:body+=f'<figure><img src="/assets/{img}.png" alt="{esc(title)}"><figcaption>{tx(lang,"Registro da apresentação institucional do IBDCyber.","Image from the IBDCyber institutional presentation.")}</figcaption></figure>'
   body+=''.join('<p>'+esc(p)+'</p>' for p in paras)
   if item.get('agenda'): body+='<h2>'+tx(lang,'Pauta','Agenda')+'</h2><ul>'+''.join('<li>'+esc(topic)+'</li>' for topic in item['agenda'][lang])+'</ul>'
   if item.get('sourceType')=='institutional-notice':
    body+='<div class="source-box"><strong>'+tx(lang,'Comunicado do IBDCyber','IBDCyber announcement')+'</strong><p>'+tx(lang,'Data do comunicado: ','Announcement date: ')+esc(item.get('sourceDate',item['date']))+'</p></div>'
   else:
    body+=f'<div class="source-box"><strong>{tx(lang,"Fonte","Source")}: {esc(item["sourceLabel"])}</strong><p><a href="{esc(item["sourceUrl"])}">{tx(lang,"Abrir documento ou página de origem","Open source document or page")} ↗</a></p><span>{tx(lang,"Referência conferida em: ","Source checked on: ")+esc(item.get("reviewedAt",item.get("date","2026-10-17")))}</span></div>'
   body+='</article></div></main>'
   save(detail(kind,item,lang),title,summary,body,parent,lang,detail(kind,item,'en' if lang=='pt' else 'pt'))
   index[lang].append({'title':title,'description':summary,'text':' '.join(paras+item.get('agenda',{}).get(lang,[])),'url':detail(kind,item,lang)})
 title=tx(lang,'Mapa do site','Site map');body='<main id="main">'+heading(lang,title,tx(lang,'Navegação','Navigation'),tx(lang,'Todas as páginas do portal em um só lugar.','All portal pages in one place.'))+'<section class="section"><div class="wrap"><ul class="sitemap-list">'+''.join('<li>'+link(id,lang)+'</li>' for id in pages)+'</ul></div></section></main>'
 save(href('sitemap',lang),title,title,body,'sitemap',lang)
 title=tx(lang,'Buscar no portal','Search the portal');payload=json.dumps(index[lang],ensure_ascii=False).replace('</','<\\/')
 body='<main id="main">'+heading(lang,title,tx(lang,'Encontre o que precisa','Find what you need'),tx(lang,'Pesquise páginas, atividades e referências por assunto.','Search pages, activities and resources by topic.'))+f'<section class="section"><div class="wrap"><form class="search-form" role="search"><label class="sr-only" for="site-search">{tx(lang,"Termo de busca","Search term")}</label><input id="site-search" type="search" name="q" required placeholder="{tx(lang,"Ex.: formação, Parlamento, cooperação","E.g. education, Parliament, cooperation")}"><button class="button" type="submit">{tx(lang,"Buscar","Search")}</button></form><p role="status" aria-live="polite" data-search-status>{tx(lang,"Digite um assunto, uma atividade ou o nome de uma página.","Enter a topic, activity or page name.")}</p><ul class="search-results"></ul><script type="application/json" id="search-index">{payload}</script></div></section></main>'
 save(href('search',lang),title,title,body,'search',lang)
(DIST/'index.html').write_text('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta http-equiv="refresh" content="0;url=/pt/"><title>IBDCyber</title></head><body><a href="/pt/">Português</a> · <a href="/en/">English</a></body></html>',encoding='utf-8')
(DIST/'404.html').write_text('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Página não encontrada | IBDCyber</title><link rel="stylesheet" href="/site.css"><link rel="stylesheet" href="/theme.css"><link rel="stylesheet" href="/light.css?v=contact-20261103"></head><body><main class="wrap section"><p class="eyebrow">IBDCyber</p><h1>Página não encontrada</h1><p>O endereço pode ter mudado. / This page could not be found.</p><a class="button" href="/pt/">Início</a> <a class="button light" href="/en/">Home in English</a></main></body></html>',encoding='utf-8')
(DIST/'content.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
(DIST/'robots.txt').write_text('User-agent: *\nAllow: /\n',encoding='utf-8')
manifest=ROOT/'.openai/hosting.json';m=json.loads(manifest.read_text(encoding='utf-8-sig'));m['static']={'directory':'dist'};manifest.write_text(json.dumps(m,indent=2),encoding='utf-8')
chat_embed = '<script src="/chat.js" defer></script>'
for page in DIST.rglob('*.html'):
 if page == DIST/'index.html': continue
 doc = page.read_text(encoding='utf-8')
 page.write_text(doc.replace('</body>', chat_embed+'</body>'), encoding='utf-8')
make_portable(DIST)
from production import enhance
enhance(DIST, ROOT)
print('Built',len(list(DIST.rglob('index.html'))),'portable HTML routes')
