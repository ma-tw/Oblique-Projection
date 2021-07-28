# Oblique-Projection
斜方投射運動におけるさまざまな値を計算します。
# インストールが必要なモジュール
無し。すぐにお使いいただけます。
# 使い方
Python3で実行してください。
 ## コマンド
    python3 main.py
 ## 初速度v0
 初速度𝑣₀を半角数字で指定します。小数にも対応しています。必ず𝑣₀ ≥ 0となるように指定してください。
 ## 角度θ
 物体を投射する角度θ(仰角)を半角数字で指定します。度数法を用いてください。小数にも対応しています。必ず0° ≤ θ ≤ 90°となるように指定してください。
# 仕様
- 現在のバージョンでは、計算されるのは**最高点に達するときの時刻**、**最高点の高さ**、**落下するときの時刻**、**落下地点の距離**です。
- 単位は国際単位系(SI)に準拠しています。
- 物体を投射した地点を 0m 、物体を投射したときの時刻を 0s としています。
- 重力加速度は 9.8m/s² として計算されます。
- 空気抵抗等は無視しています。
- 計算される数値はすべて小数第2位までで表記されます。今後のアップデートでより適切な表記になるよう改善される見込みです。
