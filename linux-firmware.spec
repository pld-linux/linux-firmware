# TODO
# - subpackages for various firmwares?
Summary:	Firmware files used by the Linux kernel
Summary(pl.UTF-8):	Pliki firmware'u używane przez jądro Linuksa
Name:		linux-firmware
Version:	20140317
Release:	1
License:	GPL+ and GPL v2+ and MIT and Redistributable, no modification permitted
Group:		Base/Kernel
Source0:	http://pkgs.fedoraproject.org/repo/pkgs/linux-firmware/%{name}-%{version}.tar.gz/8d819913b5e296fc59f6b83bf18e6d81/%{name}-%{version}.tar.gz
# Source0-md5:	8d819913b5e296fc59f6b83bf18e6d81
URL:		http://git.kernel.org/cgit/linux/kernel/git/firmware/linux-firmware.git/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package includes firmware files required for some devices to
operate.

%description -l pl.UTF-8
Ten pakiet zawiera pliki firmware'u wymagane do działania niektórych
urządzeń.

%prep
%setup -qc
mv linux-firmware-*/* .
rmdir linux-firmware-*

%build
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
# And _some_ conexant firmware. (whcih packages???)
%{__rm} v4l-cx23418-apu.fw v4l-cx23418-cpu.fw v4l-cx23418-dig.fw v4l-cx25840.fw
# Netxen firmware (which package???)
%{__rm} phanfw.bin LICENCE.phanfw
# - radeon-ucode.spec
%{__rm} radeon/{ARUBA,BTC,CAYMAN,CEDAR,CYPRESS,JUNIPER,PITCAIRN,R700,REDWOOD,SUMO,TAHITI,VERDE}_rlc.bin

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
/lib/firmware/RTL8192E
/lib/firmware/acenic
/lib/firmware/adaptec
/lib/firmware/advansys
/lib/firmware/agere_*_fw.bin
/lib/firmware/amd-ucode
/lib/firmware/ar3k
/lib/firmware/ar5523.bin
/lib/firmware/ar7010*.fw
/lib/firmware/ar9170-*.fw
/lib/firmware/ar9271.fw
/lib/firmware/ath3k-1.fw
/lib/firmware/ath6k
/lib/firmware/atmsar11.fw
/lib/firmware/av7110
/lib/firmware/bnx2
/lib/firmware/bnx2x
/lib/firmware/bnx2x-e1-*.fw
/lib/firmware/bnx2x-e1h-*.fw
/lib/firmware/brcm
/lib/firmware/carl9170-1.fw
/lib/firmware/cbfw-*.bin
/lib/firmware/cis
/lib/firmware/cpia2
/lib/firmware/ct2fw-*.bin
/lib/firmware/ctefx.bin
/lib/firmware/ctfw-*.bin
/lib/firmware/ctspeq.bin
/lib/firmware/cxgb3
/lib/firmware/cxgb4
/lib/firmware/dabusb
/lib/firmware/dsp56k
/lib/firmware/dvb-fe-xc5000-*.fw
/lib/firmware/dvb-usb-dib0700-*.fw
/lib/firmware/dvb-usb-terratec-h5-drxk.fw
/lib/firmware/e100
/lib/firmware/edgeport
/lib/firmware/emi26
/lib/firmware/emi62
/lib/firmware/ene-ub6250
/lib/firmware/f2255usb.bin
/lib/firmware/go7007
/lib/firmware/htc_7010.fw
/lib/firmware/htc_9271.fw
/lib/firmware/i2400m-fw-usb-*.sbcf
/lib/firmware/i6050-fw-usb-*.sbcf
/lib/firmware/intel
/lib/firmware/intelliport2.bin
/lib/firmware/isci
/lib/firmware/iwlwifi-100-5.ucode
/lib/firmware/iwlwifi-105-6.ucode
/lib/firmware/iwlwifi-135-6.ucode
/lib/firmware/iwlwifi-2000-6.ucode
/lib/firmware/iwlwifi-2030-6.ucode
/lib/firmware/iwlwifi-3160-7.ucode
/lib/firmware/iwlwifi-3160-8.ucode
/lib/firmware/iwlwifi-6000g2a-6.ucode
/lib/firmware/iwlwifi-6050-5.ucode
/lib/firmware/iwlwifi-7260-7.ucode
/lib/firmware/iwlwifi-7260-8.ucode
/lib/firmware/kaweth
/lib/firmware/keyspan
/lib/firmware/keyspan_pda
/lib/firmware/lbtf_usb.bin
/lib/firmware/lgs8g75.fw
/lib/firmware/libertas
/lib/firmware/matrox
/lib/firmware/moxa
/lib/firmware/mrvl
/lib/firmware/mt7650.bin
/lib/firmware/mts_*.fw
/lib/firmware/mwl8k
/lib/firmware/myri10ge_*.dat
/lib/firmware/myricom
/lib/firmware/ositech
/lib/firmware/qlogic
/lib/firmware/r128
/lib/firmware/radeon
/lib/firmware/rp2.fw
/lib/firmware/rt2860.bin
/lib/firmware/rt2870.bin
/lib/firmware/rt3070.bin
/lib/firmware/rt3071.bin
/lib/firmware/rt3090.bin
/lib/firmware/rt3290.bin
/lib/firmware/rtl_nic
/lib/firmware/rtlwifi
/lib/firmware/s2250*.fw
/lib/firmware/s5p-mfc
/lib/firmware/sdd_sagrad_*.bin
/lib/firmware/slicoss
/lib/firmware/sun
/lib/firmware/sxg
/lib/firmware/tehuti
/lib/firmware/ti-connectivity
/lib/firmware/ti_3410.fw
/lib/firmware/ti_5052.fw
/lib/firmware/tigon
/lib/firmware/tlg2300_firmware.bin
/lib/firmware/tr_smctr.bin
/lib/firmware/ttusb-budget
/lib/firmware/ueagle-atm
/lib/firmware/usbdux*_firmware.bin
/lib/firmware/v4l-cx*.fw
/lib/firmware/vicam
/lib/firmware/vntwusb.fw
/lib/firmware/vxge
/lib/firmware/whiteheat*.fw
/lib/firmware/wsm_22.bin
/lib/firmware/yam
