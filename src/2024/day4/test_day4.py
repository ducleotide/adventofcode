from unittest import TestCase

import day4 as d4


class Test(TestCase):
#     def setup(self):
#         """
# MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX
#         :return:
#         """
#         self.sample = d4.load_input("sample.txt")

    def test_check_xmas_left_right(self):

        # left - right
        t1 = ["XMAS.",
              "BLAH.",
              "BLAH.",
              "BLAH."]
        self.assertEqual(1, d4.check_xmas(t1, 0,0))

        t2 = [".XMAS",
              ".BLAH",
              ".BLAH",
              ".BLAH"]
        self.assertEqual(1, d4.check_xmas(t2, 1,0))

        t3 = ["..XMA",
              "..BLA",
              "..BLA",
              "..BLA"]
        self.assertEqual(0, d4.check_xmas(t3, 2,0))

    def test_check_xmas_down(self):
        # DOWN
        t4 = ["..XMA",
              "..MLA",
              "..ALA",
              "..SLA"]
        self.assertEqual(1, d4.check_xmas(t4, 2,0))

        t4 = ["...MA",
              "..XLA",
              "..MLA",
              "..ALA",
              "..S.."]
        self.assertEqual(1, d4.check_xmas(t4, 2,1))

        t4 = ["...MA",
              "..XLA",
              "..MLA",
              "..ALA"]
        self.assertEqual(0, d4.check_xmas(t4, 2,1))

        t5 = """..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS""".splitlines()
        self.assertEqual(2, d4.check_xmas(t5, 9,0))

    def test_check_xmas_diag_down_right(self):
        # diag down right
        t4 = ["...MA.",
              "..XLA.",
              "...MA.",
              "...LA.",
              "..S..S"]
        self.assertEqual(1, d4.check_xmas(t4, 2,1))

        t4 = ["...MA.",
              "..XLA.",
              "...MA.",
              "...LA."]
        self.assertEqual(0, d4.check_xmas(t4, 2,1))
        t5 = """....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X        
""".splitlines()
        self.assertEqual(1, d4.check_xmas(t5, 4, 0))

    def test_check_xmas_diag_up_right(self):
        # diag up right
        t5 = ["..S..S",
              "...MA.",
              "...MA.",
              "..XLA.",
              "...LA.",
              ]
        self.assertEqual(1, d4.check_xmas(t5, 2,3))

        t5 = [
              "...MA.",
              "...MA.",
              "..XLA.",
              "...LA.",
              ]
        self.assertEqual(0, d4.check_xmas(t5, 2,2))

    def test_check_xmas_diag_up_left(self):
        # diag up left
        t6 = ["..S..S",
              "...A..",
              "....M.",
              ".....X"]
        self.assertEqual(1, d4.check_xmas(t6, 5,3))

        t6 = [
              "...A..",
              "....M.",
              ".....X"]
        self.assertEqual(0, d4.check_xmas(t6, 5,2))

        t6 = [
              "A....",
              ".M...",
              "..X.."]
        self.assertEqual(0, d4.check_xmas(t6, 2,2))

    def test_check_xmas_diag_down_left(self):
        # diag down left
        t6 = ["...X..S",
              "..M....",
              ".A...A.",
              "S.....S"]
        self.assertEqual(1, d4.check_xmas(t6, 3,0))

        t6 = [".......",
              "...X..S",
              "..M....",
              ".A...A.",
              "S.....S"]
        self.assertEqual(1, d4.check_xmas(t6, 3,1))

        t6 = [
              "...X..S",
              "..M....",
              ".A...A.",
              ]
        self.assertEqual(0, d4.check_xmas(t6, 3,0))

        t6 = [
              "...X",
              "..M.",
              ".A..",
              ]
        self.assertEqual(0, d4.check_xmas(t6, 3,0))

        t6 = [
            "...X",
            "..M.",
            ".A..",
            "S..."
        ]
        self.assertEqual(1, d4.check_xmas(t6, 3, 0))


    def test_check_xmas_backward(self):
        # backward
        t7 = ["SAMX.S",
              "X.....",
              ".M....",
              "..A..."
              ]
        self.assertEqual(1, d4.check_xmas(t7, 3,0))

    def test_check_xmas_up(self):
        # up
        t6 = ["..S..S",
              "..A...",
              "..M...",
              "..X..."]
        self.assertEqual(1, d4.check_xmas(t6, 2,3))

        t6 = [
              "..A...",
              "..M...",
              "..X..."]
        self.assertEqual(0, d4.check_xmas(t6, 2, 2))

        t6 = [".....S",
              "..S..S",
              "..A...",
              "..M...",
              "..X..."]
        self.assertEqual(1, d4.check_xmas(t6, 2,4))


    def test_count_xmas(self):
        sample1 = """
....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX
""".splitlines()
        nx = d4.count_xmas(sample1)
        self.assertEqual(18, nx)

        sample = d4.load_input("sample.txt")

        num_xmas = d4.count_xmas(sample)
        self.assertEqual(18, num_xmas)

    def test_count_xmas_sample(self):
        sample = """..X...
.SAMX.
.A..A.
XMAS.S
.X....""".splitlines()
        num_xmas = d4.count_xmas(sample)
        print(f"\n{sample}")
        self.assertEqual(4, num_xmas)

    def test_count_x_mas_sample(self):
        sample = """.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........""".splitlines()
        num_x_mas = d4.count_xmas(sample, 'M', d4.check_x_mas)
        print(f"\n{sample}")
        self.assertEqual(9, num_x_mas)

    def test_count_x_mas_sample2(self):
        sample_up = """...
S.S
.A.
M.M""".splitlines()
        num_x_mas = d4.count_xmas(sample_up, 'M', d4.check_x_mas)
        print(f"\n{sample_up}")
        self.assertEqual(1, num_x_mas)

        sample2 = """.........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.""".splitlines()
        num_x_mas = d4.count_xmas(sample2, 'M', d4.check_x_mas)
        print(f"\n{sample2}")
        self.assertEqual(5, num_x_mas)

