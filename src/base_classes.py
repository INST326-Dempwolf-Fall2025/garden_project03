"""
Abstract base classes for the Garden Management System.

This module defines the abstract interfaces that all concrete container
and plant classes must implement.
"""

from abc import ABC, abstractmethod


class AbstractPlantingContainer(ABC):
    """Abstract base class for all planting containers.
    
    This class defines the interface that all container types must implement,
    ensuring consistent behavior across different container types.
    """
    
    def __init__(self, container_id, name, length, width, depth, location=None):
        """Initialize a planting container.
        
        Args:
            container_id (str): Unique identifier for the container
            name (str): Human-readable name for the container
            length (float): Container length in inches
            width (float): Container width in inches
            depth (float): Container depth in inches
            location (str, optional): Location description
        """
        self.container_id = container_id
        self.name = name
        self.length = length
        self.width = width
        self.depth = depth
        self.location = location
        self.plants = []
        
    @abstractmethod
    def calculate_area(self):
        """Calculate the planting surface area.
        
        Returns:
            float: Area in square inches
        """
        pass
    
    @abstractmethod
    def calculate_volume(self):
        """Calculate the soil volume capacity.
        
        Returns:
            float: Volume in cubic inches
        """
        pass
    
    @abstractmethod
    def get_drainage_type(self):
        """Determine the drainage characteristics of this container.
        
        Returns:
            str: Description of drainage type
        """
        pass
    
    def get_planting_capacity(self, plant_spacing):
        """Calculate how many plants can fit with given spacing.
        
        Args:
            plant_spacing (float): Space between plants in inches
            
        Returns:
            int: Number of plants that can fit
        """
        if plant_spacing <= 0:
            return 0
        
        plants_per_row = int(self.length // plant_spacing)
        rows = int(self.width // plant_spacing)
        return plants_per_row * rows
    
    def add_plant(self, plant):
        """Add a plant to this container.
        
        Args:
            plant: Plant object to add
        """
        self.plants.append(plant)
    
    def __str__(self):
        """String representation of the container."""
        return f"{self.name} ({self.container_id}) at {self.location or 'unspecified location'}"


class AbstractPlant(ABC):
    """Abstract base class for all plant types.
    
    Defines the interface that all plant types must implement to ensure
    polymorphic behavior across different plant categories.
    """
    
    def __init__(self, plant_id, common_name, scientific_name, days_to_maturity):
        """Initialize a plant.
        
        Args:
            plant_id (str): Unique identifier
            common_name (str): Common name (e.g., "Tomato")
            scientific_name (str): Scientific name (e.g., "Solanum lycopersicum")
            days_to_maturity (int): Days from planting to harvest
        """
        self.plant_id = plant_id
        self.common_name = common_name
        self.scientific_name = scientific_name
        self.days_to_maturity = days_to_maturity
        
    @abstractmethod
    def get_spacing_requirement(self):
        """Get the spacing requirement for this plant.
        
        Returns:
            float: Spacing in inches between plants
        """
        pass
    
    @abstractmethod
    def get_water_frequency(self):
        """Get watering frequency for this plant type.
        
        Returns:
            str: Description of watering needs
        """
        pass
    
    @abstractmethod
    def get_harvest_method(self):
        """Get the appropriate harvest method for this plant.
        
        Returns:
            str: Description of harvest method
        """
        pass
    
    @abstractmethod
    def is_frost_sensitive(self):
        """Check if this plant is sensitive to frost.
        
        Returns:
            bool: True if frost sensitive, False otherwise
        """
        pass
    
    def __str__(self):
        """String representation of the plant."""
        return f"{self.common_name} ({self.scientific_name})"
