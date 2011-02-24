%define upstream_name       Module-ScanDeps
%define upstream_version 1.00

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
Summary:	Recursively scan Perl code for dependencies
License:	Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source:     http://www.cpan.org/modules/by-module/Module/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Module::Build::ModuleInfo)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This is a module to recursively scan Perl programs for dependencies.

An application of Module::ScanDeps is to generate executables from scripts
that contains necessary modules; this module supports two such projects, PAR
and App::Packer.  Please see their respective documentations on CPAN for
further information.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

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
%{perl_vendorlib}/Module
