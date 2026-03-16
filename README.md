# Stock Technical Analysis | 股票技術分析

## Description | 描述

A skill for analyzing stock technical indicators including MA, RSI, and KD指標分析技能。

## Features | 功能

- Stock price data retrieval | 股票價格數據取得
- MA (Moving Average) calculation | MA 均線計算
- RSI (Relative Strength Index) calculation | RSI 相對強弱指數
- KD (Stochastic) calculation | KD 隨機指標
- Trading suggestions | 買賣建議

## Installation | 安裝

```bash
pip3 install yfinance pandas numpy matplotlib --break-system-packages
```

## Usage | 使用方式

```bash
python3 analyze.py <股票代碼>

# Example | 範例
python3 analyze.py AAPL
python3 analyze.py TSLA
python3 analyze.py 2330.TW
```

## Output | 輸出

- Price information | 價格資訊
- MA lines (5/10/20/60 days) | MA 均線
- RSI indicator | RSI 指標
- KD indicator | KD 指標
- Trading suggestions | 買賣建議

---

**Author | 作者**: Kuanlin  
**Version**: 1.0.0  
**Date**: 2026-03-16
