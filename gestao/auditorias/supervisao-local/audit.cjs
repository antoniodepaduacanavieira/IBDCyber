const { chromium } = require(process.env.TEMP + '/ibd-supervisao-tools/node_modules/playwright');
const { AxeBuilder } = require(process.env.TEMP + '/ibd-supervisao-tools/node_modules/@axe-core/playwright');
const fs = require('fs');
(async () => {
  const browser = await chromium.launch({ executablePath: 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe', headless: true });
  const base = 'http://127.0.0.1:4175';
  const paths = ['/pt/index.html','/en/index.html','/pt/contato/index.html','/en/contact/index.html','/pt/busca/index.html','/en/search/index.html','/pt/fpciberseg/index.html','/pt/agenda/index.html','/pt/governanca/index.html'];
  const out = { pages: [], interactions: {}, axe: [] };
  for (const width of [320,360,768,1440]) {
    const page = await browser.newPage({ viewport: { width, height: 900 } });
    for (const path of paths) {
      await page.goto(base + path, { waitUntil: 'networkidle' });
      out.pages.push({ path, width, overflow: await page.evaluate(() => document.documentElement.scrollWidth - innerWidth), title: await page.title(), h1: await page.locator('h1').count() });
    }
    await page.close();
  }
  const context = await browser.newContext({viewport:{width:360,height:800}});
  const page = await context.newPage();
  await page.goto(base+'/pt/index.html');
  await page.keyboard.press('Tab');
  out.interactions.skipFirst = await page.locator(':focus').getAttribute('class');
  const toggle = page.locator('.menu-toggle');
  await toggle.focus(); await page.keyboard.press('Enter');
  out.interactions.menuExpanded = await toggle.getAttribute('aria-expanded');
  await page.keyboard.press('Escape');
  out.interactions.menuClosed = await toggle.getAttribute('aria-expanded');
  out.interactions.focusReturned = await toggle.evaluate(el => el === document.activeElement);
  out.interactions.image = await page.locator('.carousel-slide').first().locator('img').evaluate(el=>({currentSrc:el.currentSrc,naturalWidth:el.naturalWidth,complete:el.complete}));
  await page.goto(base+'/pt/busca/index.html');
  out.interactions.searchFields = await page.locator('input').count();
  out.interactions.searchInput = await page.locator('input').first().getAttribute('placeholder');
  await page.locator('input').first().fill('formação');
  await page.locator('button[type=submit]').first().click();
  out.interactions.searchMatches = await page.locator('.search-results li').count();
  out.interactions.searchStatus = await page.locator('[data-search-status]').innerText();
  await page.locator('input').first().fill('zzzznada999');
  await page.locator('button[type=submit]').first().click();
  out.interactions.searchEmpty = await page.locator('[data-search-status]').innerText();
  for(const path of ['/pt/index.html','/en/index.html','/pt/contato/index.html','/pt/busca/index.html']){
    await page.goto(base+path,{waitUntil:'networkidle'});
    const results=await new AxeBuilder({page}).withTags(['wcag2a','wcag2aa','wcag21a','wcag21aa','wcag22aa']).analyze();
    out.axe.push({path,violations:results.violations.map(v=>({id:v.id,impact:v.impact,nodes:v.nodes.map(n=>n.target)}))});
  }
  const filePage=await context.newPage();
  await filePage.goto('file:///C:/IBDCiber/presenca-digital/portal/dist/pt/index.html');
  out.interactions.file={title:await filePage.title(),image:await filePage.locator('.carousel-slide img').first().evaluate(e=>e.naturalWidth),style:await filePage.locator('body').evaluate(e=>getComputedStyle(e).backgroundColor)};
  await filePage.close();
  await context.close();
  await browser.close();
  fs.writeFileSync('gestao/auditorias/supervisao-local/browser-results.json',JSON.stringify(out,null,2));
  console.log(JSON.stringify({pages:out.pages.length,overflows:out.pages.filter(x=>x.overflow>0),interactions:{...out.interactions,searchEmpty:out.interactions.searchEmpty.slice(-400)},axe:out.axe},null,2));
})().catch(e=>{console.error(e);process.exit(1)});
