---
layout:  page
title: ファイルの読み込み
docs: R documents
sidebar: "r_sidebar"
css: /_assets/css/page.css

---

<h1> {{ page.title }} </h1>
  
1. Working directoryの確認
2. Working directoryの設定
3. ファイルの読み込み

* Contetnts  
{:toc}  
  
***  
## 絶対パスと相対パス

***  

## Working directoryとは
現在、Rが開いているフォルダ（ディレクトリ）のこと.

Working directoryのファイルは、フォルダ名を明記しなくても読み込める.  
他のディレクトリにあるファイルを開くには、<b>相対パス</b>で指定する必要がある。

***  

## Working directoryの確認

以下のコマンドで、Working directoryを確認できる.  
```
getcwd()
```
結果は、`/home/user/Desktop`　という形で返される.  

***  

## Working directoryの設定
読み込みたいファイルがWorking directoryにない場合、そのファイルが入っているフォルダへ移動すると便利である.

以下のコマンドで、Working directoryを変更することができる.
```
setwd("フォルダが入っているパス")
```