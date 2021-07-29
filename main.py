import math

G = 9.8

while True:
    try:
        velocity = float(input("初速度v0 [m/s] >> "))
    except ValueError as err:
        print("値が不正です。", err)
    else:
        if velocity >= 0:
            break
        else:
            print("v0 ≥ 0で指定してください。")

while True:
    try:
        theta = float(input("角度θ >> "))
    except ValueError as err:
        print("値が不正です。", err)
    else:
        if 0 <= theta <= 90:
            break
        else:
            print("0° ≤ θ ≤ 90°で指定してください。")

v0sintheta = velocity * math.sin(math.radians(theta))
v0costheta = velocity * math.cos(math.radians(theta))

t_top = v0sintheta / G
top = v0sintheta ** 2 / (2 * G)

t_final = 2 * v0sintheta / G

l = v0costheta * t_final


print(
    "----------------------------------\n"
    "最高点に達するときの時刻: " + str(round(t_top,2)) + "s" + "\n"
    "最高点の高さ            : " + str(round(top,2)) + "m" + "\n"
    "落下するときの時刻      : " + str(round(t_final,2)) + "s" + "\n"
    "落下地点の距離          : " + str(round(l,2)) + "m" + "\n"
    "----------------------------------"
    )
