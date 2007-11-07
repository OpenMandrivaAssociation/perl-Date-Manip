%define module	Date-Manip
%define version	5.46
%define release	%mkrel 1

Summary:	%{module} module for Perl
Name:		perl-%{module}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Date/%{module}-%{version}.tar.gz
Patch0:		DateManip-COT.patch
Patch1:		DateManip-SORT.patch
Url:		http://search.cpan.org/dist/%{module}/
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%else
BuildRequires:	perl
%endif
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildArch:	noarch
Obsoletes:	perl-DateManip < 5.46
Provides:	perl-DateManip = %{version}-%{release}

%description
This is a set of routines designed to make any common date/time
manipulation easy to do. Operations such as comparing two times,
calculating a time a given amount of time from another, or parsing
international times are all easily done.


%prep
%setup -q -n %{module}-%{version}
%patch0 -p1 -b .cot
%patch1 -p0 -b .sort

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

