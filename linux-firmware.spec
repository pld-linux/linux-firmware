# TODO
# - subpackages for various firmwares?
%define		rel	1
%define		ver	20161205
Summary:	Firmware files used by the Linux kernel
Summary(pl.UTF-8):	Pliki firmware'u używane przez jądro Linuksa
Name:		linux-firmware
Version:	%{ver}
Release:	%{rel}
License:	GPL+ and GPL v2+ and MIT and Redistributable, no modification permitted
Group:		Base/Kernel
Source0:	http://pkgs.fedoraproject.org/repo/pkgs/linux-firmware/%{name}-%{version}.tar.gz/b0bf236f2ad6879a45b44852c3c30f81/linux-firmware-%{version}.tar.gz
# Source0-md5:	b0bf236f2ad6879a45b44852c3c30f81
URL:		https://git.kernel.org/cgit/linux/kernel/git/firmware/linux-firmware.git/
Obsoletes:	microcode-data-amd
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package includes firmware files required for some devices to
operate.

%description -l pl.UTF-8
Ten pakiet zawiera pliki firmware'u wymagane do działania niektórych
urządzeń.

%package -n iwl100-firmware
Summary:	Firmware for Intel(R) Wireless WiFi Link 100 Series Adapters
Version:	39.31.5.1
Release:	%{ver}.%{rel}
License:	Redistributable, no modification permitted
Obsoletes:	iwl100-firmware < 39.31.5.1-4

%description -n iwl100-firmware
This package contains the firmware required by the Intel wireless
drivers for Linux to support the iwl100 hardware. Usage of the
firmware is subject to the terms and conditions contained inside the
provided LICENSE file. Please read it carefully.

%package -n iwl105-firmware
Summary:	Firmware for Intel(R) Centrino Wireless-N 105 Series Adapters
Version:	18.168.6.1
Release:	%{ver}.%{rel}
License:	Redistributable, no modification permitted

%description -n iwl105-firmware
This package contains the firmware required by the Intel wireless
drivers for Linux to support the iwl105 hardware. Usage of the
firmware is subject to the terms and conditions contained inside the
provided LICENSE file. Please read it carefully.

%package -n iwl135-firmware
Summary:	Firmware for Intel(R) Centrino Wireless-N 135 Series Adapters
Version:	18.168.6.1
Release:	%{ver}.%{rel}
License:	Redistributable, no modification permitted

%description -n iwl135-firmware
This package contains the firmware required by the Intel wireless
drivers for Linux to support the iwl135 hardware. Usage of the
firmware is subject to the terms and conditions contained inside the
provided LICENSE file. Please read it carefully.

%package -n iwl1000-firmware
Summary:	Firmware for Intel(R) PRO/Wireless 1000 B/G/N network adaptors
Version:	39.31.5.1
Release:	%{ver}.%{rel}
License:	Redistributable, no modification permitted
Obsoletes:	iwl1000-firmware < 1:39.31.5.1-3

%description -n iwl1000-firmware
This package contains the firmware required by the Intel wireless
drivers for Linux to support the iwl1000 hardware. Usage of the
firmware is subject to the terms and conditions contained inside the
provided LICENSE file. Please read it carefully.

%package -n iwl2000-firmware
Summary:	Firmware for Intel(R) Centrino Wireless-N 2000 Series Adapters
Version:	18.168.6.1
Release:	%{ver}.%{rel}
License:	Redistributable, no modification permitted

%description -n iwl2000-firmware
This package contains the firmware required by the Intel wireless
drivers for Linux to support the iwl2000 hardware. Usage of the
firmware is subject to the terms and conditions contained inside the
provided LICENSE file. Please read it carefully.

%package -n iwl2030-firmware
Summary:	Firmware for Intel(R) Centrino Wireless-N 2030 Series Adapters
Version:	18.168.6.1
Release:	%{ver}.%{rel}
License:	Redistributable, no modification permitted

%description -n iwl2030-firmware
This package contains the firmware required by the Intel wireless
drivers for Linux to support the iwl2030 hardware. Usage of the
firmware is subject to the terms and conditions contained inside the
provided LICENSE file. Please read it carefully.

%package -n iwl3945-firmware
Summary:	Firmware for Intel(R) PRO/Wireless 3945 A/B/G network adaptors
Version:	15.32.2.9
Release:	%{ver}.%{rel}
License:	Redistributable, no modification permitted
Obsoletes:	iwl3945-firmware < 15.32.2.9-7

%description -n iwl3945-firmware
This package contains the firmware required by the iwl3945 driver for
Linux. Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%package -n iwl4965-firmware
Summary:	Firmware for Intel(R) PRO/Wireless 4965 A/G/N network adaptors
Version:	228.61.2.24
Release:	%{ver}.%{rel}
License:	Redistributable, no modification permitted
Obsoletes:	iwl4965-firmware < 228.61.2.24-5

%description -n iwl4965-firmware
This package contains the firmware required by the iwl4965 driver for
Linux. Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%package -n iwl5000-firmware
Summary:	Firmware for Intel(R) PRO/Wireless 5000 A/G/N network adaptors
Version:	8.83.5.1_1
Release:	%{ver}.%{rel}
License:	Redistributable, no modification permitted
Obsoletes:	iwl5000-firmware < 8.83.5.1_1-3

%description -n iwl5000-firmware
This package contains the firmware required by the iwl5000 driver for
Linux. Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%package -n iwl5150-firmware
Summary:	Firmware for Intel(R) PRO/Wireless 5150 A/G/N network adaptors
Version:	8.24.2.2
Release:	%{ver}.%{rel}
License:	Redistributable, no modification permitted
Obsoletes:	iwl5150-firmware < 8.24.2.2-4

%description -n iwl5150-firmware
This package contains the firmware required by the iwl5150 driver for
Linux. Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%package -n iwl6000-firmware
Summary:	Firmware for Intel(R) Wireless WiFi Link 6000 AGN Adapter
Version:	9.221.4.1
Release:	%{ver}.%{rel}
License:	Redistributable, no modification permitted
Obsoletes:	iwl6000-firmware < 9.221.4.1-4

%description -n iwl6000-firmware
This package contains the firmware required by the Intel wireless
drivers for Linux. Usage of the firmware is subject to the terms and
conditions contained inside the provided LICENSE file. Please read it
carefully.

%package -n iwl6000g2a-firmware
Summary:	Firmware for Intel(R) Wireless WiFi Link 6005 Series Adapters
Version:	18.168.6.1
Release:	%{ver}.%{rel}
License:	Redistributable, no modification permitted
Obsoletes:	iwl6000g2a-firmware < 17.168.5.3-3

%description -n iwl6000g2a-firmware
This package contains the firmware required by the Intel wireless
drivers for Linux. Usage of the firmware is subject to the terms and
conditions contained inside the provided LICENSE file. Please read it
carefully.

%package -n iwl6000g2b-firmware
Summary:	Firmware for Intel(R) Wireless WiFi Link 6030 Series Adapters
Version:	18.168.6.1
Release:	%{ver}.%{rel}
License:	Redistributable, no modification permitted
Obsoletes:	iwl6000g2b-firmware < 17.168.5.2-3

%description -n iwl6000g2b-firmware
This package contains the firmware required by the Intel wireless
drivers for Linux. Usage of the firmware is subject to the terms and
conditions contained inside the provided LICENSE file. Please read it
carefully.

%package -n iwl6050-firmware
Summary:	Firmware for Intel(R) Wireless WiFi Link 6050 Series Adapters
Version:	41.28.5.1
Release:	%{ver}.%{rel}
License:	Redistributable, no modification permitted
Obsoletes:	iwl6050-firmware < 41.28.5.1-5

%description -n iwl6050-firmware
This package contains the firmware required by the Intel wireless
drivers for Linux. Usage of the firmware is subject to the terms and
conditions contained inside the provided LICENSE file. Please read it
carefully.

%package -n iwl7260-firmware
Summary:	Firmware for Intel(R) Wireless WiFi Link 7260 Series Adapters
Version:	25.30.13.0
Release:	%{ver}.%{rel}
License:	Redistributable, no modification permitted
Obsoletes:	iwlwifi-7260-ucode

%description -n iwl7260-firmware
This package contains the firmware required by the Intel wireless
drivers for Linux. Usage of the firmware is subject to the terms and
conditions contained inside the provided LICENSE file. Please read it
carefully.

%package -n iwl3160-firmware
Summary:	Firmware for Intel(R) Wireless WiFi Link 3160 Series Adapters
Version:	25.30.13.0
Release:	%{ver}.%{rel}
License:	Redistributable, no modification permitted

%description -n iwl3160-firmware
This package contains the firmware required by the Intel wireless
drivers for Linux. Usage of the firmware is subject to the terms and
conditions contained inside the provided LICENSE file. Please read it
carefully.

%package -n libertas-usb8388-firmware
Summary:	Firmware for Marvell Libertas USB 8388 Network Adapter
Version:	0.%{ver}
Release:	%{rel}
License:	Redistributable, no modification permitted
Obsoletes:	libertas-usb8388-firmware < 2:5.110.22.p23-8

%description -n libertas-usb8388-firmware
Firmware for Marvell Libertas USB 8388 Network Adapter

%package -n libertas-usb8388-olpc-firmware
Summary:	OLPC firmware for Marvell Libertas USB 8388 Network Adapter
Version:	0.%{ver}
Release:	%{rel}
License:	Redistributable, no modification permitted

%description -n libertas-usb8388-olpc-firmware
Firmware for Marvell Libertas USB 8388 Network Adapter with OLPC mesh
network support.

%package -n libertas-sd8686-firmware
Summary:	Firmware for Marvell Libertas SD 8686 Network Adapter
Version:	0.%{ver}
Release:	%{rel}
License:	Redistributable, no modification permitted
Obsoletes:	libertas-sd8686-firmware < 9.70.20.p0-4

%description -n libertas-sd8686-firmware
Firmware for Marvell Libertas SD 8686 Network Adapter

%package -n libertas-sd8787-firmware
Summary:	Firmware for Marvell Libertas SD 8787 Network Adapter
Version:	0.%{ver}
Release:	%{rel}
License:	Redistributable, no modification permitted

%description -n libertas-sd8787-firmware
Firmware for Marvell Libertas SD 8787 Network Adapter

%prep
%setup -qc
mv linux-firmware-*/* .
rmdir linux-firmware-*

# Remove firmware shipped in separate packages already
# Perhaps these should be built as subpackages of linux-firmware?
# - ql{2100,2200,2300,2322,2400,2500}-firmware.spec
%{__rm} ql{2100,2200,2300,2322,2400,2500}_fw.bin LICENCE.qla2xxx
# - iwlwifi-{1000,3945,4965,5000,5150,6000,6030}-ucode.spec
%{__rm} iwlwifi-{1000-5,3945-[12],4965-[12],5000-[125],5150-2,6000-4,6000g2b-6}.ucode

# (note: LICENCE.iwlwifi_firmware left for remaining iwlwifi files)
# - obsolete versions of iwlwifi firmwares
%{__rm} iwlwifi-{1000-3,6000g2a-5,6000g2b-5,6050-4}.ucode
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

# Remove source files we don't need to install
%{__rm} */*.asm dsp56k/{Makefile,concat-bootstrap.pl} isci/{Makefile,README,*.[ch]}
%{__rm} -r carl9170fw usbdux
%{__rm} Makefile configure

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/firmware
cp -a . $RPM_BUILD_ROOT/lib/firmware
%{__rm} $RPM_BUILD_ROOT/lib/firmware/{GPL-3,LICENCE.*,LICENSE.*,README,TDA7706_OM_v*_boot.txt,WHENCE}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc WHENCE LICENCE.* LICENSE.* README TDA7706_OM_v*_boot.txt
/lib/firmware/3com
/lib/firmware/acenic
/lib/firmware/adaptec
/lib/firmware/advansys
/lib/firmware/agere_*_fw.bin
/lib/firmware/amdgpu
/lib/firmware/amd-ucode
/lib/firmware/ar3k
/lib/firmware/ar5523.bin
/lib/firmware/ar7010*.fw
/lib/firmware/ar9170-*.fw
/lib/firmware/ar9271.fw
/lib/firmware/as102_data1_st.hex
/lib/firmware/as102_data2_st.hex
/lib/firmware/ath10k
/lib/firmware/ath3k-1.fw
/lib/firmware/ath6k
/lib/firmware/ath9k_htc
/lib/firmware/atmel
/lib/firmware/atmsar11.fw
/lib/firmware/atusb
/lib/firmware/av7110
/lib/firmware/bnx2
/lib/firmware/bnx2x
/lib/firmware/bnx2x-e1-*.fw
/lib/firmware/bnx2x-e1h-*.fw
/lib/firmware/brcm
/lib/firmware/carl9170-1.fw
/lib/firmware/cbfw-*.bin
/lib/firmware/cis
/lib/firmware/cmmb_*_12mhz.inp
/lib/firmware/cpia2
/lib/firmware/ct2fw-*.bin
/lib/firmware/ctefx.bin
/lib/firmware/ctfw-*.bin
/lib/firmware/ctspeq.bin
/lib/firmware/cxgb3
/lib/firmware/cxgb4
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
/lib/firmware/e100
/lib/firmware/edgeport
/lib/firmware/emi26
/lib/firmware/emi62
/lib/firmware/ene-ub6250
/lib/firmware/f2255usb.bin
/lib/firmware/go7007
/lib/firmware/hfi1_dc8051.fw
/lib/firmware/hfi1_fabric.fw
/lib/firmware/hfi1_pcie.fw
/lib/firmware/hfi1_platform.dat
/lib/firmware/hfi1_sbus.fw
/lib/firmware/htc_7010.fw
/lib/firmware/htc_9271.fw
/lib/firmware/i2400m-fw-usb-*.sbcf
/lib/firmware/i6050-fw-usb-*.sbcf
/lib/firmware/i915
/lib/firmware/intel
/lib/firmware/intelliport2.bin
/lib/firmware/isci
/lib/firmware/isdbt_*.inp
/lib/firmware/kaweth
/lib/firmware/keyspan
/lib/firmware/keyspan_pda
/lib/firmware/lbtf_usb.bin
/lib/firmware/lgs8g75.fw
/lib/firmware/libertas
%exclude /lib/firmware/libertas/usb8388_v9.bin
%exclude /lib/firmware/libertas/sd8686*
%exclude /lib/firmware/libertas/usb8388_olpc.bin
/lib/firmware/liquidio
/lib/firmware/matrox
/lib/firmware/moxa
/lib/firmware/mrvl
%exclude /lib/firmware/mrvl/sd8787*
/lib/firmware/mrvl/sd8787*
/lib/firmware/mt7601u.bin
/lib/firmware/mt7650.bin
/lib/firmware/mts_*.fw
/lib/firmware/mwl8k
/lib/firmware/mwlwifi
/lib/firmware/myri10ge_*.dat
/lib/firmware/myricom
/lib/firmware/nvidia
/lib/firmware/ositech
/lib/firmware/qat_895xcc.bin
/lib/firmware/qat_895xcc_mmp.bin
/lib/firmware/qat_c3xxx.bin
/lib/firmware/qat_c3xxx_mmp.bin
/lib/firmware/qat_c62x.bin
/lib/firmware/qat_c62x_mmp.bin
/lib/firmware/qat_mmp.bin
/lib/firmware/qca
%dir /lib/firmware/qed
/lib/firmware/qed/qed_init_values_zipped-8.10.10.0.bin
/lib/firmware/qed/qed_init_values_zipped-8.10.5.0.bin
/lib/firmware/qed/qed_init_values_zipped-8.4.2.0.bin
/lib/firmware/qed/qed_init_values_zipped-8.7.3.0.bin
/lib/firmware/qlogic
/lib/firmware/r128
/lib/firmware/r8a779x_usb3_v1.dlmem
/lib/firmware/r8a779x_usb3_v2.dlmem
/lib/firmware/r8a779x_usb3_v3.dlmem
/lib/firmware/radeon
%dir /lib/firmware/rockchip
/lib/firmware/rockchip/dptx.bin
/lib/firmware/rp2.fw
/lib/firmware/rsi_91x.fw
/lib/firmware/rt2860.bin
/lib/firmware/rt2870.bin
/lib/firmware/rt3070.bin
/lib/firmware/rt3071.bin
/lib/firmware/rt3090.bin
/lib/firmware/rt3290.bin
/lib/firmware/RTL8192E
/lib/firmware/rtl_bt
/lib/firmware/rtl_nic
/lib/firmware/rtlwifi
/lib/firmware/s2250*.fw
/lib/firmware/s5p-mfc.fw
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
/lib/firmware/ti_3410.fw
/lib/firmware/ti_5052.fw
/lib/firmware/ti-connectivity
/lib/firmware/tigon
/lib/firmware/ti-keystone
/lib/firmware/tlg2300_firmware.bin
/lib/firmware/tr_smctr.bin
/lib/firmware/ttusb-budget
/lib/firmware/ueagle-atm
/lib/firmware/usbdux*_firmware.bin
/lib/firmware/v4l-cx*.fw
/lib/firmware/vicam
/lib/firmware/vntwusb.fw
/lib/firmware/vpu_d.bin
/lib/firmware/vpu_p.bin
/lib/firmware/vxge
/lib/firmware/whiteheat*.fw
/lib/firmware/wsm_22.bin
/lib/firmware/yam

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

%if 0
%files -n iwl1000-firmware
%defattr(644,root,root,755)
%doc WHENCE LICENCE.iwlwifi_firmware
/lib/firmware/iwlwifi-1000-*.ucode
%endif

%files -n iwl2000-firmware
%defattr(644,root,root,755)
%doc WHENCE LICENCE.iwlwifi_firmware
/lib/firmware/iwlwifi-2000-*.ucode

%files -n iwl2030-firmware
%defattr(644,root,root,755)
%doc WHENCE LICENCE.iwlwifi_firmware
/lib/firmware/iwlwifi-2030-*.ucode

%if 0
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
%endif

%files -n iwl6000g2a-firmware
%defattr(644,root,root,755)
%doc WHENCE LICENCE.iwlwifi_firmware
/lib/firmware/iwlwifi-6000g2a-*.ucode

%if 0
%files -n iwl6000g2b-firmware
%defattr(644,root,root,755)
%doc WHENCE LICENCE.iwlwifi_firmware
/lib/firmware/iwlwifi-6000g2b-*.ucode
%endif

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
/lib/firmware/iwlwifi-8000C-*.ucode
/lib/firmware/iwlwifi-8265-*.ucode

%files -n iwl3160-firmware
%defattr(644,root,root,755)
%doc WHENCE LICENCE.iwlwifi_firmware
/lib/firmware/iwlwifi-3160-*.ucode
/lib/firmware/iwlwifi-3168-*.ucode

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

%files -n libertas-sd8686-firmware
%defattr(644,root,root,755)
%doc WHENCE LICENCE.Marvell
%dir /lib/firmware/libertas
/lib/firmware/libertas/sd8686*

%files -n libertas-sd8787-firmware
%defattr(644,root,root,755)
%doc WHENCE LICENCE.Marvell
%dir /lib/firmware/mrvl
/lib/firmware/mrvl/sd8787*
