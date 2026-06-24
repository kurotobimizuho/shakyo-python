# @title 復習: 変数とf文字列
# @source https://docs.python.org/ja/3/tutorial/introduction.html
# @run uv run grammar1/02_variables_review.py
# @desc 01 の復習。参照では f-string の要点が隠れる。思い出して全文を打ち込む。
# @theme python
# @level 1
# @hidemode reference
# @hide f"
# @hide {city}
# @hide {temp}

city = "Kyoto"
temp = 22.5

# f-string で変数を文に埋め込んで表示する
print(f"{city} は {temp} 度")
