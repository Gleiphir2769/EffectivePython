def deco(func):
    def inner():
        print('running inner()')

    return inner()


@deco
def target():
    print('running target')

def make_average():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)
    return averager



if __name__ == '__main__':
    avg = make_average()

