# shakyo-python — Python 初学者向け写経教材

[Shakyo](https://github.com/kenjisato/shakyo) で写経するための、Python の主要文法を
1 項目ずつ短い実行可能ファイルにまとめた教材です。

## 必要なもの

- [uv](https://docs.astral.sh/uv/getting-started/installation/)（インストール方法はリンク先）
- [VS Code](https://code.visualstudio.com/)
- [VS Code の Python 拡張](https://marketplace.visualstudio.com/items?itemName=ms-python.python)（▶ 実行ボタンを使う場合）

## はじめかた

1. Shakyo 拡張をインストール:

   ```sh
   uvx vscx install github:kenjisato/shakyo --pre-release
   ```

2. このリポジトリを開き、`grammar1/01_variables.py` を開く。
3. エディタ上で**右クリック → Shakyo: Transcribe this file**。写経が始まる。

## 実行

ターミナルで:

```sh
uv run grammar1/01_variables.py
```

VS Code の ▶ ボタンで実行したい場合は、一度 `uv run` を実行すると作られる `.venv` を
インタプリタに選ぶ（コマンドパレット → **Python: Select Interpreter** → `.venv`）。
以後はエディタ右上の ▶ で実行できる。

## セクション

1 セクション ≒ 60 分。番号順に進める。詳しい内容は各セクションの README を参照。

- [grammar1](grammar1/README.md) — Python の基本文法（変数・数値・文字列・条件分岐・繰り返し・関数）

（セクションは順次追加予定）

## ライセンス

各セクションのファイルは、[Python 公式チュートリアル（日本語）](https://docs.python.org/ja/3/tutorial/)
の文法を最小の実行可能例として書き起こしたものです。各ファイルの `@source` は該当節へのリンクです。
