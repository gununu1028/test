try:
    number = int(input("整数を入力してください: "))
    doubled = number * 2
    print(f"結果: {doubled}")
except ValueError:
    print("エラー: 整数を入力してください")


d = {'a': 'エー', 'b': 'ビー'}
i = input('文字を入力してください:')
try:
    print(d[i])
except KeyError:
    print(‘エラーが出ました!')

          
d = {'a': 'エー', 'b': 'ビー'}
i = input('文字を入力してください:')
result = d.get(i)
if result is None:
    print(‘エラーが出ました!’)
else:
    print(result)
