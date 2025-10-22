"""
Concrete plant implementations demonstrating inheritance and polymorphism.

This module contains specialized plant classes that inherit from AbstractPlant
and provide type-specific behavior.
"""

from base_classes import AbstractPlant


class Vegetable(AbstractPlant):
    """Vegetable plants - typically harvested for food, annual crops."""
    
    def __init__(self, plant_id, common_name, scientific_name, days_to_maturity,
                 harvest_type="single"):
        """Initialize a vegetable plant.
        
        Args:
            plant_id (str): Unique identifier
            common_name (str): Common name
            scientific_name (str): Scientific name
            days_to_maturity (int): Days to first harvest
            harvest_type (str): "single" or "continuous"
        """
        super().__init__(plant_id, common_name, scientific_name, days_to_maturity)
        self.harvest_type = harvest_type
        self.category = "vegetable"
        
    def get_spacing_requirement(self):
        """Vegetables typically need moderate to wide spacing.
        
        Returns:
            float: Spacing in inches
        """
        # Most vegetables need 12-18 inch spacing
        spacing_map = {
            "lettuce": 6,
            "tomato": 24,
            "pepper": 18,
            "carrot": 3,
            "cucumber": 24,
            "bean": 6,
            "squash": 36
        }
        return spacing_map.get(self.common_name.lower(), 12)
    
    def get_water_frequency(self):
        """Vegetables need consistent watering.
        
        Returns:
            str: Watering frequency description
        """
        return "Daily to every other day, keep soil consistently moist"
    
    def get_harvest_method(self):
        """Harvest method varies by vegetable type.
        
        Returns:
            str: Harvest method description
        """
        if self.harvest_type == "continuous":
            return "Cut or pick regularly to encourage more production"
        else:
            return "Single harvest when fully mature"
    
    def is_frost_sensitive(self):
        """Most vegetables are frost sensitive.
        
        Returns:
            bool: True for most vegetables
        """
        # Some vegetables tolerate frost
        frost_tolerant = ["lettuce", "kale", "broccoli", "carrot"]
        return self.common_name.lower() not in frost_tolerant


class Herb(AbstractPlant):
    """Herb plants - typically aromatic, used for cooking or medicine."""
    
    def __init__(self, plant_id, common_name, scientific_name, days_to_maturity,
                 is_perennial=False):
        """Initialize an herb plant.
        
        Args:
            plant_id (str): Unique identifier
            common_name (str): Common name
            scientific_name (str): Scientific name
            days_to_maturity (int): Days to first harvest
            is_perennial (bool): Whether plant returns each year
        """
        super().__init__(plant_id, common_name, scientific_name, days_to_maturity)
        self.is_perennial = is_perennial
        self.category = "herb"
        
    def get_spacing_requirement(self):
        """Herbs typically need closer spacing than vegetables.
        
        Returns:
            float: Spacing in inches
        """
        # Most herbs need 6-12 inch spacing
        spacing_map = {
            "basil": 10,
            "parsley": 8,
            "cilantro": 6,
            "oregano": 12,
            "thyme": 8,
            "rosemary": 18
        }
        return spacing_map.get(self.common_name.lower(), 8)
    
    def get_water_frequency(self):
        """Herbs prefer moderate watering.
        
        Returns:
            str: Watering frequency description
        """
        return "Every 2-3 days, allow soil to dry slightly between watering"
    
    def get_harvest_method(self):
        """Herbs are typically harvested by cutting.
        
        Returns:
            str: Harvest method description
        """
        return "Cut stems regularly, leaving 1/3 of plant to continue growing"
    
    def is_frost_sensitive(self):
        """Tender herbs are frost sensitive, hardy herbs are not.
        
        Returns:
            bool: Depends on herb type
        """
        frost_hardy = ["oregano", "thyme", "sage", "chives"]
        return self.common_name.lower() not in frost_hardy


class Flower(AbstractPlant):
    """Flower plants - grown for ornamental beauty."""
    
    def __init__(self, plant_id, common_name, scientific_name, days_to_maturity,
                 bloom_color="mixed", attracts_pollinators=True):
        """Initialize a flower plant.
        
        Args:
            plant_id (str): Unique identifier
            common_name (str): Common name
            scientific_name (str): Scientific name
            days_to_maturity (int): Days to first bloom
            bloom_color (str): Primary bloom color
            attracts_pollinators (bool): Whether attracts bees/butterflies
        """
        super().__init__(plant_id, common_name, scientific_name, days_to_maturity)
        self.bloom_color = bloom_color
        self.attracts_pollinators = attracts_pollinators
        self.category = "flower"
        
    def get_spacing_requirement(self):
        """Flowers need spacing based on mature size.
        
        Returns:
            float: Spacing in inches
        """
        # Spacing varies widely by flower type
        spacing_map = {
            "marigold": 8,
            "zinnia": 12,
            "sunflower": 24,
            "petunia": 10,
            "cosmos": 18
        }
        return spacing_map.get(self.common_name.lower(), 12)
    
    def get_water_frequency(self):
        """Flowers need consistent moisture during blooming.
        
        Returns:
            str: Watering frequency description
        """
        return "Daily during blooming season, keep evenly moist"
    
    def get_harvest_method(self):
        """Flowers can be cut for arrangements.
        
        Returns:
            str: Harvest method description
        """
        return "Cut stems in early morning for longest vase life, deadhead spent blooms"
    
    def is_frost_sensitive(self):
        """Most annual flowers are frost sensitive.
        
        Returns:
            bool: True for most annual flowers
        """
        # Most common garden flowers are frost sensitive
        return True
    
    def get_pollinator_benefits(self):
        """Describe benefits for pollinators.
        
        Returns:
            str: Description of pollinator benefits
        """
        if self.attracts_pollinators:
            return f"{self.common_name} attracts bees and butterflies, supporting garden ecosystem"
        else:
            return f"{self.common_name} is ornamental but less attractive to pollinators"
