
%define		module	urljr

Summary:	URL-related utilites from JanRain, Inc.
Summary(pl.UTF-8):	Narzędzia związane z URL-ami napisane przez JanRain, Inc.
Name:		python-%{module}
Version:	1.0.1
Release:	6
License:	LGPL
Group:		Libraries/Python
Source0:	http://www.openidenabled.com/resources/downloads/python-openid/%{name}-%{version}.tar.gz
# Source0-md5:	0b120d08dc4538ed5c4ee5c77447b865
URL:		http://www.openidenabled.com/
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
URL-related utilites from JanRain, Inc.

This package contains the "fetchers" module, which provides
a common interface to urllib2 and curl for making HTTP requests.

%description -l pl.UTF-8
Narzędzia związane z URL-ami napisane przez JanRain, Inc.

Ten pakiet zawiera moduł "fetchers" dostarczający wspólny interfejs do
urllib2 i curl do wykonywania zapytań HTTP.

%prep
%setup -q

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
rm -f $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{py_sitescriptdir}/%{module}
