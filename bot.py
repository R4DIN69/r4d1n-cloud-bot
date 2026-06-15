import time
import requests
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from termcolor import colored

# --- SILENT WEB SERVER FOR RENDER COMPATIBILITY ---
class SilentHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"R4D1N PRO API ENGINE IS LIVE.")
    def log_message(self, format, *args): return

def run_web_server():
    httpd = HTTPServer(('0.0.0.0', 10000), SilentHandler)
    httpd.serve_forever()

# --- REAL-TIME MARKET STRATEGY ENGINE ---
def get_live_price(symbol):
    try:
        # Pulls live financial ticker data instantly via public API
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
        response = requests.get(url, timeout=5)
        data = response.json()
        return float(data['price'])
    except:
        return None

def analyze_market_momentum(symbol):
    # Fetch price updates to detect direction
    p1 = get_live_price(symbol)
    time.sleep(1)
    p2 = get_live_price(symbol)
    
    if p1 and p2:
        change = p2 - p1
        if change > 0:
            return "🟢 CALL (UP)", "BULLISH MOMENTUM DETECTED"
        elif change < 0:
            return "🔴 PUT (DOWN)", "BEARISH MOMENTUM DETECTED"
    return "⚪ HOLD", "MARKET STAGNANT"

def start_r4d1n_engine():
    # Clean mobile-optimized ASCII layout
    print(colored("\n██████╗ ██╗  ██╗██████╗  ██╗███╗   ██╗    ██████╗ ██████╗  ██████╗ ", "cyan"))
    print(colored("██╔══██╗██║  ██║██╔══██╗███║████╗  ██║    ██╔══██╗██╔══██╗██╔═══██╗", "cyan"))
    print(colored("██████╔╝███████║██║  ██║╚██║██╔██╗ ██║    ██████╔╝██████╔╝██║   ██║", "cyan"))
    print(colored("██╔══██╗╚════██║██║  ██║ ██║██║╚██╗██║    ██╔═══╝ ██╔══██╗██║   ██║", "cyan"))
    print(colored("██║  ██║     ██║██████╔╝ ██║██║ ╚████║    ██║     ██║  ██║╚██████╔╝", "cyan"))
    print(colored("╚═╝  ╚═╝     ╚═╝╚═════╝  ╚═╝╚═╝  ╚═══╝    ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ", "cyan"))
    print("="*68)
    print("                R4D1N PRO - LIVE API STREAM CORE")
    print("="*68)
    
    # Using BTCUSDT as a high-speed live benchmark for accurate directional testing
    TARGET_ASSET = "BTCUSDT" 
    print(colored(f"[📡 STREAM ACTIVE] Streaming live ticks for target: {TARGET_ASSET}\n", "yellow"))
    
    while True:
        # Wait for the candle close block setup
        current_sec = time.localtime().tm_sec
        if current_sec >= 54:
            direction, reason = analyze_market_momentum(TARGET_ASSET)
            target_min = (time.localtime().tm_min + 1) % 60
            entry_time = f"{time.strftime('%H')}:{target_min:02d}:00"
            
            print(colored("»"*68, "white"))
            print(colored(f" ⚡ LIVE SURESHOT SIGNAL -> TARGET: {TARGET_ASSET}", "cyan", attrs=["bold"]))
            print(colored(f" ENTRY TIME    : {entry_time}", "white"))
            print(colored(f" SIGNAL REASON : {reason}", "yellow"))
            print(colored(f" TARGET TRADE  : {direction}", "green" if "CALL" in direction else "red", attrs=["bold"]))
            print(colored("»"*68, "white"))
            print("\n")
            
            time.sleep(10) # Pause so it doesn't double print
        time.sleep(1)

if __name__ == "__main__":
    threading.Thread(target=run_web_server, daemon=True).start()
    start_r4d1n_engine()
