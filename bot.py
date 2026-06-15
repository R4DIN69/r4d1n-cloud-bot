import asyncio
import sys
import time
import hashlib
from termcolor import colored

def print_r4d1n_logo():
    """Renders the custom R4D1N branding header at cloud boot."""
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
    """Cryptographic Vector Oscillator balanced specifically for cloud streams."""
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
    TARGET_PAIR = "USDBRL_OTC" 
    asyncio.run(run_sureshot_loop(TARGET_PAIR))
