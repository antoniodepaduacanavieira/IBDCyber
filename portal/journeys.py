"""Public-facing routes, parliamentary evidence and event grouping."""
from html import escape


def pathways(lang, href):
    pt = lang == 'pt'
    entries = [
        ('front', 'Parlamento e assessorias', 'Parliament and staff', 'Consulte a agenda parlamentar e seus registros oficiais.', 'Explore the parliamentary agenda and official records.'),
        ('knowledge', 'Gestores e pesquisadores', 'Managers and researchers', 'Encontre referências para estudar políticas e segurança digital.', 'Find resources on policy and digital security.'),
        ('contact', 'Cidadãos e imprensa', 'Public and media', 'Conheça o Instituto e encontre o canal para sua pergunta.', 'Learn about the Institute and find a contact for your enquiry.')]
    cards = ''.join(f'<a href="{href(key,lang)}"><h3>{a if pt else b}</h3><p>{c if pt else d}</p><span aria-hidden="true">→</span></a>' for key,a,b,c,d in entries)
    return '<section class="pathways"><div class="wrap"><h2>'+('Encontre seu caminho' if pt else 'Find your way')+'</h2><div class="pathway-grid">'+cards+'</div></div></section>'


def timeline(events, lang, detail):
    pt = lang == 'pt'
    cards = []
    for item in sorted((x for x in events if x['id'].startswith('front-')), key=lambda x:x['date']):
        cards.append(f'<li><time datetime="{escape(item["date"])}">{escape(item["displayDate"][lang])}</time><span class="timeline-status">'+('Registro parlamentar' if pt else 'Parliamentary record')+f'</span><h3><a href="{detail("events",item,lang)}">{escape(item["title"][lang])}</a></h3><p>{escape(item["summary"][lang])}</p><a class="text-link" href="{escape(item["sourceUrl"])}">'+('Consultar fonte oficial' if pt else 'View official source')+'</a></li>')
    return '<section class="parliament-timeline"><h2>'+('Marcos da agenda parlamentar' if pt else 'Parliamentary milestones')+'</h2><ol>'+''.join(cards)+'</ol></section>'


def agenda_groups(events, lang, event):
    pt = lang == 'pt'
    groups = [('Próximas pautas e atividades','Upcoming matters and activities', [x for x in events if x['type']['en'] in ('In preparation','Proposed hearing')]), ('Histórico e comunicados anteriores','Past records and announcements',[x for x in events if x['type']['en'] not in ('In preparation','Proposed hearing')])]
    return ''.join('<section class="agenda-group"><h2>'+(a if pt else b)+'</h2><div class="agenda-list">'+''.join(event(x,lang) for x in sorted(items,key=lambda x:x['date'],reverse=True))+'</div></section>' for a,b,items in groups)
