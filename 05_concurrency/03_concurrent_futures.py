from concurrent.futures import ThreadPoolExecutor
import requests # Necesitarías instalarlo o usar un mock

def check_website(url: str) -> str:
    # Simulación de petición I/O
    return f"Status for {url}: OK"

urls = ["https://google.com", "https://python.org", "https://github.com"]

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(check_website, urls))
    
    for res in results:
        print(res)