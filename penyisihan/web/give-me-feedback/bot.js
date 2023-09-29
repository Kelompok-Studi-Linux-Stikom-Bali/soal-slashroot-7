import puppeteer from "puppeteer";

export const runBot = async(script) => {
    const browser = await puppeteer.launch({
        headless: true,
        executablePath: '/usr/bin/chromium-browser',
        args: ['--no-sandbox', '--headless', '--disable-gpu', '--disable-dev-shm-usage']
    })
    const page = await browser.newPage()
    const cookies = [{
        name: 'flag',
        value: 'slashroot7{xss_inj3ct1on}'
    }];

    await page.goto("http://localhost:3000")
    await page.setCookie(...cookies)
    await page.setContent(`<html><body>${script}</body></html>`);

    // await browser.close()
    
}