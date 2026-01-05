import re
import time
import string

def benchmark_regex():
    # The patterns from the plugin
    percentage_patterns = [
        r'(\d+(?:\.\d+)?)\s*%',           # 150%, 200 %, 150.5%
        r'(\d+(?:\.\d+)?)\s*percent',     # 150 percent
    ]
    intensity_patterns = [
        r'intensity[:\s]+(\d+(?:\.\d+)?)',
        r'at\s+(\d+(?:\.\d+)?)\s+intensity',
        r'(\d+(?:\.\d+)?)\s+intensity',
    ]

    # 1. Normal short string
    short_text = "The intensity is 150% which is very high."
    
    # 2. Long string with no matches (worst case for some backtracking?)
    long_text = "The intensity is high " * 10000 
    
    # 3. Pathological string for 'intensity[:\s]+'
    # "intensity" followed by 50,000 spaces, then "X" (non-digit)
    pathological_text = "intensity" + " " * 50000 + "X"

    print("Benchmarking Regex...")

    start = time.time()
    for pattern in percentage_patterns + intensity_patterns:
        re.findall(pattern, short_text)
    print(f"Short text: {time.time() - start:.6f}s")

    start = time.time()
    for pattern in percentage_patterns + intensity_patterns:
        re.findall(pattern, long_text)
    print(f"Long text (10k repeats): {time.time() - start:.6f}s")
    
    start = time.time()
    for pattern in intensity_patterns:
        re.findall(pattern, pathological_text)
    print(f"Pathological text (50k spaces): {time.time() - start:.6f}s")

if __name__ == "__main__":
    benchmark_regex()
