"""
Composition classes demonstrating "has-a" relationships.

This module shows how objects can contain and coordinate other objects
without using inheritance.
"""

from datetime import datetime, timedelta


class GardenCell:
    """Represents a plantable cell within a container.
    
    This class demonstrates composition - a cell "has-a" container reference
    and "has-a" plant, but is not a subclass of either.
    """
    
    def __init__(self, cell_id, container, row, column):
        """Initialize a garden cell.
        
        Args:
            cell_id (str): Unique identifier for this cell
            container: PlantingContainer object this cell belongs to
            row (str): Row identifier (A, B, C, etc.)
            column (int): Column number
        """
        self.cell_id = cell_id
        self.container = container  # Composition: has-a container
        self.row = row
        self.column = column
        self.current_plant = None  # Composition: has-a plant
        self.planting_date = None
        self.is_occupied = False
        
    def plant_in_cell(self, plant, planting_date=None):
        """Plant something in this cell.
        
        Args:
            plant: Plant object to plant
            planting_date (datetime, optional): When planted, defaults to today
            
        Returns:
            bool: True if successful, False if cell occupied
        """
        if self.is_occupied:
            return False
            
        self.current_plant = plant
        self.planting_date = planting_date or datetime.now()
        self.is_occupied = True
        return True
    
    def harvest_cell(self):
        """Harvest and clear this cell.
        
        Returns:
            Plant: The plant that was harvested, or None
        """
        if not self.is_occupied:
            return None
            
        harvested_plant = self.current_plant
        self.current_plant = None
        self.planting_date = None
        self.is_occupied = False
        return harvested_plant
    
    def get_expected_harvest_date(self):
        """Calculate when this cell should be ready to harvest.
        
        Returns:
            datetime: Expected harvest date, or None if not planted
        """
        if not self.is_occupied or not self.current_plant:
            return None
            
        return self.planting_date + timedelta(days=self.current_plant.days_to_maturity)
    
    def get_cell_location(self):
        """Get human-readable location of this cell.
        
        Returns:
            str: Location description
        """
        return f"{self.container.name} - Cell {self.row}{self.column}"
    
    def __str__(self):
        """String representation of cell."""
        status = f"Growing {self.current_plant.common_name}" if self.is_occupied else "Empty"
        return f"{self.get_cell_location()}: {status}"


class GardenManager:
    """Main management system coordinating all garden components.
    
    This class demonstrates composition at a system level - it contains
    and manages collections of containers, plants, and cells.
    """
    
    def __init__(self, garden_name, zone):
        """Initialize the garden management system.
        
        Args:
            garden_name (str): Name of the garden
            zone (str): USDA hardiness zone (e.g., "7a")
        """
        self.garden_name = garden_name
        self.zone = zone
        self.containers = []  # Composition: has-many containers
        self.cells = []       # Composition: has-many cells
        self.plant_library = []  # Composition: has-many plant types
        
    def add_container(self, container):
        """Add a container to the garden.
        
        Args:
            container: PlantingContainer object
        """
        self.containers.append(container)
        
    def add_plant_to_library(self, plant):
        """Add a plant type to the library.
        
        Args:
            plant: Plant object (template, not actual planting)
        """
        self.plant_library.append(plant)
        
    def create_cell(self, container, row, column):
        """Create a plantable cell in a container.
        
        Args:
            container: PlantingContainer object
            row (str): Row identifier
            column (int): Column number
            
        Returns:
            GardenCell: The created cell
        """
        cell_id = f"{container.container_id}_{row}{column}"
        cell = GardenCell(cell_id, container, row, column)
        self.cells.append(cell)
        return cell
    
    def get_total_planting_area(self):
        """Calculate total planting area across all containers.
        
        Returns:
            float: Total area in square inches
        """
        return sum(container.calculate_area() for container in self.containers)
    
    def get_available_cells(self):
        """Get all unoccupied cells.
        
        Returns:
            list: List of empty GardenCell objects
        """
        return [cell for cell in self.cells if not cell.is_occupied]
    
    def get_occupied_cells(self):
        """Get all cells with plants.
        
        Returns:
            list: List of occupied GardenCell objects
        """
        return [cell for cell in self.cells if cell.is_occupied]
    
    def get_upcoming_harvests(self, days_ahead=7):
        """Get cells ready to harvest within specified days.
        
        Args:
            days_ahead (int): Number of days to look ahead
            
        Returns:
            list: List of tuples (GardenCell, harvest_date)
        """
        upcoming = []
        cutoff_date = datetime.now() + timedelta(days=days_ahead)
        
        for cell in self.get_occupied_cells():
            harvest_date = cell.get_expected_harvest_date()
            if harvest_date and harvest_date <= cutoff_date:
                upcoming.append((cell, harvest_date))
                
        return sorted(upcoming, key=lambda x: x[1])
    
    def get_plants_by_category(self, category):
        """Get all plants of a specific category from library.
        
        Args:
            category (str): Category name (vegetable, herb, flower)
            
        Returns:
            list: List of Plant objects in that category
        """
        return [plant for plant in self.plant_library 
                if hasattr(plant, 'category') and plant.category == category]
    
    def get_garden_summary(self):
        """Generate a summary of the garden status.
        
        Returns:
            dict: Summary statistics
        """
        return {
            "garden_name": self.garden_name,
            "zone": self.zone,
            "total_containers": len(self.containers),
            "total_cells": len(self.cells),
            "occupied_cells": len(self.get_occupied_cells()),
            "available_cells": len(self.get_available_cells()),
            "total_planting_area": round(self.get_total_planting_area(), 2),
            "plant_types_in_library": len(self.plant_library)
        }
    
    def __str__(self):
        """String representation of garden."""
        summary = self.get_garden_summary()
        return (f"{summary['garden_name']} (Zone {summary['zone']}): "
                f"{summary['occupied_cells']} of {summary['total_cells']} cells planted")
