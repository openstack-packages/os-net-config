Name:			os-net-config
Version:		XXX
Release:		1%{?dist}
Summary:		os-net-config

License:		ASL 2.0
URL:			http://pypi.python.org/pypi/%{name}
Source0:		http://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz

Patch0001: 0001-PATCH-Remove-pbr-runtime-dependency.patch

BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRequires:	python2-devel
BuildRequires:	python-pbr

Requires:	python-setuptools
Requires:	python-argparse
Requires:	python-anyjson
Requires:	python-babel
Requires:	python-eventlet
Requires:	python-oslo-config
Requires:	python-netaddr
Requires:	python-iso8601
Requires:	PyYAML

Requires(post):		systemd
Requires(preun):	systemd
Requires(postun):	systemd

%description
Host network configuration tool for OpenStack.

%prep

%setup -q -n %{name}-%{upstream_version}

%patch0001 -p1

sed -i '/setuptools_git/d' setup.py
sed -i s/REDHATOSAPPLYCONFIGVERSION/%{version}/ os_apply_config/version.py
sed -i s/REDHATOSAPPLYCONFIGRELEASE/%{release}/ os_apply_config/version.py

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%files
%doc README.rst
%doc LICENSE
%{_bindir}/os-net-config
%{python_sitelib}/os_net_config*


%changelog
* Mon Sep 29 2014 Dan Prince <dprince@redhat.com> - XXX
- initial package
