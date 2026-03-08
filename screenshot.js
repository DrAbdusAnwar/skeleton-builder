const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('http://127.0.0.1:8000');
  await page.waitForTimeout(1000);
  await page.screenshot({ path: 'skeleton.png' });
  await browser.close();
})();
