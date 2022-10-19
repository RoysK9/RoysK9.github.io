---
title: "STIP"
date: 2022-09-18T23:00:00+09:00
tags: [thesis]
draft: false
---

## 論文情報

- 論文名：Exploring Structure-aware Transformer over Interaction Proposals for Human-Object Interaction Detection　
- 学会：CVPR (2022)
- 投稿者：Yong Zhang (香港中文大学)
- 被引用数：2 (2022/10/16時点)
- タスク：Human Object Interaction

## 新規性・差分

- **インタラクション提案**と**空間構造符号化**の2段階でHOIを予測
<!--more-->

## 概要

- 画像内のヒトとモノのインタラクションを検出する．例えば，**人間**が**バット**を**握っている**など．
- ヒトとモノのインタラクション候補を**提案**し，**意味構造・空間構造**とともに予測を行う．


## ネットワーク

![network](/STIP/network.png) 
- (a)のDETRを使用してヒトとモノを検出
    - DETRによって特徴表現も得られる
- (b)のIntaraction Proposal Networkを使用してインタラクションペアを提案
    - ヒト特徴表現とモノ特徴表現とそれらのIOUから**インタラクションスコア**を予測し，それに基づいてインタラクション候補を提案
![image_label](/STIP/image_label.png) 
- ヒトとモノの空間構造を考慮するために画像をラベル化
![inter_interaction](/STIP/interaction.png) 
- インタラクション同士の関係性を考慮
    - 例えば，2つのHOIのHumanの部分が一致している場合，そのHOIの関係性は「同一ヒト」とされ、関連があることを示す
![cross_attn](/STIP/cross_attn.png) 
- 画像情報とインタラクション情報を統合して**HOI表現**を獲得する機構
    - 最終的にこの出力をMLPに入力し，holdやwearなどの動詞，あるいはインタラクションなしといった**インタラクションを予測**

### 所感

- 画像外観情報，空間構造，インタラクション情報を統合的に取り入れることに成功したネットワークであるように思います．
- Interaction Proposal Networkから提案された候補に直接MLPをかけてもそれなりに予測ができそうな気がします．
