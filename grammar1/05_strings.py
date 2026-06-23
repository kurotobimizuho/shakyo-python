# @title 文字列の基本操作
# @source https://docs.python.org/ja/3/tutorial/introduction.html#strings
# @run uv run grammar1/05_strings.py
# @desc 連結・繰り返し・添字・スライス・主なメソッド。文字列は変更できない。
# @theme python
# @level 1
# @highlight [0]
# @highlight [-1]

s = "Python"

# + で連結、* で繰り返し
print(s + " 入門")
print("-" * 10)

# 添字は0始まり。-1 は末尾を表す
print(s[0])
print(s[-1])

# スライス [start:stop] は stop を含まない
print(s[0:3])

# len() で文字数
print(len(s))

# 文字列メソッド（元の s は変化しない）
print(s.upper())
print(s.lower())
print(s.replace("Py", "My"))
