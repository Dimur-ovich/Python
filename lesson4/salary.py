
from sys import argv

file_name, hours, cost, bonus = argv

hs = float(hours)
ct = float(cost)
bs = float(bonus)

print(f'Заработано: {(lambda p1, p2, p3: p1 * p2 + p3) (hs, ct, bs)}')
print(f'  (выработка в часах: {hours}, ставка в час: {cost}, премия: {bonus})')