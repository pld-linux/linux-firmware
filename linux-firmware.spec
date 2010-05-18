Summary:	Firmware files used by the Linux kernel
Name:		linux-firmware
Version:	20100430
Release:	1
License:	GPL+ and GPLv2+ and MIT and Redistributable, no modification permitted
Group:		Base/Kernel
URL:		http://www.kernel.org/
Source0:	ftp://ftp.kernel.org/pub/linux/kernel/people/dwmw2/firmware/%{name}-%{version}.tar.bz2
# Source0-md5:	d4cfb7d359d8ef6dd50e69225ac6c82b
Requires:	udev
Provides:	kernel-firmware = %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kernel-firmware includes firmware files required for some devices to
operate.

%prep
%setup -q

%build
# Remove firmware shipped in separate packages already
# Perhaps these should be built as subpackages of linux-firmware?
rm ql2???_fw.bin LICENCE.qla2xxx
rm iwlwifi-*.ucode LICENCE.iwlwifi_firmware

# Remove source files we don't need to install
rm -f usbdux/*dux */*.asm

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/firmware
cp -r * $RPM_BUILD_ROOT/lib/firmware
rm $RPM_BUILD_ROOT/lib/firmware/{WHENCE,LICENCE.*}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%doc WHENCE LICENCE.* LICENSE.*
/lib/firmware/*
