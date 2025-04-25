import unittest
from simple_notebook import Notebook

class TestNotebook(unittest.TestCase):
    def test_add_note(self):
        notebook = Notebook()
        notebook.add_note("Test note")
        self.assertEqual(len(notebook.notes), 1)

    def test_remove_note(self):
        notebook = Notebook()
        notebook.add_note("Test note")
        notebook.remove_note(0)
        self.assertEqual(len(notebook.notes), 0)

if __name__ == '__main__':
    unittest.main()
