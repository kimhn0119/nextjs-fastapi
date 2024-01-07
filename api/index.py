from fastapi import FastAPI

from pybroker import Strategy, YFinance, highest



app = FastAPI()
def exec_fn(ctx):
    # Get the rolling 10 day high.
    high_10d = ctx.indicator('high_10d')
    # Buy on a new 10 day high.
    if not ctx.long_pos() and high_10d[-1] > high_10d[-2]:
        ctx.buy_shares = 100
        # Hold the position for 5 days.
        ctx.hold_bars = 5
        # Set a stop loss of 2%.
        ctx.stop_loss_pct = 2
@app.get("/api/python")
def hello_world():



    strategy = Strategy(YFinance(), start_date='1/1/2022', end_date='7/1/2022')
    strategy.add_execution(
        exec_fn, ['AAPL', 'MSFT'], indicators=highest('high_10d', 'close', period=10))
    # Run the backtest after 20 days have passed.
    result = strategy.backtest(warmup=20)
    rdf=result.portfolio
    rdf['cash']=rdf['cash'].astype(str)
    rlist=rdf.cash.tolist()

    print(''.join(rlist))
    return {"message": ''.join(rlist)}