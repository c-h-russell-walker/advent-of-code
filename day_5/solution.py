# http://adventofcode.com/day/5

with open('input.txt') as f:
    santa_strings = [p_s.rstrip('\r\n') for p_s in f.readlines()]

    nice_count_two = 0
    double_show_ctr = 0
    bookend_ctr = 0
    for string in santa_strings:
        if not string:
            continue

        repeated_bookend = None
        double_show = None
        char_to_check = ''
        newstr = ''
        for index, char in enumerate(string):
            if index == 0 or index == len(string) - 1:
                continue

            next_char = string[index + 1]
            previous_char = string[index - 1]
            if not double_show:
                char_to_check = previous_char + char
                newstr = string[:index-1] + string[index+1:]
                if char_to_check in newstr:
                    double_show_ctr += 1
                    double_show = True
            if not repeated_bookend:
                if previous_char == next_char:
                    bookend_ctr += 1
                    repeated_bookend = True


        if not repeated_bookend or not double_show:
            continue

        nice_count_two += 1

    print("Original string count: ", len(santa_strings))

    # print("Part 1 => Count of nice strings: ", nice_count)

    print("Part 2 => Count of nice strings: ", nice_count_two)

    print("double_show_ctr: {}".format(double_show_ctr))
    print("bookend_ctr: {}".format(bookend_ctr))

    # Now, a nice string is one with all of the following properties:

    # It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
    # It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
