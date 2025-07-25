---
layout: rwiki
permalink: /hiroakif93-rwiki/object
title: オブジェクト・型
description: オブジェクトの型と主に使うクラスを紹介
---

# {{ page.title }}
## {{ page.description }}

### オブジェクトとは
直感的な理解は、**データ構造や処理結果を保存**したもの.
以下では、Rが扱うデータ構造 = 型とクラスについて説明する.
  
***
  
### Rで扱える型

|型名|書き方|例|
|:---|:---|:---|
|文字型/character型| 文字をシングルクォート（'）またはダブルクォート（"）で囲むことで表現.|'a', "a"
|数値型/numeric型| 小数点を含む数字はnumeric型になる.<br>|1.0, 2.0, 3.1415. <br>* "1"だと文字列型.|
|整数型/integer型| 整数のみを扱う数値型. 特に操作しなければ数字だけ打つとnumeric型になる.|1L, 2L, 3L |
|論理型/logical型| 論理式(==, >など)を扱う時に用いる型.  論理型は整数値でも表すことができ、TRUEは1、FALSEは0として扱われる。|TRUE, FALSE, NA 
|factor| NA |
|NULL| NULL |
|NaN| NaN |
|Inf| Inf |
|-Inf| -Inf |

<!--
- 文字型/character型  
    文字列を扱うための型. 文字を、シングルクォート（'）またはダブルクォート（"）で囲むことで表現.  
    数字も、クォートで囲むと文字型として扱われる.  
    例：'a', 'A', '-', '#', '1'  
  
- 数値型/numeric型, 整数型/integer型  
    数値を扱うための型。四則演算などが可能です.整数型は、小数点以下がない数値を扱うための型.  
    例：1, 2.0, 3.1415, 4, 5, 1+1, 4-1, 2*3, 4/2  
    * "1"+"1"は、１が文字列型になるため、計算できない.  
  
- 論理型  
    論理型は、真偽値を扱うための型です。TRUEまたはFALSEの値を持ちます。  
    論理型は整数値でも表すことができ、TRUEは1、FALSEは0として扱われます。
-->
***  
  
### Rのクラス

- ベクトル/vector
- 行列/matrix, array
- データフレーム/data.frame
- list