from dataclasses import dataclass
@dataclass(frozen=True, slots=True)

class Food:
    name: str
    value: int
    cost: int

    def getValue(self):
        return self.value

    def getCost(self):
        return self.cost

    def density(self):
        return self.value/self.cost

    def __str__(self):
        return f'{self.name}: <{self.value}, {self.cost}>'

def buildMenu(names, values, costs):
    return [Food(name, value, cost) for name, value, cost in
            zip(names, values, costs, strict=True)]

def greedy(items, maxCost, keyFunction):
    itemsCopy = sorted(items, key=keyFunction, reverse=True)
    result = []
    totalValue, totalCost = 0.0, 0.0
    for item in itemsCopy:
        if totalCost + item.getCost() <= maxCost:
            result.append(item)
            totalCost += item.getCost()
            totalValue += item.getValue()
    return result, totalValue

# Three sorting rules:
by_value = Food.getValue
by_cost = lambda x: -x.getCost()
by_density = Food.density

# 第一：删除 Food.getValue 和 Food.density 后面的 ()。
# Food.getValue    # 函数对象
# Food.getValue()  # 立即调用函数
# 因为 greedy() 函数需要接收一个排序函数，而不是立即执行该函数。
# 当 sorted() 处理某个具体食物时，会把那个对象传给 Food.getValue，充当 self。

# 第二：lambda 中也不需要立即提供某个具体的 Food 对象。
# lambda food: -food.getCost()
# 它表示：将来给我一个 food 对象，我就返回它的负成本。

names = ['wine', 'bear', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donut']
values = [89, 90, 95, 100, 90, 79, 50, 10]
costs = [123, 154, 258, 354, 365, 150, 95, 195]

foods = buildMenu(names, values, costs)

for rule in (by_value, by_cost, by_density):
    taken, score = greedy(foods, 750, rule)
    print(score, [item.name for item in taken])