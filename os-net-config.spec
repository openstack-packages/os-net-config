
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:			os-net-config
Version:		0.2.2
Release:		1%{?dist}
Summary:		Host network configuration tool

License:		ASL 2.0
URL:			http://pypi.python.org/pypi/%{name}
Source0:		http://tarballs.openstack.org/%{name}/%{name}-%{version}%{?milestone}.tar.gz

Patch0001: 0001-PATCH-Remove-pbr-runtime-dependency.patch

BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRequires:	python2-devel
BuildRequires:	python-pbr
BuildRequires:	python-sphinx
BuildRequires:	python-oslo-sphinx

Requires:	python-setuptools
Requires:	python-argparse
Requires:	python-anyjson
Requires:	python-babel
Requires:	python-eventlet
Requires:	python-oslo-concurrency
Requires:	python-oslo-config
Requires:	python-oslo-utils
Requires:	python-netaddr
Requires:	python-iso8601
Requires:	python-six >= 1.5.0
Requires:	initscripts
Requires:	PyYAML

%description
Host network configuration tool for OpenStack.

%prep

%setup -q -n %{name}-%{upstream_version}

%patch0001 -p1

sed -i '/setuptools_git/d' setup.py
sed -i s/REDHATOSNETCONFIGVERSION/%{version}/ os_net_config/version.py
sed -i s/REDHATOSNETCONFIGRELEASE/%{release}/ os_net_config/version.py

%build
%{__python} setup.py build
%{__python} setup.py build_sphinx

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%files
%doc README.rst
%doc LICENSE
%doc doc/build/html
%{_bindir}/os-net-config
%{python_sitelib}/os_net_config*


%changelog
* Thu Mar 31 2016 RDO <rdo-list@redhat.com> 0.2.2-1
- RC1 Rebuild for Mitaka RC1 0.2.2
