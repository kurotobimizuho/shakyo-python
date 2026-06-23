# @title 復習: 繰り返し
# @source https://docs.python.org/ja/3/tutorial/controlflow.html#for-statements
# @run uv run grammar1/10_for_review.py
# @desc 09 の復習。range / enumerate が参照で隠れる。思い出して打ち込む。
# @theme python
# @level 1
# @hidemode reference
# @hide range
# @hide enumerate

# 0, 1, 2 を順に表示
for i in range(3):
    print(i)

# 番号つきで表示（1 から始める）
for i, name in enumerate(["Alice", "Bob"], start=1):
    print(f"{i}: {name}")
