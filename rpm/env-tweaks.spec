
Summary: env-tweaks Scripts
Name: env-tweaks
Version: 1.0.0
Release: 1%{?dist}
License: Distributable
Group: System Environment/Base
BuildArch: noarch

Packager: Nathan Neulinger <nneul@neulinger.org>

Source: env-tweaks-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Custom environment tweaks to apply to all hosts

%prep
%setup -c -q -n env-tweaks

%build
cd env-tweaks-%{version}
make DESTDIR=$RPM_BUILD_ROOT

%install

cd env-tweaks-%{version}
make DESTDIR=$RPM_BUILD_ROOT install

#mkdir -p $RPM_BUILD_ROOT/etc/profile.d
#cp -pr env-tweaks.sh $RPM_BUILD_ROOT/etc/profile.d/

%clean
%{__rm} -rf %{buildroot}

%files

#%attr(0644, root, root) /etc/profile.d/env-tweaks.sh

%changelog
