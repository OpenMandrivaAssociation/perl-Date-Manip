%define upstream_name	 Date-Manip
%define upstream_version 6.24

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    3

Summary:	%{upstream_name} upstream_name for Perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/Date/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Test::Inter)
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Test::Pod::Coverage)
BuildRequires: perl(YAML::Syck)
BuildRequires: perl(Module::Build)

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

Obsoletes:	perl-DateManip < 5.46
Provides:	perl-DateManip < 5.46

%description
This is a set of routines designed to make any common date/time
manipulation easy to do. Operations such as comparing two times,
calculating a time a given amount of time from another, or parsing
international times are all easily done.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
%{__rm} -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc HISTORY INSTALL README
%{_mandir}/man*/*
%{perl_vendorlib}/Date


%changelog
* Wed Jun 15 2011 Guillaume Rousse <guillomovitch@mandriva.org> 6.240.0-1mdv2011.0
+ Revision: 685312
- update to new version 6.24

* Sun Apr 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 6.230.0-1
+ Revision: 654054
- update to new version 6.23

* Mon Mar 14 2011 Guillaume Rousse <guillomovitch@mandriva.org> 6.220.0-1
+ Revision: 644747
- update to new version 6.22

* Mon Jan 31 2011 Guillaume Rousse <guillomovitch@mandriva.org> 6.210.0-1
+ Revision: 634428
- update to new version 6.21

* Mon Dec 06 2010 Guillaume Rousse <guillomovitch@mandriva.org> 6.200.0-1mdv2011.0
+ Revision: 612074
- update to new version 6.20

* Sat Oct 23 2010 Guillaume Rousse <guillomovitch@mandriva.org> 6.140.0-1mdv2011.0
+ Revision: 587612
- new version

* Mon Jul 26 2010 Funda Wang <fwang@mandriva.org> 6.110.0-1mdv2011.0
+ Revision: 560869
- fix summary

  + Jérôme Quelin <jquelin@mandriva.org>
    - adding missing buildrequires:
    - update to 6.11

* Mon Feb 08 2010 Jérôme Quelin <jquelin@mandriva.org> 6.70.0-1mdv2010.1
+ Revision: 502104
- update to 6.07

* Sat Dec 12 2009 Jérôme Quelin <jquelin@mandriva.org> 6.50.0-1mdv2010.1
+ Revision: 477626
- update to 6.05

* Fri Nov 27 2009 Jérôme Quelin <jquelin@mandriva.org> 6.40.0-1mdv2010.1
+ Revision: 470499
- removing test::pod* buildrequires
- they are in contrib while date::manip is in main
- their use is conditional, skipping tests if not present
- adding missing buildrequires:
- update to 6.04

  + Shlomi Fish <shlomif@mandriva.org>
    - Upgraded to Date-Manip version 6.04, no longer installing the non-existent TODO and got rid of the "cot" patch

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 5.540.0-1mdv2010.0
+ Revision: 403090
- rebuild using %%perl_convert_version

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 5.54-3mdv2009.1
+ Revision: 351709
- rebuild

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 5.54-2mdv2009.0
+ Revision: 265353
- rebuild early 2009.0 package (before pixel changes)

* Sat May 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 5.54-1mdv2009.0
+ Revision: 208378
- new version
  rediff patch 0

* Tue May 06 2008 Guillaume Rousse <guillomovitch@mandriva.org> 5.50-1mdv2009.0
+ Revision: 202291
- new version
- update to new version 5.50

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Dec 05 2007 Guillaume Rousse <guillomovitch@mandriva.org> 5.48-2mdv2008.1
+ Revision: 115554
- re-add backward compatibility virtual package to ease upgrade

* Wed Nov 28 2007 Guillaume Rousse <guillomovitch@mandriva.org> 5.48-1mdv2008.1
+ Revision: 113647
- new version
  spec cleanup
  drop unappliable and undocumented sort patch

* Wed Nov 07 2007 Frederic Crozat <fcrozat@mandriva.com> 5.46-1mdv2008.1
+ Revision: 106705
- upstream module changed name
-Release 5.46
-rename package, since perl module changed name

* Tue Jul 31 2007 David Walluck <walluck@mandriva.org> 5.44-4mdv2008.0
+ Revision: 56781
- rebuild to fix %%mkrel

