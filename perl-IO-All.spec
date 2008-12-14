%define	module	IO-All
%define	name	perl-%{module}
%define	version	0.39
%define	release	%mkrel 1

Version:	%{version}
Name:		%{name}
Release:	%{release}
Summary:	Magic all-in-one IO class
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/IO/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
Buildrequires:  perl(IO::String)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
IO::All combines all of the best Perl IO modules into a single Spiffy object
oriented interface to greatly simplify your everyday Perl IO idioms. It exports
a single function called io, which returns a new IO::All object. And that
object can do it all!

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make 

%check
%{__make} test

%install
rm -rf %{buildroot}
%{makeinstall_std}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man*/*
%{perl_vendorlib}/IO



