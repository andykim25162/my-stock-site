
import yfinance as yf
import json
from datetime import datetime

# 관심 있는 종목 (야후 파이낸스 티커 기준)
# 한국 주식은 .KS(코스피) 또는 .KQ(코스닥)를 붙입니다.
tickers = ["AAPL", "TSLA", "005930.KS", "NVDA"]
data_results = {}

for t in tickers:
    try:
        stock = yf.Ticker(t)
        # 최신 가격 가져오기
        price = stock.fast_info['last_price']
        data_results[t] = {
            "price": round(price, 2),
            "updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    except:
        print(f"{t} 데이터를 가져오는데 실패했습니다.")

# data.json 파일로 저장
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data_results, f, ensure_ascii=False, indent=4)
