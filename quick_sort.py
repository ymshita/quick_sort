import sys

def quick_sort(array: [], left: int, right: int):
    """まずは基準となる値を決め、その値より大きいか、小さいかで並び替える
    その後、基準となる値を、より小さい数とより大きい数の真ん中に移動する
    :param left: int #並び変え範囲の先頭要素の添字を入れる変数
    :param right: int #並び替え範囲の末尾要素を探すための変数
    :return: 整列後のarray
    """
    i:int #基準値より大きい要素を探すための変数
    k: int #基準値より小さい要素を探すための変数
    w: int #データ交換用の変数

    i = left + 1
    k = right

    print(f'loop start i: {i}, k: {k}, left: {left}, right: {right}')
    # i < k の間該当するiとkの交換をループ
    while i < k:
        #基準値 array[left] より大きい数array[i]を探す
        while array[i] < array[left] and i < right :
            i += 1
        else:
            print("i= ", i)

        #基準値 array[left] より小さい数array[k]を探す
        while array[k] >= array[left] and k > left :
            k -= 1
        else:
            print("k= ", k)

        if i < k:
            # iとkの値の交換
            w = array[i]
            array[i] = array[k]
            array[k] = w
            print(f'swap i= {i}, k= {k}')
    else:
        print(f'loop end i: {i}, k: {k}, left: {left}, right: {right}')

    # 交換できないポジションまで移動後, 交換の必要があれば（array[left] > array[k]）kとleftを交換
    if array[left] > array[k]:
        w = array[left]
        array[left] = array[k]
        array[k] = w
    print('intermediate', array)

    if left < k-1:
        array = quick_sort(array, left, k-1)

    if k+1 < right:
        array = quick_sort(array, k+1, right)

    return array

def main():
    """コマンドで実行する場合には引数として、リストの数字をスペース区切りで入力します
    ex: 整列対象が　[3,8,0,4,2,5,9,1]　の時、
        => # python3 quick_sort 3 8 0 4 2 5 9 1
    """
    if len(sys.argv) > 1:
        array = []
        target = sys.argv[1:]
        for value in target:
            try:
                num = int(value)
                array.append(num)
            except ValueError:
                print(f'{value}は数値ではありません。')
        print('array=　', quick_sort(array, 0, len(array)-1))
    else:
        raise ValueError('引数がありません')

if __name__ == '__main__':
    main()