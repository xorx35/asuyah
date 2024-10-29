import aiohttp
import asyncio
from fake_useragent import UserAgent
import random
import platform

# Fix for Windows
if platform.system() == 'Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# Define URLs and payloads
urls_payloads = [
    {
        "url": "https://api.adsgram.ai/adv",
        "params": {
            "blockId": "2994",
            "tg_id": "1471058240",
            "tg_platform": "tdesktop",
            "platform": "Win32",
            "language": "en",
            "top_domain": "timefarm.app"
        }
    },
    {
        "url": "https://api.adsgram.ai/event",
        "params": {
            "record": "IiQyNThiOTk3OS1lNDBmLTQ0NTUtYjQ1Ni00MzVjMWNmN2M4ZjAqBTE3ODMyMgUyMTgyNToGMzUwODc3QNvcg7kGSgoxOTkzNjYzNzQ5UgQyOTk0WhVodHRwczovL3RpbWVmYXJtLmFwcC9iATJqCHRkZXNrdG9wcgJlbooBBDg3NjCSAQQ2NjkwmgENMTc1NDM4LjUwMDAwMKoBCDEuMDAwMDAwsgEBMroBDTEyNS4xNjQuNC4xOTHCAQJpZPIBDTE0OTEyMi41MDAwMDD6AQYyOTgyNDWCAgEx",
            "type": "render",
            "trackingtypeid": "13"
        }
    },
    {
        "url": "https://api.adsgram.ai/event",
        "params": {
            "record": "IiQyNThiOTk3OS1lNDBmLTQ0NTUtYjQ1Ni00MzVjMWNmN2M4ZjAqBTE3ODMyMgUyMTgyNToGMzUwODc3QNvcg7kGSgoxOTkzNjYzNzQ5UgQyOTk0WhVodHRwczovL3RpbWVmYXJtLmFwcC9iATJqCHRkZXNrdG9wcgJlbooBBDg3NjCSAQQ2NjkwmgENMTc1NDM4LjUwMDAwMKoBCDEuMDAwMDAwsgEBMroBDTEyNS4xNjQuNC4xOTHCAQJpZPIBDTE0OTEyMi41MDAwMDD6AQYyOTgyNDWCAgEx",
            "type": "show",
            "trackingtypeid": "0"
        }
    },
    {
        "url": "https://api.adsgram.ai/event",
        "params": {
            "record": "IiQyNThiOTk3OS1lNDBmLTQ0NTUtYjQ1Ni00MzVjMWNmN2M4ZjAqBTE3ODMyMgUyMTgyNToGMzUwODc3QNvcg7kGSgoxOTkzNjYzNzQ5UgQyOTk0WhVodHRwczovL3RpbWVmYXJtLmFwcC9iATJqCHRkZXNrdG9wcgJlbooBBDg3NjCSAQQ2NjkwmgENMTc1NDM4LjUwMDAwMKoBCDEuMDAwMDAwsgEBMroBDTEyNS4xNjQuNC4xOTHCAQJpZPIBDTE0OTEyMi41MDAwMDD6AQYyOTgyNDWCAgEx",
            "type": "reward",
            "trackingtypeid": "14"
        }
    }
]

# Define headers template
base_headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Host": "api.adsgram.ai",
    "Origin": "https://timefarm.app",
    "Referer": "https://timefarm.app/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "sec-ch-ua": '"Chromium";v="130", "Microsoft Edge";v="130", "Not?A_Brand";v="99", "Microsoft Edge WebView2";v="130"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"'
}

# Function to send requests
async def fetch(session, url, params):
    ua = UserAgent()
    headers = base_headers.copy()
    headers["User-Agent"] = ua.random  # Set fake user-agent

    try:
        async with session.get(url, params=params, headers=headers) as response:
            # Print status and response data (limited)
            data = await response.text()
            print(f"Status: {response.status}, URL: {url}, Data: {data[:100]}...")
    except Exception as e:
        print(f"Error for URL {url}: {e}")

# Main async function to handle 1000 threads
async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(5000):
            # Randomly select a URL and payload combination
            target = random.choice(urls_payloads)
            task = fetch(session, target["url"], target["params"])
            tasks.append(task)
        
        # Run tasks concurrently
        await asyncio.gather(*tasks)

# Run the script
if __name__ == "__main__":
    import random
    asyncio.run(main())
