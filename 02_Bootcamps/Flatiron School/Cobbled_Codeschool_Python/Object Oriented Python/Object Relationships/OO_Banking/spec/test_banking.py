"""
This program contains all units tests BankAccount and Transfer classes.
"""

import unittest

from lib.transfer import Transfer
from lib.bank_account import BankAccount


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        """setUp function for BankAccount unit tests """
        self.avi = BankAccount("Avi")

    def test_initialization(self):
        """ Unit test for BankAccount.__init__ errors """
        self.assertTrue(isinstance(self.avi, BankAccount))

    def test_bankAccountHasName(self):
        """ Unit test for BankAccount.__init__ errors """
        self.assertEqual(self.avi.get_name(), "Avi")

    def test_bankAccountHasInitialBalance(self):
        """ Unit test for BankAccount.__init__ errors """
        self.assertEqual(self.avi.get_balance(), 1000.0)

    def test_bankAccountHasInitialStatus(self):
        """ Unit test for BankAccount.__init__ errors """
        self.assertEqual(self.avi.get_status(), "open")

    def test_bankAccount_deposit(self):
        """Test deposit functionality"""
        self.assertEqual(self.avi.get_balance(), 1000.0)
        self.avi.deposit(1000.0)
        self.assertEqual(self.avi.get_balance(), 2000.0)

    def test_bankAccount_displayBalance(self):
        """Test balance functionality"""
        self.assertEqual(self.avi.display_balance(), f'Your balance is {self.avi.get_balance()}.')

    def test_is_valid(self):
        """Returns True if is valid with an open status and a balance greater than 0"""
        self.broke = BankAccount("Kat Dennings")
        self.broke.set_balance(0)
        self.closed = BankAccount("Neth Behrs")
        self.closed.set_status("closed")
        self.assertTrue(self.avi.is_valid())
        self.assertFalse(self.broke.is_valid())
        self.assertFalse(self.closed.is_valid())

    def test_close_account(self):
        """Can close its account"""
        self.avi.close_account()
        self.assertEqual(self.avi.get_status(), "closed")


class TestTransfer(unittest.TestCase):

    def setUp(self):
        """setUp function for Transfer unit tests """
        self.avi = BankAccount("Avi")
        self.amanda = BankAccount("Amanda")
        self.transfer = Transfer(self.amanda, self.avi, 50.0)
        self.bad_transfer = Transfer(self.amanda, self.avi, 4000.0)

    def test_initialization(self):
        """ Unit test for Transfer.__init__ errors """
        self.assertTrue(isinstance(self.transfer, Transfer))

    def test_init_has_sender(self):
        """ Unit test for Transfer.__init__ errors """
        self.assertEqual(self.transfer.get_sender(), self.amanda)

    def test_init_has_receiver(self):
        """ Unit test for Transfer.__init__ errors """
        self.assertEqual(self.transfer.get_receiver(), self.avi)

    def test_init_has_pending_status(self):
        """ Unit test for Transfer.__init__ errors """
        self.assertEqual(self.transfer.get_status(), "pending")

    def test_init_has_amount(self):
        """ Unit test for Transfer.__init__ errors """
        self.assertEqual(self.transfer.get_amount(), 50.0)

    def test_transfer_is_valid(self):
        """Checks that both accounts are valid"""
        self.assertTrue(self.avi.is_valid())
        self.assertTrue(self.amanda.is_valid())
        self.assertTrue(self.transfer.is_valid())

    def test_execute_transaction(self):
        """Can execute a successful transaction between two accounts"""
        self.transfer.execute_transaction()
        self.assertEqual(self.amanda.get_balance(), 950)
        self.assertEqual(self.avi.get_balance(), 1050)
        self.assertEqual(self.transfer.get_status(), "complete")

    def test_execute_transaction_only_once(self):
        """each transfer can only happen once"""
        self.transfer.execute_transaction()
        self.assertEqual(self.amanda.get_balance(), 950)
        self.assertEqual(self.avi.get_balance(), 1050)
        self.assertEqual(self.transfer.get_status(), "complete")
        self.transfer.execute_transaction()
        self.assertEqual(self.amanda.get_balance(), 950)
        self.assertEqual(self.avi.get_balance(), 1050)

    def test_rejects_transfer(self):
        """rejects a transfer if the sender doesn't have a valid account"""
        self.assertEqual(self.bad_transfer.execute_transaction(), "Transaction rejected. Please check your account balance.")
        self.assertEqual(self.bad_transfer.get_status(), "rejected")

    def test_reverse_transfer(self):
        """can reverse a transfer between two accounts"""
        self.transfer.execute_transaction()
        self.assertEqual(self.amanda.get_balance(), 950)
        self.assertEqual(self.avi.get_balance(), 1050)
        self.transfer.reverse_transaction()
        self.assertEqual(self.amanda.get_balance(), 1000)
        self.assertEqual(self.avi.get_balance(), 1000)
        self.assertEqual(self.transfer.get_status(), "reversed")

    def test_invalid_reverse(self):
        """It can only reverse executed transactions"""
        self.transfer.reverse_transaction()
        self.assertEqual(self.amanda.get_balance(), 1000)
        self.assertEqual(self.avi.get_balance(), 1000)


if __name__ == '__main__':
    unittest.main(verbosity=2)

"""
===== OUTPUT =====
Ran 19 tests in 0.015s

OK
"""