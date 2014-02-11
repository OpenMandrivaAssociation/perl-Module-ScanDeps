%define modname	Module-ScanDeps
%define modver 1.13

Summary:	Recursively scan Perl code for dependencies
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Module/Module-ScanDeps-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(File::Temp)
BuildRequires: perl(Test::Requires)
BuildRequires:	perl(Module::Build::ModuleInfo)
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

%check
%make test

%install
%makeinstall_std

%files
%doc AUTHORS Changes README
%{_bindir}/*
%{perl_vendorlib}/Module
%{_mandir}/man1/*
%{_mandir}/man3/*



