# English version
  - Please scroll down for the Japanese version.
## Requirement
  - macOS
  - Python 3.9.6
  - nltk 3.8.1
  - numpy 1.25.2

  ## Build an environment
    1. Building a virtual environment with Pipenv.
      - Reference URL: https://docs.python-guide.org/dev/virtualenvs/
      1. Installing pipenv
        ```
        $ pip install --user pipenv
        ```
      2. Install requests library
        ```
        $ pipenv install requests
        ```

    2. Install NLTK
      - Reference URL: https://www.nltk.org/install.html
      1. Install NLTK
        ```
        $ pip install -U nltk
        ```
      2. Installing Numpy
        ```
        $ pip install -U numpy
        ```
      3. Install NLTK within the python runtime environment
        ```
        $ python
        >>> import nltk
        ```
      4. Installation of NLTK data
        - Reference URL: https://www.nltk.org/data.html
        ```
        >>> nltk.download('all')
        ```

  ## Usage
    1. Launching the pienve virtual environment
      ```
      $ pipenv shell
      ```
    2. Run the main.py file
      ```
      ()$ pipenv run python main.py
      ```
    3. Check output.
      - In console: It appears as follows.
      ```
      These contain NNP tags ['Alice', 'Wonderland', 'ALICE', 'ADVENTURES',...
      ```
      - The following file is created in the same directory as main.py each time the command is executed.
        `result_20230914_12....txt`

      4. Exiting the virtual environment
      ```
      ()$ exit
      ```

# 日本語版
  ## 実行環境
  - macOS
  - Python 3.9.6
  - nltk 3.8.1
  - numpy 1.25.2

  ## 環境構築
    1. Pipenvで仮想環境を構築する
      - 参考URL: https://docs.python-guide.org/dev/virtualenvs/
      1. pipenvのインストール
        ```
        $ pip install --user pipenv
        ```
      2. requestsライブラリをインストール
        ```
        $ pipenv install requests
        ```

    2. NLTKをインストールする
      - 参考URL: https://www.nltk.org/install.html
      1. NLTKのインストール
        ```
        $ pip install -U nltk
        ```
      2. Numpyのインストール
        ```
        $ pip install -U numpy
        ```
      3. pythonの実行環境内で NLTK をインストール
        ```
        $ python
        >>> import nltk
        ```
      4. NLTKデータのインストール
        - 参考URL: https://www.nltk.org/data.html
        ```
        >>> nltk.download('all')
        ```

  ## 使用方法
    1. pipenveの仮想環境を起動する
      ```
      $ pipenv shell
      ```
    2. main.pyファイルを実行する
      ```
      ()$ pipenv run python main.py
      ```
    3. 出力を確認する
      - コンソール: 下記のように表示される
      ```
      These contain NNP tags ['Alice', 'Wonderland', 'ALICE', 'ADVENTURES',...
      ```
      - ファイル: コマンドを実行するたびにmain.pyと同じディレクトリに下記のようなファイルが作成される。
      `result_20230914_12.....txt`
    4. pipenveの仮想環境を出る
      ```
      ()$ exit
      ```