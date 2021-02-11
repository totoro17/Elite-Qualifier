import unittest
from main import chat

class TestExit(unittest.TestCase):
  #inputs that should trigger the repl to die
  def test_exit1(self):
    with self.assertRaises(SystemExit):
      chat.exitcheck(self, "exit")
  def test_exit2(self):
    with self.assertRaises(SystemExit):
      chat.exitcheck(self, "Exit")
  def test_exit3(self):
    with self.assertRaises(SystemExit):
      chat.exitcheck(self, "EXIT")
  #inputs that should NOT trigger the repl to die
  def test_no_exit1(self):
    chat.exitcheck(self, "beep boop")
  def test_no_exit2(self):
    chat.exitcheck(self, "this should not exit")


        

if __name__ == '__main__':
  unittest.main()
  