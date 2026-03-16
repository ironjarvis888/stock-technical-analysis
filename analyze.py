#!/usr/bin/env python3
"""
Stock Technical Analysis Skill for OpenClaw
分析股票技術指標和趨勢
"""

import sys
import json
import subprocess

def install_dependencies():
    """安裝必要的依賴"""
    subprocess.run([sys.executable, "-m", "pip", "install", "yfinance", "pandas", "numpy", "matplotlib", "-q"])

def get_stock_data(symbol, period="6mo"):
    """取得股票數據"""
    try:
        import yfinance as yf
        stock = yf.Ticker(symbol)
        df = stock.history(period=period)
        return df
    except Exception as e:
        return {"error": str(e)}

def calculate_ma(df, windows=[5, 10, 20, 60]):
    """計算移動平均線"""
    import pandas as pd
    result = {}
    for w in windows:
        if len(df) >= w:
            result[f"MA{w}"] = round(df['Close'].rolling(w).mean().iloc[-1], 2)
    return result

def calculate_rsi(df, period=14):
    """計算 RSI 指標"""
    import pandas as pd
    delta = df['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return round(rsi.iloc[-1], 2)

def calculate_kd(df, n=9, m1=3, m2=3):
    """計算 KD 指標"""
    import pandas as pd
    low_n = df['Low'].rolling(window=n).min()
    high_n = df['High'].rolling(window=n).max()
    rsv = (df['Close'] - low_n) / (high_n - low_n) * 100
    k = rsv.ewm(com=m1-1, adjust=False).mean()
    d = k.ewm(com=m2-1, adjust=False).mean()
    return round(k.iloc[-1], 2), round(d.iloc[-1], 2)

def analyze(symbol):
    """執行股票分析"""
    # 取得數據
    df = get_stock_data(symbol)
    
    if "error" in df:
        return f"無法取得 {symbol} 的數據：{df['error']}"
    
    if len(df) == 0:
        return f"找不到股票 {symbol} 的數據"
    
    # 計算指標
    ma = calculate_ma(df)
    rsi = calculate_rsi(df)
    k, d = calculate_kd(df)
    
    # 取得最新價格
    current_price = round(df['Close'].iloc[-1], 2)
    price_change = round(df['Close'].iloc[-1] - df['Close'].iloc[-2], 2)
    change_pct = round((price_change / df['Close'].iloc[-2]) * 100, 2)
    change_pct_str = f"{change_pct:+.2f}%"
    
    # 買賣建議
    signal = "持有"
    if rsi < 30:
        signal = "買入 🟢 (RSI 超賣)"
    elif rsi > 70:
        signal = "賣出 🔴 (RSI 超買)"
    
    if k < 20 and d < 20:
        signal = "買入 🟢 (KD 超賣)"
    elif k > 80 and d > 80:
        signal = "賣出 🔴 (KD 超買)"
    
    # 輸出結果
    result = f"""
📈 **{symbol} 技術分析**

**價格資訊**
- 現價: ${current_price}
- 漲跌: {price_change:+} ({change_pct_str})

**技術指標**
- MA5: {ma.get('MA5', '-')}
- MA10: {ma.get('MA10', '-')}
- MA20: {ma.get('MA20', '-')}
- MA60: {ma.get('MA60', '-')}

- RSI(14): {rsi}
- K: {k}
- D: {d}

**建議**: {signal}
"""
    return result

def main():
    if len(sys.argv) < 2:
        print("使用方法: stock-technical-analysis <股票代碼>")
        print("例如: stock-technical-analysis AAPL")
        sys.exit(1)
    
    symbol = sys.argv[1].upper()
    
    # 嘗試分析，失敗則安裝依賴
    try:
        result = analyze(symbol)
    except ImportError:
        install_dependencies()
        result = analyze(symbol)
    
    print(result)

if __name__ == "__main__":
    main()
