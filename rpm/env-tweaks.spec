
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

%post

/etc/env-tweaks/setup-env-tweaks

%clean
%{__rm} -rf %{buildroot}

%files

%attr(0755, root, root) /etc/env-tweaks/setup-env-tweaks

/etc/env-tweaks/indent.pro
/etc/env-tweaks/perltidyrc
/etc/env-tweaks/vimrc


%changelog
