const {chromium}=require(process.env.TEMP+'/ibd-supervisao-tools/node_modules/playwright');
const fs=require('fs');
(async()=>{
 const b=await chromium.launch({executablePath:'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',headless:true});
 const o={};
 for(const w of [360,1440]){
  const context=await b.newContext({viewport:{width:w,height:900}});
  const p=await context.newPage();let errors=[];let requests=[];
  p.on('pageerror',e=>errors.push(e.message));p.on('requestfailed',r=>errors.push(r.url()+' '+r.failure()?.errorText));
  p.on('response',r=>requests.push({url:r.url(),status:r.status(),size:Number(r.headers()['content-length']||0)}));
  await p.goto('http://127.0.0.1:4175/pt/index.html',{waitUntil:'networkidle'});
  await p.screenshot({path:'gestao/auditorias/supervisao-local/home-'+w+'.png',fullPage:false});
  o[w]={errors,requests,firstImage:await p.locator('.carousel-slide img').first().evaluate(e=>({src:e.currentSrc,loaded:e.complete,naturalWidth:e.naturalWidth})),chatRequests:requests.filter(x=>/hostgator/i.test(x.url))};
  await context.close();
 }
 const p=await b.newPage();await p.goto('http://127.0.0.1:4176/site/pt/index.html');
 o.subpath={title:await p.title(),css:await p.locator('body').evaluate(e=>getComputedStyle(e).backgroundColor),image:await p.locator('.carousel-slide img').first().evaluate(e=>e.naturalWidth)};
 await p.getByRole('link',{name:'Contato',exact:true}).first().click();o.subpath.contact=await p.title();
 await p.goto('http://127.0.0.1:4175/en/search/index.html');await p.locator('input').fill('education');await p.locator('button[type=submit]').first().click();o.englishSearch={count:await p.locator('.search-results li').count(),status:await p.locator('[data-search-status]').innerText()};
 await b.close();fs.writeFileSync('gestao/auditorias/supervisao-local/extra-results.json',JSON.stringify(o,null,2));
 console.log(JSON.stringify({mobile:o[360],desktop:o[1440],subpath:o.subpath,englishSearch:o.englishSearch},null,2));
})().catch(e=>{console.error(e);process.exit(1)});
