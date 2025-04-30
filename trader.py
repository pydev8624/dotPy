import MetaTrader5 as mt5
import pandas as pd
import numpy as np
import time
from datetime import datetime

SYMBOLS = ['BTCUSD.i', 'ETHUSD.i', 'XAUUSD.i']
MAGIC_NUMBER = 987654
LOT_SIZE = 0.01
TIMEFRAME = mt5.TIMEFRAME_M5
CANDLES_TO_FETCH = 100
DEVIATION = 50
FILL_POLICY = mt5.ORDER_FILLING_RETURN  # Fixed for error 10016

SL_TP_SETTINGS = {
    'BTCUSD.i': {'sl': 3000, 'tp': 6000},
    'ETHUSD.i': {'sl': 100,  'tp': 200},
    'XAUUSD.i': {'sl': 500,  'tp': 1000}
}

TRAIL_STOP_DISTANCE = 200  # profit points

def compute_rsi(series, period=14):
    delta = series.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))

def compute_macd(series, short=12, long=26, signal=9):
    short_ema = series.ewm(span=short, adjust=False).mean()
    long_ema = series.ewm(span=long, adjust=False).mean()
    macd = short_ema - long_ema
    macd_signal = macd.ewm(span=signal, adjust=False).mean()
    return macd, macd_signal

def connect():
    if not mt5.initialize():
        print("❌ Failed to connect to MetaTrader 5:", mt5.last_error())
        quit()
    print("✅ Connected to MetaTrader 5")

def fetch_data(symbol):
    if not mt5.symbol_select(symbol, True):
        print(f"⚠️ Symbol not available: {symbol}")
        return None
    rates = mt5.copy_rates_from_pos(symbol, TIMEFRAME, 0, CANDLES_TO_FETCH)
    if rates is None or len(rates) == 0:
        print(f"⚠️ No data for symbol {symbol}")
        return None
    df = pd.DataFrame(rates)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    df['close'] = df['close'].astype(float)
    return df

def add_indicators(df):
    df['rsi'] = compute_rsi(df['close'])
    df['macd'], df['macd_signal'] = compute_macd(df['close'])
    df.dropna(inplace=True)
    return df

def signal_generator(df):
    last = df.iloc[-1]
    prev = df.iloc[-2]
    macd_up = prev['macd'] < prev['macd_signal'] and last['macd'] > last['macd_signal']
    macd_down = prev['macd'] > prev['macd_signal'] and last['macd'] < last['macd_signal']
    if last['rsi'] < 45 and macd_up:
        return 'BUY'
    elif last['rsi'] > 55 and macd_down:
        return 'SELL'
    return None

def open_trade(symbol, action):
    info = mt5.symbol_info(symbol)
    if not info.visible:
        mt5.symbol_select(symbol, True)
    if not info.trade_mode == mt5.SYMBOL_TRADE_MODE_FULL:
        print(f"⛔ Trading not allowed for {symbol}")
        return
    tick = mt5.symbol_info_tick(symbol)
    if not tick:
        print(f"⛔ Tick unavailable for {symbol}")
        return

    price = tick.ask if action == 'BUY' else tick.bid
    sl_points = SL_TP_SETTINGS[symbol]['sl']
    tp_points = SL_TP_SETTINGS[symbol]['tp']
    point = info.point

    if action == 'BUY':
        sl = price - sl_points * point
        tp = price + tp_points * point
        order_type = mt5.ORDER_TYPE_BUY
    else:
        sl = price + sl_points * point
        tp = price - tp_points * point
        order_type = mt5.ORDER_TYPE_SELL

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": LOT_SIZE,
        "type": order_type,
        "price": round(price, info.digits),
        "sl": round(sl, info.digits),
        "tp": round(tp, info.digits),
        "deviation": DEVIATION,
        "magic": MAGIC_NUMBER,
        "comment": "AI Bot Trade with SL/TP",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": FILL_POLICY,
    }

    result = mt5.order_send(request)
    if result.retcode == mt5.TRADE_RETCODE_DONE:
        print(f"✅ {action} order placed for {symbol} at {price:.2f} | SL: {sl:.2f} | TP: {tp:.2f}")
    else:
        print(f"❌ Order failed: RetCode={result.retcode}, Error={mt5.last_error()}")

def get_positions(symbol):
    positions = mt5.positions_get(symbol=symbol)
    return [p for p in positions if p.magic == MAGIC_NUMBER] if positions else []

def close_trade(position):
    tick = mt5.symbol_info_tick(position.symbol)
    price = tick.bid if position.type == 0 else tick.ask
    order_type = mt5.ORDER_TYPE_SELL if position.type == 0 else mt5.ORDER_TYPE_BUY
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": position.symbol,
        "volume": position.volume,
        "type": order_type,
        "position": position.ticket,
        "price": round(price, mt5.symbol_info(position.symbol).digits),
        "deviation": DEVIATION,
        "magic": MAGIC_NUMBER,
        "comment": "Closed by AI",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": FILL_POLICY,
    }
    result = mt5.order_send(request)
    if result.retcode == mt5.TRADE_RETCODE_DONE:
        print(f"✅ Closed trade {position.ticket} with profit: {position.profit:.2f}")
    else:
        print(f"❌ Failed to close trade: {result.retcode}")

def modify_trailing_stop(position, symbol):
    info = mt5.symbol_info(symbol)
    point = info.point
    tick = mt5.symbol_info_tick(symbol)
    current_price = tick.bid if position.type == 0 else tick.ask
    profit = position.profit

    if profit * 10 < TRAIL_STOP_DISTANCE:
        return

    if position.type == 0:  # BUY
        new_sl = current_price - TRAIL_STOP_DISTANCE * point
        if new_sl > position.sl:
            request = {
                "action": mt5.TRADE_ACTION_SLTP,
                "position": position.ticket,
                "sl": round(new_sl, info.digits),
                "tp": position.tp,
                "symbol": symbol,
                "magic": MAGIC_NUMBER,
            }
            mt5.order_send(request)
    else:  # SELL
        new_sl = current_price + TRAIL_STOP_DISTANCE * point
        if new_sl < position.sl or position.sl == 0.0:
            request = {
                "action": mt5.TRADE_ACTION_SLTP,
                "position": position.ticket,
                "sl": round(new_sl, info.digits),
                "tp": position.tp,
                "symbol": symbol,
                "magic": MAGIC_NUMBER,
            }
            mt5.order_send(request)

def main_loop():
    connect()
    last_time_checked = {s: None for s in SYMBOLS}
    print("🤖 AI Trading Bot is running...")

    while True:
        try:
            for symbol in SYMBOLS:
                df = fetch_data(symbol)
                if df is None:
                    continue
                df = add_indicators(df)
                signal = signal_generator(df)
                current_time = df.iloc[-1]['time']

                if last_time_checked[symbol] == current_time:
                    continue

                last_time_checked[symbol] = current_time
                positions = get_positions(symbol)

                for pos in positions:
                    if pos.profit <= -0.1:
                        print(f"🔻 Closing trade {pos.ticket} due to loss: {pos.profit:.2f}")
                        close_trade(pos)
                    else:
                        modify_trailing_stop(pos, symbol)

                if not positions and signal:
                    print(f"{symbol} → Signal: {signal}")
                    open_trade(symbol, signal)

            time.sleep(3)

        except Exception as e:
            print(f"⚠️ Error in main loop: {e}")
            time.sleep(5)

if __name__ == "__main__":
    main_loop()
