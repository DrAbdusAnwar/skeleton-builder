const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 375, height: 667 } });

  // Navigate to the local server
  await page.goto('http://localhost:8000/index.html');

  // Execute script to show the victory modal directly
  await page.evaluate(() => {
    // We override winGame or just show it directly
    const modal = document.getElementById('victory-modal');
    modal.style.display = 'flex';
    modal.classList.add('visible');
    modal.style.opacity = '1';
  });

  // Wait a moment for styles to apply
  await page.waitForTimeout(500);

  // Take a screenshot
  const screenshotPath = path.join(__dirname, 'victory_mobile.png');
  await page.screenshot({ path: screenshotPath, fullPage: true });

  console.log(`Screenshot saved to ${screenshotPath}`);

  await browser.close();
})();
