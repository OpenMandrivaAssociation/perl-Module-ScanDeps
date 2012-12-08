%define upstream_name       Module-ScanDeps
%define upstream_version 1.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5
Summary:	Recursively scan Perl code for dependencies
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source:		http://www.cpan.org/modules/by-module/Module/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Module::Build::ModuleInfo)
BuildRequires:	perl-devel
BuildArch:	noarch

%description
This is a module to recursively scan Perl programs for dependencies.

An application of Module::ScanDeps is to generate executables from scripts
that contains necessary modules; this module supports two such projects, PAR
and App::Packer.  Please see their respective documentations on CPAN for
further information.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make 

%check
%__make test

%install
%makeinstall_std

%files
%doc AUTHORS Changes README
%{_bindir}/*
%{_mandir}/man*/*
%{perl_vendorlib}/Module


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.20.0-4mdv2012.0
+ Revision: 765491
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.20.0-2
+ Revision: 667263
- mass rebuild

* Mon Apr 04 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.20.0-1
+ Revision: 650341
- update to new version 1.02

* Wed Mar 30 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.10.0-1
+ Revision: 649152
- update to new version 1.01

* Thu Feb 24 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.0-1
+ Revision: 639658
- update to new version 1.00

* Tue Jul 27 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.980.0-1mdv2011.0
+ Revision: 561942
- update to 0.98

* Sun Apr 18 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.970.0-1mdv2011.0
+ Revision: 536205
- update to 0.97

* Sat Nov 14 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.960.0-1mdv2010.1
+ Revision: 466003
- update to 0.96

* Thu Sep 17 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.950.0-1mdv2010.0
+ Revision: 443880
- update to 0.95
- update to 0.95

* Sun Aug 16 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.940.0-1mdv2010.0
+ Revision: 416950
- update to 0.94

* Mon Jul 20 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.930.0-1mdv2010.0
+ Revision: 398199
- new version

* Thu Jun 25 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.91-1mdv2010.0
+ Revision: 389096
- update to new version 0.91

* Sun May 10 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.90-1mdv2010.0
+ Revision: 373932
- update to new version 0.90

* Tue Nov 04 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.89-1mdv2009.1
+ Revision: 299760
- update to new version 0.89

* Fri Oct 24 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.86-1mdv2009.1
+ Revision: 296947
- update to new version 0.86

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.84-2mdv2009.0
+ Revision: 268618
- rebuild early 2009.0 package (before pixel changes)

* Sat May 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.84-1mdv2009.0
+ Revision: 208356
- update to new version 0.84

* Tue Apr 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.83-1mdv2009.0
+ Revision: 193865
- update to new version 0.83

* Tue Jan 29 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.82-1mdv2008.1
+ Revision: 159768
- update to new version 0.82

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Dec 08 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.81-1mdv2008.1
+ Revision: 116441
- update to new version 0.81

* Mon Dec 03 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.80-1mdv2008.1
+ Revision: 114490
- update to new version 0.80

* Mon Nov 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.78-1mdv2008.1
+ Revision: 110279
- update to new version 0.78

* Sat Oct 13 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.77-1mdv2008.1
+ Revision: 98035
- update to new version 0.77
- update to new version 0.77

* Thu Jul 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.76-1mdv2008.0
+ Revision: 55818
- update to new version 0.76

* Sun Jul 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.75-1mdv2008.0
+ Revision: 46766
- update to new version 0.75

* Wed May 02 2007 Olivier Thauvin <nanardon@mandriva.org> 0.74-1mdv2008.0
+ Revision: 20312
- 0.74


* Sat Mar 03 2007 Olivier Thauvin <nanardon@mandriva.org> 0.72-1mdv2007.0
+ Revision: 131693
- 0.72

* Mon Aug 07 2006 Scott Karns <scottk@mandriva.org> 0.62-1mdv2007.0
+ Revision: 53472
- Version 0.62
- import perl-Module-ScanDeps-0.61-1mdv2007.0

* Sun Jul 02 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.61-1mdv2007.0
- New version 0.61
- use HTTP source URL

* Fri May 26 2006 Scott Karns <scottk@mandriva.org> 0.60-1mdv2007.0
- New release 0.60

* Sat May 06 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.59-1mdk
- New release 0.59

* Wed Apr 19 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.58-1mdk
- New release 0.58
- fix directory ownership
- better source URL
- spec cleanup

* Mon Mar 06 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.57-1mdk
- 0.57

* Mon Feb 27 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.56-1mdk
- 0.56

* Mon Jan 30 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.54-1mdk
- 0.54

* Tue Jan 10 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.53-1mdk
- 0.53

* Tue Dec 13 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.52-1mdk
- 0.52
- Clean up BuildRequires

* Mon Jan 10 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.51-1mdk
- 0.51 (now scandeps.pl doesn't require CPANPLUS anymore)

* Tue Oct 12 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.50-1mdk
- 0.50

* Wed Sep 01 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.47-1mdk
- 0.47

* Sat Jul 03 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.46-1mdk
- 0.46

* Fri Jun 11 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.44-1mdk
- 0.44

* Sat Jun 05 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.43-1mdk
- 0.43
- cosmetics

* Sat May 22 2004 Florin <florin@mandrakesoft.com> 0.42-1mdk
- first Mandrake Release

