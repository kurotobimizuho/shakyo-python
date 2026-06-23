# @title 条件分岐（if / elif / else）
# @source https://docs.python.org/ja/3/tutorial/controlflow.html#if-statements
# @run uv run grammar1/07_if.py
# @desc 比較演算子と if/elif/else。インデント（字下げ）でブロックを表す。
# @theme python
# @level 1
# @highlight elif

score = 72

# elif は直前の条件が偽のときだけ評価される
if score >= 80:
    grade = "A"
elif score >= 70:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "D"

print(f"点数 {score} の評価は {grade}")

# and / or / not で条件を組み合わせる
if 0 <= score <= 100 and grade != "D":
    print("合格圏内です")
