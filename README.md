# summarize-form
テキストを要約するフォーム


## 必要なもの

- Python 2.7
- Flask
- Requests
- petitviolet/python-extractcontent https://github.com/petitviolet/python-extractcontent
- Summpy https://github.com/recruit-tech/summpy

## 実行

```sh
git clone https://github.com/nus/summarize-form.git
cd summarize-form
python server.py
```

ブラウザで http://localhost:8080/ を開き、要約したいテキストを貼り付けて `要約` を押す。
