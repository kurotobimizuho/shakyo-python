# @title 復習: 条件分岐
# @source https://docs.python.org/ja/3/tutorial/controlflow.html#if-statements
# @run uv run grammar1/08_if_review.py
# @desc 07 の復習。elif / else が参照で隠れる。思い出して打ち込む。
# @theme python
# @level 1
# @hidemode reference
# @hide elif
# @hide else

temp = 25

# 気温で3段階に分ける
if temp >= 30:
    print("暑い")
elif temp >= 20:
    print("快適")
else:
    print("寒い")
