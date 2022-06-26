'''
    @Author: Nishanth
    @Date: 30-03-2022 22:51:00
    @Last Modified by: Nishanth
    @Last Modified time: 30-03-2022 22:51:00
    @Title: UnitTesting the Management of JSON Inventory Data
'''
import json
import unittest
from inventory_management import InventoryManagement

class InventoryTest(unittest.TestCase):

    def test_read_inventory(self):
        inventory_mngmt = InventoryManagement()
        self.assertFalse(inventory_mngmt.read_inventory(r"grains_inventory.json"))
        self.assertTrue(inventory_mngmt.read_inventory(r"json_inventory\grains_inventory.json"))
    
    def test_compute_inventory_value(self):
        inventory_mngmt = InventoryManagement()
        inventory_mngmt.read_inventory(r"json_inventory\grains_inventory.json")
        total_value, item_values = inventory_mngmt.compute_inventory_value()
        self.assertEqual(total_value, 4939)
        total_item_value = 0.0
        for _,item_value in item_values.items():
            total_item_value += item_value
        self.assertEqual(total_item_value, 4939)
    
    def test_get_json_string(self):
        inventory_mngmt = InventoryManagement()
        inventory_mngmt.read_inventory(r"json_inventory\grains_inventory.json")
        serialized_json_string = inventory_mngmt.get_json_string()
        deserialized_json = json.loads(serialized_json_string)
        self.assertTrue(inventory_mngmt.inventory, deserialized_json)

if __name__ == '__main__':
    unittest.main()