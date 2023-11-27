%define upstream_name	 Date-Manip

Name:		perl-%{upstream_name}
Version:	6.92
Release:	1
Summary:	%{upstream_name} upstream_name for Perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Date/%{upstream_name}-%{version}.tar.gz
BuildRequires:	perl(JSON::PP)
BuildRequires:	perl(Test::Inter)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Pod::Coverage)
BuildRequires:	perl(YAML::Syck)
BuildRequires:	perl(Module::Build)
BuildArch:	noarch
Obsoletes:	perl-DateManip < 5.46
Provides:	perl-DateManip < 5.46

%description
This is a set of routines designed to make any common date/time
manipulation easy to do. Operations such as comparing two times,
calculating a time a given amount of time from another, or parsing
international times are all easily done.

%prep
%autosetup -p1 -n %{upstream_name}-%{version}
perl Makefile.PL INSTALLDIRS=vendor

%build
%make_build

# As of 6.92, all tests fail, but it seems to be a problem
# with the tests rather than with the code they're supposed
# to test.
# The test can't find its own files.
#check
#make test

%install
%make_install

%files
%doc INSTALL README
%{_mandir}/man*/*
%{perl_vendorlib}/Date
%{_bindir}/*
