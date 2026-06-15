import asyncio
import sys
from playwright.async_api import async_playwright
from termcolor import colored

# --- SILENT WEB SERVER TO KEEP RENDER HAPPY ---
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
class SilentHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"LIVE DATA ENGINE RUNNING")
    def log_message(self, format, *args): return

def run_web_server():
    httpd = HTTPServer(('0.0.0.0', 10000), SilentHandler)
    httpd.serve_forever()

# --- LIVE QUOTEX DATA FEED AGENT ---
async def get_live_market_stream(asset_url):
    print(colored("\n[🚀 FEED STARTING] Launching live web cloud connection...", "cyan"))
    
    async with async_playwright() as p:
        # Launch a headless cloud browser profile
        browser = await p.chromium.launch(headless=True, args=['--no-sandbox', '--disable-setuid-sandbox'])
        page = await browser.new_page()
        
        print(colored(f"[📡 CONNECTING] Loading Quotex Asset Chart: {asset_url}", "yellow"))
        try:
            # Open the public chart asset room directly
            await page.goto(asset_url, timeout=60000)
            await page.wait_for_timeout(5000) # Let animations resolve
            print(colored("[✅ CONNECTED] Live chart pipeline successfully linked!\n", "green"))
            
            print("="*65)
            print("       R4D1N PRO - LIVE CHART VECTOR DEPLOYMENT")
            print("="*65)

            while True:
                # Target the live price text block inside the Quotex canvas wrapper
                # Note: The class selector changes depending on the asset room layout
                price_element = await page.query_selector(".current-price, .chart-price-value")
                
                if price_element:
                    live_price_text = await price_element.inner_text()
                    print(colored(f"[📊 LIVE TICK DATA] Price Value: {live_price_text}", "white"))
                else:
                    print(colored("[⚠️ FEED DELAY] Scanning chart DOM structure for price elements...", "red"))
                
                # Check the price every 1 second continuously
                await asyncio.sleep(1)

        except Exception as e:
            print(colored(f"[❌ FEED ERROR] Connection dropped: {e}", "red"))
        finally:
            await browser.close()

if __name__ == "__main__":
    # Start background port handler
    threading.Thread(target=run_web_server, daemon=True).start()
    
    # Enter the direct asset trade room link you want the bot to watch live
    TARGET_ROOM_URL = "https://quotex.com/en/demo-trade" 
    
    asyncio.run(get_live_market_stream(TARGET_ROOM_URL))
