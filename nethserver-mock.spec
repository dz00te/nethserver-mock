Name:           nethserver-mock
Version: 1.1.0
Release: 1%{?dist}
Summary:        RPM build automation scripts for NethServer packages
BuildArch:	noarch

License:        GPLv3
URL:            http://www.nethserver.org
Source0:        https://github.com/nethesis/nethserver-mock/%{version}/%{name}-%{version}.tar.gz

Requires: mock => 1.1.41
Requires: rpmdevtools >= 7.5
Requires: git >= 1.7.1
Requires: bash
Requires: coreutils
Requires: expect

%description
Provides build automation scripts for NethServer packages

%prep
%setup -q

%build


%install
rm -rf %{buildroot}
mkdir -p  %{buildroot}/%{_bindir} %{buildroot}/%{_sysconfdir}/mock
install -vp src/bin/* %{buildroot}/%{_bindir}
install -vp src/mock/* %{buildroot}/%{_sysconfdir}/mock

%files
%defattr(-,root,root,-)
%{_bindir}/make-rpms
%{_bindir}/make-srpm
%{_bindir}/sign-rpms
%{_bindir}/prep-sources
%{_bindir}/release-tag
%config(noreplace) %{_sysconfdir}/mock/nethserver-6.5-x86_64.cfg
%config(noreplace) %{_sysconfdir}/mock/nethserver-6.6-x86_64.cfg
%doc COPYING

%changelog
* Thu Mar 05 2015 Davide Principi <davide.principi@nethesis.it> - 1.1.0-1
- nethserver-devbox replacements - Feature #3009 [NethServer]
- build-rpm error on Fedora 20 - Bug #2879 [NethServer]
- Devbox: missing rpmspec command - Bug #2770 [NethServer]
- Changed URLs pointing to mirrorlist.nethserver.org
- YUM groups from nethserver-updates

* Thu Feb 12 2015 Davide Principi <davide.principi@nethesis.it> - 0.0.3-1
- Insert development changelog from `git log` output

* Tue Jan 27 2015 Davide Principi <davide.principi@nethesis.it> - 0.0.2-1
- Added NethServer 6.6 configuration

* Tue Dec 23 2014 Davide Principi <davide.principi@nethesis.it> - 0.0.1-1
- Initial version

