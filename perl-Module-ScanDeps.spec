%define modname	Module-ScanDeps

Summary:	Recursively scan Perl code for dependencies
Name:		perl-%{modname}
Version:	1.37
Release:	1
License:	Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/Module::ScanDeps
Source0:	http://www.cpan.org/modules/by-module/Module/%{modname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Test::Requires)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl-devel

%description
This is a module to recursively scan Perl programs for dependencies.

An application of Module::ScanDeps is to generate executables from scripts
that contains necessary modules; this module supports two such projects, PAR
and App::Packer.  Please see their respective documentations on CPAN for
further information.

%prep
%autosetup -p1 -n %{modname}-%{version} 

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make_build

%if 0
# Checks require FTP access
%check
%make test
%endif

%install
%make_install

%files
%doc AUTHORS Changes README
%{_bindir}/*
%{perl_vendorlib}/Module
%{_mandir}/man1/*
%{_mandir}/man3/*
