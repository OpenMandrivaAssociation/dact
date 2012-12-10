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

%changelog
* Sun Jul 01 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 0.8.42-2
- Minor cleanups

* Wed Oct 05 2011 Andrey Bondrov <abondrov@mandriva.org> 0.8.42-1mdv2012.0
+ Revision: 703127
- New version: 0.8.42

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 0.8.41-1mdv2008.1
+ Revision: 140717
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Sep 01 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-09-01 22:32:40 (59568)
- 0.8.41

* Fri Jul 28 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-07-28 20:57:46 (42476)
- rebuild

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 12:36:37 (31646)
renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Wed Jan 11 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-01-11 22:07:04 (1409)
- dact-0.8.39-3mdk

* Wed Jan 11 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-01-11 21:27:20 (1408)
- dact-0.8.39-2mdk

* Wed Jan 11 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-01-11 21:26:49 (1407)
- dact-0.8.39-2mdk

* Wed Jan 11 2006 Olivier Thauvin <nanardon@mandriva.org> 0.8.39-3mdk
- rebuild

* Fri May 13 2005 Olivier Thauvin <nanardon@mandriva.org> 0.8.39-2mdk
- birthday rebuild
- put .so files in %%_libdir

* Sat Apr 17 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.8.39-1mdk
- 0.8.39

* Wed Jan 07 2004 Olivier Thauvin <nanardon@klama.mandrake.org> 0.8.35-1mdk
- 0.8.35
- DIRM fix

* Fri Dec 12 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.8.34-1mdk
- 1mdk spec

