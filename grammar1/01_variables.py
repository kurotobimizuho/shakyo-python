# @original .shakyo/grammar1/01_variables.py

# 変数に値を代入する。型は値から自動で決まる
# 順に 文字列(str)・整数(int)・浮動小数点数(float)
name = "Python"
year = 1991
pi = 3.14159


# f-string なら {} の中に変数や式を直接書ける
print(f"{name} は {year} 年に誕生した")


# :.2f は小数点以下2桁で表示する書式
print(f"円周率はおよそ {pi: .2f}")

# type() で型を確認できる
print(type(name), type(year), type(pi))

