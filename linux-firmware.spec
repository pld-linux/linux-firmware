Summary:	Firmware files used by the Linux kernel
Name:		linux-firmware
Version:	20120720
Release:	1
License:	GPL+ and GPLv2+ and MIT and Redistributable, no modification permitted
Group:		Base/Kernel
URL:		http://git.kernel.org/?p=linux/kernel/git/firmware/linux-firmware.git
Source0:	ftp://ftp.kernel.org/pub/linux/kernel/people/dwmw2/firmware/%{name}-%{version}.tar.gz
# Source0-md5:	a26f3e6042afccf12a4633050e1c8c0c
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kernel-firmware includes firmware files required for some devices to
operate.

%prep
%setup -qc
mv linux-firmware-*/* .
rmdir linux-firmware-*

%build
# Remove firmware shipped in separate packages already
# Perhaps these should be built as subpackages of linux-firmware?
%{__rm} ql2???_fw.bin LICENCE.qla2xxx
%{__rm} iwlwifi-*.ucode LICENCE.iwlwifi_firmware
%{__rm} -rf ess korg sb16 yamaha
# We have _some_ ralink firmware in separate packages already.
%{__rm} rt73.bin rt2561.bin rt2561s.bin rt2661.bin
# And _some_ conexant firmware.
%{__rm} v4l-cx23418-apu.fw v4l-cx23418-cpu.fw v4l-cx23418-dig.fw v4l-cx25840.fw
# Netxen firmware
%{__rm} phanfw.bin LICENCE.phanfw

# Remove source files we don't need to install
%{__rm} usbdux/*dux */*.asm

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/firmware
cp -a . $RPM_BUILD_ROOT/lib/firmware
%{__rm} $RPM_BUILD_ROOT/lib/firmware/{WHENCE,LICENCE.*,LICENSE.*}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc WHENCE LICENCE.* LICENSE.*
/lib/firmware/*
