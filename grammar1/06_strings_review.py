# @title 復習: 文字列の基本操作
# @source https://docs.python.org/ja/3/tutorial/introduction.html#strings
# @run uv run grammar1/06_strings_review.py
# @desc 05 の復習。添字・スライスが参照で隠れる。思い出して打ち込む。
# @theme python
# @level 1
# @hidemode reference
# @hide [0]
# @hide [-1]
# @hide [0:3]

word = "Python"

# 先頭・末尾の1文字
print(word[0])
print(word[-1])

# 先頭3文字（スライス）
print(word[0:3])

# 大文字にする
print(word.upper())
