/* AI-assisted 2026-11-01; docs/ai-usage.md. Optional Playwright demo capture.
 * Requires playwright installed outside the runtime application dependencies.
 * Never prints or overlays passwords. Uses only the dedicated synthetic fixture.
 */
const fs = require('node:fs');
const path = require('node:path');
const { chromium } = require('playwright');
const root = path.resolve(__dirname, '..');
const config = Object.fromEntries(fs.readFileSync(path.join(root, '.env'), 'utf8')
  .split(/\r?\n/).filter(x => x && !x.startsWith('#')).map(x => {
    const i=x.indexOf('='); return [x.slice(0,i),x.slice(i+1)];
  }));
const output = path.resolve(process.env.DEMO_OUTPUT || path.join(root,'.runtime','recording'));
const base = process.env.DEMO_BASE_URL || 'http://127.0.0.1:5010';
const sleep = ms => new Promise(resolve => setTimeout(resolve,ms));

(async () => {
  fs.mkdirSync(output,{recursive:true});
  const browser = await chromium.launch({headless:true});
  const context = await browser.newContext({viewport:{width:1440,height:1000},
    recordVideo:{dir:output,size:{width:1440,height:1000}}, reducedMotion:'reduce'});
  const page = await context.newPage();
  const started = Date.now();
  async function caption(text) {
    await page.evaluate(text => {
      let box=document.querySelector('#demo-caption');
      if(!box) {
        box=document.createElement('aside'); box.id='demo-caption';
        box.style.cssText='position:fixed;bottom:0;left:0;right:0;z-index:999999;background:#102538;color:#fff;padding:18px 32px;font:20px/1.45 Arial;border-top:4px solid #61d4bd;white-space:pre-line;box-shadow:0 -4px 18px #0005';
        document.body.appendChild(box);
      }
      box.textContent='ACCOUNTABILIBUDDY · ITERATION ONE · AUTOMATED LIVE BROWSER DEMO\n'+text;
    }, text);
  }
  async function until(seconds) { await sleep(Math.max(0,seconds*1000-(Date.now()-started))); }
  async function login(name,password) {
    await page.goto(base+'/login');
    await page.getByLabel('Username',{exact:true}).fill(name);
    await page.getByLabel('Password',{exact:true}).fill(password);
    await page.getByRole('button',{name:'Sign in',exact:true}).click();
  }
  try {
    await login('iteration_leader',config.SKELETON_PASSWORD);
    await caption('Owner: Liam Pheng · Instructor: Dr. Litman\nThree slices: FR-ACCT-03 password change, FR-CHAT-04 send message, FR-CLNDR-03 delete event.\nReal local Flask server and MongoDB; fictional committed seed data. Captions describe automated actions.');
    await page.screenshot({path:path.join(output,'01-dashboard.png')});
    await until(35);
    await page.getByRole('link',{name:'Change password',exact:true}).click();
    await caption('FR-ACCT-03: the signed-in user opens Change password.\nThe server requires the current password. New passwords need 8–128 characters, uppercase, lowercase and one of !@#$%.');
    await until(47);
    await page.getByLabel('Current password',{exact:true}).fill(config.SKELETON_PASSWORD);
    await page.getByLabel('New password',{exact:true}).fill('weak');
    await page.getByRole('button',{name:'Change password',exact:true}).click();
    await page.getByRole('status').filter({hasText:'Password does not meet the secure requirements'}).waitFor();
    await caption('Handled failure: weak replacement rejected with the exact acceptance-criterion message.\nThe existing password remains unchanged. The automated tests check the stored hash.');
    await page.screenshot({path:path.join(output,'02-handled-failure.png')});
    await until(65);
    const replacement='Changed!'+require('node:crypto').randomBytes(20).toString('hex');
    await page.getByLabel('Current password',{exact:true}).fill(config.SKELETON_PASSWORD);
    await page.getByLabel('New password',{exact:true}).fill(replacement);
    await page.getByRole('button',{name:'Change password',exact:true}).click();
    await page.getByRole('status').filter({hasText:'Password changed.'}).waitFor();
    await caption('Valid replacement stored as a password hash. Existing sessions are revoked.\nThe application asks the user to sign in again; no password is shown or narrated.');
    await until(80);
    await login('iteration_leader',replacement);
    await caption('Signed in successfully with the new password.\nTests separately verify that the old password fails and a second prior session can no longer open protected pages.');
    await until(95);
    await page.getByRole('link',{name:/Iteration One Squad/}).click();
    await page.getByLabel('Message',{exact:true}).fill('Meet at Demo Field at 0600.');
    await caption('FR-CHAT-04: a unit member writes a message for this unit.\nOnly authenticated members may send. Empty messages and messages above 2000 characters are rejected server-side.');
    await until(110);
    await page.getByRole('button',{name:'Send message',exact:true}).click();
    await page.getByText('Meet at Demo Field at 0600.',{exact:true}).waitFor();
    await caption('Message sent through HTTP and persisted in MongoDB.\nThe chat shows the sender username iteration_leader and the UTC creation time. Other authorized members can read it.');
    await page.screenshot({path:path.join(output,'03-message.png')});
    await until(132);
    await page.reload();
    await page.getByText('Meet at Demo Field at 0600.',{exact:true}).waitFor();
    await caption('Refresh: the message remains because this is stored data, not a placeholder.\nTests also prove that outsiders cannot post and that HTML message content is escaped.');
    await until(155);
    await page.getByRole('link',{name:'Delete event: Practice briefing',exact:true}).click();
    await caption('FR-CLNDR-03: a leader selects Practice briefing for deletion.\nThe confirmation names the event and unit. Opening this page does not delete anything.');
    await page.screenshot({path:path.join(output,'04-confirmation.png')});
    await until(171);
    await page.getByRole('link',{name:'Cancel — keep this event',exact:true}).click();
    await page.getByRole('heading',{name:'Practice briefing',exact:true}).waitFor();
    await caption('Cancel: Practice briefing is still present.\nThe two-step workflow protects against accidental deletion. Server-side tests prove GET and cancelled actions do not mutate data.');
    await until(187);
    await page.getByRole('link',{name:'Delete event: Practice briefing',exact:true}).click();
    const deletedPath=new URL(page.url()).pathname;
    await page.getByRole('button',{name:'Confirm delete event',exact:true}).click();
    await page.getByRole('status').filter({hasText:'Calendar event deleted.'}).waitFor();
    if(await page.getByRole('heading',{name:'Practice briefing',exact:true}).count()) throw Error('Event remains');
    await page.getByRole('heading',{name:'Keep this formation',exact:true}).waitFor();
    await page.getByRole('heading',{name:'Keep this formation',exact:true}).scrollIntoViewIfNeeded();
    await caption('Confirmed: Practice briefing is deleted; Keep this formation remains.\nThe database acceptance smoke verifies removal. An invalid or already deleted event returns the specified cancellation message.');
    await page.screenshot({path:path.join(output,'05-deleted.png')});
    await until(215);
    await page.getByRole('button',{name:/Sign out/}).click();
    await login('iteration_member',config.SKELETON_PASSWORD);
    await page.goto(base+deletedPath);
    await caption('Denied role: a standard unit member attempts the same leader-only delete URL.\nHTTP 403: the server denies the request. Hiding the delete link is not the authorization control.');
    await page.screenshot({path:path.join(output,'06-denied.png')});
    await until(240);
    await page.goto(base+'/');
    await caption('VERIFIED EVIDENCE\n23 pytest tests passed, including invalid passwords, old-session revocation, message boundaries and cross-unit denial.\nLive HTTP + MongoDB acceptance passed for all three slices. CI also runs lint, secret audit, build and outage smoke.');
    await until(260);
    await caption('WHAT IS NOT DONE\nWeek 11: calendar creation and remaining unit/group membership acceptance. Week 12: accessibility and measured performance.\nWeek 13: user trials. Week 14: security/hosting hardening. No claim of complete product acceptance or production readiness.');
    await until(280);
    await caption('PROCESS STATUS\n14 actual Week 10 hours reported by Liam Pheng; no session times invented. Commits were made on November 1, not backdated.\nThis is an automated fallback recording. Liam Pheng still needs to complete and record the personal code self-review.');
    await until(300);
    const video=page.video();
    await context.close();
    await video.saveAs(path.join(output,'iteration-1-demo.webm'));
    fs.writeFileSync(path.join(output,'recording-result.json'),JSON.stringify({
      status:'passed',durationSeconds:(Date.now()-started)/1000,
      automated:true,realHttp:true,realMongoDB:true,requirements:['FR-ACCT-03','FR-CHAT-04','FR-CLNDR-03']},null,2));
    console.log('RECORDING PASS: five-minute real-browser demo saved.');
  } finally { await browser.close(); }
})().catch(error=>{console.error(error.message);process.exitCode=1;});
