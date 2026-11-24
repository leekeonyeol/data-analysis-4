import csv
import os


def dp(name):

    here = os.path.dirname(os.path.abspath(__file__))
    for c in (
        os.path.join(here, name),
        os.path.join(here, "data", name),
        os.path.join(here, "..", "data", name),
    ):
        if os.path.exists(c):
            return c
    return os.path.join("data", name)


LOT = dp("17_열처리.csv")  # 오늘의 주 데이터
PROC = dp("17_열처리_공정.csv")  # 빈 칸이 섞인 파일
WIDE = dp("20_cmapss_fd001_sample.csv")  # 열 수만 셉니다.

# ========================================
# 오늘 계속 만날 파이썬 표현 7가지 (미리보기)
# ========================================

x = 859.5318
print(
    f"1) {x:.2f} <- 소수 둘째자리 | {x:10.1f} <- 열 칸 폭 첫째 자리",
    f"| {44:>5d} <- 정수 다섯칸 오른쪽 정렬 | {0.0455:.1%} <- 퍼센트로",
)

with open(LOT, encoding="utf-8-sig") as f:
    r = csv.reader(f)
    header = next(r)
    rows = list(r)

temps = [
    float(row[2]) for row in rows
]  # rows안은 문자열 형태이므로 float으로 변경한다.
print(" 2) 리스트 컴프리헨션:", temps[:5], "...총", len(temps), "개")
print(" 3) 조건을 붙이면:", [t for t in temps if t > 862])

pairs = [("온도", 1.39), ("OP값", 13.75), ("CP값", 0.01)]
# 이 세 숫자는 밑에서 할 걸 숫자 열 셋의 '흔들림'을 잰 값입니다.

print(" 4) 흔들림이 큰 순서:", sorted(pairs, key=lambda t: -t[1]))

print(" 5) 삼항연산자: ", "넓다" if max(temps) - min(temps) > 10 else "좁다")

kinds = {}
for row in rows:
    kinds[row[1]] = (
        kinds.get(row[1], 0) + 1
    )  # 딕셔너리는 kinds[row[1]] = a 는 값을 수정하는 메커니즘, get은 row[1] 의 값을 보내준다.

print(
    "딕셔너리로 세기:", kinds, "| 셋으로 종류만:", sorted(set(row[5] for row in rows))
)
