"""
Garden Management System Demonstration

This script demonstrates all Project 3 requirements:
- Inheritance hierarchies
- Polymorphic behavior
- Abstract base classes
- Composition relationships
"""

from datetime import datetime, timedelta
from containers import RaisedBed, ContainerPot, GreenhousePlanter
from plants import Vegetable, Herb, Flower
from garden_manager import GardenCell, GardenManager


def demonstrate_inheritance():
    """Demonstrate inheritance hierarchy."""
    print("=" * 60)
    print("INHERITANCE DEMONSTRATION")
    print("=" * 60)
    
    # Create different container types - all inherit from AbstractPlantingContainer
    bed = RaisedBed("bed1", "Backyard Raised Bed", 48, 24, 12, "backyard", "cedar")
    pot = ContainerPot("pot1", "Patio Tomato Pot", 16, 14, "patio", has_drainage_holes=True)
    greenhouse = GreenhousePlanter("gh1", "Greenhouse Planter 1", 72, 30, 14, 
                                   "greenhouse", has_heating=True, has_supplemental_light=True)
    
    print(f"\nCreated three container types:")
    print(f"  - {bed} (RaisedBed)")
    print(f"  - {pot} (ContainerPot)")
    print(f"  - {greenhouse} (GreenhousePlanter)")
    
    print(f"\nAll inherit from AbstractPlantingContainer:")
    print(f"  - RaisedBed is AbstractPlantingContainer: {isinstance(bed, type(bed).__bases__[0])}")
    print(f"  - ContainerPot is AbstractPlantingContainer: {isinstance(pot, type(pot).__bases__[0])}")
    print(f"  - GreenhousePlanter is AbstractPlantingContainer: {isinstance(greenhouse, type(greenhouse).__bases__[0])}")


def demonstrate_polymorphism():
    """Demonstrate polymorphic behavior."""
    print("\n" + "=" * 60)
    print("POLYMORPHISM DEMONSTRATION")
    print("=" * 60)
    
    # Create containers
    containers = [
        RaisedBed("bed1", "Square Bed", 36, 36, 12),
        ContainerPot("pot1", "Round Pot", 14, 12),
        GreenhousePlanter("gh1", "Rectangular Planter", 48, 24, 10)
    ]
    
    print("\nSame method call, different behavior based on object type:")
    print("\nArea Calculations (polymorphic calculate_area method):")
    for container in containers:
        area = container.calculate_area()
        print(f"  {container.name:25s} -> {area:8.1f} square inches")
    
    print("\nVolume Calculations (polymorphic calculate_volume method):")
    for container in containers:
        volume = container.calculate_volume()
        print(f"  {container.name:25s} -> {volume:10.1f} cubic inches")
        
    print("\nDrainage Types (polymorphic get_drainage_type method):")
    for container in containers:
        drainage = container.get_drainage_type()
        print(f"  {container.name:25s} -> {drainage}")
    
    # Plant polymorphism
    print("\n" + "-" * 60)
    plants = [
        Vegetable("v1", "Tomato", "Solanum lycopersicum", 75),
        Herb("h1", "Basil", "Ocimum basilicum", 21),
        Flower("f1", "Marigold", "Tagetes", 45, "orange")
    ]
    
    print("\nPlant Spacing Requirements (polymorphic get_spacing_requirement):")
    for plant in plants:
        spacing = plant.get_spacing_requirement()
        print(f"  {plant.common_name:20s} -> {spacing} inches apart")
        
    print("\nWatering Frequencies (polymorphic get_water_frequency):")
    for plant in plants:
        water = plant.get_water_frequency()
        print(f"  {plant.common_name:20s} -> {water}")


def demonstrate_abstract_base_classes():
    """Demonstrate abstract base class usage."""
    print("\n" + "=" * 60)
    print("ABSTRACT BASE CLASS DEMONSTRATION")
    print("=" * 60)
    
    print("\nAbstract classes define interfaces that concrete classes must implement.")
    print("\nAbstractPlantingContainer requires:")
    print("  - calculate_area()")
    print("  - calculate_volume()")
    print("  - get_drainage_type()")
    
    print("\nAbstractPlant requires:")
    print("  - get_spacing_requirement()")
    print("  - get_water_frequency()")
    print("  - get_harvest_method()")
    print("  - is_frost_sensitive()")
    
    print("\nTrying to instantiate abstract classes directly would fail.")
    print("(Commented out to prevent errors)")
    # This would raise TypeError:
    # container = AbstractPlantingContainer("id", "name", 10, 10, 10)
    # plant = AbstractPlant("id", "name", "scientific", 30)
    
    print("\nConcrete classes implement all required methods:")
    bed = RaisedBed("bed1", "Test Bed", 48, 24, 12)
    tomato = Vegetable("v1", "Tomato", "Solanum lycopersicum", 75)
    
    print(f"  RaisedBed implements calculate_area: {bed.calculate_area()}")
    print(f"  Vegetable implements get_spacing_requirement: {tomato.get_spacing_requirement()}")


def demonstrate_composition():
    """Demonstrate composition relationships."""
    print("\n" + "=" * 60)
    print("COMPOSITION DEMONSTRATION")
    print("=" * 60)
    
    print("\nComposition: Objects contain other objects ('has-a' relationships)")
    
    # Create a garden manager
    manager = GardenManager("Demonstration Garden", "7a")
    
    # Add containers
    bed = RaisedBed("bed1", "Main Vegetable Bed", 96, 48, 12, "backyard")
    pot = ContainerPot("pot1", "Herb Container", 16, 12, "patio")
    manager.add_container(bed)
    manager.add_container(pot)
    
    print(f"\nGardenManager 'has-a' collection of containers:")
    print(f"  Manager contains {len(manager.containers)} containers")
    
    # Create cells
    cell1 = manager.create_cell(bed, "A", 1)
    cell2 = manager.create_cell(bed, "A", 2)
    cell3 = manager.create_cell(pot, "A", 1)
    
    print(f"\nGardenManager 'has-a' collection of cells:")
    print(f"  Manager contains {len(manager.cells)} cells")
    
    # Add plants to library
    tomato = Vegetable("v1", "Tomato", "Solanum lycopersicum", 75)
    basil = Herb("h1", "Basil", "Ocimum basilicum", 21)
    manager.add_plant_to_library(tomato)
    manager.add_plant_to_library(basil)
    
    print(f"\nGardenManager 'has-a' plant library:")
    print(f"  Library contains {len(manager.plant_library)} plant types")
    
    # GardenCell has-a container and has-a plant
    print(f"\nGardenCell 'has-a' container reference:")
    print(f"  {cell1.get_cell_location()} references {cell1.container.name}")
    
    cell1.plant_in_cell(tomato)
    print(f"\nGardenCell 'has-a' plant reference:")
    print(f"  {cell1.get_cell_location()} now contains {cell1.current_plant.common_name}")
    
    print("\nComposition allows flexible relationships without inheritance!")


def demonstrate_complete_system():
    """Demonstrate the complete integrated system."""
    print("\n" + "=" * 60)
    print("COMPLETE SYSTEM DEMONSTRATION")
    print("=" * 60)
    
    # Create garden
    garden = GardenManager("My Backyard Garden", "7a")
    print(f"\nCreated garden: {garden}")
    
    # Add diverse containers
    containers = [
        RaisedBed("bed1", "Main Vegetable Bed", 96, 48, 12, "backyard", "cedar"),
        RaisedBed("bed2", "Herb Bed", 48, 24, 10, "side_yard", "composite"),
        ContainerPot("pot1", "Tomato Pot 1", 18, 16, "deck"),
        ContainerPot("pot2", "Tomato Pot 2", 18, 16, "deck"),
        GreenhousePlanter("gh1", "Winter Greens", 60, 24, 12, "greenhouse", 
                         has_heating=True, has_supplemental_light=True)
    ]
    
    for container in containers:
        garden.add_container(container)
    
    print(f"Added {len(containers)} containers")
    
    # Create plant library
    plants = [
        Vegetable("v1", "Tomato", "Solanum lycopersicum", 75, "continuous"),
        Vegetable("v2", "Lettuce", "Lactuca sativa", 30, "continuous"),
        Vegetable("v3", "Pepper", "Capsicum annuum", 70, "continuous"),
        Herb("h1", "Basil", "Ocimum basilicum", 21, False),
        Herb("h2", "Oregano", "Origanum vulgare", 90, True),
        Herb("h3", "Parsley", "Petroselinum crispum", 70, False),
        Flower("f1", "Marigold", "Tagetes", 45, "orange", True),
        Flower("f2", "Zinnia", "Zinnia elegans", 60, "mixed", True),
    ]
    
    for plant in plants:
        garden.add_plant_to_library(plant)
    
    print(f"Added {len(plants)} plant types to library")
    
    # Create cells in main bed (4x8 grid)
    for row in ['A', 'B', 'C', 'D']:
        for col in range(1, 9):
            garden.create_cell(containers[0], row, col)
    
    # Create cells in herb bed (2x4 grid)
    for row in ['A', 'B']:
        for col in range(1, 5):
            garden.create_cell(containers[1], row, col)
    
    # Create cells in pots (1 cell each)
    garden.create_cell(containers[2], "A", 1)
    garden.create_cell(containers[3], "A", 1)
    
    print(f"Created {len(garden.cells)} planting cells")
    
    # Plant some things
    print("\nPlanting schedule:")
    planting_date = datetime.now() - timedelta(days=30)  # Planted 30 days ago
    
    plantings = [
        (0, plants[0]),   # Tomato in cell 0
        (1, plants[0]),   # Tomato in cell 1
        (5, plants[2]),   # Pepper in cell 5
        (32, plants[3]),  # Basil in herb bed
        (33, plants[4]),  # Oregano in herb bed
        (40, plants[0]),  # Tomato in pot 1
        (41, plants[0]),  # Tomato in pot 2
    ]
    
    for cell_index, plant in plantings:
        cell = garden.cells[cell_index]
        cell.plant_in_cell(plant, planting_date)
        print(f"  {cell.get_cell_location():30s} <- {plant.common_name}")
    
    # Show summary
    print("\n" + "-" * 60)
    summary = garden.get_garden_summary()
    print("Garden Summary:")
    for key, value in summary.items():
        print(f"  {key:25s}: {value}")
    
    # Show upcoming harvests
    print("\n" + "-" * 60)
    print("Upcoming harvests (next 60 days):")
    harvests = garden.get_upcoming_harvests(days_ahead=60)
    for cell, date in harvests:
        days_until = (date - datetime.now()).days
        print(f"  {cell.get_cell_location():30s} -> {cell.current_plant.common_name:15s} in {days_until} days")
    
    # Show plants by category
    print("\n" + "-" * 60)
    print("Plant Library by Category:")
    for category in ["vegetable", "herb", "flower"]:
        plants_in_category = garden.get_plants_by_category(category)
        print(f"  {category.capitalize()}s: {len(plants_in_category)} types")
        for plant in plants_in_category:
            print(f"    - {plant.common_name}")


def main():
    """Run all demonstrations."""
    print("\n" + "=" * 60)
    print("GARDEN MANAGEMENT SYSTEM - PROJECT 3 DEMONSTRATION")
    print("Object-Oriented Programming with Inheritance & Polymorphism")
    print("=" * 60)
    
    demonstrate_inheritance()
    demonstrate_polymorphism()
    demonstrate_abstract_base_classes()
    demonstrate_composition()
    demonstrate_complete_system()
    
    print("\n" + "=" * 60)
    print("DEMONSTRATION COMPLETE")
    print("=" * 60)
    print("\nThis system demonstrates:")
    print("  ✓ Inheritance hierarchies (containers and plants)")
    print("  ✓ Polymorphic behavior (methods behave differently per type)")
    print("  ✓ Abstract base classes (enforce interface contracts)")
    print("  ✓ Composition relationships (has-a relationships)")
    print("  ✓ Complete system integration")
    print("\nAll Project 3 requirements satisfied!")


if __name__ == "__main__":
    main()
