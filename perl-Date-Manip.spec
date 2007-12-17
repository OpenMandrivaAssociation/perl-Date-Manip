%define module	Date-Manip
%define version	5.48
%define release	%mkrel 2

Summary:	%{module} module for Perl
Name:		perl-%{module}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}/
Source:     http://www.cpan.org/modules/by-module/Date/%{module}-%{version}.tar.gz
Patch0:		DateManip-COT.patch
Obsoletes:	perl-DateManip < 5.46
Provides:	perl-DateManip < 5.46
BuildArch:	noarch

%description
This is a set of routines designed to make any common date/time
manipulation easy to do. Operations such as comparing two times,
calculating a time a given amount of time from another, or parsing
international times are all easily done.


%prep
%setup -q -n %{module}-%{version}
%patch0 -p1 -b .cot

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%__make

%check
%__make test

%clean
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc HISTORY INSTALL README TODO
%{_mandir}/man*/*
%{perl_vendorlib}/Date

