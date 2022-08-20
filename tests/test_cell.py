from unittest import TestCase
from cell import *


class TestCell(TestCase):
    def test_set_future_state(self):
        active_test_cell = Cell((0, 0), (0, 0), active=True)
        # neighbor count will have values from 0 to 8 inclusive.
        # This works because a cell can have 0 to 8 active neighbors

        # Active cells should only stay active if they have 2 or 3 neighbors
        for neighbor_count in range(9):
            active_test_cell.set_future_state(neighbor_count)
            if neighbor_count == 2 or neighbor_count == 3:
                self.assertTrue(active_test_cell.future_state, f'future_state should be true for {neighbor_count} neighbors')
            else:
                self.assertFalse(active_test_cell.future_state, f'future_state should be false for {neighbor_count} neighbors')

        # Inactive cells should only be activated if they have exactly 3 neighbors
        inactive_test_cell = Cell((0, 0), (0, 0), active=False)
        for neighbor_count in range(9):
            inactive_test_cell.set_future_state(neighbor_count)
            if neighbor_count == 3:
                self.assertTrue(inactive_test_cell.future_state, f'future_state should be true for {neighbor_count} neighbors')
            else:
                self.assertFalse(inactive_test_cell.future_state, f'future_state should be false for {neighbor_count} neighbors')

    def test_update(self):
        # scenario 1: inactive cell becomes active
        cell = Cell((0, 0), (0, 0))
        self.assertFalse(cell.active)
        cell.set_future_state(3)
        self.assertTrue(cell.future_state, 'Future state was set to true so the state should become active')
        cell.update()
        self.assertTrue(cell.active)
        self.assertIs(cell.future_state, None, 'Future state should be reset after an update')
        # scenario 2: active cell becomes inactive
        cell = Cell((0, 0), (0, 0), active=True)
        self.assertTrue(cell.active)
        cell.set_future_state(0)
        self.assertFalse(cell.future_state, 'Future state was set to false so the state should become inactive')
        cell.update()
        self.assertFalse(cell.active)
        self.assertIs(cell.future_state, None, 'Future state should be reset after an update')

    def test_flip(self):
        # test the flip method of the cell class
        # self.fail()
        cell = Cell((0, 0), (0, 0))
        self.assertFalse(cell.active)
        cell.flip()
        self.assertTrue(cell.active)
        cell.flip()
        self.assertFalse(cell.active)
