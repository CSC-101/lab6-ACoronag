import data
import lab6
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1
    def test_selection_sort_books_1(self):
        book1 = data.Book("percy", "olympian")
        book2 = data.Book("durk", "apples")
        book3 = data.Book("Amy", "dirty")
        books = [book1, book2, book3]
        result = lab6.selection_sort_books(books)
        expected = [book2, book3, book1]
        self.assertEqual(result,expected)

    def test_selection_sort_books_2(self):
        book1 = data.Book("percy", "sheep")
        book2 = data.Book("durk", "awesome")
        book3 = data.Book("Amy", "apples")
        books = [book3, book2, book1]
        result = lab6.selection_sort_books(books)
        expected = [book3, book2, book1]
        self.assertEqual(result,expected)    # Part 2


    # Part 3
    def test_str_translate_1(self):
        result = lab6.str_translate("hello","l","s")
        expected = "hesso"
        self.assertEqual(expected, result)

    def test_str_translate_2(self):
        result = lab6.str_translate("Hello how are you","o","w")
        expected = "Hellw hww are ywu"
        self.assertEqual(expected, result)

    # Part 4
    def test_histogram_1(self):
        result = lab6.histogram("i know who you are know know you")
        expected = {"i":1,"know":3,"who":1,"you":2,"are":1}
        self.assertEqual(expected,result)

    def test_histogram_2(self):
        result = lab6.histogram("hi hello Hi  hey heyo Hello heyo heyo")
        expected = {"hi":2,"hello":2,"hey":1,"heyo":3}
        self.assertEqual(expected,result)


if __name__ == '__main__':
    unittest.main()
