%define upstream_name	 Date-Manip
%define upstream_version 6.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	%{module} upstream_name for Perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/Date/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Test::Pod)
BuildRequires: perl(Test::PodCoverage)
BuildRequires: perl(YAML::Syck)

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%clean
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc HISTORY INSTALL README
%{_mandir}/man*/*
%{perl_vendorlib}/Date
