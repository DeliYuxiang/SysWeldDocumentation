---
title: Quick Start Tutorial
category: getting-started
topics: [tutorial, quickstart, first-simulation, basics]
difficulty: beginner
last_updated: 2025-10-31
related:
  - ./README.md
  - ./installation.md
  - ../tutorials/simple-weld.md
---

# Quick Start Tutorial

This tutorial will guide you through creating your first welding simulation in SysWeld. You'll learn the basic workflow and run a simple butt weld simulation.

## Prerequisites

- SysWeld installed and activated
- Basic understanding of welding concepts
- Time required: 30-45 minutes

## Tutorial Overview

In this tutorial, you will:
1. Create a new project
2. Import or create geometry
3. Generate a mesh
4. Define materials
5. Set up welding parameters
6. Run thermal analysis
7. View and analyze results

## Step 1: Create a New Project

1. Launch SysWeld
2. Click **File > New Project**
3. In the dialog:
   - **Project Name**: `QuickStart_ButtWeld`
   - **Location**: Choose a working directory
   - **Template**: Select "Standard Welding"
4. Click **Create**

## Step 2: Import Geometry

For this tutorial, we'll use a simple butt weld geometry:

### Option A: Use Example Geometry
1. Go to **File > Import > Examples**
2. Select **Butt Weld - Two Plates**
3. Click **Open**

### Option B: Create Simple Geometry
1. Click **Geometry > Create > Box**
2. Create first plate:
   - Length: 100 mm
   - Width: 50 mm
   - Height: 10 mm
   - Position: (0, 0, 0)
3. Create second plate:
   - Length: 100 mm
   - Width: 50 mm
   - Height: 10 mm
   - Position: (0, 50, 0)
4. Click **Create**

## Step 3: Generate Mesh

### 3.1 Set Mesh Parameters

1. Select both plates in the model tree
2. Go to **Mesh > Auto Mesh**
3. Configure mesh settings:
   - **Element Type**: 3D Hexahedral
   - **Global Size**: 5 mm
   - **Refinement at Weld**: 2 mm
   - **Element Order**: Linear

### 3.2 Create Mesh

1. Click **Generate Mesh**
2. Wait for meshing to complete (1-2 minutes)
3. Review mesh quality:
   - Go to **Mesh > Quality Check**
   - Ensure aspect ratio < 5
   - Check for distorted elements

**Expected Result**: ~10,000-15,000 elements

## Step 4: Define Materials

### 4.1 Assign Material to Plates

1. Select both plates
2. Go to **Model > Materials**
3. From library, select **Steel > Structural Steel > S235JR**
4. Click **Assign**

### 4.2 Review Material Properties

1. Click **Edit Material**
2. Review:
   - Thermal conductivity (temperature-dependent)
   - Specific heat
   - Density
   - Mechanical properties (Young's modulus, Poisson's ratio, yield stress)
3. Click **OK**

## Step 5: Define Welding Process

### 5.1 Create Weld Seam

1. Go to **Welding > Define Weld Seam**
2. Click on the gap between plates to select the seam
3. Configure:
   - **Seam Type**: Butt weld
   - **Weld Path**: Linear (auto-detected)
   - **Start Point**: (0, 50, 5)
   - **End Point**: (100, 50, 5)

### 5.2 Set Welding Parameters

1. Select the weld seam
2. Go to **Welding > Parameters**
3. Set process parameters:
   - **Process**: GMAW (Gas Metal Arc Welding)
   - **Current**: 200 A
   - **Voltage**: 25 V
   - **Travel Speed**: 5 mm/s
   - **Efficiency**: 0.85

### 5.3 Configure Heat Source

1. Go to **Welding > Heat Source**
2. Select **Goldak Double Ellipsoid**
3. Parameters (auto-calculated, but verify):
   - **af (front)**: 3 mm
   - **ar (rear)**: 6 mm
   - **b (width)**: 4 mm
   - **c (depth)**: 8 mm

## Step 6: Set Boundary Conditions

### 6.1 Thermal Boundary Conditions

1. **Initial Temperature**: 
   - Select all parts
   - **Model > Initial Conditions > Temperature**: 20°C

2. **Convection**:
   - Select all external surfaces
   - **Model > Boundary Conditions > Convection**
   - Coefficient: 10 W/(m²·K)
   - Ambient temperature: 20°C

### 6.2 Mechanical Boundary Conditions (for subsequent mechanical analysis)

1. **Fixturing**:
   - Select bottom face of first plate
   - **Model > Constraints > Fixed**
2. **Symmetry** (if applicable):
   - Select symmetry plane
   - **Model > Constraints > Symmetry**

## Step 7: Run Thermal Analysis

### 7.1 Analysis Settings

1. Go to **Analysis > Thermal Analysis**
2. Configure:
   - **Time Step**: Automatic
   - **Total Time**: 200 seconds (weld time + cooling)
   - **Output Frequency**: 100 steps
   - **Solver**: Direct

### 7.2 Run Simulation

1. Click **Run Analysis**
2. Monitor progress in the status window
3. Expected runtime: 5-10 minutes (depending on hardware)

## Step 8: View Results

### 8.1 Temperature Results

1. Go to **Results > Temperature**
2. Use the timeline slider to animate temperature evolution
3. Key frames to check:
   - During welding: Peak temperature ~1500°C at weld pool
   - After welding: Cooling gradients
   - Final: Return to ambient

### 8.2 Create Plots

1. **Temperature vs. Time at a Point**:
   - **Results > Probe > Point**
   - Select a point near the weld
   - View temperature history

2. **Temperature Distribution**:
   - **Results > Contour > Temperature**
   - Adjust color scale for better visualization
   - Create snapshots at key times

### 8.3 Export Results

1. **Images**:
   - **File > Export > Image**
   - Choose PNG or JPEG
   
2. **Data**:
   - **Results > Export > CSV**
   - Select variables to export

## Step 9: Run Mechanical Analysis (Optional)

If you want to predict distortion and residual stress:

1. Go to **Analysis > Mechanical Analysis**
2. Use thermal results as input (automatic)
3. Click **Run Analysis**
4. View results:
   - Distortion (displacement magnitude)
   - Residual stress (von Mises stress)

## Verification Checklist

✓ Mesh quality is acceptable  
✓ Material properties are correct  
✓ Welding parameters are realistic  
✓ Heat source dimensions are appropriate  
✓ Boundary conditions are properly applied  
✓ Peak temperatures are within expected range (1200-1800°C for steel)  
✓ Results are physically reasonable  

## Common Issues and Solutions

**Issue**: Simulation crashes or doesn't converge
- **Solution**: Reduce time step, refine mesh at weld, check boundary conditions

**Issue**: Unrealistic temperatures (too high/low)
- **Solution**: Verify welding parameters, check heat source model, review efficiency factor

**Issue**: Very long computation time
- **Solution**: Increase time step (if stable), use coarser mesh away from weld, enable parallel processing

## Next Steps

Now that you've completed your first simulation:

1. **[Tutorials](../tutorials/README.md)**: Try more advanced simulations
2. **[User Guide](../user-guide/README.md)**: Learn detailed features
3. **[API Reference](../api-reference/README.md)**: Automate simulations with scripting

## Summary

Congratulations! You have successfully:
- Created a SysWeld project
- Set up a simple butt weld simulation
- Run thermal analysis
- Viewed and interpreted results

This workflow forms the foundation for more complex simulations in SysWeld.

## Additional Resources

- Video tutorial: [Link to video]
- Example files: Available in installation directory
- Community forum: [Forum link]
- Support: support@sysweld.com
