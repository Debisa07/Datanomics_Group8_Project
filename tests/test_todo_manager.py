import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.todo_manager.todo_manager import add_task, delete_task, complete_task

class TestTodoManager(unittest.TestCase):
    def setUp(self):
        self.tasks = []

    def test_add_task(self):
        add_task(self.tasks, "Buy milk", "high")
        self.assertEqual(len(self.tasks), 1)
        self.assertEqual(self.tasks[0]["desc"], "Buy milk")
        self.assertEqual(self.tasks[0]["priority"], "high")
        self.assertFalse(self.tasks[0]["completed"])

    def test_delete_task(self):
        add_task(self.tasks, "Buy milk", "high")
        add_task(self.tasks, "Read book", "low")
        removed = delete_task(self.tasks, "1")
        self.assertEqual(removed["desc"], "Buy milk")
        self.assertEqual(len(self.tasks), 1)
        self.assertEqual(self.tasks[0]["desc"], "Read book")

    def test_complete_task(self):
        add_task(self.tasks, "Buy milk", "high")
        result = complete_task(self.tasks, "1")
        self.assertTrue(result)
        self.assertTrue(self.tasks[0]["completed"])
        # Try completing again
        result2 = complete_task(self.tasks, "1")
        self.assertFalse(result2)

    def test_invalid_delete(self):
        add_task(self.tasks, "Buy milk", "high")
        removed = delete_task(self.tasks, "2")
        self.assertIsNone(removed)

    def test_invalid_complete(self):
        add_task(self.tasks, "Buy milk", "high")
        result = complete_task(self.tasks, "2")
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
