# Garden Management System - Project 3

**INST326: Object-Oriented Programming for Information Science**  
**Advanced OOP with Inheritance & Polymorphism**

## Project Overview

A comprehensive garden management system demonstrating advanced object-oriented programming principles including inheritance hierarchies, polymorphic behavior, abstract base classes, and composition relationships.

## System Architecture

### Inheritance Hierarchies

#### Container Hierarchy
```
AbstractPlantingContainer (Abstract Base Class)
├── RaisedBed (rectangular beds with excellent drainage)
├── ContainerPot (circular pots, mobile)
└── GreenhousePlanter (climate-controlled planters)
```

#### Plant Hierarchy
```
AbstractPlant (Abstract Base Class)
├── Vegetable (food crops, harvest-focused)
├── Herb (aromatic plants, continuous harvest)
└── Flower (ornamental, pollinator-focused)
```

### Composition Relationships

- **GardenManager** contains:
  - Collection of containers (has-many)
  - Collection of cells (has-many)
  - Plant library (has-many)

- **GardenCell** contains:
  - Reference to container (has-a)
  - Reference to plant (has-a)
  - Planting date and status

## Key Features

### 1. Polymorphic Behavior
Same method calls produce different results based on object type:
- `calculate_area()` - Rectangular vs. circular calculations
- `calculate_volume()` - Different geometric formulas
- `get_drainage_type()` - Container-specific drainage characteristics
- `get_spacing_requirement()` - Plant-type-specific spacing
- `get_water_frequency()` - Plant-category-specific watering needs

### 2. Abstract Base Classes
Enforce consistent interfaces across implementations:
- **AbstractPlantingContainer** - Requires area, volume, and drainage methods
- **AbstractPlant** - Requires spacing, watering, harvest, and frost methods

### 3. Composition Over Inheritance
- GardenManager coordinates multiple object types
- GardenCell links containers and plants without inheritance
- Flexible "has-a" relationships enable system scalability

## Installation & Setup

```bash
# Clone or download the project
cd garden_system

# No additional dependencies required - uses Python standard library
python3 --version  # Requires Python 3.7+
```

## Running the System

### Run Demonstrations
```bash
python3 demo.py
```

This demonstrates:
- Inheritance hierarchies
- Polymorphic behavior
- Abstract base class enforcement
- Composition relationships
- Complete integrated system

### Run Tests
```bash
python3 test_garden_system.py -v
```

Comprehensive test suite covering:
- Inheritance relationships
- Polymorphic method behavior
- Abstract class enforcement
- Composition functionality
- System integration

### Quick Test
```bash
python3 -m unittest test_garden_system.TestPolymorphism -v
```

## Usage Examples

### Creating Containers
```python
from containers import RaisedBed, ContainerPot, GreenhousePlanter

# Create different container types
bed = RaisedBed("bed1", "Vegetable Bed", 96, 48, 12, "backyard")
pot = ContainerPot("pot1", "Herb Pot", 14, 12, "patio")
planter = GreenhousePlanter("gh1", "Winter Greens", 72, 30, 14, 
                           "greenhouse", has_heating=True)

# Polymorphic area calculation
print(bed.calculate_area())      # Rectangular: length * width
print(pot.calculate_area())      # Circular: π * r²
print(planter.calculate_area())  # Rectangular: length * width
```

### Creating Plants
```python
from plants import Vegetable, Herb, Flower

# Create different plant types
tomato = Vegetable("v1", "Tomato", "Solanum lycopersicum", 75)
basil = Herb("h1", "Basil", "Ocimum basilicum", 21)
marigold = Flower("f1", "Marigold", "Tagetes", 45, "orange")

# Polymorphic spacing requirements
print(tomato.get_spacing_requirement())   # 24 inches
print(basil.get_spacing_requirement())    # 10 inches
print(marigold.get_spacing_requirement()) # 8 inches
```

### Managing a Complete Garden
```python
from garden_manager import GardenManager

# Create garden system
garden = GardenManager("My Garden", "7a")

# Add containers
garden.add_container(bed)
garden.add_container(pot)

# Create planting cells
cell1 = garden.create_cell(bed, "A", 1)
cell2 = garden.create_cell(bed, "A", 2)

# Plant in cells
cell1.plant_in_cell(tomato)
cell2.plant_in_cell(basil)

# Get garden summary
summary = garden.get_garden_summary()
print(f"Garden has {summary['occupied_cells']} planted cells")

# Check upcoming harvests
harvests = garden.get_upcoming_harvests(days_ahead=30)
for cell, date in harvests:
    print(f"{cell.get_cell_location()} ready on {date}")
```

## File Structure

```
garden_system/
├── base_classes.py           # Abstract base classes
├── containers.py             # Concrete container implementations
├── plants.py                 # Concrete plant implementations
├── garden_manager.py         # Composition classes
├── test_garden_system.py     # Comprehensive test suite
├── demo.py                   # Full system demonstration
└── README.md                 # This file
```

## Project 3 Requirements Checklist

✅ **Inheritance Hierarchy**
- Abstract base classes for containers and plants
- 3 concrete container types (RaisedBed, ContainerPot, GreenhousePlanter)
- 3 concrete plant types (Vegetable, Herb, Flower)
- Proper use of `super()` in constructors

✅ **Polymorphism**
- Area/volume calculations differ by container shape
- Plant spacing/watering varies by plant category
- Drainage characteristics differ by container type
- Harvest methods vary by plant type

✅ **Abstract Base Classes**
- Using Python's `abc` module
- Abstract methods enforced in concrete classes
- Cannot instantiate abstract classes directly
- Clear interface contracts

✅ **Composition**
- GardenManager contains containers, cells, and plant library
- GardenCell has-a container and has-a plant
- No inheritance between manager/cell and other classes
- Flexible relationships without tight coupling

✅ **Testing**
- 19 comprehensive unit tests
- Tests for inheritance, polymorphism, ABC, composition
- Integration tests for complete workflow
- All tests passing

✅ **Documentation**
- README with clear explanations
- Docstrings for all classes and methods
- Usage examples provided
- Architecture documentation

## Design Decisions

### Why Inheritance for Containers and Plants?

**Containers** share common attributes (dimensions, location) and operations (area, volume) but differ in:
- Shape calculations (rectangular vs. circular)
- Drainage characteristics
- Mobility (fixed vs. movable)

**Plants** share core attributes (name, maturity time) but differ in:
- Spacing requirements
- Watering needs
- Harvest methods
- Growing characteristics

Inheritance provides:
- Code reuse for shared attributes
- Polymorphic method implementation
- Clear "is-a" relationships

### Why Composition for GardenManager and GardenCell?

**GardenManager** coordinates multiple object types:
- Not "a type of" container or plant
- Needs flexible relationships with many objects
- Should manage, not inherit from, domain objects

**GardenCell** links containers and plants:
- Not "a type of" container or plant
- Represents a relationship, not an entity type
- Needs references to both without being either

Composition provides:
- Flexibility to change relationships
- No artificial inheritance hierarchies
- Clear separation of concerns

### Balancing Inheritance vs. Composition

**Use Inheritance When:**
- Clear "is-a" relationship exists
- Shared behavior across types
- Polymorphic behavior needed

**Use Composition When:**
- "Has-a" relationship exists
- Coordinating multiple types
- Relationship more important than type

## Learning Outcomes

This project demonstrates:

1. **Inheritance Design** - Logical hierarchies that reflect real-world relationships
2. **Polymorphic Behavior** - Same interface, different implementations
3. **Abstract Interfaces** - Enforcing consistent contracts
4. **Composition Patterns** - Flexible object relationships
5. **System Integration** - Multiple patterns working together

## Future Enhancements

Potential extensions:
- Additional container types (hanging baskets, window boxes)
- More plant categories (trees, vines, ground covers)
- Seasonal tracking and crop rotation
- Watering schedule optimization
- Companion planting recommendations
- Pest and disease tracking

## Team Information

**Team Members:** [Your team members here]  
**Section:** [Your section number]  
**Completion Date:** November 23, 2025

## Questions?

Contact your TA or attend office hours for assistance with:
- OOP design decisions
- Inheritance vs. composition trade-offs
- Abstract base class usage
- Testing strategies
