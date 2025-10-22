"""
Comprehensive test suite for Garden Management System.

Tests inheritance, polymorphism, abstract base classes, and composition.
"""

import unittest
from datetime import datetime, timedelta
from base_classes import AbstractPlantingContainer, AbstractPlant
from containers import RaisedBed, ContainerPot, GreenhousePlanter
from plants import Vegetable, Herb, Flower
from garden_manager import GardenCell, GardenManager


class TestInheritance(unittest.TestCase):
    """Test inheritance hierarchies."""
    
    def test_container_inheritance(self):
        """Test that all containers inherit from AbstractPlantingContainer."""
        bed = RaisedBed("bed1", "Front Bed", 48, 24, 12, "front yard")
        pot = ContainerPot("pot1", "Tomato Pot", 14, 12, "patio")
        planter = GreenhousePlanter("gh1", "GH Planter 1", 60, 24, 10, "greenhouse")
        
        self.assertIsInstance(bed, AbstractPlantingContainer)
        self.assertIsInstance(pot, AbstractPlantingContainer)
        self.assertIsInstance(planter, AbstractPlantingContainer)
        
    def test_plant_inheritance(self):
        """Test that all plants inherit from AbstractPlant."""
        veg = Vegetable("v1", "Tomato", "Solanum lycopersicum", 75)
        herb = Herb("h1", "Basil", "Ocimum basilicum", 21)
        flower = Flower("f1", "Marigold", "Tagetes", 45, "orange")
        
        self.assertIsInstance(veg, AbstractPlant)
        self.assertIsInstance(herb, AbstractPlant)
        self.assertIsInstance(flower, AbstractPlant)


class TestPolymorphism(unittest.TestCase):
    """Test polymorphic behavior across different object types."""
    
    def test_container_area_calculation(self):
        """Test that different containers calculate area polymorphically."""
        bed = RaisedBed("bed1", "Bed", 48, 24, 12)
        pot = ContainerPot("pot1", "Pot", 12, 10)  # diameter 12
        planter = GreenhousePlanter("gh1", "Planter", 60, 24, 10)
        
        # Each calculates area differently
        self.assertEqual(bed.calculate_area(), 1152)  # 48 * 24
        self.assertAlmostEqual(pot.calculate_area(), 113.1, places=0)  # π * 6²
        self.assertEqual(planter.calculate_area(), 1440)  # 60 * 24
        
    def test_container_volume_calculation(self):
        """Test that different containers calculate volume polymorphically."""
        bed = RaisedBed("bed1", "Bed", 48, 24, 12)
        pot = ContainerPot("pot1", "Pot", 12, 10)
        
        self.assertEqual(bed.calculate_volume(), 13824)
        self.assertAlmostEqual(pot.calculate_volume(), 1131, places=0)
        
    def test_drainage_differences(self):
        """Test that different containers report drainage differently."""
        bed = RaisedBed("bed1", "Bed", 48, 24, 12)
        pot_with_holes = ContainerPot("pot1", "Pot1", 12, 10, has_drainage_holes=True)
        pot_without_holes = ContainerPot("pot2", "Pot2", 12, 10, has_drainage_holes=False)
        planter = GreenhousePlanter("gh1", "Planter", 60, 24, 10)
        
        self.assertIn("Excellent", bed.get_drainage_type())
        self.assertIn("Good", pot_with_holes.get_drainage_type())
        self.assertIn("Poor", pot_without_holes.get_drainage_type())
        self.assertIn("Controlled", planter.get_drainage_type())
        
    def test_plant_spacing_polymorphism(self):
        """Test that different plants report different spacing needs."""
        tomato = Vegetable("v1", "Tomato", "Solanum lycopersicum", 75)
        basil = Herb("h1", "Basil", "Ocimum basilicum", 21)
        marigold = Flower("f1", "Marigold", "Tagetes", 45)
        
        self.assertEqual(tomato.get_spacing_requirement(), 24)
        self.assertEqual(basil.get_spacing_requirement(), 10)
        self.assertEqual(marigold.get_spacing_requirement(), 8)
        
    def test_plant_watering_polymorphism(self):
        """Test that different plants have different watering needs."""
        veg = Vegetable("v1", "Tomato", "Solanum lycopersicum", 75)
        herb = Herb("h1", "Basil", "Ocimum basilicum", 21)
        flower = Flower("f1", "Marigold", "Tagetes", 45)
        
        # Each should return different watering instructions
        veg_water = veg.get_water_frequency()
        herb_water = herb.get_water_frequency()
        flower_water = flower.get_water_frequency()
        
        self.assertNotEqual(veg_water, herb_water)
        self.assertIsInstance(veg_water, str)
        self.assertIsInstance(herb_water, str)
        self.assertIsInstance(flower_water, str)
        
    def test_harvest_method_polymorphism(self):
        """Test that different plants have different harvest methods."""
        veg = Vegetable("v1", "Tomato", "Solanum lycopersicum", 75, "continuous")
        herb = Herb("h1", "Basil", "Ocimum basilicum", 21)
        flower = Flower("f1", "Marigold", "Tagetes", 45)
        
        # Each should return different harvest instructions
        self.assertIn("regularly", veg.get_harvest_method())
        self.assertIn("Cut stems", herb.get_harvest_method())
        self.assertIn("Cut stems", flower.get_harvest_method())


class TestAbstractBaseClasses(unittest.TestCase):
    """Test that abstract base classes enforce implementation."""
    
    def test_cannot_instantiate_abstract_container(self):
        """Test that AbstractPlantingContainer cannot be instantiated."""
        with self.assertRaises(TypeError):
            AbstractPlantingContainer("id", "name", 10, 10, 10)
            
    def test_cannot_instantiate_abstract_plant(self):
        """Test that AbstractPlant cannot be instantiated."""
        with self.assertRaises(TypeError):
            AbstractPlant("id", "name", "scientific", 30)
            
    def test_concrete_classes_implement_abstract_methods(self):
        """Test that concrete classes implement all required methods."""
        bed = RaisedBed("bed1", "Bed", 48, 24, 12)
        
        # Should have all abstract methods implemented
        self.assertTrue(callable(bed.calculate_area))
        self.assertTrue(callable(bed.calculate_volume))
        self.assertTrue(callable(bed.get_drainage_type))
        
        veg = Vegetable("v1", "Tomato", "Solanum lycopersicum", 75)
        
        self.assertTrue(callable(veg.get_spacing_requirement))
        self.assertTrue(callable(veg.get_water_frequency))
        self.assertTrue(callable(veg.get_harvest_method))
        self.assertTrue(callable(veg.is_frost_sensitive))


class TestComposition(unittest.TestCase):
    """Test composition relationships."""
    
    def test_garden_cell_has_container(self):
        """Test that GardenCell has-a container reference."""
        bed = RaisedBed("bed1", "Front Bed", 48, 24, 12)
        cell = GardenCell("cell1", bed, "A", 1)
        
        self.assertIs(cell.container, bed)
        self.assertEqual(cell.container.name, "Front Bed")
        
    def test_garden_cell_has_plant(self):
        """Test that GardenCell has-a plant reference."""
        bed = RaisedBed("bed1", "Front Bed", 48, 24, 12)
        cell = GardenCell("cell1", bed, "A", 1)
        tomato = Vegetable("v1", "Tomato", "Solanum lycopersicum", 75)
        
        self.assertIsNone(cell.current_plant)
        cell.plant_in_cell(tomato)
        self.assertIs(cell.current_plant, tomato)
        
    def test_garden_manager_has_containers(self):
        """Test that GardenManager has-many containers."""
        manager = GardenManager("My Garden", "7a")
        bed = RaisedBed("bed1", "Bed", 48, 24, 12)
        pot = ContainerPot("pot1", "Pot", 12, 10)
        
        manager.add_container(bed)
        manager.add_container(pot)
        
        self.assertEqual(len(manager.containers), 2)
        self.assertIn(bed, manager.containers)
        self.assertIn(pot, manager.containers)
        
    def test_garden_manager_has_cells(self):
        """Test that GardenManager has-many cells."""
        manager = GardenManager("My Garden", "7a")
        bed = RaisedBed("bed1", "Bed", 48, 24, 12)
        manager.add_container(bed)
        
        cell1 = manager.create_cell(bed, "A", 1)
        cell2 = manager.create_cell(bed, "A", 2)
        
        self.assertEqual(len(manager.cells), 2)
        self.assertIn(cell1, manager.cells)
        self.assertIn(cell2, manager.cells)


class TestSystemIntegration(unittest.TestCase):
    """Test complete system working together."""
    
    def setUp(self):
        """Set up a complete garden system for testing."""
        self.manager = GardenManager("Test Garden", "7a")
        
        # Add containers
        self.bed = RaisedBed("bed1", "Main Bed", 48, 24, 12, "backyard")
        self.pot = ContainerPot("pot1", "Herb Pot", 12, 10, "patio")
        self.manager.add_container(self.bed)
        self.manager.add_container(self.pot)
        
        # Add plants to library
        self.tomato = Vegetable("v1", "Tomato", "Solanum lycopersicum", 75)
        self.basil = Herb("h1", "Basil", "Ocimum basilicum", 21)
        self.marigold = Flower("f1", "Marigold", "Tagetes", 45, "orange")
        self.manager.add_plant_to_library(self.tomato)
        self.manager.add_plant_to_library(self.basil)
        self.manager.add_plant_to_library(self.marigold)
        
        # Create cells
        self.cell1 = self.manager.create_cell(self.bed, "A", 1)
        self.cell2 = self.manager.create_cell(self.bed, "A", 2)
        self.cell3 = self.manager.create_cell(self.pot, "A", 1)
        
    def test_complete_planting_workflow(self):
        """Test complete workflow from planting to harvest."""
        # Plant in cells
        self.assertTrue(self.cell1.plant_in_cell(self.tomato))
        self.assertTrue(self.cell2.plant_in_cell(self.marigold))
        
        # Check status
        self.assertEqual(len(self.manager.get_occupied_cells()), 2)
        self.assertEqual(len(self.manager.get_available_cells()), 1)
        
        # Harvest
        harvested = self.cell1.harvest_cell()
        self.assertEqual(harvested, self.tomato)
        self.assertEqual(len(self.manager.get_occupied_cells()), 1)
        
    def test_garden_summary(self):
        """Test garden summary generation."""
        summary = self.manager.get_garden_summary()
        
        self.assertEqual(summary['garden_name'], "Test Garden")
        self.assertEqual(summary['zone'], "7a")
        self.assertEqual(summary['total_containers'], 2)
        self.assertEqual(summary['total_cells'], 3)
        self.assertEqual(summary['plant_types_in_library'], 3)
        
    def test_upcoming_harvests(self):
        """Test harvest date calculation."""
        # Plant something that matures in 21 days
        self.cell1.plant_in_cell(self.basil, datetime.now() - timedelta(days=15))
        
        # Should be ready in 6 days
        upcoming = self.manager.get_upcoming_harvests(days_ahead=10)
        self.assertEqual(len(upcoming), 1)
        
    def test_plants_by_category(self):
        """Test filtering plants by category."""
        vegetables = self.manager.get_plants_by_category("vegetable")
        herbs = self.manager.get_plants_by_category("herb")
        flowers = self.manager.get_plants_by_category("flower")
        
        self.assertEqual(len(vegetables), 1)
        self.assertEqual(len(herbs), 1)
        self.assertEqual(len(flowers), 1)


if __name__ == '__main__':
    unittest.main()
