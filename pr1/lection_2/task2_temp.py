import sys
from prettytable import PrettyTable

# x.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
# x.add_row(["Adelaide", 1295, 1158259, 600.5])
# x.add_row(["Brisbane", 5905, 1857594, 1146.4])
# x.add_row(["Darwin", 112, 120900, 1714.7])
# x.add_row(["Hobart", 1357, 205556, 619.5])
# x.add_row(["Sydney", 2058, 4336374, 1214.8])
# x.add_row(["Melbourne", 1566, 3806092, 646.9])
# x.add_row(["Perth", 5386, 1554769, 869.4])

x = PrettyTable()
data = [54, 55.6, '4', True, None, 'TExt', 344, 5.5, 'END', '4', 4, 344]
print('%-5s%-18s%-18s%-12s%-20s%12s' % ('п/п', 'значение', 'адрес', 'размер', 'хэш', 'comment'))
x.field_names = ["п/п", "значение", "адрес", "размер", 'хэш', 'comment']
for i, item in enumerate(data, start=1):
    print('%-5s%-18s%-18s%-12s%-20s%12s' % (i, item, id(item), sys.getsizeof(item), hash(item), 'comment'))
    x.add_row([i, item, id(item), sys.getsizeof(item), hash(item), 'comment'])
print(x)