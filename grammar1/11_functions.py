# @title 関数の定義（引数・戻り値・デフォルト引数）
# @source https://docs.python.org/ja/3/tutorial/controlflow.html#defining-functions
# @run uv run grammar1/11_functions.py
# @desc def で関数を定義し return で値を返す。引数には既定値を持たせられる。
# @theme python
# @level 2
# @highlight def
# @highlight return

# greeting を省略すると "こんにちは" が使われる（デフォルト引数）
def greet(name, greeting="こんにちは"):
    return f"{greeting}、{name}さん"


def add(a, b):
    return a + b


# このファイルを直接実行したときだけ動く
if __name__ == "__main__":
    print(greet("田中"))
    print(greet("Smith", "Hello"))
    print(add(3, 4))
