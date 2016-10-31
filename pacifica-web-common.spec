Name:		pacifica-web-common
Epoch:		1
Version:	0.99.4
Release:	1%{?dist}
Summary:	The pacifica common resources for web pages
Group:		System Environment/Libraries
License:	GPLv2
URL:		http://www.example.com/
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:	rsync

%description

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/var/www/resources
rsync -r fonts images stylesheets scripts %{buildroot}/var/www/resources/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/var/www/resources

%changelog
* Mon Mar 21 2016 David Brown <david.brown@pnnl.gov> 0.99.0-1
- Initial RHEL release.
