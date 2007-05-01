%define	module	Module-ScanDeps
%define	name	perl-%{module}
%define	modprefix Module

%define	version	0.74
%define	release	%mkrel 1

Version:	%{version}
Name:		%{name}
Release:	%{release}
Summary:	Recursively scan Perl code for dependencies
License:	Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/%{modprefix}/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
Buildrequires:	perl-devel >= 5.4
%endif
BuildRequires:	perl(File::Temp)
Requires:	perl >= 5.4
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This is a module to recursively scan Perl programs for dependencies.

An application of Module::ScanDeps is to generate executables from scripts
that contains necessary modules; this module supports two such projects, PAR
and App::Packer.  Please see their respective documentations on CPAN for
further information.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make 

%check
%__make test

%install
rm -rf %{buildroot}
%{makeinstall_std}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS Changes README
%{_bindir}/*
%{_mandir}/man*/*
%{perl_vendorlib}/%{modprefix}


