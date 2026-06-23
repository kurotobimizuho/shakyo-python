# @title 繰り返し（for と range）
# @source https://docs.python.org/ja/3/tutorial/controlflow.html#for-statements
# @run uv run grammar1/09_for.py
# @desc for はリストや range の要素を順に取り出す。enumerate で添字も得る。
# @theme python
# @level 1
# @highlight range
# @highlight enumerate

# range(start, stop) は start 以上 stop 未満
for i in range(1, 4):
    print(i)

# リストの各要素を順に取り出す
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# enumerate で番号つきにできる（start で開始番号を指定）
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")
