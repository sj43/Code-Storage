INF = 987654321

# 만들 수 있는 음식의 종류 수
M = 6

def canEverybodyEat(menu):
    pass


def selectMenu(menu, food):
    if food == M:
        if canEverybodyEat(menu):
            return len(menu)
        return INF
    ret = selectMenu(menu, food + 1)
    menu.append(food)
    ret = min(ret, selectMenu(menu, food + 1))
    menu.pop()
    return ret
