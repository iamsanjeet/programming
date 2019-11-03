class Solutions:
    def coin_change(self, coins, amount):
        coins.sort(reverse=True)
        coin_map = {}
        i = 0
        size = len(coins)
        while True:
            if amount - coins[i] >= 0:
                amount = amount - coins[i]
                if coin_map.get(coins[i]):
                    coin_map[coins[i]] += 1
                else:
                    coin_map[coins[i]] = 1

                if amount == 0:
                    return coin_map.keys(), coin_map
            else:
                if i == size-1:
                    break
                else:
                    i +=1
        return -1


def count(arr, index, sum):
    # if sum is 0 then there is one solution,
    # solution (do not include any coin)
    if sum == 0:
        return 1

    # if index is negative, then no solution exist
    if sum < 0:
        return 0

    # if index is 0 and sum is positive,
    # then no solutions exist
    if index <= 0 and sum >= 1:
        return 0







if __name__ == '__main__':
    res, map = Solutions().coin_change([7,2,1], 20)
    print(res)
    print(map)
