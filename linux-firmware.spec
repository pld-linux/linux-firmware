# TODO
# - separate new iwlwifi-* subpackages from iwl7260 subpackage or merge:
#   - all iwl* into single iwlwifi-firmware package
#   - 1000+2000+5000+6000 into iwlwifi-dvm-firmware, 7000+8000+9000+22000+ax210+bz+sc into iwlwifi-mvm-firmware
# - subpackages for various firmwares?
# - (since 5.3) compress firmware: https://git.kernel.org/linus/82fd7a8142a10b8eb41313074b3859d82c0857dc
%define		rel	1
%define		ver	20250613
Summary:	Firmware files used by the Linux kernel
Summary(pl.UTF-8):	Pliki firmware'u używane przez jądro Linuksa
Name:		linux-firmware
Version:	%{ver}
Release:	%{rel}
License:	GPL+ and GPL v2+ and MIT and Redistributable, no modification permitted
Group:		Base/Kernel
# in case git snapshot is needed
#define		snap b6ea35ff6b9869470a0c68813f1668acb3d356a8
#Source0:	https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/snapshot/%{name}-%{snap}.tar.gz
# upstream tarball
Source0:	https://www.kernel.org/pub/linux/kernel/firmware/%{name}-%{version}.tar.xz
# Source0-md5:	2c86d7d1e2287deef2175a9c680ff713
Patch0:		check-files.patch
URL:		https://git.kernel.org/cgit/linux/kernel/git/firmware/linux-firmware.git/
BuildRequires:	rdfind
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Suggests:	%{name}-amd = %{ver}-%{rel}
Suggests:	%{name}-arm = %{ver}-%{rel}
Suggests:	%{name}-atheros = %{ver}-%{rel}
Suggests:	%{name}-broadcom = %{ver}-%{rel}
Suggests:	%{name}-cavium = %{ver}-%{rel}
Suggests:	%{name}-chelsio = %{ver}-%{rel}
Suggests:	%{name}-intel = %{ver}-%{rel}
Suggests:	%{name}-marvell = %{ver}-%{rel}
Suggests:	%{name}-mediatek = %{ver}-%{rel}
Suggests:	%{name}-mellanox = %{ver}-%{rel}
Suggests:	%{name}-netronome = %{ver}-%{rel}
Suggests:	%{name}-nvidia = %{ver}-%{rel}
Suggests:	%{name}-nxp = %{ver}-%{rel}
Suggests:	%{name}-qlogic = %{ver}-%{rel}
Suggests:	%{name}-qualcomm = %{ver}-%{rel}
Suggests:	%{name}-realtek = %{ver}-%{rel}
Suggests:	%{name}-ti = %{ver}-%{rel}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_strip	1
%define		_enable_debug_packages	0
%define		_noautochrpath		.*/lib/firmware/.*

%description
This package includes firmware files required for some devices to
operate.

%description -l pl.UTF-8
Ten pakiet zawiera pliki firmware'u wymagane do działania niektórych
urządzeń.

%package amd
Summary:	Firmware for AMD devices
Summary(pl.UTF-8):	Firmware dla urządzeń firmy AMD
Group:		Base/Kernel
Obsoletes:	microcode-data-amd < 20191221

%description amd
Firmware for AMD devices.

%description amd -l pl.UTF-8
Firmware dla urządzeń firmy AMD.

%package arm
Summary:	Firmware for ARM devices
Summary(pl.UTF-8):	Firmware dla urządzeń firmy ARM
Group:		Base/Kernel

%description arm
Firmware for ARM devices.

%description arm -l pl.UTF-8
Firmware dla urządzeń firmy ARM.

%package atheros
Summary:	Firmware for Atheros devices
Summary(pl.UTF-8):	Firmware dla urządzeń firmy Atheros
Group:		Base/Kernel

%description atheros
Firmware for Atheros devices.

%description atheros -l pl.UTF-8
Firmware dla urządzeń firmy Atheros.

%package broadcom
Summary:	Firmware for Broadcom devices
Summary(pl.UTF-8):	Firmware dla urządzeń firmy Broadcom
Group:		Base/Kernel

%description broadcom
Firmware for Broadcom devices.

%description broadcom -l pl.UTF-8
Firmware dla urządzeń firmy Broadcom.

%package cavium
Summary:	Firmware for Cavium devices
Summary(pl.UTF-8):	Firmware dla urządzeń firmy Cavium
Group:		Base/Kernel

%description cavium
Firmware for Cavium devices.

%description cavium -l pl.UTF-8
Firmware dla urządzeń firmy Cavium.

%package chelsio
Summary:	Firmware for Chelsio devices
Summary(pl.UTF-8):	Firmware dla urządzeń firmy Chelsio
Group:		Base/Kernel

%description chelsio
Firmware for Chelsio devices.

%description chelsio -l pl.UTF-8
Firmware dla urządzeń firmy Chelsio.

%package intel
Summary:	Firmware for Intel devices
Summary(pl.UTF-8):	Firmware dla urządzeń firmy Intel
Group:		Base/Kernel

%description intel
Firmware for Intel devices.

%description intel -l pl.UTF-8
Firmware dla urządzeń firmy Intel.

%package marvell
Summary:	Firmware for Marvell devices
Summary(pl.UTF-8):	Firmware dla urządzeń firmy Marvell
Group:		Base/Kernel

%description marvell
Firmware for Marvell devices.

%description marvell -l pl.UTF-8
Firmware dla urządzeń firmy Marvell.

%package mediatek
Summary:	Firmware for MediaTek devices
Summary(pl.UTF-8):	Firmware dla urządzeń firmy MediaTek
Group:		Base/Kernel

%description mediatek
Firmware for MediaTek devices.

%description mediatek -l pl.UTF-8
Firmware dla urządzeń firmy MediaTek.

%package mellanox
Summary:	Firmware for Mellanox devices
Summary(pl.UTF-8):	Firmware dla urządzeń firmy Mellanox
Group:		Base/Kernel

%description mellanox
Firmware for Mellanox devices.

%description mellanox -l pl.UTF-8
Firmware dla urządzeń firmy Mellanox.

%package netronome
Summary:	Firmware for Netronome devices
Summary(pl.UTF-8):	Firmware dla urządzeń firmy Netronome
Group:		Base/Kernel

%description netronome
Firmware for Netronome devices.

%description netronome -l pl.UTF-8
Firmware dla urządzeń firmy Netronome.

%package nvidia
Summary:	Firmware for NVIDIA devices
Summary(pl.UTF-8):	Firmware dla urządzeń firmy NVIDIA
Group:		Base/Kernel

%description nvidia
Firmware for NVIDIA devices.

%description nvidia -l pl.UTF-8
Firmware dla urządzeń firmy NVIDIA.

%package nxp
Summary:	Firmware for NXP devices
Summary(pl.UTF-8):	Firmware dla urządzeń firmy NXP
Group:		Base/Kernel

%description nxp
Firmware for NXP devices.

%description nxp -l pl.UTF-8
Firmware dla urządzeń firmy NXP.

%package qlogic
Summary:	Firmware for QLogic devices
Summary(pl.UTF-8):	Firmware dla urządzeń firmy QLogic
Group:		Base/Kernel

%description qlogic
Firmware for QLogic devices.

%description qlogic -l pl.UTF-8
Firmware dla urządzeń firmy QLogic.

%package qualcomm
Summary:	Firmware for Qualcomm devices
Summary(pl.UTF-8):	Firmware dla urządzeń firmy Qualcomm
Group:		Base/Kernel

%description qualcomm
Firmware for Qualcomm devices.

%description qualcomm -l pl.UTF-8
Firmware dla urządzeń firmy Qualcomm.

%package realtek
Summary:	Firmware for Realtek devices
Summary(pl.UTF-8):	Firmware dla urządzeń firmy Realtek
Group:		Base/Kernel

%description realtek
Firmware for Realtek devices.

%description realtek -l pl.UTF-8
Firmware dla urządzeń firmy Realtek.

%package ti
Summary:	Firmware for Texas Instruments devices
Summary(pl.UTF-8):	Firmware dla urządzeń firmy Texas Instruments
Group:		Base/Kernel

%description ti
Firmware for Texas Instruments devices.

%description ti -l pl.UTF-8
Firmware dla urządzeń firmy Texas Instruments.

%package -n iwl100-firmware
Summary:	Firmware for Intel(R) Wireless WiFi Link 100 Series Adapters
Summary(pl.UTF-8):	Firmware dla kart bezprzewodowych Intela z serii WiFi Link 100
Version:	39.31.5.1
Release:	%{ver}.%{rel}
License:	Redistributable, no modification permitted
Group:		Base/Kernel

%description -n iwl100-firmware
This package contains the firmware required by the Intel wireless
drivers for Linux to support the iwl100 hardware. Usage of the
firmware is subject to the terms and conditions contained inside the
provided LICENSE file. Please read it carefully.

%description -n iwl100-firmware -l pl.UTF-8
Ten pakiet zawiera firmware wymagane przez linuksowe sterowniki do
kart bezprzewodowych Intela typu iwl100. Używanie firmware'u podlega
warunkom opisanym w załączonym pliku LICENSE.

%package -n iwl105-firmware
Summary:	Firmware for Intel(R) Centrino Wireless-N 105 Series Adapters
Summary(pl.UTF-8):	Firmware dla kart bezprzewodowych Intela z serii Centrino Wireless-N 105
Version:	18.168.6.1
Release:	%{ver}.%{rel}
License:	Redistributable, no modification permitted
Group:		Base/Kernel

%description -n iwl105-firmware
This package contains the firmware required by the Intel wireless
drivers for Linux to support the iwl105 hardware. Usage of the
firmware is subject to the terms and conditions contained inside the
provided LICENSE file. Please read it carefully.

%description -n iwl105-firmware -l pl.UTF-8
Ten pakiet zawiera firmware wymagane przez linuksowe sterowniki do
kart bezprzewodowych Intela typu iwl105. Używanie firmware'u podlega
warunkom opisanym w załączonym pliku LICENSE.

%package -n iwl135-firmware
Summary:	Firmware for Intel(R) Centrino Wireless-N 135 Series Adapters
Summary(pl.UTF-8):	Firmware dla kart bezprzewodowych Intela z serii Centrino Wireless-N 135
Version:	18.168.6.1
Release:	%{ver}.%{rel}
License:	Redistributable, no modification permitted
Group:		Base/Kernel

%description -n iwl135-firmware
This package contains the firmware required by the Intel wireless
drivers for Linux to support the iwl135 hardware. Usage of the
firmware is subject to the terms and conditions contained inside the
provided LICENSE file. Please read it carefully.

%description -n iwl135-firmware -l pl.UTF-8
Ten pakiet zawiera firmware wymagane przez linuksowe sterowniki do
kart bezprzewodowych Intela typu iwl135. Używanie firmware'u podlega
warunkom opisanym w załączonym pliku LICENSE.

%package -n iwl1000-firmware
Summary:	Firmware for Intel(R) PRO/Wireless 1000 B/G/N network adaptors
Summary(pl.UTF-8):	Firmware dla kart bezprzewodowych Intela z serii Pro/Wireless 1000 B/G/N
Version:	39.31.5.1
Release:	%{ver}.%{rel}
License:	Redistributable, no modification permitted
Group:		Base/Kernel
Obsoletes:	iwl1000-firmware < 1:39.31.5.1-3
Obsoletes:	iwlwifi-1000-ucode < 1:39.31.5.1-2

%description -n iwl1000-firmware
This package contains the firmware required by the Intel wireless
drivers for Linux to support the iwl1000 hardware. Usage of the
firmware is subject to the terms and conditions contained inside the
provided LICENSE file. Please read it carefully.

%description -n iwl1000-firmware -l pl.UTF-8
Ten pakiet zawiera firmware wymagane przez linuksowe sterowniki do
kart bezprzewodowych Intela typu iwl1000. Używanie firmware'u podlega
warunkom opisanym w załączonym pliku LICENSE.

%package -n iwl2000-firmware
Summary:	Firmware for Intel(R) Centrino Wireless-N 2000 Series Adapters
Summary(pl.UTF-8):	Firmware dla kart bezprzewodowych Intela z serii Centrino Wireless-N 2000
Version:	18.168.6.1
Release:	%{ver}.%{rel}
License:	Redistributable, no modification permitted
Group:		Base/Kernel

%description -n iwl2000-firmware
This package contains the firmware required by the Intel wireless
drivers for Linux to support the iwl2000 hardware. Usage of the
firmware is subject to the terms and conditions contained inside the
provided LICENSE file. Please read it carefully.

%description -n iwl2000-firmware -l pl.UTF-8
Ten pakiet zawiera firmware wymagane przez linuksowe sterowniki do
kart bezprzewodowych Intela typu iwl2000. Używanie firmware'u podlega
warunkom opisanym w załączonym pliku LICENSE.

%package -n iwl2030-firmware
Summary:	Firmware for Intel(R) Centrino Wireless-N 2030 Series Adapters
Summary(pl.UTF-8):	Firmware dla kart bezprzewodowych Intela z serii Centrino Wireless-N 2030
Version:	18.168.6.1
Release:	%{ver}.%{rel}
License:	Redistributable, no modification permitted
Group:		Base/Kernel

%description -n iwl2030-firmware
This package contains the firmware required by the Intel wireless
drivers for Linux to support the iwl2030 hardware. Usage of the
firmware is subject to the terms and conditions contained inside the
provided LICENSE file. Please read it carefully.

%description -n iwl2030-firmware -l pl.UTF-8
Ten pakiet zawiera firmware wymagane przez linuksowe sterowniki do
kart bezprzewodowych Intela typu iwl2030. Używanie firmware'u podlega
warunkom opisanym w załączonym pliku LICENSE.

%package -n iwl3160-firmware
Summary:	Firmware for Intel(R) Wireless WiFi Link 3160 Series Adapters
Summary(pl.UTF-8):	Firmware dla kart bezprzewodowych Intela z serii WiFi Link 3160
Version:	25.30.13.0
Release:	%{ver}.%{rel}
License:	Redistributable, no modification permitted
Group:		Base/Kernel

%description -n iwl3160-firmware
This package contains the firmware required by the Intel wireless
drivers for Linux to support the iwl3160 hardware. Usage of the
firmware is subject to the terms and conditions contained inside the
provided LICENSE file. Please read it carefully.

%description -n iwl3160-firmware -l pl.UTF-8
Ten pakiet zawiera firmware wymagane przez linuksowe sterowniki do
kart bezprzewodowych Intela typu iwl3160. Używanie firmware'u podlega
warunkom opisanym w załączonym pliku LICENSE.

%package -n iwl3945-firmware
Summary:	Firmware for Intel(R) PRO/Wireless 3945 A/B/G network adaptors
Summary(pl.UTF-8):	Firmware dla kart bezprzewodowych Intela z serii PRO/Wireless 3945 A/B/G
Version:	15.32.2.9
Release:	%{ver}.%{rel}
License:	Redistributable, no modification permitted
Group:		Base/Kernel
Obsoletes:	iwlwifi-3945-ucode < 15.32.2.9-2

%description -n iwl3945-firmware
This package contains the firmware required by the iwl3945 driver for
Linux. Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%description -n iwl3945-firmware -l pl.UTF-8
Ten pakiet zawiera firmware wymagany przez linuksowy sterownik
iwl3945. Używanie firmware'u podlega warunkom opisanym w załączonym
pliku LICENSE.

%package -n iwl4965-firmware
Summary:	Firmware for Intel(R) PRO/Wireless 4965 A/G/N network adaptors
Summary(pl.UTF-8):	Firmware dla kart bezprzewodowych Intela z serii PRO/Wireless 4965 A/G/N
Version:	228.61.2.24
Release:	%{ver}.%{rel}
License:	Redistributable, no modification permitted
Group:		Base/Kernel
Obsoletes:	iwlwifi-4965-ucode < 228.61.2.24-2

%description -n iwl4965-firmware
This package contains the firmware required by the iwl4965 driver for
Linux. Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%description -n iwl4965-firmware -l pl.UTF-8
Ten pakiet zawiera firmware wymagany przez linuksowy sterownik
iwl4965. Używanie firmware'u podlega warunkom opisanym w załączonym
pliku LICENSE.

%package -n iwl5000-firmware
Summary:	Firmware for Intel(R) PRO/Wireless 5000 A/G/N network adaptors
Summary(pl.UTF-8):	Firmware dla kart bezprzewodowych Intela z serii PRO/Wireless 5000 A/G/N
Version:	8.83.5.1_1
Release:	%{ver}.%{rel}
License:	Redistributable, no modification permitted
Group:		Base/Kernel
Obsoletes:	iwlwifi-5000-ucode < 8.83.5.1-5

%description -n iwl5000-firmware
This package contains the firmware required by the Intel wireless
drivers for Linux to support the iwl5000 hardware. Usage of the
firmware is subject to the terms and conditions contained inside the
provided LICENSE file. Please read it carefully.

%description -n iwl5000-firmware -l pl.UTF-8
Ten pakiet zawiera firmware wymagane przez linuksowe sterowniki do
kart bezprzewodowych Intela typu iwl5000. Używanie firmware'u podlega
warunkom opisanym w załączonym pliku LICENSE.

%package -n iwl5150-firmware
Summary:	Firmware for Intel(R) PRO/Wireless 5150 A/G/N network adaptors
Summary(pl.UTF-8):	Firmware dla kart bezprzewodowych Intela z serii PRO/Wireless 5150 A/G/N
Version:	8.24.2.2
Release:	%{ver}.%{rel}
License:	Redistributable, no modification permitted
Group:		Base/Kernel
Obsoletes:	iwlwifi-5150-ucode < 8.24.2.2-2

%description -n iwl5150-firmware
This package contains the firmware required by the Intel wireless
drivers for Linux to support the iwl5150 hardware. Usage of the
firmware is subject to the terms and conditions contained inside the
provided LICENSE file. Please read it carefully.

%description -n iwl5150-firmware -l pl.UTF-8
Ten pakiet zawiera firmware wymagane przez linuksowe sterowniki do
kart bezprzewodowych Intela typu iwl5150. Używanie firmware'u podlega
warunkom opisanym w załączonym pliku LICENSE.

%package -n iwl6000-firmware
Summary:	Firmware for Intel(R) Wireless WiFi Link 6000 AGN Adapter
Summary(pl.UTF-8):	Firmware dla kart bezprzewodowych Intela z serii WiFi Link 6000 AGN
Version:	9.221.4.1
Release:	%{ver}.%{rel}
License:	Redistributable, no modification permitted
Group:		Base/Kernel
Obsoletes:	iwlwifi-6000-ucode < 9.221.4.1-2

%description -n iwl6000-firmware
This package contains the firmware required by the Intel wireless
drivers for Linux to support the iwl6000 hardware. Usage of the
firmware is subject to the terms and conditions contained inside the
provided LICENSE file. Please read it carefully.

%description -n iwl6000-firmware -l pl.UTF-8
Ten pakiet zawiera firmware wymagane przez linuksowe sterowniki do
kart bezprzewodowych Intela typu iwl6000. Używanie firmware'u podlega
warunkom opisanym w załączonym pliku LICENSE.

%package -n iwl6000g2a-firmware
Summary:	Firmware for Intel(R) Wireless WiFi Link 6005 Series Adapters
Summary(pl.UTF-8):	Firmware dla kart bezprzewodowych Intela z serii WiFi Link 6005
Version:	18.168.6.1
Release:	%{ver}.%{rel}
Group:		Base/Kernel
License:	Redistributable, no modification permitted

%description -n iwl6000g2a-firmware
This package contains the firmware required by the Intel wireless
drivers for Linux to support the iwl6000g2a hardware. Usage of the
firmware is subject to the terms and conditions contained inside the
provided LICENSE file. Please read it carefully.

%description -n iwl6000g2a-firmware -l pl.UTF-8
Ten pakiet zawiera firmware wymagane przez linuksowe sterowniki do
kart bezprzewodowych Intela typu iwl6000g2a. Używanie firmware'u
podlega warunkom opisanym w załączonym pliku LICENSE.

%package -n iwl6000g2b-firmware
Summary:	Firmware for Intel(R) Wireless WiFi Link 6030 Series Adapters
Summary(pl.UTF-8):	Firmware dla kart bezprzewodowych Intela z serii WiFi Link 6030
Version:	18.168.6.1
Release:	%{ver}.%{rel}
License:	Redistributable, no modification permitted
Group:		Base/Kernel
Obsoletes:	iwlwifi-6030-ucode < 18.168.6.1-2

%description -n iwl6000g2b-firmware
This package contains the firmware required by the Intel wireless
drivers for Linux to support the iwl6000g2b hardware. Usage of the
firmware is subject to the terms and conditions contained inside the
provided LICENSE file. Please read it carefully.

%description -n iwl6000g2b-firmware -l pl.UTF-8
Ten pakiet zawiera firmware wymagane przez linuksowe sterowniki do
kart bezprzewodowych Intela typu iwl6000g2b. Używanie firmware'u
podlega warunkom opisanym w załączonym pliku LICENSE.

%package -n iwl6050-firmware
Summary:	Firmware for Intel(R) Wireless WiFi Link 6050 Series Adapters
Summary(pl.UTF-8):	Firmware dla kart bezprzewodowych Intela z serii WiFi Link 6050
Version:	41.28.5.1
Release:	%{ver}.%{rel}
License:	Redistributable, no modification permitted
Group:		Base/Kernel
Obsoletes:	iwlwifi-6050-ucode < 41.28.5.1-2

%description -n iwl6050-firmware
This package contains the firmware required by the Intel wireless
drivers for Linux to support the iwl6050 hardware. Usage of the
firmware is subject to the terms and conditions contained inside the
provided LICENSE file. Please read it carefully.

%description -n iwl6050-firmware -l pl.UTF-8
Ten pakiet zawiera firmware wymagane przez linuksowe sterowniki do
kart bezprzewodowych Intela typu iwl6050. Używanie firmware'u podlega
warunkom opisanym w załączonym pliku LICENSE.

%package -n iwl7260-firmware
Summary:	Firmware for Intel(R) Wireless WiFi Link 726x/8000/9000/AX200/AX201 Series Adapters
Summary(pl.UTF-8):	Firmware dla kart bezprzewodowych Intela z serii WiFi Link 726x/8000/9000/AX200/AX201
Version:	25.228.9.0
Release:	%{ver}.%{rel}
License:	Redistributable, no modification permitted
Group:		Base/Kernel
Obsoletes:	iwlwifi-7260-ucode < 25.228.9.0-8
Conflicts:	linux-firmware < 20181008-4

%description -n iwl7260-firmware
This package contains the firmware required by the Intel wireless
drivers for Linux to support the iwl7260 hardware. Usage of the
firmware is subject to the terms and conditions contained inside the
provided LICENSE file. Please read it carefully.

%description -n iwl7260-firmware -l pl.UTF-8
Ten pakiet zawiera firmware wymagane przez linuksowe sterowniki do
kart bezprzewodowych Intela typu iwl7260. Używanie firmware'u podlega
warunkom opisanym w załączonym pliku LICENSE.

%package -n libertas-sd8686-firmware
Summary:	Firmware for Marvell Libertas SD 8686 Network Adapter
Summary(pl.UTF-8):	Firmware dla kart sieciowych Marvell Libertas SD 8686
Version:	0.%{ver}
Release:	%{rel}
License:	Redistributable, no modification permitted
Group:		Base/Kernel
Obsoletes:	libertas-sd8686-firmware < 9.70.20.p0-4

%description -n libertas-sd8686-firmware
Firmware for Marvell Libertas SD 8686 Network Adapter.

%description -n libertas-sd8686-firmware -l pl.UTF-8
Firmware dla kart sieciowych Marvell Libertas SD 8686.

%package -n libertas-sd8787-firmware
Summary:	Firmware for Marvell Libertas SD 8787 Network Adapter
Summary(pl.UTF-8):	Firmware dla kart sieciowych Marvell Libertas SD 8787
Version:	0.%{ver}
Release:	%{rel}
License:	Redistributable, no modification permitted
Group:		Base/Kernel

%description -n libertas-sd8787-firmware
Firmware for Marvell Libertas SD 8787 Network Adapter.

%description -n libertas-sd8787-firmware -l pl.UTF-8
Firmware dla kart sieciowych Marvell Libertas SD 8787.

%package -n libertas-usb8388-firmware
Summary:	Firmware for Marvell Libertas USB 8388 Network Adapter
Summary(pl.UTF-8):	Firmware dla kart sieciowych Marvell Libertas USB 8388
Version:	0.%{ver}
Release:	%{rel}
License:	Redistributable, no modification permitted
Group:		Base/Kernel
Obsoletes:	libertas-usb8388-firmware < 2:5.110.22.p23-8

%description -n libertas-usb8388-firmware
Firmware for Marvell Libertas USB 8388 Network Adapter.

%description -n libertas-usb8388-firmware -l pl.UTF-8
Firmware dla kart sieciowych Marvell Libertas USB 8388.

%package -n libertas-usb8388-olpc-firmware
Summary:	OLPC firmware for Marvell Libertas USB 8388 Network Adapter
Summary(pl.UTF-8):	Firmware OLPC dla kart sieciowych Marvell Libertas USB 8388
Version:	0.%{ver}
Release:	%{rel}
Group:		Base/Kernel
License:	Redistributable, no modification permitted

%description -n libertas-usb8388-olpc-firmware
Firmware for Marvell Libertas USB 8388 Network Adapter with OLPC mesh
network support.

%description -n libertas-usb8388-olpc-firmware -l pl.UTF-8
Firmware dla kart sieciowych Marvell Libertas USB 8388 z obsługą
punktów sieci OLPC.

%prep
%setup -q
%patch -P0 -p1

# Remove firmware shipped in separate packages already
# Perhaps these should be built as subpackages of linux-firmware?
# - ql{2100,2200,2300,2322,2400,2500}-firmware.spec
%{__rm} ql{2100,2200,2300,2322,2400,2500}_fw.bin LICENCE.qla2xxx
# - alsa-firmware.spec
%{__rm} -r ess korg sb16 yamaha
# We have _some_ ralink firmware in separate packages already. (which packages???)
%{__rm} rt73.bin rt2561.bin rt2561s.bin rt2661.bin
# And _some_ conexant firmware. (which packages???)
%{__rm} v4l-cx23418-apu.fw v4l-cx23418-cpu.fw v4l-cx23418-dig.fw v4l-cx25840.fw
# Netxen firmware (which package???)
%{__rm} phanfw.bin LICENCE.phanfw
# - radeon-ucode.spec
%{__rm} radeon/{ARUBA,BARTS,BONAIRE,BTC,CAICOS,CAYMAN,CEDAR,CYPRESS,HAINAN,HAWAII,JUNIPER,KABINI,KAVERI,MULLINS,OLAND,PALM,PITCAIRN,R700,REDWOOD,SUMO,SUMO2,TAHITI,TURKS,VERDE,bonaire,hainan,hawaii,kabini,kaveri,mullins,oland,pitcairn,tahiti,verde}_*.bin
# R{100,200,300,420,520}_cp.bin, R600_{me,pfp}.bin, RS{600,690}_cp.bin, RS780_{me,pfp}.bin, RV610_{me,pfp}.bin RV620_{me,pfp}.bin, RV630_{me,pfp}.bin, RV635_{me,pfp}.bin, RV710-{me,pfp}.bin, RV730_{me,pfp}.bin RV770_{me,pfp}.bin are missing in radeon_ucode
%{__rm} radeon/R600_{rlc,uvd}.bin
%{__rm} radeon/RS780_uvd.bin
%{__rm} radeon/RV710_{smc,uvd}.bin
%{__rm} radeon/RV730_smc.bin
%{__rm} radeon/RV740_smc.bin
%{__rm} radeon/RV770_{smc,uvd}.bin

# No need to install old firmware versions where we also provide newer versions
# which are preferred and support the same (or more) hardware
%{__rm} libertas/sd8686_v8*
%{__rm} libertas/usb8388_v5.bin

# Remove source files we don't need to install
%{__rm} */*.asm dsp56k/{Makefile,concat-bootstrap.pl} isci/{Makefile,README,*.[ch]}
%{__rm} -r carl9170fw usbdux
%{__rm} Makefile

%{__mv} rtw88/README README.rtw88

%install
rm -rf $RPM_BUILD_ROOT

./copy-firmware.sh $RPM_BUILD_ROOT/lib/firmware

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc WHENCE LICENCE.* LICENSE.* README.md
# TDA7706_OM_v*_boot.txt
/lib/firmware/3com
/lib/firmware/acenic
/lib/firmware/adaptec
/lib/firmware/advansys
/lib/firmware/aeonsemi
/lib/firmware/agere_*_fw.bin
%dir /lib/firmware/airoha
/lib/firmware/airoha/EthMD32.DSP.bin
/lib/firmware/airoha/EthMD32.dm.bin
/lib/firmware/amlogic
/lib/firmware/amphion
%dir /lib/firmware/ar3k
/lib/firmware/as102_data1_st.hex
/lib/firmware/as102_data2_st.hex
/lib/firmware/atmel
/lib/firmware/atusb
/lib/firmware/av7110
/lib/firmware/bmi260-init-data.fw
/lib/firmware/cadence
/lib/firmware/cirrus
/lib/firmware/cis
/lib/firmware/cmmb_*_12mhz.inp
/lib/firmware/cnm
/lib/firmware/cpia2
/lib/firmware/cs42l43.bin
/lib/firmware/ctefx.bin
/lib/firmware/ctspeq.bin
/lib/firmware/dabusb
/lib/firmware/dsp56k
/lib/firmware/dvb-fe-xc4000-*.fw
/lib/firmware/dvb-fe-xc5000c-*.fw
/lib/firmware/dvb-fe-xc5000-*.fw
/lib/firmware/dvb_nova_12mhz*.inp
/lib/firmware/dvb-usb-dib0700-*.fw
/lib/firmware/dvb-usb-it9135-01.fw
/lib/firmware/dvb-usb-it9135-02.fw
/lib/firmware/dvb-usb-terratec-h5-drxk.fw
/lib/firmware/edgeport
/lib/firmware/emi26
/lib/firmware/emi62
/lib/firmware/ene-ub6250
/lib/firmware/f2255usb.bin
/lib/firmware/go7007
/lib/firmware/imx
%dir /lib/firmware/inside-secure
%dir /lib/firmware/inside-secure/eip197_minifw
/lib/firmware/inside-secure/eip197_minifw/ifpp.bin
/lib/firmware/inside-secure/eip197_minifw/ipue.bin
/lib/firmware/isdbt_*.inp
/lib/firmware/ixp4xx
/lib/firmware/kaweth
/lib/firmware/keyspan
/lib/firmware/keyspan_pda
/lib/firmware/lgs8g75.fw
%dir /lib/firmware/libertas
/lib/firmware/lt9611uxc_fw.bin
/lib/firmware/matrox
/lib/firmware/meson
%dir /lib/firmware/microchip
/lib/firmware/microchip/mscc_vsc8574_revb_int8051_29e8.bin
/lib/firmware/microchip/mscc_vsc8584_revb_int8051_fb48.bin
/lib/firmware/moxa
/lib/firmware/mts_*.fw
/lib/firmware/myri10ge_*.dat
/lib/firmware/myricom
/lib/firmware/ositech
%dir /lib/firmware/powervr
/lib/firmware/powervr/rogue_33.15.11.3_v1.fw
/lib/firmware/powervr/rogue_36.53.104.796_v1.fw
/lib/firmware/r128
/lib/firmware/r8a779x_usb3_v1.dlmem
/lib/firmware/r8a779x_usb3_v2.dlmem
/lib/firmware/r8a779x_usb3_v3.dlmem
%dir /lib/firmware/rockchip
/lib/firmware/rockchip/dptx.bin
/lib/firmware/rp2.fw
/lib/firmware/rsi
/lib/firmware/rsi_91x.fw
/lib/firmware/rt2860.bin
/lib/firmware/rt2870.bin
# link to rt2870.bin
/lib/firmware/rt3070.bin
/lib/firmware/rt3071.bin
# link to rt2860.bin
/lib/firmware/rt3090.bin
/lib/firmware/rt3290.bin
# links to go7007/s2250*
/lib/firmware/s2250*.fw
/lib/firmware/s5p-mfc.fw
/lib/firmware/s5p-mfc-v12.fw
/lib/firmware/s5p-mfc-v6.fw
/lib/firmware/s5p-mfc-v6-v2.fw
/lib/firmware/s5p-mfc-v7.fw
/lib/firmware/s5p-mfc-v8.fw
/lib/firmware/sdd_sagrad_*.bin
/lib/firmware/slicoss
/lib/firmware/sms1xxx-*.fw
/lib/firmware/sun
/lib/firmware/sxg
/lib/firmware/tdmb_nova_12mhz.inp
/lib/firmware/tehuti
/lib/firmware/tlg2300_firmware.bin
/lib/firmware/tsse_firmware.bin
/lib/firmware/ttusb-budget
/lib/firmware/ueagle-atm
/lib/firmware/usbdux*_firmware.bin
/lib/firmware/v4l-cx*.fw
/lib/firmware/vicam
/lib/firmware/vntwusb.fw
/lib/firmware/vxge
/lib/firmware/wfx
/lib/firmware/whiteheat*.fw
/lib/firmware/wsm_22.bin
/lib/firmware/yam

%files amd
%defattr(644,root,root,755)
%doc WHENCE LICENSE.amdgpu LICENSE.amd-sev LICENSE.amd-ucode LICENSE.radeon
/lib/firmware/amd
/lib/firmware/amdgpu
/lib/firmware/amdnpu
/lib/firmware/amdtee
/lib/firmware/amd-ucode
/lib/firmware/radeon

%files arm
%defattr(644,root,root,755)
%doc WHENCE LICENCE.mali_csffw
/lib/firmware/arm

%files atheros
%defattr(644,root,root,755)
%doc WHENCE LICENCE.atheros_firmware
/lib/firmware/ar3k/1020200
/lib/firmware/ar3k/1020201
/lib/firmware/ar3k/30000
/lib/firmware/ar3k/30101
/lib/firmware/ar3k/30101coex
/lib/firmware/ar3k/AthrBT_0x01020001.dfu
/lib/firmware/ar3k/AthrBT_0x01020200.dfu
/lib/firmware/ar3k/AthrBT_0x11020000.dfu
/lib/firmware/ar3k/AthrBT_0x11020100.dfu
/lib/firmware/ar3k/AthrBT_0x31010000.dfu
/lib/firmware/ar3k/AthrBT_0x31010100.dfu
/lib/firmware/ar3k/AthrBT_0x41020000.dfu
/lib/firmware/ar3k/ramps_0x01020001_26.dfu
/lib/firmware/ar3k/ramps_0x01020200_26.dfu
/lib/firmware/ar3k/ramps_0x01020200_40.dfu
/lib/firmware/ar3k/ramps_0x01020201_26.dfu
/lib/firmware/ar3k/ramps_0x01020201_40.dfu
/lib/firmware/ar3k/ramps_0x11020000_40.dfu
/lib/firmware/ar3k/ramps_0x11020100_40.dfu
/lib/firmware/ar3k/ramps_0x31010000_40.dfu
/lib/firmware/ar3k/ramps_0x31010100_40.dfu
/lib/firmware/ar3k/ramps_0x41020000_40.dfu
/lib/firmware/ar5523.bin
/lib/firmware/ar7010*.fw
/lib/firmware/ar9170-*.fw
/lib/firmware/ar9271.fw
/lib/firmware/ath3k-1.fw
/lib/firmware/ath6k
/lib/firmware/carl9170-1.fw
/lib/firmware/htc_7010.fw
/lib/firmware/htc_9271.fw

%files broadcom
%defattr(644,root,root,755)
%doc WHENCE LICENCE.broadcom_bcm43xx
/lib/firmware/bnx2
/lib/firmware/bnx2x
/lib/firmware/brcm
/lib/firmware/cypress
/lib/firmware/tigon

%files cavium
%defattr(644,root,root,755)
%doc WHENCE LICENCE.cavium LICENCE.cavium_liquidio
/lib/firmware/cavium
/lib/firmware/liquidio

%files chelsio
%defattr(644,root,root,755)
%doc WHENCE LICENCE.chelsio_firmware
/lib/firmware/cxgb3
/lib/firmware/cxgb4

%files intel
%defattr(644,root,root,755)
%doc WHENCE LICENCE.e100 LICENSE.ipu3_firmware LICENCE.ibt_firmware LICENCE.qat_firmware LICENCE.fw_sst_0f28 LICENCE.IntcSST2 LICENCE.adsp_sst LICENSE.i915 LICENSE.hfi1_firmware LICENSE.ice LICENSE.ice_enhanced LICENSE.xe
/lib/firmware/e100
/lib/firmware/hfi1_dc8051.fw
/lib/firmware/hfi1_fabric.fw
/lib/firmware/hfi1_pcie.fw
/lib/firmware/hfi1_sbus.fw
/lib/firmware/i915
/lib/firmware/intel
/lib/firmware/isci
/lib/firmware/qat_402xx.bin
/lib/firmware/qat_402xx_mmp.bin
/lib/firmware/qat_420xx.bin
/lib/firmware/qat_420xx_mmp.bin
/lib/firmware/qat_4xxx.bin
/lib/firmware/qat_4xxx_mmp.bin
/lib/firmware/qat_895xcc.bin
/lib/firmware/qat_895xcc_mmp.bin
/lib/firmware/qat_c3xxx.bin
/lib/firmware/qat_c3xxx_mmp.bin
/lib/firmware/qat_c62x.bin
/lib/firmware/qat_c62x_mmp.bin
# link to qat_895xcc_mmp.bin
/lib/firmware/qat_mmp.bin
/lib/firmware/xe

%files marvell
%defattr(644,root,root,755)
%doc WHENCE LICENCE.Marvell LICENCE.OLPC
/lib/firmware/lbtf_usb.bin
/lib/firmware/mwl8k
/lib/firmware/mwlwifi
# XXX: shared with libertas
%dir /lib/firmware/mrvl
/lib/firmware/mrvl/pcie8897_uapsta.bin
/lib/firmware/mrvl/pcie8997_wlan_v4.bin
/lib/firmware/mrvl/pcieuart8997_combo_v4.bin
/lib/firmware/mrvl/pcieusb8997_combo_v4.bin
/lib/firmware/mrvl/sd8688*.bin
/lib/firmware/mrvl/sd8797_uapsta.bin
/lib/firmware/mrvl/sd8801_uapsta.bin
/lib/firmware/mrvl/sd8887_uapsta.bin
/lib/firmware/mrvl/sd8897_uapsta.bin
/lib/firmware/mrvl/sdsd8977_combo_v2.bin
/lib/firmware/mrvl/sdsd8997_combo_v4.bin
/lib/firmware/mrvl/usb8766_uapsta.bin
/lib/firmware/mrvl/usb8797_uapsta.bin
/lib/firmware/mrvl/usb8801_uapsta.bin
/lib/firmware/mrvl/usb8897_uapsta.bin
/lib/firmware/mrvl/usbusb8997_combo_v4.bin
/lib/firmware/mrvl/cpt01
/lib/firmware/mrvl/cpt02
/lib/firmware/mrvl/cpt03
/lib/firmware/mrvl/cpt04
%dir /lib/firmware/mrvl/prestera
/lib/firmware/mrvl/prestera/mvsw_prestera_fw-v2.0.img
/lib/firmware/mrvl/prestera/mvsw_prestera_fw-v3.0.img
/lib/firmware/mrvl/prestera/mvsw_prestera_fw-v4.0.img
/lib/firmware/mrvl/prestera/mvsw_prestera_fw-v4.1.img
/lib/firmware/mrvl/prestera/mvsw_prestera_fw_arm64-v4.1.img
/lib/firmware/libertas/cf8381*.bin
/lib/firmware/libertas/cf8385*.bin
/lib/firmware/libertas/gspi8682*.bin
/lib/firmware/libertas/gspi8686_v9*.bin
/lib/firmware/libertas/gspi8688*.bin
/lib/firmware/libertas/lbtf_sdio.bin
/lib/firmware/libertas/sd8385*.bin
/lib/firmware/libertas/sd8682*.bin
# links to mrvl/sd8688*
/lib/firmware/libertas/sd8688*.bin
/lib/firmware/libertas/usb8682.bin

%files mediatek
%defattr(644,root,root,755)
%doc WHENCE LICENCE.ralink_a_mediatek_company_firmware LICENCE.mediatek
%dir /lib/firmware/mediatek
/lib/firmware/mediatek/BT_RAM_CODE_MT7922_1_1_hdr.bin
/lib/firmware/mediatek/BT_RAM_CODE_MT7961_1_2_hdr.bin
/lib/firmware/mediatek/BT_RAM_CODE_MT7961_1a_2_hdr.bin
/lib/firmware/mediatek/WIFI_MT7922_patch_mcu_1_1_hdr.bin
/lib/firmware/mediatek/WIFI_MT7961_patch_mcu_1_2_hdr.bin
/lib/firmware/mediatek/WIFI_MT7961_patch_mcu_1a_2_hdr.bin
/lib/firmware/mediatek/WIFI_RAM_CODE_MT7922_1.bin
/lib/firmware/mediatek/WIFI_RAM_CODE_MT7961_1.bin
/lib/firmware/mediatek/WIFI_RAM_CODE_MT7961_1a.bin
/lib/firmware/mediatek/mt7601u.bin
/lib/firmware/mediatek/mt7610e.bin
/lib/firmware/mediatek/mt7610u.bin
/lib/firmware/mediatek/mt7615_cr4.bin
/lib/firmware/mediatek/mt7615_n9.bin
/lib/firmware/mediatek/mt7615_rom_patch.bin
/lib/firmware/mediatek/mt7622_n9.bin
/lib/firmware/mediatek/mt7622_rom_patch.bin
/lib/firmware/mediatek/mt7622pr2h.bin
/lib/firmware/mediatek/mt7650.bin
/lib/firmware/mediatek/mt7650e.bin
/lib/firmware/mediatek/mt7662.bin
/lib/firmware/mediatek/mt7662_rom_patch.bin
/lib/firmware/mediatek/mt7662u.bin
/lib/firmware/mediatek/mt7662u_rom_patch.bin
/lib/firmware/mediatek/mt7663_n9_rebb.bin
/lib/firmware/mediatek/mt7663_n9_v3.bin
/lib/firmware/mediatek/mt7663pr2h.bin
/lib/firmware/mediatek/mt7663pr2h_rebb.bin
/lib/firmware/mediatek/mt7668pr2h.bin
/lib/firmware/mediatek/mt7915_eeprom.bin
/lib/firmware/mediatek/mt7915_eeprom_dbdc.bin
/lib/firmware/mediatek/mt7915_rom_patch.bin
/lib/firmware/mediatek/mt7915_wa.bin
/lib/firmware/mediatek/mt7915_wm.bin
/lib/firmware/mediatek/mt7916_eeprom.bin
/lib/firmware/mediatek/mt7916_rom_patch.bin
/lib/firmware/mediatek/mt7916_wa.bin
/lib/firmware/mediatek/mt7916_wm.bin
%dir /lib/firmware/mediatek/mt7925
/lib/firmware/mediatek/mt7925/BT_RAM_CODE_MT7925_1_1_hdr.bin
/lib/firmware/mediatek/mt7925/WIFI_MT7925_PATCH_MCU_1_1_hdr.bin
/lib/firmware/mediatek/mt7925/WIFI_RAM_CODE_MT7925_1_1.bin
/lib/firmware/mediatek/mt7981_rom_patch.bin
/lib/firmware/mediatek/mt7981_wa.bin
/lib/firmware/mediatek/mt7981_wm.bin
/lib/firmware/mediatek/mt7981_wo.bin
/lib/firmware/mediatek/mt7986_eeprom_mt7975_dual.bin
/lib/firmware/mediatek/mt7986_eeprom_mt7976.bin
/lib/firmware/mediatek/mt7986_eeprom_mt7976_dbdc.bin
/lib/firmware/mediatek/mt7986_eeprom_mt7976_dual.bin
/lib/firmware/mediatek/mt7986_rom_patch.bin
/lib/firmware/mediatek/mt7986_rom_patch_mt7975.bin
/lib/firmware/mediatek/mt7986_wa.bin
/lib/firmware/mediatek/mt7986_wm.bin
/lib/firmware/mediatek/mt7986_wm_mt7975.bin
/lib/firmware/mediatek/mt7986_wo_*.bin
/lib/firmware/mediatek/mt7988
/lib/firmware/mediatek/mt7988_wo_0.bin
/lib/firmware/mediatek/mt7988_wo_1.bin
/lib/firmware/mediatek/mt7996
/lib/firmware/mediatek/mt8173
/lib/firmware/mediatek/mt8183
/lib/firmware/mediatek/mt8186
/lib/firmware/mediatek/mt8188
/lib/firmware/mediatek/mt8192
/lib/firmware/mediatek/mt8195
/lib/firmware/mediatek/mt8196
/lib/firmware/mediatek/sof
/lib/firmware/mediatek/sof-tplg
/lib/firmware/mt7601u.bin
/lib/firmware/mt7650.bin
/lib/firmware/mt7662*.bin
/lib/firmware/vpu_d.bin
/lib/firmware/vpu_p.bin

%files mellanox
%defattr(644,root,root,755)
%doc WHENCE
/lib/firmware/mellanox

%files netronome
%defattr(644,root,root,755)
%doc WHENCE LICENCE.Netronome
/lib/firmware/netronome

%files nvidia
%defattr(644,root,root,755)
%doc WHENCE LICENCE.nvidia
/lib/firmware/nvidia

%files nxp
%defattr(644,root,root,755)
%doc WHENCE LICENSE.nxp_mc_firmware
/lib/firmware/dpaa2
/lib/firmware/nxp

%files qlogic
%defattr(644,root,root,755)
%doc WHENCE LICENCE.qla1280
/lib/firmware/cbfw-*.bin
/lib/firmware/ct2fw-*.bin
/lib/firmware/ctfw-*.bin
%dir /lib/firmware/qed
/lib/firmware/qed/qed_init_values-8.10.9.0.bin
/lib/firmware/qed/qed_init_values-8.14.6.0.bin
/lib/firmware/qed/qed_init_values-8.18.9.0.bin
/lib/firmware/qed/qed_init_values-8.20.0.0.bin
/lib/firmware/qed/qed_init_values-8.30.12.0.bin
/lib/firmware/qed/qed_init_values-8.33.12.0.bin
/lib/firmware/qed/qed_init_values-8.37.7.0.bin
/lib/firmware/qed/qed_init_values-8.40.33.0.bin
/lib/firmware/qed/qed_init_values_zipped-8.10.10.0.bin
/lib/firmware/qed/qed_init_values_zipped-8.10.5.0.bin
/lib/firmware/qed/qed_init_values_zipped-8.15.3.0.bin
/lib/firmware/qed/qed_init_values_zipped-8.20.0.0.bin
/lib/firmware/qed/qed_init_values_zipped-8.33.1.0.bin
/lib/firmware/qed/qed_init_values_zipped-8.33.11.0.bin
/lib/firmware/qed/qed_init_values_zipped-8.37.2.0.bin
/lib/firmware/qed/qed_init_values_zipped-8.37.7.0.bin
/lib/firmware/qed/qed_init_values_zipped-8.4.2.0.bin
/lib/firmware/qed/qed_init_values_zipped-8.7.3.0.bin
/lib/firmware/qed/qed_init_values_zipped-8.42.2.0.bin
/lib/firmware/qed/qed_init_values_zipped-8.59.1.0.bin
/lib/firmware/qlogic

%files qualcomm
%defattr(644,root,root,755)
%doc WHENCE LICENSE.QualcommAtheros_ar3k LICENSE.QualcommAtheros_ath10k LICENCE.open-ath9k-htc-firmware LICENSE.qcom
# links to qcom/a300_*.fw
/lib/firmware/a300_pfp.fw
/lib/firmware/a300_pm4.fw
/lib/firmware/ar3k/1020201coex
/lib/firmware/ar3k/AthrBT_0x01020201.dfu
/lib/firmware/ath10k
/lib/firmware/ath11k
/lib/firmware/ath12k
/lib/firmware/ath9k_htc
/lib/firmware/qca
/lib/firmware/qcom
/lib/firmware/wil6210.brd
/lib/firmware/wil6210.fw

%files realtek
%defattr(644,root,root,755)
%doc WHENCE README.rtw88 LICENCE.rtlwifi_firmware.txt
%dir /lib/firmware/realtek
%dir /lib/firmware/realtek/rt1320
/lib/firmware/realtek/rt1320/rt1320-patch-code-vab.bin
/lib/firmware/realtek/rt1320/rt1320-patch-code-vc.bin
/lib/firmware/rtl_bt
/lib/firmware/rtl_nic
/lib/firmware/rtlwifi
%dir /lib/firmware/rtw88
/lib/firmware/rtw88/rtw8703b_fw.bin
/lib/firmware/rtw88/rtw8703b_wow_fw.bin
/lib/firmware/rtw88/rtw8723d_fw.bin
/lib/firmware/rtw88/rtw8812a_fw.bin
/lib/firmware/rtw88/rtw8814a_fw.bin
/lib/firmware/rtw88/rtw8821a_fw.bin
/lib/firmware/rtw88/rtw8821c_fw.bin
/lib/firmware/rtw88/rtw8822b_fw.bin
/lib/firmware/rtw88/rtw8822c_fw.bin
/lib/firmware/rtw88/rtw8822c_wow_fw.bin
%dir /lib/firmware/rtw89
/lib/firmware/rtw89/rtw8851b_fw.bin
/lib/firmware/rtw89/rtw8852a_fw.bin
/lib/firmware/rtw89/rtw8852b_fw.bin
/lib/firmware/rtw89/rtw8852b_fw-1.bin
/lib/firmware/rtw89/rtw8852bt_fw.bin
/lib/firmware/rtw89/rtw8852c_fw.bin
/lib/firmware/rtw89/rtw8852c_fw-1.bin
/lib/firmware/rtw89/rtw8852c_fw-2.bin
/lib/firmware/rtw89/rtw8922a_fw.bin
/lib/firmware/rtw89/rtw8922a_fw-1.bin
/lib/firmware/rtw89/rtw8922a_fw-2.bin
/lib/firmware/rtw89/rtw8922a_fw-3.bin

%files ti
%defattr(644,root,root,755)
%doc WHENCE LICENCE.ti-tspa LICENCE.wl1251 LICENCE.ti-connectivity LICENCE.ti-keystone
/lib/firmware/INT8866RCA2.bin
/lib/firmware/TAS2XXX*.bin
/lib/firmware/TIAS2781RCA2.bin
/lib/firmware/TIAS2781RCA4.bin
/lib/firmware/TXNW2781*.bin
/lib/firmware/ti
/lib/firmware/ti_3410.fw
/lib/firmware/ti_5052.fw
/lib/firmware/ti-connectivity
/lib/firmware/ti-keystone

%files -n iwl100-firmware
%defattr(644,root,root,755)
%doc WHENCE LICENCE.iwlwifi_firmware
/lib/firmware/iwlwifi-100-5.ucode

%files -n iwl105-firmware
%defattr(644,root,root,755)
%doc WHENCE LICENCE.iwlwifi_firmware
/lib/firmware/iwlwifi-105-*.ucode

%files -n iwl135-firmware
%defattr(644,root,root,755)
%doc WHENCE LICENCE.iwlwifi_firmware
/lib/firmware/iwlwifi-135-*.ucode

%files -n iwl1000-firmware
%defattr(644,root,root,755)
%doc WHENCE LICENCE.iwlwifi_firmware
/lib/firmware/iwlwifi-1000-*.ucode

%files -n iwl2000-firmware
%defattr(644,root,root,755)
%doc WHENCE LICENCE.iwlwifi_firmware
/lib/firmware/iwlwifi-2000-*.ucode

%files -n iwl2030-firmware
%defattr(644,root,root,755)
%doc WHENCE LICENCE.iwlwifi_firmware
/lib/firmware/iwlwifi-2030-*.ucode

%files -n iwl3160-firmware
%defattr(644,root,root,755)
%doc WHENCE LICENCE.iwlwifi_firmware
/lib/firmware/iwlwifi-3160-*.ucode
/lib/firmware/iwlwifi-3168-*.ucode

%files -n iwl3945-firmware
%defattr(644,root,root,755)
%doc WHENCE LICENCE.iwlwifi_firmware
/lib/firmware/iwlwifi-3945-*.ucode

%files -n iwl4965-firmware
%defattr(644,root,root,755)
%doc WHENCE LICENCE.iwlwifi_firmware
/lib/firmware/iwlwifi-4965-*.ucode

%files -n iwl5000-firmware
%defattr(644,root,root,755)
%doc WHENCE LICENCE.iwlwifi_firmware
/lib/firmware/iwlwifi-5000-*.ucode

%files -n iwl5150-firmware
%defattr(644,root,root,755)
%doc WHENCE LICENCE.iwlwifi_firmware
/lib/firmware/iwlwifi-5150-*.ucode

%files -n iwl6000-firmware
%defattr(644,root,root,755)
%doc WHENCE LICENCE.iwlwifi_firmware
/lib/firmware/iwlwifi-6000-*.ucode

%files -n iwl6000g2a-firmware
%defattr(644,root,root,755)
%doc WHENCE LICENCE.iwlwifi_firmware
/lib/firmware/iwlwifi-6000g2a-*.ucode

%files -n iwl6000g2b-firmware
%defattr(644,root,root,755)
%doc WHENCE LICENCE.iwlwifi_firmware
/lib/firmware/iwlwifi-6000g2b-*.ucode

%files -n iwl6050-firmware
%defattr(644,root,root,755)
%doc WHENCE LICENCE.iwlwifi_firmware
/lib/firmware/iwlwifi-6050-*.ucode

%files -n iwl7260-firmware
%defattr(644,root,root,755)
%doc WHENCE LICENCE.iwlwifi_firmware
/lib/firmware/iwlwifi-7260-*.ucode
/lib/firmware/iwlwifi-7265-*.ucode
/lib/firmware/iwlwifi-7265D-*.ucode
# iwlwifi-8000 subpackage?
/lib/firmware/iwlwifi-8000C-*.ucode
/lib/firmware/iwlwifi-8265-*.ucode
# iwlwifi-9000 subpackage?
/lib/firmware/iwlwifi-9000-pu-b0-jf-b0-*.ucode
/lib/firmware/iwlwifi-9260-th-b0-jf-b0-*.ucode
# iwlwifi-22000 subpackage?
/lib/firmware/iwlwifi-Qu-*.ucode
/lib/firmware/iwlwifi-QuZ-*.ucode
/lib/firmware/iwlwifi-cc-a0-*.ucode
# iwlwifi-ax210 subpackage?
/lib/firmware/iwlwifi-ma-b0-*.ucode
/lib/firmware/iwlwifi-ma-b0-*.pnvm
/lib/firmware/iwlwifi-so-a0-*.ucode
/lib/firmware/iwlwifi-so-a0-*.pnvm
/lib/firmware/iwlwifi-ty-a0-gf-a0-*.ucode
/lib/firmware/iwlwifi-ty-a0-gf-a0.pnvm
# iwlwifi-bz subpackage?
/lib/firmware/iwlwifi-bz-b0-fm-c0-92.ucode
/lib/firmware/iwlwifi-bz-b0-fm-c0-93.ucode
/lib/firmware/iwlwifi-bz-b0-fm-c0-94.ucode
/lib/firmware/iwlwifi-bz-b0-fm-c0-96.ucode
/lib/firmware/iwlwifi-bz-b0-fm-c0-97.ucode
/lib/firmware/iwlwifi-bz-b0-fm-c0-98.ucode
/lib/firmware/iwlwifi-bz-b0-fm-c0.pnvm
/lib/firmware/iwlwifi-bz-b0-gf-a0-92.ucode
/lib/firmware/iwlwifi-bz-b0-gf-a0-94.ucode
/lib/firmware/iwlwifi-bz-b0-gf-a0-96.ucode
/lib/firmware/iwlwifi-bz-b0-gf-a0-97.ucode
/lib/firmware/iwlwifi-bz-b0-gf-a0-98.ucode
/lib/firmware/iwlwifi-bz-b0-gf-a0.pnvm
/lib/firmware/iwlwifi-bz-b0-hr-b0-96.ucode
/lib/firmware/iwlwifi-bz-b0-hr-b0-98.ucode
/lib/firmware/iwlwifi-bz-b0-hr-b0.pnvm
/lib/firmware/iwlwifi-gl-c0-fm-c0-*.ucode
/lib/firmware/iwlwifi-gl-c0-fm-c0.pnvm

%files -n libertas-sd8686-firmware
%defattr(644,root,root,755)
%doc WHENCE LICENCE.Marvell
%dir /lib/firmware/libertas
/lib/firmware/libertas/sd8686_v9*.bin

%files -n libertas-sd8787-firmware
%defattr(644,root,root,755)
%doc WHENCE LICENCE.Marvell
# XXX: shared with marvell
%dir /lib/firmware/mrvl
/lib/firmware/mrvl/sd8787_uapsta.bin

%files -n libertas-usb8388-firmware
%defattr(644,root,root,755)
%doc WHENCE LICENCE.Marvell
%dir /lib/firmware/libertas
/lib/firmware/libertas/usb8388_v9.bin

%files -n libertas-usb8388-olpc-firmware
%defattr(644,root,root,755)
%doc WHENCE LICENCE.Marvell
%dir /lib/firmware/libertas
/lib/firmware/libertas/usb8388_olpc.bin
