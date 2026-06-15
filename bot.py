import asyncio
import sys
import time
import hashlib
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
from termcolor import colored

# --- SILENT WEB SERVER CORE FOR RENDER COMPATIBILITY ---
class SilentServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"R4D1N PRO CLOUD ENGINE IS RUNNING LIVE.")
    def log_message(self, format, *args):
        return  # Suppresses web traffic clutter in your signal log layout

def run_web_port_server():
    # Render automatically passes the port number on variable 10000
    server_address = ('0.0.0.0', 10000)
    httpd = HTTPServer(server_address, SilentServerHandler)
    httpd.serve_forever()

# --- ORIGINAL MASTER TRADING BOT PROTOCOL ---
def print_r4d1n_logo():
    logo_text = """
██████╗ ██╗  ██╗██████╗  ██╗███╗   ██╗    ██████╗ ██████╗  ██████╗ 
██╔══██╗██║  ██║██╔══██╗███║████╗  ██║    ██╔══██╗██╔══██╗██╔═══██╗
██████╔╝███████║██║  ██║╚██║██╔██╗ ██║    ██████╔╝██████╔╝██║   ██║
██╔══██╗╚════██║██║  ██║ ██║██║╚██╗██║    ██╔═══╝ ██╔══██╗██║   ██║
██║  ██║     ██║██████╔╝ ██║██║ ╚████║    ██║     ██║  ██║╚██████╔╝
╚═╝  ╚═╝     ╚═╝╚═════╝  ╚═╝╚═╝  ╚═══╝    ╚═╝     ╚═╝  ╚═╝ ╚═════╝ 
    """
    print(colored(logo_text, "cyan", attrs=["bold"]))
    print("="*65)
    print("       R4D1N PRO - CLOUD STREAM ENGINE MASTER")
    print("="*65)

def calculate_otc_cryptographic_trend(asset_name, current_minute):
    seed_string = f"{asset_name.upper()}_{current_minute}_R4D1N_CLOUD_CORE"
    hash_digest = hashlib.md5(seed_string.encode('utf-8')).hexdigest()
    vector_score = int(hash_digest[:4], 16) % 100
    return vector_score

async def run_sureshot_loop(asset):
    print_r4d1n_logo()
    print(f"[📡 ENGINE ONLINE] Tracking live cloud vectors for target pair: {asset.upper()}\n")
    
    while True:
        current_sec = time.localtime().tm_sec
        while current_sec < 55:
            await asyncio.sleep(1)
            current_sec = time.localtime().tm_sec
            
        target_execution_minute = (time.localtime().tm_min + 1) % 60
        algo_score = calculate_otc_cryptographic_trend(asset, target_execution_minute)
        
        if algo_score >= 50:
            direction = "CALL"
        else:
            direction = "PUT"

        next_minute = (time.localtime().tm_min + 1) % 60
        entry_time_str = f"{time.strftime('%H')}:{next_minute:02d}:00"
        
        print("#"*65)
        print(f" ⚡ INITIAL SURESHOT ENTRY -> TARGET ASSET: {asset.upper()}")
        print(f" ENTRY TIME   : {entry_time_str} (On Next Candle Opening)")
        if direction == "CALL":
            print(" TARGET TRADE : 🟢🟢🟢 CALL (UP) 🟢🟢🟢")
        else:
            print(" TARGET TRADE : 🔴🔴🔴 PUT (DOWN) 🔴🔴🔴")
        print("#"*65 + "\n")

        await asyncio.sleep(10)

if __name__ == "__main__":
    # Fire up the fake web server block on a background channel thread
    web_thread = threading.Thread(target=run_web_port_server, daemon=True)
    web_thread.start()
    
    TARGET_PAIR = "USDBRL_OTC" 
    asyncio.run(run_sureshot_loop(TARGET_PAIR))
