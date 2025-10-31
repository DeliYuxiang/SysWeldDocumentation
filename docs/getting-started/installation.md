---
title: SysWeld Installation Guide
category: getting-started
topics: [installation, setup, configuration, prerequisites]
difficulty: beginner
last_updated: 2025-10-31
related:
  - ./README.md
  - ./quickstart.md
  - ../troubleshooting/installation-issues.md
---

# SysWeld Installation Guide

This guide walks you through installing SysWeld on your system.

## Prerequisites

Before installing SysWeld, ensure your system meets the requirements:

### System Requirements
- Operating System: Windows 10/11 64-bit or Linux (RHEL 7+, Ubuntu 20.04+)
- Processor: Intel Core i5 or AMD equivalent (i7/i9 or Ryzen 7/9 recommended)
- RAM: 8 GB minimum (32 GB recommended)
- Disk Space: 10 GB minimum (50 GB recommended)
- Graphics: OpenGL 3.3 compatible (Dedicated GPU recommended)

### Software Prerequisites
- **.NET Framework 4.8** (Windows only)
- **Visual C++ Redistributables** (Windows only)
- **Graphics drivers**: Up-to-date OpenGL drivers

## Windows Installation

### Step 1: Download Installer

1. Visit the SysWeld download portal
2. Log in with your credentials
3. Select your version (latest stable version recommended)
4. Download the Windows installer (e.g., `SysWeld_v2024_Setup.exe`)

### Step 2: Run Installer

1. **Right-click** the installer and select **Run as Administrator**
2. If prompted by User Account Control, click **Yes**
3. Wait for the installer to initialize

### Step 3: Installation Wizard

1. **Welcome Screen**: Click **Next**
2. **License Agreement**: Read and accept the terms, click **Next**
3. **Installation Directory**: 
   - Default: `C:\Program Files\SysWeld`
   - Or choose custom location
   - Click **Next**
4. **Component Selection**:
   - **Full Installation**: All components (recommended for new users)
   - **Custom**: Select specific components
   - Click **Next**
5. **Start Menu Folder**: Accept default or customize, click **Next**
6. **Ready to Install**: Review settings, click **Install**

### Step 4: Installation Progress

The installer will:
- Extract files (2-5 minutes)
- Install components
- Configure registry entries
- Create shortcuts

### Step 5: Complete Installation

1. Click **Finish**
2. Restart your computer if prompted
3. Launch SysWeld from the Start Menu or desktop shortcut

## Linux Installation

### Supported Distributions
- Red Hat Enterprise Linux (RHEL) 7.x, 8.x, 9.x
- Ubuntu 20.04 LTS, 22.04 LTS
- CentOS 7.x, 8.x (Stream)

### Step 1: Download Package

Download the appropriate package for your distribution:
- RHEL/CentOS: `sysweld-2024.rpm`
- Ubuntu/Debian: `sysweld-2024.deb`
- Generic: `sysweld-2024-linux.tar.gz`

### Step 2: Install Dependencies

**RHEL/CentOS:**
```bash
sudo yum install -y mesa-libGL mesa-libGLU libXt libXext
```

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install -y libgl1-mesa-glx libglu1-mesa libxt6 libxext6
```

### Step 3: Install SysWeld

**Using RPM:**
```bash
sudo rpm -ivh sysweld-2024.rpm
```

**Using DEB:**
```bash
sudo dpkg -i sysweld-2024.deb
sudo apt-get install -f  # Install missing dependencies
```

**Using TAR.GZ:**
```bash
tar -xzf sysweld-2024-linux.tar.gz
cd sysweld-2024
sudo ./install.sh
```

### Step 4: Configure Environment

Add SysWeld to your PATH (optional):
```bash
echo 'export PATH=/opt/sysweld/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

### Step 5: Launch SysWeld

```bash
sysweld
# Or
/opt/sysweld/bin/sysweld
```

## License Activation

### Node-Locked License

1. Launch SysWeld
2. Go to **Help > License Manager**
3. Click **Activate License**
4. Enter your license key
5. Click **Activate Online** (requires internet) or **Generate Request** (offline activation)

### Network License

1. Install the license server on a network machine
2. Configure the license server with your license file
3. On client machines:
   - Go to **Help > License Manager**
   - Click **Configure Network License**
   - Enter license server address: `@<server_ip>` or `<port>@<server_ip>`
   - Click **OK**

### Offline Activation

1. Generate a license request file
2. Submit to SysWeld licensing portal
3. Download the license response file
4. Import the response file in License Manager

## Post-Installation Configuration

### Graphics Configuration

For optimal performance:

1. **Update Graphics Drivers**: Ensure latest drivers installed
2. **Configure OpenGL**:
   - Go to **Tools > Options > Graphics**
   - Select **Hardware Acceleration**: Enabled
   - Set **Anti-aliasing**: 4x or 8x
   - Apply changes

### Memory Settings

For large models (Windows):

1. Right-click SysWeld shortcut
2. Select **Properties**
3. In **Target**, add: `-Xmx16g` (for 16GB max memory)
4. Apply changes

### Default Directories

Configure default directories:

1. **Tools > Options > Directories**
2. Set paths for:
   - Working directory
   - Material library
   - Examples
   - Scripts
3. Click **OK**

## Verification

Verify installation:

1. Launch SysWeld
2. Go to **Help > About**
3. Check version information
4. Run a test simulation (File > Examples > Simple Welding)

## Troubleshooting

### Common Issues

**Issue: Installer fails to start**
- Solution: Run as Administrator, disable antivirus temporarily

**Issue: Graphics errors or black screen**
- Solution: Update graphics drivers, check OpenGL compatibility

**Issue: License not found**
- Solution: Verify license server connectivity, check firewall settings

**Issue: Insufficient memory errors**
- Solution: Increase system RAM, adjust memory settings

For more help, see [Installation Troubleshooting](../troubleshooting/installation-issues.md)

## Updating SysWeld

To update to a newer version:

1. Download the latest installer
2. Close all SysWeld instances
3. Run the new installer (it will detect existing installation)
4. Choose **Update** or **Clean Install**
5. Follow installation wizard

## Uninstallation

### Windows

1. Go to **Settings > Apps > Apps & Features**
2. Find **SysWeld** in the list
3. Click **Uninstall**
4. Follow the uninstall wizard

Or use Control Panel:
1. **Control Panel > Programs > Uninstall a program**
2. Select **SysWeld**
3. Click **Uninstall**

### Linux

**RPM:**
```bash
sudo rpm -e sysweld
```

**DEB:**
```bash
sudo apt-get remove sysweld
```

**Manual:**
```bash
sudo /opt/sysweld/uninstall.sh
```

## Next Steps

Now that SysWeld is installed:

1. [Quick Start Tutorial](./quickstart.md) - Run your first simulation
2. [Basic Concepts](./basic-concepts.md) - Learn fundamental concepts
3. [Interface Overview](../user-guide/interface-overview.md) - Explore the interface

## Support

For installation support:
- Email: support@sysweld.com
- Phone: [Your support number]
- Online: [Support portal URL]
