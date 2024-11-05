---
layout:  page
title: Rのはじめ方
docs: R documents
sidebar: "r_sidebar"
css: /_assets/css/page.css

---

<h1> {{ page.title }} </h1>
  
ここでは、Rを使う上で、必要なもの・便利なものと、前提知識を紹介します。

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
  
## 必要な知識  
- File path  
  ファイル・フォルダ間の位置関係、フォルダの階層構造のこと  
- Working directory  
  プログラムが実行されているベースのフォルダ  

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
しかし、プログラムはスクリプト、計算式をメモに書いて、実行するのが基本となります.  
  
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


Rは、基本的にどこかのフォルダ上で実行されます.  
このRが実行されているフォルダのことを<b>Working directory</b>といいます.  
  
例えば、<b>Work</b>という名前のフォルダ上で、Rを開いたらWork内のファイルしか直接的に開けません.  
  
