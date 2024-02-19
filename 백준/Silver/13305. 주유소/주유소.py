def main():
    city = int(input())
    distance = list(map(int, input().split()))
    gas_price = list(map(int, input().split()))

    result = 0
    min_gas_price = gas_price[0]

    for i in range(city - 1):
        if i == 0:
            result = distance[0] * min_gas_price
            continue

        if gas_price[i] < min_gas_price:
            min_gas_price = gas_price[i]

        result += distance[i] * min_gas_price

    print(result)


if __name__ == "__main__":
    main()
