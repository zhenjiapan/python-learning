from dataclasses import dataclass
@dataclass(frozen=True, slots=True)

class Item:
    name: str
    value: int
    weight: int

    def getValue(self):
        return self.value

    def getWeight(self):
        return self.weight

    def __str__(self):
        return f'{self.name}: <{self.value}, {self.weight}>'

def buildItems(names, values, weights):
    return [Item(name, value, weight) for name, value, weight in
            zip(names, values, weights, strict=True)]

def maxVal(items, capacity):
    def search(i, remaining):
        if i == len(items):
            return 0, ()

        item = items[i]
        skip_val, skip_items = search(i + 1, remaining)
        if item.getWeight() > remaining:
            return skip_val, skip_items

        take_val, take_items = search(i + 1, remaining - item.getWeight())
        take_val += item.getValue()

        if take_val > skip_val:
            return take_val, (item,) + take_items
        return skip_val, skip_items

    return search(0, capacity)

names = ['A', 'B', 'C', 'D', 'E', 'F']
values = [7, 11, 21, 23, 24, 28]
weights = [2, 5, 7, 8, 11, 12]

items = buildItems(names, values, weights)

bestVal, bestItems = maxVal(items, 20)
print(f'The highest value is {bestVal}, and the items combination is '
      f'{[item.name for item in bestItems]}.')
