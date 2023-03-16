Name:          bdii-config-site
Version:       1.0.8
Release:       1%{?dist}
Summary:       Site BDII configuration files
Group:         Development/Libraries
License:       ASL 2.0
URL:           https://github.com/EGI-Foundation/bdii-config-site
Source:        %{name}-%{version}.tar.gz
BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-build
BuildRequires: rsync
BuildRequires: make
Requires:      bdii
Requires:      openldap-servers
Requires:      glite-info-provider-ldap
Requires:      glite-info-provider-service
Requires:      glite-info-static
Requires:      glite-info-site

%description
Configuration files for the Site BDII.

%prep
%setup -q

%build
# Nothing to build

%install
rm -rf %{buildroot}
make install prefix=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_sharedstatedir}/bdii/gip/provider/glite-info-provider-service-bdii-site
%{_sharedstatedir}/bdii/gip/provider/glite-info-provider-site
%config(noreplace) %{_sysconfdir}/bdii/gip/site-urls.conf
%{_sharedstatedir}/bdii/gip/provider/glite-info-provider-service-bdii-site-glue2
%{_sharedstatedir}/bdii/gip/provider/glite-info-provider-site-entry
%{_sharedstatedir}/bdii/gip/provider/glite-info-provider-site-entry-glue2
%{_sharedstatedir}/bdii/gip/provider/glite-info-provider-site-glue2
%doc %{_docdir}/%{name}-%{version}/README.md
%doc %{_docdir}/%{name}-%{version}/AUTHORS.md
%license /usr/share/licenses/%{name}-%{version}/COPYRIGHT
%license /usr/share/licenses/%{name}-%{version}/LICENSE.txt

%changelog
* Thu Mar 16 2023 Baptiste Grenier <baptiste.grenier@egi.eu> - 1.0.8-1
- Update source URL information, package additional documentation. (#3) (Baptiste Grenier)

* Wed Apr 24 2013 Maria Alandes <maria.alandes.pradillo@cern.ch> - 1.0.7-2
- Added Source URL information

* Wed Oct 24 2012 Maria Alandes <maria.alandes.pradillo@cern.ch> - 1.0.7-1
- #BUG 98427: Fixed rpmlint errors: Changed /opt/glite/libexec to /usr/libexec

* Wed Mar 14 2012 Laurence Field <laurence.field@cern.ch> - 1.0.6-1
- Improved dependency definition

* Mon Aug 22 2011 Laurence Field <laurence.field@cern.ch> - 1.0.5-1
- Fixed #84241

* Mon Apr 18 2011 Laurence Field <laurence.field@cern.ch> - 1.0.3-1
- Removed the dependency on glite-info-provider-release

* Tue Apr 05 2011 Laurence Field <laurence.field@cern.ch> - 1.0.2-1
- Fixed error due to new version of glite-info-provider-service

* Mon Mar 21 2011 Laurence Field <laurence.field@cern.ch> - 1.0.1-1
- Changed config location to /etc/bdii/gip

* Tue Mar 15 2011 Laurence Field <laurence.field@cern.ch> - 1.0.0-1
- Fixed Is-148

* Mon Sep 06 2010 Laurence Field <laurence.field@cern.ch> - 0.9.0-1
- Fixed Is-148

* Thu May 20 2010 Laurence Field <laurence.field@cern.ch> - 0.7.0-1
- Changed to /opt/glite/etc

* Wed Apr 07 2010 Laurence Field <laurence.field@cern.ch> - 0.4.0-1
- New package
