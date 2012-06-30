%define _disable_ld_no_undefined 1

Summary:	Dinamically choose best algorithm to compress a file
Name:		dact
Version:	0.8.42
Release:	2
License:	LGPL
Group:		Archiving/Compression
Url:		http://www.rkeene.org/oss/dact/
Source:		http://www.rkeene.org/files/oss/dact/release/%{name}-%{version}.tar.gz
BuildRequires:	bzip2-devel
BuildRequires:	liblzo-devel
BuildRequires:	libmcrypt-devel

%description
DACT is a compression tool designed to compress a file dynamically,
choosing the algorithm that works best per block of input data to
produce an overall smaller output file.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall

%files
%doc MD5SUMS README TODO.ideas TODO VERSION ChangeLog AUTHORS
%doc Docs/config_help.txt Docs/dact.txt Docs/helpfile.txt
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_libdir}/lib%{name}.*
%{_mandir}/man1/%{name}.*

