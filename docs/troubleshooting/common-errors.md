---
title: Troubleshooting Common Errors
category: troubleshooting
topics: [errors, debugging, solutions, fixes]
difficulty: intermediate
last_updated: 2025-10-31
related:
  - ./faq.md
  - ./installation-issues.md
  - ../getting-started/installation.md
---

# Troubleshooting Common Errors

This guide helps you diagnose and resolve common errors encountered when using SysWeld.

## Table of Contents

- [Installation Errors](#installation-errors)
- [License Errors](#license-errors)
- [Meshing Errors](#meshing-errors)
- [Analysis Errors](#analysis-errors)
- [Convergence Issues](#convergence-issues)
- [Memory Errors](#memory-errors)
- [Graphics Errors](#graphics-errors)

## Installation Errors

### Error: "Installation failed - Error code 1603"

**Cause**: Insufficient permissions or conflicting software

**Solutions**:
1. Run installer as Administrator
2. Disable antivirus temporarily
3. Close all other applications
4. Check disk space (need 10+ GB free)
5. Verify system requirements

### Error: "Missing DLL files"

**Cause**: Missing Visual C++ redistributables or .NET Framework

**Solutions**:
1. Install Visual C++ Redistributables (2015-2022)
2. Install .NET Framework 4.8
3. Run Windows Update
4. Restart computer and retry installation

## License Errors

### Error: "License not found"

**Cause**: License server not reachable or license expired

**Solutions**:
1. Check license server connectivity:
   ```bash
   ping <license_server_ip>
   ```
2. Verify license configuration in **Help > License Manager**
3. Check firewall settings (port 27000-27009)
4. Verify license expiration date
5. Contact license administrator

### Error: "No licenses available"

**Cause**: All licenses in use or license pool exhausted

**Solutions**:
1. Wait for license to become available
2. Check who is using licenses (license manager)
3. Verify correct feature is being requested
4. Consider purchasing additional licenses

### Error: "License hostid mismatch"

**Cause**: Hardware change or license tied to different machine

**Solutions**:
1. Regenerate license for current hardware
2. Use license transfer tool
3. Contact licensing support with new hostid

## Meshing Errors

### Error: "Mesh generation failed - Invalid geometry"

**Cause**: Geometry issues (gaps, overlaps, degenerate faces)

**Solutions**:
1. Use **Geometry > Repair > Auto-fix** to repair geometry
2. Check for small gaps: **Geometry > Check > Gap Detection**
3. Remove tiny faces or edges: **Geometry > Clean > Remove Small Features**
4. Verify solid bodies are properly closed
5. Re-import geometry with tighter tolerances

### Error: "Mesh quality too poor"

**Cause**: High aspect ratio or distorted elements

**Solutions**:
1. Reduce global mesh size
2. Increase refinement at complex areas
3. Use **Mesh > Quality > Improve** tool
4. Adjust mesh transition ratio
5. Consider tetrahedral mesh for complex geometry

### Error: "Mesh generation timeout"

**Cause**: Geometry too complex or mesh too fine

**Solutions**:
1. Increase mesh size
2. Simplify geometry (remove small features)
3. Mesh in sections
4. Increase timeout limit in settings
5. Use more powerful hardware

## Analysis Errors

### Error: "Thermal analysis failed to converge"

**Cause**: Improper boundary conditions, time step too large, or numerical instability

**Solutions**:
1. Reduce time step size
2. Check boundary conditions (especially convection coefficients)
3. Verify initial conditions
4. Review heat source parameters
5. Check material properties (ensure no negative values)
6. Use smaller load increments

**Diagnostic Steps**:
```
1. View last successful time step
2. Check residual plot for divergence point
3. Review element quality near failure location
4. Verify contact definitions if applicable
```

### Error: "Mechanical analysis failed - Negative Jacobian"

**Cause**: Severe element distortion or rigid body motion

**Solutions**:
1. Improve mesh quality
2. Add proper constraints (prevent rigid body motion)
3. Check for overlapping elements
4. Review large deformation settings
5. Use stabilization if needed

### Error: "Material property error"

**Cause**: Invalid or missing material data

**Solutions**:
1. Verify all required properties defined
2. Check for negative values
3. Ensure temperature-dependent data covers simulation range
4. Review yield stress curve
5. Check material units consistency

## Convergence Issues

### Slow Convergence

**Symptoms**: Analysis runs but very slowly

**Solutions**:
1. **Adjust time stepping**:
   - Increase initial time step (if stable)
   - Use adaptive time stepping
   - Reduce maximum time step if overshooting

2. **Solver settings**:
   - Try different solver (Direct vs. Iterative)
   - Adjust convergence criteria
   - Enable line search
   - Use stabilization techniques

3. **Model simplification**:
   - Remove unnecessary details
   - Use symmetry if applicable
   - Coarsen mesh away from areas of interest

### Oscillating Solution

**Symptoms**: Convergence plot shows oscillations

**Solutions**:
1. Reduce time step size
2. Enable damping
3. Check for contact instabilities
4. Review load application (apply gradually)
5. Check material model (avoid discontinuities)

## Memory Errors

### Error: "Out of memory"

**Cause**: Insufficient RAM for model size

**Solutions**:
1. **Increase virtual memory**:
   - Windows: System Properties > Advanced > Performance Settings
   - Set custom size: Initial = RAM size, Maximum = 2× RAM size

2. **Reduce memory usage**:
   - Use shell elements instead of solids if possible
   - Reduce mesh density
   - Limit output frequency
   - Close other applications

3. **Increase Java heap** (if applicable):
   - Add `-Xmx16g` to launcher parameters
   - Replace 16 with available RAM in GB

4. **Use solver optimization**:
   - Enable out-of-core solver
   - Use iterative solver for large models

### Error: "Insufficient disk space"

**Cause**: Not enough disk space for results files

**Solutions**:
1. Free up disk space (need 2-3× model size)
2. Change working directory to larger drive
3. Reduce output frequency
4. Delete old result files
5. Compress previous results

## Graphics Errors

### Error: "Graphics initialization failed"

**Cause**: Incompatible or outdated graphics drivers

**Solutions**:
1. Update graphics drivers from manufacturer website
2. Check OpenGL version: **Help > System Info**
3. Disable hardware acceleration: **Tools > Options > Graphics**
4. Try compatibility mode (Windows)
5. Check if graphics card meets minimum requirements

### Black Screen or Rendering Issues

**Solutions**:
1. Update graphics drivers
2. Change anti-aliasing settings
3. Disable certain OpenGL features
4. Try different rendering mode
5. Check cable connections and monitor

### Error: "OpenGL context creation failed"

**Cause**: Graphics card doesn't support required OpenGL version

**Solutions**:
1. Update drivers
2. Check OpenGL version support
3. Use software rendering (slower): Set `LIBGL_ALWAYS_SOFTWARE=1`
4. Upgrade graphics card if necessary

## Error Messages Reference

### Critical Errors

| Error Code | Message | Common Cause | Solution |
|------------|---------|--------------|----------|
| E001 | "Solver failed" | Convergence issue | Reduce time step, check BCs |
| E002 | "Invalid input" | Bad parameter | Verify input values |
| E003 | "File not found" | Missing file | Check file path |
| E004 | "License error" | License issue | Check license server |
| E005 | "Memory allocation failed" | Out of memory | Free memory, reduce model |

### Warning Messages

| Warning Code | Message | Impact | Action |
|--------------|---------|--------|--------|
| W001 | "Poor mesh quality" | May affect accuracy | Review and improve mesh |
| W002 | "Extrapolating material data" | Reduced accuracy | Extend material data range |
| W003 | "Large deformation detected" | May cause instability | Monitor convergence |
| W004 | "Time step reduced" | Longer runtime | Normal, no action needed |

## Diagnostic Tools

### Log Files

SysWeld creates log files in the project directory:

- **`analysis.log`**: Analysis progress and errors
- **`solver.log`**: Detailed solver information
- **`error.log`**: Error messages and stack traces

**View logs**:
```bash
# Windows
notepad %USERPROFILE%\SysWeld\Projects\<project>\analysis.log

# Linux
cat ~/SysWeld/Projects/<project>/analysis.log
```

### System Information

Collect system info for support:

1. Go to **Help > System Information**
2. Click **Export**
3. Save as `system_info.txt`
4. Include in support ticket

### Debug Mode

Enable debug mode for detailed diagnostics:

1. Go to **Tools > Options > Advanced**
2. Check **Enable Debug Mode**
3. Set **Log Level**: Verbose
4. Reproduce issue
5. Check debug logs

## Getting Help

If you can't resolve the issue:

1. **Check documentation**: Search user guide for specific topics
2. **Knowledge base**: Visit online knowledge base
3. **Community forum**: Post question with error details
4. **Technical support**: 
   - Email: support@sysweld.com
   - Phone: [Support number]
   - Include: Error message, log files, system info, steps to reproduce

### Information to Include in Support Request

- SysWeld version and build number
- Operating system version
- Error message (exact text or screenshot)
- Log files (analysis.log, error.log)
- System information export
- Steps to reproduce
- When issue started occurring
- Any recent changes (software updates, etc.)

## Preventive Measures

### Best Practices

1. **Keep software updated**: Install latest patches
2. **Regular backups**: Save project files frequently
3. **Validate input**: Double-check parameters before running
4. **Monitor resources**: Watch memory and disk usage
5. **Clean working directory**: Delete old temporary files
6. **Document settings**: Keep notes on working configurations

### Pre-Analysis Checklist

Before running analysis:
- ✓ Geometry is clean and valid
- ✓ Mesh quality is acceptable
- ✓ Materials are properly defined
- ✓ Boundary conditions are correct
- ✓ Initial conditions are set
- ✓ Sufficient disk space available
- ✓ License is available

## Additional Resources

- [FAQ](./faq.md) - Frequently asked questions
- [Installation Issues](./installation-issues.md) - Installation-specific problems
- [Performance Optimization](../user-guide/performance.md) - Speed up simulations
- [User Forum](https://forum.sysweld.com) - Community discussions
