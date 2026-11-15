const { chromium } = require(process.env.TEMP + '/ibd-supervisao-tools/node_modules/playwright');
const { spawnSync } = require('child_process');
(async () => {
 const browser = await chromium.launch({executablePath:process.env.LOCALAPPDATA+'/ms-playwright/chromium-1248/chrome-win64/chrome.exe',headless:true,args:['--remote-debugging-port=9223']});
 for (let i=1;i<=3;i++) {
  const args=[process.env.TEMP+'/ibd-supervisao-tools/node_modules/lighthouse/cli/index.js','http://127.0.0.1:4175/pt/index.html','--port=9223','--only-categories=performance,seo,accessibility','--output=json','--output-path=gestao/auditorias/supervisao-local/lighthouse-mobile-'+i+'.json','--max-wait-for-load=10000','--max-wait-for-fcp=10000','--disable-full-page-screenshot','--verbose'];
  const r=spawnSync(process.execPath,args,{encoding:'utf8',timeout:45000});
  console.log('run',i,'exit',r.status,'error',r.error?.message,'stderr',r.stderr?.slice(-1000));
 }
 await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
