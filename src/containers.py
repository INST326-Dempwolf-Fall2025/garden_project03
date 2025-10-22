"""
Concrete container implementations demonstrating inheritance and polymorphism.

This module contains specialized container classes that inherit from
AbstractPlantingContainer and provide specific implementations.
"""

from base_classes import AbstractPlantingContainer


class RaisedBed(AbstractPlantingContainer):
    """A raised bed container - fixed location, excellent drainage."""
    
    def __init__(self, container_id, name, length, width, depth, location=None, 
                 material="wood"):
        """Initialize a raised bed.
        
        Args:
            container_id (str): Unique identifier
            name (str): Name of the bed
            length (float): Length in inches
            width (float): Width in inches
            depth (float): Depth in inches
            location (str, optional): Location description
            material (str): Construction material (wood, composite, metal)
        """
        super().__init__(container_id, name, length, width, depth, location)
        self.material = material
        self.is_mobile = False
        
    def calculate_area(self):
        """Calculate rectangular planting area.
        
        Returns:
            float: Area in square inches
        """
        return self.length * self.width
    
    def calculate_volume(self):
        """Calculate rectangular volume.
        
        Returns:
            float: Volume in cubic inches
        """
        return self.length * self.width * self.depth
    
    def get_drainage_type(self):
        """Raised beds have excellent drainage.
        
        Returns:
            str: Drainage description
        """
        return "Excellent - elevated with bottom drainage"
    
    def calculate_soil_needed(self, unit="cubic_feet"):
        """Calculate soil needed for this bed.
        
        Args:
            unit (str): Unit for result (cubic_feet or cubic_yards)
            
        Returns:
            float: Amount of soil needed
        """
        cubic_inches = self.calculate_volume()
        cubic_feet = cubic_inches / 1728
        
        if unit == "cubic_feet":
            return round(cubic_feet, 2)
        elif unit == "cubic_yards":
            return round(cubic_feet / 27, 2)
        else:
            return cubic_inches


class ContainerPot(AbstractPlantingContainer):
    """A container pot - mobile, circular, moderate drainage."""
    
    def __init__(self, container_id, name, diameter, depth, location=None,
                 has_drainage_holes=True):
        """Initialize a container pot.
        
        Args:
            container_id (str): Unique identifier
            name (str): Name of the pot
            diameter (float): Diameter in inches
            depth (float): Depth in inches
            location (str, optional): Location description
            has_drainage_holes (bool): Whether pot has drainage holes
        """
        # For pots, length and width are both diameter
        super().__init__(container_id, name, diameter, diameter, depth, location)
        self.diameter = diameter
        self.has_drainage_holes = has_drainage_holes
        self.is_mobile = True
        
    def calculate_area(self):
        """Calculate circular planting area.
        
        Returns:
            float: Area in square inches
        """
        import math
        radius = self.diameter / 2
        return math.pi * (radius ** 2)
    
    def calculate_volume(self):
        """Calculate cylindrical volume.
        
        Returns:
            float: Volume in cubic inches
        """
        import math
        radius = self.diameter / 2
        return math.pi * (radius ** 2) * self.depth
    
    def get_drainage_type(self):
        """Pot drainage depends on holes.
        
        Returns:
            str: Drainage description
        """
        if self.has_drainage_holes:
            return "Good - drainage holes present"
        else:
            return "Poor - no drainage holes (needs careful watering)"
    
    def move_to_location(self, new_location):
        """Move pot to a new location (pots are mobile).
        
        Args:
            new_location (str): New location description
        """
        old_location = self.location
        self.location = new_location
        return f"Moved {self.name} from {old_location} to {new_location}"


class GreenhousePlanter(AbstractPlantingContainer):
    """A greenhouse planter - controlled environment, optimal conditions."""
    
    def __init__(self, container_id, name, length, width, depth, location=None,
                 has_heating=False, has_supplemental_light=False):
        """Initialize a greenhouse planter.
        
        Args:
            container_id (str): Unique identifier
            name (str): Name of the planter
            length (float): Length in inches
            width (float): Width in inches
            depth (float): Depth in inches
            location (str, optional): Location in greenhouse
            has_heating (bool): Whether planter has heating system
            has_supplemental_light (bool): Whether has grow lights
        """
        super().__init__(container_id, name, length, width, depth, location)
        self.has_heating = has_heating
        self.has_supplemental_light = has_supplemental_light
        self.is_mobile = False
        self.climate_controlled = True
        
    def calculate_area(self):
        """Calculate rectangular planting area.
        
        Returns:
            float: Area in square inches
        """
        return self.length * self.width
    
    def calculate_volume(self):
        """Calculate rectangular volume.
        
        Returns:
            float: Volume in cubic inches
        """
        return self.length * self.width * self.depth
    
    def get_drainage_type(self):
        """Greenhouse planters have controlled drainage.
        
        Returns:
            str: Drainage description
        """
        return "Controlled - designed for optimal moisture retention"
    
    def can_grow_year_round(self):
        """Check if this planter supports year-round growing.
        
        Returns:
            bool: True if heating available for winter growing
        """
        return self.has_heating
    
    def get_growing_advantages(self):
        """List the advantages of this greenhouse planter.
        
        Returns:
            list: Advantages over outdoor growing
        """
        advantages = ["Protected from weather", "Pest control easier"]
        
        if self.has_heating:
            advantages.append("Year-round growing possible")
        if self.has_supplemental_light:
            advantages.append("Extended day length for faster growth")
            
        return advantages
