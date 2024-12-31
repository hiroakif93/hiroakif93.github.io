---
layout:  page
title: Rのはじめ方
docs: R documents
sidebar: "r_sidebar"
css: /_assets/css/page.css

---

<h1> {{ page.title }} </h1>
  
ここでは、Rの実行方法について説明します。
また、プログラミングを触ったことがない人向けに書いているつもりです。
そのため、端端で語弊のある言い方をしていますが、ご容赦ください。

* Contetnts  
{:toc}  
  
***  
  
## Rを使うにあたって必要なもの  
  - R本体
  - Rstudio （Rを使う上で、便利なツール）
  
1. 以下からR本体をダウンロード  
    [https://mirrors.cicku.me/cran/](https://mirrors.cicku.me/cran/)
2. 以下からRstudioをダウンロード  
    [https://posit.co/download/rstudio-desktop/](https://posit.co/download/rstudio-desktop/)

Rの実行自体は、R本体を起動して操作するのでも、問題はないです.  
ただ、Rstudioは、とても便利な機能を有しているので、基本的にRstudioを使った方法を以下で解説します.

***  
  
## Rの実行
### 1. Rの起動  
Rstudioを開きます.
{% include image.html 
max-width="100px" file="/_assets/images/rstudio.png" alt=""
caption="" %}
  
そうすると以下の画面が開きます.  
{% include image.html 
max-width="500px" file="/_assets/images/rstudio_home.png" alt=""
caption="" %}

`Console` パネルに、計算式などを打ち込んで、実行すれば計算ができます.  
（例: `1+1`　と入力して、エンターを押してみてください）  
しかし、プログラムは、実行したい内容（計算・統計解析）をスクリプトと呼ばれるメモに書いて、実行するのが基本となります.  

### 2. Rスクリプト
そこで、まずはRスクリプトを作成します.

四角で囲っている箇所をクリックすると、いろいろなメモの書式（スクリプト）が出てきます.
{% include image.html 
max-width="500px" file="/_assets/images/rstudio_script.png" alt=""
caption="" %}

ここで、Rスクリプトを選択すると、新たなパネルが開きます.
新しく開いたパネルに`1+1`と記入して、以下の様に実行します.  
  
カーソルを実行したい行に合わせて  
Windows/Linux : Controlキー＋エンターキー
Mac : Commandキー＋エンターキー

その結果、`Console`パネルには、`2`と計算した結果が表示されます。

以上のように、Rは、  
1. スクリプトに実行内容を記述  
2. スクリプトを実行 (Ctl/Cmd + Enter) 
3. コンソールで結果の確認  
という流れで使用します。  

### 3. オブジェクト
計算した結果を、後の計算に使いたい時がしばしばあります。
結果を保存することを、「オブジェクトに格納する/作成」と言います。

最初のイメージとしては、結果を何らかの名前がついたファイルに保存するのと同じです。

例えば、先ほどの`1+1`の結果を、保存したい時は、以下の様に記述して、実行します。
```
a <- 1+1 
# または  
a = 1+1  
```
そうすると、先ほど違って、`Console`には、２と表示されず `a = 1+1` と実行内容しか表示されません。  
{% include image.html 
max-width="300px" file="/_assets/images/object1.png" alt=""
caption="" %}

これは、`a`というファイル（オブジェクト）に、`1+1`の結果を格納したことを意味します。
`a`というファイル（オブジェクト）の中身を開くためには、`a`のみを実行します。
{% include image.html 
max-width="300px" file="/_assets/images/object2.png" alt=""
caption="" %}

そうすると、計算結果の`2`が表示されました。  
つまり、「オブジェクト単体の実行は、オブジェクトの中身を表示する」ということになります。  
\* 語弊のある言い方をしています。
  
次に、オブジェクトに保存した結果を利用する方法を示します。  
ここで、オブジェクトの概念を拡張します。  
  
オブジェクトは、結果の性質/ここで言うと`2`という数字の性質も持っています。   
つまり、<b>`α`は`２`という数字であり、`a + 1`という計算が可能ということです</b>。  
実際に、`a + 1`を実行すると、`3`という結果が表示されます。  
{% include image.html 
max-width="300px" file="/_assets/images/object3.png" alt=""
caption="" %}

もちろん、`3`という結果を別のオブジェクトに保存して、その結果を別の計算に使用することは可能です。
{% include image.html 
max-width="300px" file="/_assets/images/object4.png" alt=""
caption="" %}

ここまでのRの使い方を、まとめると
1. スクリプトに実行内容を記述  
2. スクリプトを実行 (Ctl/Cmd + Enter) 
3. 実行内容をオブジェクトに保存
4. 1-3を繰り返して、計算し、最終結果をオブジェクトに保存
5. 最終オブジェクトを実行して、コンソールで結果の確認  
  
  
  
Rは、基本的にどこかのフォルダ上で実行されます.  
このRが実行されているフォルダのことを<b>Working directory</b>といいます.  
  
例えば、<b>Work</b>という名前のフォルダ上で、Rを開いたらWork内のファイルしか直接的に開けません.  
  

## 必要な知識  
- File path  
  ファイル・フォルダ間の位置関係、フォルダの階層構造のこと  
- Working directory  
  プログラムが実行されているベースのフォルダ  
