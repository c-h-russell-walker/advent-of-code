# http://adventofcode.com/day/2

# Should equal 101 & 48
# present_sizes = ["2x3x4", "1x1x10"]

with open('input.txt') as f:
    present_sizes = [p_s.rstrip('\r\n') for p_s in f.readlines()]

    total_wrapping_paper = 0
    ribbon_length = 0

    for present in present_sizes:
        sizes = [int(x) for x in present.split('x')]

        # After getting largest side remove it from list    
        h = max(sizes)
        sizes.remove(h)

        l = sizes[0]
        w = sizes[1]

        area = 2*l*w + 2*w*h + 2*h*l
        slack = l * w
        area += slack
        total_wrapping_paper += area

        ribbon_length += 2*l + 2*w
        ribbon_length += h*l*w

    print("Total Wrapping Paper: {}".format(total_wrapping_paper))
    print("Ribbon Length: {}".format(ribbon_length))
