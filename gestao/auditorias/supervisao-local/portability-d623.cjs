const {chromium}=require(process.env.TEMP+'/ibd-supervisao-tools/node_modules/playwright');
const {pathToFileURL}=require('url');const path=require('path');
(async()=>{const b=await chromium.launch({executablePath:'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',headless:true});const p=await b.newPage();const o={};
for(const [name,url] of [['subpath','http://127.0.0.1:4176/site/pt/index.html'],['file',pathToFileURL(path.resolve('portal/dist/pt/index.html')).href]]){await p.goto(url);o[name]={title:await p.title(),photo:await p.locator('.carousel-slide img').first().evaluate(e=>e.naturalWidth),background:await p.locator('body').evaluate(e=>getComputedStyle(e).backgroundColor),pathways:await p.locator('.pathway-grid a').count()};await p.locator('.pathway-grid a').first().click();o[name].destination=await p.title()}
await b.close();console.log(JSON.stringify(o,null,2))})().catch(e=>{console.error(e);process.exit(1)});
