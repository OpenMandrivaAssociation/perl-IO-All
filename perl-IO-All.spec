%define	upstream_name	 IO-All
%define upstream_version 0.56

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Magic all-in-one IO class
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/IO/IO-All-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(IO::String)
BuildArch:	noarch

%description
IO::All combines all of the best Perl IO modules into a single Spiffy object
oriented interface to greatly simplify your everyday Perl IO idioms. It exports
a single function called io, which returns a new IO::All object. And that
object can do it all!

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make 

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man*/*
%{perl_vendorlib}/IO

%changelog
* Tue Aug 17 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.410.0-1mdv2011.0
+ Revision: 570744
- update to 0.41

* Mon Aug 03 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.390.0-1mdv2011.0
+ Revision: 407785
- rebuild using %%perl_convert_version

* Sun Dec 14 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.39-1mdv2009.1
+ Revision: 314248
- update to new version 0.39

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.38-3mdv2009.0
+ Revision: 241542
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue May 01 2007 Olivier Thauvin <nanardon@mandriva.org> 0.38-1mdv2008.0
+ Revision: 20197
- 0.38


* Tue Dec 12 2006 Olivier Thauvin <nanardon@mandriva.org> 0.36-1mdv2007.0
+ Revision: 95141
- 0.36

* Sat Oct 28 2006 Nicolas LÃ©cureuil <neoclust@mandriva.org> 0.35-3mdv2007.1
+ Revision: 73503
- import perl-IO-All-0.35-3mdv2007.1

* Sat Jun 24 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.35-2mdv2007.0
- drop perl(Spiffy) buildrequires

* Fri Jun 02 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.35-1mdv2007.0
- New release 0.35
- fix directory ownership

* Fri Sep 30 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.33-2mdk
- fix buildrequires

* Sat Dec 18 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.33-1mdk
- First MDK release




