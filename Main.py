base_frequency = 528.0
#intervals = [(1.0/1.0),(9.0/8.0),(5.0/4.0),(4.0/3.0),(3.0/2.0),(5.0/3.0),(15.0/8.0),(2.0/1.0)]
root_intervals = [1.0, round((4.0/3.0),2), round((3.0/2.0),2)]
ram_scale = []

def generate_ram_scale():
    for intv in root_intervals:
        ram_scale.extend(get_generate_triad_from_root(intv))
    return ram_scale


def get_generate_triad_from_root(root):
    triad = [None] * 3

    third = round((root * (5.0/4.0)), 2)
    if third > 2.0:
        third /= 2.0
    fifth = round((third * (6.0/5.0)),2)
    if fifth > 2.0:
        fifth /= 2.0
    triad[0] = root
    triad[1] = third
    triad[2] = fifth
    return triad

def main():
    unsorted_scale = generate_ram_scale()
    print(unsorted_scale)
    sorted_Scale = sorted(unsorted_scale)
    print(sorted_Scale)

if __name__ == '__main__':
    main()


__author__ = 'jaclyn'
