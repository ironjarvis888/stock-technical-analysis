# stock-technical-analysis

股票技術分析技能 - 分析股票技術指標和趨勢

## 功能

- 取得股票價格數據
- 計算技術指標 (MA, RSI, MACD, KD)
- 產生技術分析建議

## 安裝依賴

```bash
pip3 install yfinance pandas numpy matplotlib --break-system-packages
```

## 使用方式

```bash
python3 analyze.py <股票代碼>
```

## 範例

```bash
# 分析蘋果股票
python3 analyze.py AAPL

# 分析特斯拉
python3 analyze.py TSLA

# 分析台積電
python3 analyze.py 2330.TW
```

## 輸出說明

- **價格資訊**：現價、漲跌金額與百分比
- **MA 均線**：5日、10日、20日、60日均線
- **RSI**：相對強弱指數（<30 超賣，>70 超買）
- **KD**：隨機指標（<20 超賣，>80 超買）
- **買賣建議**：根據技術指標給出建議

---

*版本：1.0 | 建立日期：2026-03-16*
