import puppeteer from "puppeteer";

export const runBot = async (username) => {
  const browser = await puppeteer.launch({
    headless: true,
    executablePath: process.env.PUPPETEER_EXECUTABLE_PATH || null,
    args: [
      "--no-sandbox",
      "--headless",
      "--disable-gpu",
      "--disable-dev-shm-usage",
    ],
  });
  const page = await browser.newPage();
  await page.goto("http://localhost:21204/");
  await page.type("#username", "admin");
  await page.type(
    "#password",
    "75918197d351421efc2b52a4fdfbe165de3ca6ff7a37090e7ca539bbeb92656e"
  );
  await page.click(".btn");

  const cookies = await page.cookies();
  const page2 = await browser.newPage();

  await page2.setCookie(...cookies);
  await page2.goto("http://localhost:21204/complain/" + username);
};
