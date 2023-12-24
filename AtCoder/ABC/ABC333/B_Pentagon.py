# https://atcoder.jp/contests/abc333/tasks/abc333_b

def is_equal_segment(segment1, segment2):
    def normalize(segment):
        return {segment, segment[::-1]}

    sides = {'AB', 'BC', 'CD', 'DE', 'EA'}
    diagonals = {'AC', 'BD', 'CE', 'DA', 'EB'}

    segment1 = normalize(segment1)
    segment2 = normalize(segment2)

    if (segment1.intersection(sides) and segment2.intersection(sides)) or \
       (segment1.intersection(diagonals) and segment2.intersection(diagonals)):
        return 'Yes'
    else:
        return 'No'

segment1 = input()
segment2 = input()
print(is_equal_segment(segment1, segment2))