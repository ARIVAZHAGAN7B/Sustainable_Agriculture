class FarmerAgent:
    def __init__(self):
        self.farm_data = {}

    def collect_data(self, land_size, crop_preference, financial_budget):
        """Collects input from the farmer."""
        self.farm_data = {
            "land_size": land_size,
            "crop_preference": crop_preference,
            "financial_budget": financial_budget
        }
        return self.farm_data
