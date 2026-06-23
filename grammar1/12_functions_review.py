# @title 復習: 関数の定義
# @source https://docs.python.org/ja/3/tutorial/controlflow.html#defining-functions
# @run uv run grammar1/12_functions_review.py
# @desc 11 の復習。def / return・デフォルト引数が参照で隠れる。思い出して打ち込む。
# @theme python
# @level 2
# @hidemode reference
# @hide def
# @hide return
# @hide b=2

# a の b 乗を返す。b を省略すると 2 乗（デフォルト引数）
def power(a, b=2):
    return a ** b


if __name__ == "__main__":
    print(power(3))
    print(power(2, 5))
