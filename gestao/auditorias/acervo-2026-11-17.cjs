// Re-run with a local portal preview at port 4177 and Playwright/axe available.
const {chromium}=require(process.env.TEMP+'/ibd-supervisao-tools/node_modules/playwright');
const {AxeBuilder}=require(process.env.TEMP+'/ibd-supervisao-tools/node_modules/@axe-core/playwright');
const fs=require('fs');
(async()=>{
 const browser=await chromium.launch({executablePath:'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',headless:true});
 const out={layout:[],filters:[],axe:[],externalChatRequests:[]};
 const paths=['pt','en','pt/conhecimento','en/knowledge','pt/governanca','en/governance','pt/privacidade','en/privacy','pt/agenda/requerimento-102-2026-ia-ciberseguranca','en/activity/requerimento-102-2026-ia-ciberseguranca'];
 for(const width of [360,1440]){
  const context=await browser.newContext({viewport:{width,height:900}});
  const p=await context.newPage();
  p.on('request',r=>{if(/hostgator|start-chat|chat\.js/.test(r.url()))out.externalChatRequests.push(r.url())});
  for(const path of paths){
   await p.goto('http://127.0.0.1:4177/'+path+'/index.html');
   await p.evaluate(async()=>{await Promise.all(document.getAnimations().map(a=>a.finished.catch(()=>{})))});
   out.layout.push({path,width,overflow:await p.evaluate(()=>document.documentElement.scrollWidth-innerWidth),h1:await p.locator('h1').count()});
   if(path==='pt'||path==='en'){
    const above=await p.evaluate(()=>document.querySelector('.hearing-spotlight').getBoundingClientRect().bottom<=document.querySelector('[data-carousel]').getBoundingClientRect().top);
    if(!above)throw Error('Announcement is not above carousel');
    if(await p.locator('.spotlight-bar').count()!==1)throw Error('Duplicate announcement');
    await p.screenshot({path:'entregas/audiencia-'+path+'-'+width+'.png',fullPage:false});
   }
   if(width===360){const a=await new AxeBuilder({page:p}).withTags(['wcag2a','wcag2aa','wcag21aa','wcag22aa']).analyze();out.axe.push({path,violations:a.violations.map(v=>({id:v.id,nodes:v.nodes.map(n=>n.target)}))})}
   if(path.includes('conhecimento')||path.includes('knowledge')){
    if(await p.locator('.resource').count()!==48)throw Error('Incorrect resource count');
    await p.locator('[data-filters] input').fill('LGPD');const found=await p.locator('.resource:visible').count();
    if(!found)throw Error('LGPD not found');
    await p.locator('[data-filters] input').fill('xyz-no-match-231');if(!await p.locator('.empty').isVisible())throw Error('Empty state missing');
    await p.locator('[data-filters] button').click(); await p.waitForFunction(()=>document.querySelectorAll('.resource:not([hidden])').length===48);
    const options=await p.locator('[data-filters] option').allTextContents();
    for(const topic of options.slice(1)){await p.locator('[data-filters] select').selectOption({label:topic});if(!await p.locator('.resource:visible').count())throw Error('Empty topic '+topic)}
    await p.locator('[data-filters] button').click(); await p.waitForFunction(()=>document.querySelectorAll('.resource:not([hidden])').length===48);
    out.filters.push({path,width,count:48,topics:options.length-1,lgpd:found,emptyAndReset:true});
    if(path.startsWith('pt'))await p.screenshot({path:'entregas/acervo-'+width+'.png',fullPage:false});
   }
  }
  await p.goto('http://127.0.0.1:4177/pt/conhecimento/lgpd/index.html');
  await p.getByRole('link',{name:'EN: Read this page in English'}).click();
  if(!p.url().endsWith('/en/knowledge/lgpd/index.html'))throw Error('Language equivalent wrong');
  await p.goto('http://127.0.0.1:4177/pt/busca/index.html?q=NIST');if(!await p.locator('.search-results li').count())throw Error('Global search missing NIST');
  await p.close();
 }
 const p=await browser.newPage();
 await p.goto('file:///'+process.cwd().replaceAll('\\','/')+'/portal/dist/pt/conhecimento/index.html');
 await p.locator('[data-filters] input').fill('NIST');out.fileResults=await p.locator('.resource:visible').count();if(!out.fileResults)throw Error('File search failed');
 await browser.close();
 fs.writeFileSync('gestao/auditorias/acervo-2026-11-17.json',JSON.stringify(out,null,2));
 console.log(JSON.stringify(out));
 if(out.layout.some(x=>x.overflow>0||x.h1!==1)||out.axe.some(x=>x.violations.length)||out.externalChatRequests.length)process.exit(1);
})().catch(e=>{console.error(e);process.exit(1)});
