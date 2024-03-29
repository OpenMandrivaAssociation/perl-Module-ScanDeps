%define modname	Module-ScanDeps
%define modver 1.31

Summary:	Recursively scan Perl code for dependencies
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	2
License:	Artistic
Group:		Development/Perl
Url:		http://metacpan.org/pod/Module::ScanDeps
Source0:	http://www.cpan.org/modules/by-module/Module/%{modname}-%{modver}.tar.gz
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
%setup -qn %{modname}-%{modver} 

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make 

%if 0
# Checks require FTP access
%check
%make test
%endif

%install
%makeinstall_std

%files
%doc AUTHORS Changes README
%{_bindir}/*
%{perl_vendorlib}/Module
%{_mandir}/man1/*
%{_mandir}/man3/*
