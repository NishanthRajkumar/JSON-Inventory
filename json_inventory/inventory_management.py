'''
    @Author: Nishanth
    @Date: 30-03-2022 22:15:00
    @Last Modified by: Nishanth
    @Last Modified time: 30-03-2022 22:15:00
    @Title: Management of JSON Inventory Data
'''
import json
import os

class InventoryManagement:

    def __init__(self) -> None:
        self.inventory: dict[str, dict[str, float]] = {}
    
    def read_inventory(self, file_path) -> bool:
        """
            Description:
                reads the json file and stores the inventory details in inventory dictionary
            
            Parameter:
                file_path: file path of the json file
            
            Return:
                True if succesfully read from file, else False
        """
        if os.path.isfile(file_path) == False:
            return False
        file_stream = open(file_path)
        self.inventory = json.load(file_stream)
        file_stream.close()
        return True
    
    def compute_inventory_value(self) -> tuple[float, dict[str, float]]:
        """
            Description:
                computes the inventory value and returns value of each item and total.
            
            Parameter:
                None
            
            Return:
                a tuple (total_inventory_value, value_dict[str, float])
        """
        total_inventory_value = 0.0
        inventory_value_dict: dict[str, float] = {}
        for name, item_inventory in self.inventory.items():
            inventory_value_dict[name] = item_inventory['Weight'] * item_inventory['PricePerKG']
            total_inventory_value += inventory_value_dict[name]
        return (total_inventory_value, inventory_value_dict)
    
    def get_json_string(self) -> str:
        """
            Description:
                serializes inventory to json and returns the json string
            
            Parameter:
                None
            
            Return:
                returns str
        """
        return json.dumps(self.inventory, indent=4)