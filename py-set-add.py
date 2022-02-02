
if __name__ == "__main__":
    no_of_stamps = int(input())
    country_stamps = [ ]
    for i in range(0,no_of_stamps-1):
        country_stamps.append(input())
    country_stamps = set(country_stamps)

    print(len(country_stamps))