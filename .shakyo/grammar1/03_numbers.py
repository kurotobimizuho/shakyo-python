# @title 数値演算
# @source https://docs.python.org/ja/3/tutorial/introduction.html#numbers
# @run uv run grammar1/03_numbers.py
# @desc 四則演算と、割り算の3種類（/, //, %）、べき乗。実行して結果を確かめる。
# @theme python
# @level 1
# @highlight //
# @highlight %

a = 17
b = 5

# 足し算・引き算・掛け算
print(a + b)
print(a - b)
print(a * b)

# 割り算 / は必ず float になる
print(a / b)

# // は切り捨て除算（商）、% は剰余（余り）
print(a // b)
print(a % b)

# ** はべき乗
print(a ** b)
