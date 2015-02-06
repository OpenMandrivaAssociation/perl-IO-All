%define	upstream_name	 IO-All
%define upstream_version 0.61

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Magic all-in-one IO class


License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/IO/%{upstream_name}-%{upstream_version}.tar.gz

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



