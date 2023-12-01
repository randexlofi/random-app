import time
import random

def LoadingBar(barAmount, loadText='Loading', backChar='░', frontChar='█'):
    for x in range(barAmount + 1):
        barFull = frontChar * x + backChar * (barAmount - x)
        percentage = format(((x * 100) / barAmount), ".1f")
        print(f' {loadText} [{barFull}] {percentage}%', end='\r')
        time.sleep(random.uniform(0.1, 1))

# Example:
#bar_amount = 15
#LoadingBar(bar_amount, backChar='░', frontChar='█')