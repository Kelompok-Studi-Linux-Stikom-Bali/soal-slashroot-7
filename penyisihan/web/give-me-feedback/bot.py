import sys
import asyncio
from pyppeteer import launch

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

value = sys.argv

async def main():
    cookies = {'name': 'flag','value': 'slashroot7{y0u_g0t_me}'}

    browser = await launch()
    page = await browser.newPage()
    try:
        await page.goto('http://localhost/ctf_1/index.php')
        await page.setCookie(cookies)
        await asyncio.wait_for(page.evaluate(' '.join(value[1:])), timeout=5)
        
        await asyncio.sleep(3)
    finally:
        await browser.close()

loop.run_until_complete(main())
loop.close()