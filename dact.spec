%define name dact
%define version 0.8.42
%define release %mkrel 1

%define _disable_ld_no_undefined 1

Summary: Dinamically choose best algorithm to compress a file
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.rkeene.org/files/oss/dact/%{name}-%{version}.tar.gz
License: LGPL
Group: Archiving/Compression
Url: http://www.rkeene.org/oss/dact/
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: liblzo-devel
BuildRequires: libbzip2-devel
BuildRequires: libmcrypt-devel

%description
DACT is a compression tool designed to compress a file dynamically, 
choosing the algorithm that works best per block of input data to 
produce an overall smaller output file. 

%prep
%setup -q

%build
%configure
%make

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sysconfdir}
mkdir -p %{buildroot}%{_mandir}/man1

%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc MD5SUMS README TODO.ideas TODO VERSION ChangeLog AUTHORS
%doc Docs/config_help.txt Docs/dact.txt Docs/helpfile.txt
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_libdir}/lib%{name}.*
%{_mandir}/man1/%{name}.*

